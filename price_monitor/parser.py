import logging
from decimal import Decimal
from typing import Optional
import lxml.html


logger = logging.getLogger(__name__)


def parse_evroopt(data: str) -> Optional[dict]:
    page = lxml.html.fromstring(data)
    element = page.cssselect('.price_byn>.price>meta[itemprop="price"]')
    if len(element) == 0:
        if len(page.cssselect('.out_of_stock')):
            return None

        raise ValueError()

    price = element[0].attrib['content']
    return Decimal(price)