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

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'een Euro an null Cent'),
    (2.01, 'zwee Euro an een Cent'),
    (8.10, 'aacht Euro an zéng Cent'),
    (12.26, 'zwielef Euro an sechsanzwanzeg Cent'),
    (21.29, 'eenanzwanzeg Euro an nénganzwanzeg Cent'),
    (81.25, 'eenanachtzeg Euro an fënnefanzwanzeg Cent'),
    (100.00, 'honnert Euro an null Cent'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'een Dollar an null Cent'),
    (2.01, 'zwee Dollar an een Cent'),
    (8.10, 'aacht Dollar an zéng Cent'),
    (12.26, 'zwielef Dollar an sechsanzwanzeg Cent'),
    (21.29, 'eenanzwanzeg Dollar an nénganzwanzeg Cent'),
    (81.25, 'eenanachtzeg Dollar an fënnefanzwanzeg Cent'),
    (100.00, 'honnert Dollar an null Cent'),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, 'een Pond an null Pence'),
    (2.01, 'zwee Pond an een Penny'),
    (8.10, 'aacht Pond an zéng Pence'),
    (12.26, 'zwielef Pond an sechsanzwanzeg Pence'),
    (21.29, 'eenanzwanzeg Pond an nénganzwanzeg Pence'),
    (81.25, 'eenanachtzeg Pond an fënnefanzwanzeg Pence'),
    (100.00, 'honnert Pond an null Pence'),
)

TEST_CASES_TO_CARDINAL =(
    (81, 'eenanachtzeg'),
    (51, 'eenafofzeg'),
    (35, 'fënnefandrësseg'),
    (101, 'honnerteent'),
    (1101, 'dausendeenhonnerteent'),
    (10101011, 'zéng Milliounen honnerteendausendeelef'),
    (41237894, 'eenavéierzeg Milliounen zweehonnertsiwenandrëssegdausendaachthonnertvéierannonzeg'),
)


class Num2WordsLUTest(TestCase):

    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(0, ordinal=True, lang='lu'), "nullt")
        self.assertEqual(num2words(1, ordinal=True, lang='lu'), "éischt")
        self.assertEqual(num2words(7, ordinal=True, lang='lu'), "siwent")
        self.assertEqual(num2words(8, ordinal=True, lang='lu'), "aacht")
        self.assertEqual(num2words(12, ordinal=True, lang='lu'), "zwieleft")
        self.assertEqual(num2words(17, ordinal=True, lang='lu'), "siwwenzéngt")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            num2words(81, ordinal=True, lang='lu'), "eenanachtzegst"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(
            num2words(100, ordinal=True, lang='lu'), "honnertst"
        )
        self.assertEqual(
            num2words(1000, ordinal=True, lang='lu'), "dausendst"
        )
        self.assertEqual(
            num2words(4000, ordinal=True, lang='lu'), "véierdausendst"
        )
        self.assertEqual(
            num2words(1000000, ordinal=True, lang='lu'), "eng milliounst"
        )

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(num2words(100, lang='lu'), "honnert")
        self.assertEqual(num2words(1000, lang='lu'), "dausend")
        self.assertEqual(num2words(5000, lang='lu'), "fënnefdausend")
        self.assertEqual(num2words(10000, lang='lu'), "zéngdausend")
        self.assertEqual(num2words(1000000, lang='lu'), "eng Millioun")
        self.assertEqual(num2words(2000000, lang='lu'), "zwou Milliounen")
        self.assertEqual(num2words(4000000000, lang='lu'), "véier Milliarden")
        self.assertEqual(num2words(1000000000, lang='lu'), "eng Milliard")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(3.486, lang='lu'), "dräi Komma véier aacht sechs"
        )

    def test_giant_cardinal_for_merge(self):
        self.assertEqual(
            num2words(4500072900000111, lang='lu'),
            "véier Billiarden fënnefhonnert Billionen " +
            "zweeasiwwenzeg Milliarden nénghonnert Milliounen honnerteelef"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(7, to="ordinal_num", lang='lu'), "7.")
        self.assertEqual(num2words(81, to="ordinal_num", lang='lu'), "81.")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='lu')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang='lu')

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='lu', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='lu', to='currency', currency='USD'),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang='lu', to='currency', currency='GBP'),
                test[1]
            )

    def test_year(self):
        self.assertEqual(num2words(2002, to='year', lang='lu'),
                         'zweedausendzwee')

    def test_year_before_2000(self):
        self.assertEqual(num2words(1780, to='year', lang='lu'),
                         'siwwenzénghonnertachtzeg')
