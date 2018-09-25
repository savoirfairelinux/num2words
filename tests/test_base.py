from __future__ import unicode_literals

from decimal import Decimal
from unittest import TestCase

from num2words.base import Num2Word_Base


class Num2WordBaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(Num2WordBaseTest, cls).setUpClass()
        cls.base = Num2Word_Base()

    def test_to_currency_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.base.to_currency(Decimal('1.00'), currency='EUR')
