# -*- coding: utf-8 -*-
from unittest import TestCase

from num2words import num2words


class NegativeDecimalTest(TestCase):
    def test_turkish_negative_fraction_keeps_sign(self):
        for value in (0.4, 0.12, 0.99, 1.4, 10.25):
            with self.subTest(value=value):
                self.assertEqual(
                    num2words(-value, lang='tr'),
                    'eksi' + num2words(value, lang='tr'))
        self.assertEqual(num2words(-0.4, lang='tr'), u'eksisıfırvirgülkırk')

    def test_english_negative_fraction(self):
        self.assertEqual(num2words(-0.4), 'minus zero point four')

    def test_turkish_zero_is_unsigned(self):
        self.assertEqual(num2words(-0.0, lang='tr'), num2words(0, lang='tr'))
