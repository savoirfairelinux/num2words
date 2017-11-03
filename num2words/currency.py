from __future__ import division

from decimal import Decimal


def parse_currency_parts(value):
    if isinstance(value, int):
        # assume cents if value is integer
        negative = value < 0
        value = abs(value)
        integer, cents = divmod(value, 100)

    elif isinstance(value, Decimal):
        negative = value < 0
        value = abs(value)
        integer, fraction = divmod(value, 1)
        integer = int(integer)
        cents = int(fraction * 100)

    else:
        # @TODO consider using something (babel) that does locale aware parsing
        value = str(value).replace(',', '.')
        negative = value.startswith('-')

        if negative:
            value = value.lstrip('-')

        if '.' in value:
            integer, fraction = value.rsplit('.', 1)
            fraction = fraction.ljust(2, "0")
        else:
            integer, fraction = value, 0

        integer = int(integer)
        cents = int(fraction)

    return integer, cents, negative


def prefix_currency(prefix, base):
    return tuple("%s %s" % (prefix, i) for i in base)
