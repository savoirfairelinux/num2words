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

from unittest import TestCase

from num2words import num2words


class Num2WordsENTest(TestCase):
    def test_and_join_199(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/8
        self.assertEqual(num2words(199), "one hundred and ninety-nine")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='am', to='ordinal'),
            'զրոերորդ'
        )
        self.assertEqual(
            num2words(1, lang='am', to='ordinal'),
            'առաջին'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='am', to='ordinal_num'), '10երորդ')

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(num2words(12.5), "տասներկու ամբողջ հինգ")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")

    def test_to_currency(self):
        pass

    def test_to_year(self):
        pass
