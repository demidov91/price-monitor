import csv
import datetime
import decimal
import logging

from price_monitor.db import PRODUCTS


logger = logging.getLogger(__name__)


def analyze(date):
    today_as_str = date.strftime("%Y-%m-%d")
    filename = today_as_str + '.csv'
    with open(filename, 'rt', newline='') as f:
        reader = csv.DictReader(f)
        todays_data = {f'{x["source"]}-{x["identifier"]}': x for x in reader if x['datetime'].split()[0] == today_as_str}

    products = PRODUCTS

    all_items = tuple(prepare_data(todays_data, products))

    categories = {x['categories'][0] for x in products}
    price = build_categories_prices(all_items)
    missing = {x for x in categories if x not in price}
    if missing:
        logger.warning('Some categories are missing:\n%s', missing)
        price.update(build_categories_prices(all_items, missing))
        missing = {x for x in categories if x not in price}
        if missing:
            logger.error('Some categories are really missing:\n%s', missing)

    print(price)


def prepare_data(data, products):
    for p in products:
        item = data.get(f'{p["source"]}-{p["identifier"]}')
        if not item['price']:
            continue

        if item is not None:
            item['category'] = p['categories'][0]
            price = decimal.Decimal(item.pop('price'))
            item['original_price'] = price
            coeff = p.get('coefficients', {}).get(item['category'])
            if coeff:
                item['effective_price'] = price * coeff
            else:
                item['effective_price'] = price

            item['prefer'] = p.get('prefer', True)
            yield item


def build_categories_prices(data, missing_categories=None):
    missing_categories = missing_categories or set()
    prices = {}
    for item in data:
        print(item)
        category = item['category']
        if item['prefer'] or category in missing_categories:
            if category not in prices or prices[category]['effective_price'] > item['effective_price']:
                prices[category] = item

    return prices


if __name__ == '__main__':
    analyze(datetime.date.today())