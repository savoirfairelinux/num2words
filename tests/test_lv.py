# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsLVTest(TestCase):
    def test_to_cardinal(self):
        self.assertEqual(num2words(0, lang='lv'), 'nulle')
        self.assertEqual(num2words(5, lang='lv'), "pieci")
        self.assertEqual(num2words(15, lang='lv'), "piecpadsmit")
        self.assertEqual(num2words(154, lang='lv'), "simts piecdesmit četri")
        self.assertEqual(num2words(101, lang='lv'), "simtu viens")
        self.assertEqual(
            num2words(1135, lang='lv'), "tūkstotis simts trīsdesmit pieci"
        )
        self.assertEqual(
            num2words(418531, lang='lv'),
            "četri simti astoņpadsmit tūkstoši pieci simti trīsdesmit viens"
        )
        self.assertEqual(
            num2words(1000139, lang='lv'),
            "miljons simts trīsdesmit deviņi"
        )

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

        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', seperator=' un',
                      cents=False, currency='USD', adjective=False),
            "trīsdesmit astoņi dolāri un 40 centi"
        )

        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', seperator=' un',
                      cents=False, currency='USD', adjective=True),
            "trīsdesmit astoņi ASV dolāri un 40 centi"
        )

    def test_fractions(self):
        self.assertEqual(num2words(5.2, lang='lv'), "pieci komats divi")
        self.assertEqual(
            num2words(561.42, lang='lv'),
            "pieci simti sešdesmit viens komats četrdesmit divi"
        )
