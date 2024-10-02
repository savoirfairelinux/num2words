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
    (1, 'un'),
    (2, 'deux'),
    (3, 'trois'),
    (5.5, 'cinq virgule cinq'),
    (11, 'onze'),
    (12, 'douze'),
    (16, 'seize'),
    (17.42, 'dix-sept virgule quatre deux'),
    (19, 'dix-neuf'),
    (20, 'vingt'),
    (21, 'vingt et un'),
    (26, 'vingt-six'),
    (27.312, 'vingt-sept virgule trois un deux'),
    (28, 'vingt-huit'),
    (30, 'trente'),
    (31, 'trente et un'),
    (40, 'quarante'),
    (44, 'quarante-quatre'),
    (50, 'cinquante'),
    (53.486, 'cinquante-trois virgule quatre huit six'),
    (55, 'cinquante-cinq'),
    (60, 'soixante'),
    (67, 'soixante-sept'),
    (70, 'soixante-dix'),
    (79, 'soixante-dix-neuf'),
    (89, 'quatre-vingt-neuf'),
    (95, 'quatre-vingt-quinze'),
    (100, 'cent'),
    (101, 'cent un'),
    (199, 'cent quatre-vingt-dix-neuf'),
    (203, 'deux cent trois'),
    (287, 'deux cent quatre-vingt-sept'),
    (300.42, 'trois cents virgule quatre deux'),
    (356, 'trois cent cinquante-six'),
    (400, 'quatre cents'),
    (434, 'quatre cent trente-quatre'),
    (578, 'cinq cent soixante-dix-huit'),
    (689, 'six cent quatre-vingt-neuf'),
    (729, 'sept cent vingt-neuf'),
    (894, 'huit cent quatre-vingt-quatorze'),
    (999, 'neuf cent quatre-vingt-dix-neuf'),
    (1000, 'mille'),
    (1001, 'mille un'),
    (1097, 'mille quatre-vingt-dix-sept'),
    (1104, 'mille cent quatre'),
    (1243, 'mille deux cent quarante-trois'),
    (2385, 'deux mille trois cent quatre-vingt-cinq'),
    (3766, 'trois mille sept cent soixante-six'),
    (4196, 'quatre mille cent quatre-vingt-seize'),
    (4196.42, 'quatre mille cent quatre-vingt-seize virgule quatre deux'),
    (5846, 'cinq mille huit cent quarante-six'),
    (6459, 'six mille quatre cent cinquante-neuf'),
    (7232, 'sept mille deux cent trente-deux'),
    (8569, 'huit mille cinq cent soixante-neuf'),
    (9539, 'neuf mille cinq cent trente-neuf'),
    (1000000, 'un million'),
    (1000001, 'un million un'),
    (4000000, 'quatre millions'),
    (4000004, 'quatre millions quatre'),
    (4300000, 'quatre millions trois cent mille'),
    (80000000, 'quatre-vingts millions'),
    (300000000, 'trois cents millions'),
    (10000000000000, 'dix billions'),
    (10000000000010, 'dix billions dix'),
    (100000000000000, 'cent billions'),
    (1000000000000000000, 'un trillion'),
    (1000000000000000000000, 'un trilliard'),
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
    (1000000, 'un millionième'),
    (1000000000000000, 'un billiardième'),
    (1000000000000000000, 'un trillionième')  # over 1e18 is not supported
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1er'),
    (8, '8me'),
    (11, '11me'),
    (12, '12me'),
    (14, '14me'),
    (21, '21me'),
    (28, '28me'),
    (100, '100me'),
    (101, '101me'),
    (1000, '1000me'),
    (1000000, '1000000me')
)

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'un euro et zéro centimes'),
    (2.01, 'deux euros et un centime'),
    (8.10, 'huit euros et dix centimes'),
    (12.26, 'douze euros et vingt-six centimes'),
    (21.29, 'vingt et un euros et vingt-neuf centimes'),
    (81.25, 'quatre-vingt-un euros et vingt-cinq centimes'),
    (100.00, 'cent euros et zéro centimes'),
)

TEST_CASES_TO_CURRENCY_FRF = (
    (1.00, 'un franc et zéro centimes'),
    (2.01, 'deux francs et un centime'),
    (8.10, 'huit francs et dix centimes'),
    (12.27, 'douze francs et vingt-sept centimes'),
    (21.29, 'vingt et un francs et vingt-neuf centimes'),
    (81.25, 'quatre-vingt-un francs et vingt-cinq centimes'),
    (100.00, 'cent francs et zéro centimes'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'un dollar et zéro cents'),
    (2.01, 'deux dollars et un cent'),
    (8.10, 'huit dollars et dix cents'),
    (12.26, 'douze dollars et vingt-six cents'),
    (21.29, 'vingt et un dollars et vingt-neuf cents'),
    (81.25, 'quatre-vingt-un dollars et vingt-cinq cents'),
    (100.00, 'cent dollars et zéro cents'),
)


class Num2WordsFRTest(TestCase):
    def test_ordinal_special_joins(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/18
        self.assertEqual(
            num2words(5, ordinal=True, lang='fr'), "cinquième"
        )
        self.assertEqual(
            num2words(35, ordinal=True, lang='fr'), "trente-cinquième"
        )
        self.assertEqual(
            num2words(9, ordinal=True, lang='fr'), "neuvième"
        )
        self.assertEqual(
            num2words(49, ordinal=True, lang='fr'), "quarante-neuvième"
        )

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='fr'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='fr', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='fr', to='ordinal_num'),
                test[1]
            )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='fr', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='fr', to='currency', currency='FRF'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='fr', to='currency', currency='USD'),
                test[1]
            )

    def test_max_numbers(self):

        with self.assertRaises(OverflowError) as context:
            num2words(10 ** 700, lang='fr')

        self.assertTrue('trop grand' in str(context.exception))
