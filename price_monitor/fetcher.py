import asyncio

from aiohttp.client import ClientSession, TCPConnector

from price_monitor.db import PRODUCTS


def query_data():
    return asyncio.run(query_evroopt_data())


async def query_evroopt_data():
    with ClientSession(connector=TCPConnector(limit_per_host=3)) as client:
        for product in PRODUCTS:
            pass
