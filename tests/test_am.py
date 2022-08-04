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


class Num2WordsAMTest(TestCase):
    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='am'), "մեկ հարյուր իննսունինը")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='am', to='ordinal'),
            'զրոերորդ'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='am', to='ordinal_num'),
                         '10րդ')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='am'), "տասներկու ամբողջ հինգ")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='am', to='currency', separator=' և',
                      cents=False, currency='USD'),
            "երեսունութ dollars և 40 cents"
        )

    def test_to_year(self):
        self.assertEqual(num2words(1990, lang='am', to='year'),
                         'տասնինը իննսուն')
