from decimal import Decimal
from unittest import TestCase

from num2words.currency import parse_currency_parts


class CurrencyTestCase(TestCase):
    def test_parse_currency_parts(self):
        # integer cents
        self.assertEqual(parse_currency_parts(101), (1, 1, False))
        self.assertEqual(parse_currency_parts(-123), (1, 23, True))

        # decimal
        self.assertEqual(parse_currency_parts(Decimal("1.01")), (1, 1, False))
        self.assertEqual(parse_currency_parts(Decimal("-1.23")), (1, 23, True))
        self.assertEqual(parse_currency_parts(Decimal("-1.233")),
                         (1, 23, True))

        # string
        self.assertEqual(parse_currency_parts("1.01"), (1, 1, False))
        self.assertEqual(parse_currency_parts("-1.23"), (1, 23, True))
        self.assertEqual(parse_currency_parts("-1.2"), (1, 20, True))
        self.assertEqual(parse_currency_parts("1"), (1, 0, False))

        # float
        self.assertEqual(parse_currency_parts(1.01), (1, 1, False))
        self.assertEqual(parse_currency_parts(-1.23), (1, 23, True))
        self.assertEqual(parse_currency_parts(-1.2), (1, 20, True))
