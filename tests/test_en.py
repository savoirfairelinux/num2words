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
            num2words(0, lang='en', to='ordinal'),
            'zeroth'
        )
        self.assertEqual(
            num2words(1, lang='en', to='ordinal'),
            'first'
        )
        self.assertEqual(
            num2words(13, lang='en', to='ordinal'),
            'thirteenth'
        )
        self.assertEqual(
            num2words(22, lang='en', to='ordinal'),
            'twenty-second'
        )
        self.assertEqual(
            num2words(12, lang='en', to='ordinal'),
            'twelfth'
        )
        self.assertEqual(
            num2words(130, lang='en', to='ordinal'),
            'one hundred and thirtieth'
        )
        self.assertEqual(
            num2words(1003, lang='en', to='ordinal'),
            'one thousand and third'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='en', to='ordinal_num'), '10th')
        self.assertEqual(num2words(21, lang='en', to='ordinal_num'), '21st')
        self.assertEqual(num2words(102, lang='en', to='ordinal_num'), '102nd')
        self.assertEqual(num2words(73, lang='en', to='ordinal_num'), '73rd')

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(num2words(12.5), "twelve point five")
        self.assertEqual(num2words(12.51), "twelve point five one")
        self.assertEqual(num2words(12.53), "twelve point five three")
        self.assertEqual(num2words(12.59), "twelve point five nine")

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
            num2words('38.4', lang='en', to='currency', separator=' and',
                      cents=False, currency='USD'),
            "thirty-eight dollars and 40 cents"
        )
        self.assertEqual(
            num2words('0', lang='en', to='currency', separator=' and',
                      cents=False, currency='USD'),
            "zero dollars and 00 cents"
        )

        self.assertEqual(
            num2words('1.01', lang='en', to='currency', separator=' and',
                      cents=True, currency='USD'),
            "one dollar and one cent"
        )

        self.assertEqual(
            num2words('4778.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='USD', adjective=True),
            'four thousand, seven hundred and seventy-eight US dollars'
            ' and zero cents')

        self.assertEqual(
            num2words('4778.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='USD'),
            'four thousand, seven hundred and seventy-eight dollars and'
            ' zero cents')

        self.assertEqual(
            num2words('1.1', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "one peso and ten cents"
        )

        self.assertEqual(
            num2words('158.3', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "one hundred and fifty-eight pesos and thirty cents"
        )

        self.assertEqual(
            num2words('2000.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "two thousand pesos and zero cents"
        )

        self.assertEqual(
            num2words('4.01', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "four pesos and one cent"
        )

    def test_to_year(self):
        # issue 141
        # "e2 e2"
        self.assertEqual(num2words(1990, lang='en', to='year'),
                         'nineteen ninety')
        self.assertEqual(num2words(5555, lang='en', to='year'),
                         'fifty-five fifty-five')
        self.assertEqual(num2words(2017, lang='en', to='year'),
                         'twenty seventeen')
        self.assertEqual(num2words(1066, lang='en', to='year'),
                         'ten sixty-six')
        self.assertEqual(num2words(1865, lang='en', to='year'),
                         'eighteen sixty-five')
        # "e3 and e1"; "e2 oh-e1"; "e3"
        self.assertEqual(num2words(3000, lang='en', to='year'),
                         'three thousand')
        self.assertEqual(num2words(2001, lang='en', to='year'),
                         'two thousand and one')
        self.assertEqual(num2words(1901, lang='en', to='year'),
                         'nineteen oh-one')
        self.assertEqual(num2words(2000, lang='en', to='year'),
                         'two thousand')
        self.assertEqual(num2words(905, lang='en', to='year'),
                         'nine oh-five')
        # "e2 hundred"; "e3"
        self.assertEqual(num2words(6600, lang='en', to='year'),
                         'sixty-six hundred')
        self.assertEqual(num2words(1900, lang='en', to='year'),
                         'nineteen hundred')
        self.assertEqual(num2words(600, lang='en', to='year'),
                         'six hundred')
        self.assertEqual(num2words(50, lang='en', to='year'),
                         'fifty')
        self.assertEqual(num2words(0, lang='en', to='year'),
                         'zero')
        # suffixes
        self.assertEqual(num2words(-44, lang='en', to='year'),
                         'forty-four BC')
        self.assertEqual(num2words(-44, lang='en', to='year', suffix='BCE'),
                         'forty-four BCE')
        self.assertEqual(num2words(1, lang='en', to='year', suffix='AD'),
                         'one AD')
        self.assertEqual(num2words(66, lang='en', to='year',
                                   suffix='m.y.a.'),
                         'sixty-six m.y.a.')
        self.assertEqual(num2words(-66000000, lang='en', to='year'),
                         'sixty-six million BC')
