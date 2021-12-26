import asyncio
import datetime
import logging

from aiohttp.client import ClientSession, TCPConnector

from price_monitor.db import PRODUCTS
from price_monitor.parser import parse_evroopt


logger = logging.getLogger(__name__)


def query_data():
    return asyncio.run(save_evroopt_data())


async def save_evroopt_data():
    return [x async for x in query_evroopt_data()]


async def query_evroopt_data():
    query_time = datetime.datetime.utcnow()
    products = PRODUCTS

    async with ClientSession(connector=TCPConnector(limit_per_host=3)) as client:
        results = await asyncio.gather(
            *[query_evroopt_product(client, x['identifier']) for x in products],
            return_exceptions=True,
        )
        for product, data in zip(products, results):
            if isinstance(data, BaseException):
                logger.error(
                    'Failed to get %s data. Name: %s. Error: %s', product['identifier'], product['name_ru'], data
                )

            else:
                yield {
                    'source': 'evroopt',
                    'identifier': product['identifier'],
                    'price': data,
                    'datetime': query_time,
                }


async def query_evroopt_product(client: ClientSession, identifier: str):
    url = f'https://e-dostavka.by/catalog/item_{identifier}.html'
    response = await client.get(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
            'Host': 'e-dostavka.by',
            'Accept': '*/*',
            'Accept-Language': 'be,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip,deflate,br',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        },
    )
    if response.status != 200:
        logger.error(
            'Gor %s status code instead of 200 on %s query. Body:\n%s',
            response.status,
            url,
            await response.read(),
        )
        return None

    body = await response.text()
    try:
        return parse_evroopt(body)
    except ValueError:
        logger.exception('Failed to parse identifier %s. Url: %s. Page body:\n%s', identifier, url, body)
        raise ValueError



