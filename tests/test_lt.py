# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsLTTest(TestCase):
    def test_to_cardinal(self):
        self.assertEqual(num2words(100, lang='lt'), 'vienas šimtas')
        self.assertEqual(num2words(101, lang='lt'), 'vienas šimtas vienas')
        self.assertEqual(num2words(110, lang='lt'), 'vienas šimtas dešimt')
        self.assertEqual(num2words(115, lang='lt'),
                         'vienas šimtas penkiolika')
        self.assertEqual(num2words(123, lang='lt'),
                         'vienas šimtas dvidešimt trys')
        self.assertEqual(num2words(1000, lang='lt'), 'vienas tūkstantis')
        self.assertEqual(num2words(1001, lang='lt'),
                         'vienas tūkstantis vienas')
        self.assertEqual(num2words(2012, lang='lt'),
                         'du tūkstančiai dvylika')
        self.assertEqual(
            num2words(1234567890, lang='lt'),
            "vienas milijardas du šimtai trisdešimt keturi milijonai "
            "penki šimtai šešiasdešimt septyni tūkstančiai aštuoni šimtai "
            "devyniasdešimt")
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='lt'),
            "du šimtai penkiolika naintilijonų keturi šimtai šešiasdešimt "
            "vienas oktilijonas keturi šimtai septyni septilijonai aštuoni "
            "šimtai devyniasdešimt du sikstilijonai trisdešimt devyni "
            "kvintilijonai du kvadrilijonai vienas šimtas penkiasdešimt "
            "septyni trilijonai vienas šimtas aštuoniasdešimt devyni "
            "milijardai aštuoni šimtai aštuoniasdešimt trys milijonai "
            "devyni šimtai vienas tūkstantis šeši šimtai "
            "septyniasdešimt šeši")
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='lt'),
            "septyni šimtai devyniolika naintilijonų devyniasdešimt keturi "
            "oktilijonai du šimtai trisdešimt keturi septilijonai šeši "
            "šimtai devyniasdešimt trys sikstilijonai šeši šimtai "
            "šešiasdešimt trys kvintilijonai trisdešimt keturi kvadrilijonai "
            "aštuoni šimtai dvidešimt du trilijonai aštuoni šimtai dvidešimt "
            "keturi milijardai trys šimtai aštuoniasdešimt keturi milijonai "
            "du šimtai dvidešimt tūkstančių du šimtai devyniasdešimt vienas")

        # print(fill(n2w(1000000000000000000000000000000)))
        # naintilijonas

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='lt', to='ordinal')

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='LTL'),
            'vienas litas, nulis centų'
        )
        self.assertEqual(
            num2words(1234.56, lang='lt', to='currency', currency='LTL'),
            'vienas tūkstantis du šimtai trisdešimt keturi litai, '
            'penkiasdešimt šeši centai'
        )
        self.assertEqual(
            num2words(-1251985, lang='lt', to='currency', currency='EUR',
                      cents=False),
            'minus dvylika tūkstančių penki šimtai devyniolika eurų, '
            '85 centai'
        )
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='EUR'),
            'vienas euras, nulis centų'
        )
        self.assertEqual(
            num2words(1234.56, lang='lt', to='currency', currency='EUR'),
            'vienas tūkstantis du šimtai trisdešimt keturi eurai, '
            'penkiasdešimt šeši centai'
        )
