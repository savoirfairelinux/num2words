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
from num2words.lang_LB import Num2Word_LB

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
    (1.00, 'een Pond an null Pennies'),
    (2.01, 'zwee Pond an een Penny'),
    (8.10, 'aacht Pond an zéng Pennies'),
    (12.26, 'zwielef Pond an sechsanzwanzeg Pennies'),
    (21.29, 'eenanzwanzeg Pond an nénganzwanzeg Pennies'),
    (81.25, 'eenanachtzeg Pond an fënnefanzwanzeg Pennies'),
    (100.00, 'honnert Pond an null Pennies'),
)

TEST_CASES_TO_CURRENCY_CHF = (
    (1.00, 'een Schwäizer Frang an null Rappen'),
    (2.01, 'zwee Schwäizer Frang an een Rappen'),
    (8.10, 'aacht Schwäizer Frang an zéng Rappen'),
    (12.26, 'zwielef Schwäizer Frang an sechsanzwanzeg Rappen'),
    (21.29, 'eenanzwanzeg Schwäizer Frang an nénganzwanzeg Rappen'),
    (81.25, 'eenanachtzeg Schwäizer Frang an fënnefanzwanzeg Rappen'),
    (100.00, 'honnert Schwäizer Frang an null Rappen'),
)


class Num2WordsLBTest(TestCase):

    def setUp(self):
        self.n2w = Num2Word_LB()

    def test_ordinal_less_than_twenty(self):
        self.assertEqual(num2words(1, ordinal=True, lang='lb'), "éischt")
        self.assertEqual(num2words(2, ordinal=True, lang='lb'), "zweet")
        self.assertEqual(num2words(3, ordinal=True, lang='lb'), "drëtt")
        self.assertEqual(num2words(7, ordinal=True, lang='lb'), "siwent")
        self.assertEqual(num2words(8, ordinal=True, lang='lb'), "aacht")
        self.assertEqual(num2words(12, ordinal=True, lang='lb'), "zwieleft")
        self.assertEqual(num2words(17, ordinal=True, lang='lb'), "siwwenzéngt")

    def test_ordinal_more_than_twenty(self):
        self.assertEqual(
            num2words(21, ordinal=True, lang='lb'), "eenanzwanzegst"
        )
        self.assertEqual(
            num2words(81, ordinal=True, lang='lb'), "eenanachtzegst"
        )

    def test_ordinal_at_crucial_number(self):
        self.assertEqual(
            num2words(100, ordinal=True, lang='lb'), "honnertst"
        )
        self.assertEqual(
            num2words(1000, ordinal=True, lang='lb'), "dausendst"
        )
        self.assertEqual(
            num2words(4000, ordinal=True, lang='lb'), "véierdausendst"
        )
        self.assertEqual(
            num2words(1000000, ordinal=True, lang='lb'), "milliounst"
        )
        self.assertEqual(
            num2words(2000000, ordinal=True, lang='lb'), "zweemilliounst"
        )
        self.assertEqual(
            num2words(1000000000, ordinal=True, lang='lb'), "milliardst"
        )
        self.assertEqual(
            num2words(5000000000, ordinal=True, lang='lb'),
            "fënnefmilliardst"
        )

    def test_cardinal_at_some_numbers(self):
        self.assertEqual(num2words(100, lang='lb'), "honnert")
        self.assertEqual(num2words(1000, lang='lb'), "dausend")
        self.assertEqual(num2words(5000, lang='lb'), "fënnefdausend")
        self.assertEqual(num2words(10000, lang='lb'), "zéngdausend")
        self.assertEqual(num2words(1000000, lang='lb'), "eng Millioun")
        self.assertEqual(num2words(2000000, lang='lb'), "zwee Milliounen")
        self.assertEqual(num2words(4000000000, lang='lb'), "véier Milliarden")
        self.assertEqual(num2words(1000000000, lang='lb'), "eng Milliard")

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(3.486, lang='lb'), "dräi Komma véier aacht sechs"
        )

    def test_giant_cardinal_for_merge(self):
        self.assertEqual(
            num2words(4500072900000111, lang='lb'),
            "véier Billiarden fënnefhonnert Billiounen " +
            "zweeasiwwenzeg Milliarden nénghonnert Milliounen honnerteelef"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(7, to="ordinal_num", lang='lb'), "7.")
        self.assertEqual(num2words(81, to="ordinal_num", lang='lb'), "81.")

    def test_ordinal_for_negative_numbers(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='lb')

    def test_ordinal_for_floating_numbers(self):
        self.assertRaises(TypeError, num2words, 2.453, ordinal=True, lang='lb')

    def test_n_drop_rule(self):
        # Test the n-drop rule (Eifel rule)
        self.assertTrue(self.n2w.should_drop_n("millioun"))   # Before m (consonant)
        self.assertFalse(self.n2w.should_drop_n("null"))      # Before n (keep n)
        self.assertFalse(self.n2w.should_drop_n("dollar"))    # Before d (keep n)
        self.assertFalse(self.n2w.should_drop_n("zwanzeg"))   # Before z (keep n)
        self.assertTrue(self.n2w.should_drop_n("frang"))      # Before f (consonant)

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='lb', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='lb', to='currency', currency='USD'),
                test[1]
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang='lb', to='currency', currency='GBP'),
                test[1]
            )

    def test_currency_chf(self):
        for test in TEST_CASES_TO_CURRENCY_CHF:
            self.assertEqual(
                num2words(test[0], lang='lb', to='currency', currency='CHF'),
                test[1]
            )

    def test_year(self):
        self.assertEqual(num2words(2002, to='year', lang='lb'),
                         'zweedausendzwee')

    def test_year_before_2000(self):
        self.assertEqual(num2words(1780, to='year', lang='lb'),
                         'siwwenzénghonnertachtzeg')
                         
    def test_year_bc(self):
        self.assertEqual(num2words(-44, to='year', lang='lb'),
                         'véieravéierzeg viru Christus')


if __name__ == '__main__':
    unittest.main()
