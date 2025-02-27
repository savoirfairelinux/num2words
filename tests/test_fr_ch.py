# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (70, 'septante'),
    (79, 'septante-neuf'),
    (89, 'huitante-neuf'),
    (95, 'nonante-cinq'),
    (729, 'sept cents vingt-neuf'),
    (894, 'huit cents nonante-quatre'),
    (999, 'neuf cents nonante-neuf'),
    (7232, 'sept mille deux cents trente-deux'),
    (8569, 'huit mille cinq cents soixante-neuf'),
    (9539, 'neuf mille cinq cents trente-neuf'),
    (1000000, 'un millions'),
    (1000001, 'un millions un'),
    (4000000, 'quatre millions'),
    (10000000000000, 'dix billions'),
    (100000000000000, 'cent billions'),
    (1000000000000000000, 'un trillions'),
    (1000000000000000000000, 'un trilliards'),
    (10000000000000000000000000, 'dix quadrillions')
)

TEST_CASES_ORDINAL = (
    (1, 'premier'),
    (8, 'huitième'),
    (12, 'douzième'),
    (14, 'quatorzième'),
    (28, 'vingt-huitième'),
    (100, 'centième'),
    (1000, 'millième'),
    (1000000, 'un millionsième'),
    (1000000000000000, 'un billiardsième'),
    (1000000000000000000, 'un trillionsième')  # over 1e18 is not supported
)

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'un euro et zéro centimes'),
    (2.01, 'deux euros et un centime'),
    (8.10, 'huit euros et dix centimes'),
    (12.26, 'douze euros et vingt-six centimes'),
    (21.29, 'vingt et un euros et vingt-neuf centimes'),
    (81.25, 'huitante et un euros et vingt-cinq centimes'),
    (100.00, 'cent euros et zéro centimes'),
)

TEST_CASES_TO_CURRENCY_FRF = (
    (1.00, 'un franc et zéro centimes'),
    (2.01, 'deux francs et un centime'),
    (8.10, 'huit francs et dix centimes'),
    (12.27, 'douze francs et vingt-sept centimes'),
    (21.29, 'vingt et un francs et vingt-neuf centimes'),
    (81.25, 'huitante et un francs et vingt-cinq centimes'),
    (100.00, 'cent francs et zéro centimes'),
)


class Num2WordsENTest(TestCase):
    def test_ordinal_special_joins(self):
        self.assertEqual(
            num2words(5, ordinal=True, lang='fr_CH'), "cinquième"
        )
        self.assertEqual(
            num2words(6, ordinal=True, lang='fr_CH'), "sixième"
        )
        self.assertEqual(
            num2words(35, ordinal=True, lang='fr_CH'), "trente-cinquième"
        )
        self.assertEqual(num2words(9, ordinal=True, lang='fr_CH'), "neuvième")
        self.assertEqual(
            num2words(49, ordinal=True, lang='fr_CH'), "quarante-neuvième"
        )
        self.assertEqual(num2words(71, lang='fr_CH'), "septante et un")
        self.assertEqual(num2words(81, lang='fr_CH'), "huitante et un")
        self.assertEqual(num2words(80, lang='fr_CH'), "huitante")
        self.assertEqual(num2words(880, lang='fr_CH'), "huit cents huitante")
        self.assertEqual(
            num2words(91, ordinal=True, lang='fr_CH'), "nonante et unième"
        )
        self.assertEqual(num2words(53, lang='fr_CH'), "cinquante-trois")

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='fr_CH'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='fr_CH', ordinal=True),
                test[1]
            )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='fr_CH', to='currency'),
                test[1]
            )

    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='fr_CH', to='currency',
                          currency='FRF'),
                test[1]
            )
