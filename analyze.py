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

    all_items = tuple(prepare_data(todays_data, products, date))

    categories = {x['categories'][0] for x in products}
    price = build_categories_prices(all_items)
    missing = {x for x in categories if x not in price}
    if missing:
        logger.warning('Some categories are missing:\n%s', missing)
        price.update(build_categories_prices(all_items, missing))
        missing = {x for x in categories if x not in price}
        if missing:
            logger.error('Some categories are really missing:\n%s', missing)

    save_analytics(price.values())


def prepare_data(data, products, date):
    for p in products:
        item = data.get(f'{p["source"]}-{p["identifier"]}')
        if item is None or not item['price']:
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
            item['date'] = date.strftime('%Y-%m-%d')
            item['name'] = p['name_ru']
            yield item


def build_categories_prices(data, missing_categories=None):
    missing_categories = missing_categories or set()
    categories_are_specified = bool(missing_categories)
    prices = {}
    for item in (x for x in data if x['prefer'] is not categories_are_specified):
        category = item['category']

        if categories_are_specified and category not in missing_categories:
            continue

        if category not in prices or prices[category]['effective_price'] > item['effective_price']:
            prices[category] = item

    return prices


def save_analytics(data):
    with open('info.csv', mode='a', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['category', 'effective_price', 'source', 'identifier', 'original_price', 'datetime', 'date', 'prefer', 'name'],
        )
        writer.writerows(data)


if __name__ == '__main__':
    analyze(datetime.date.today())
