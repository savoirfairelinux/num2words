# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsLVTest(TestCase):
    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', seperator=' un',
                      cents=False, currency='EUR'),
            "trīsdesmit astoņi eiro un 40 centi"
        )

        # EUR legal form
        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', seperator=' un',
                      cents=False, currency='EUR_LEGAL'),
            "trīsdesmit astoņi euro un 40 centi"
        )

    def test_fractions(self):
        self.assertEqual(num2words(5.2, lang='lv'), "pieci komats divi")
        self.assertEqual(
            num2words(561.42, lang='lv'),
            "pieci simti sešdesmit viens komats četrdesmit divi"
        )
