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
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='am'), 'መቶ')
        self.assertEqual(num2words(100000, lang='am'), 'አንድ መቶ ሺህ')
        self.assertEqual(num2words(101, lang='am'), 'አንድ መቶ አንድ')
        self.assertEqual(num2words(568476685, lang='am'), 'አምስት መቶ ስድሳ ስምንት mሚሊዮን, አራት መቶ ሰባ ስድስት ሺህ, ስድስት መቶ ሰማኒያ አምስት')
        self.assertEqual(num2words(56847, lang='am'), 'አምሳ ስድስት ሺህ, ስምንት መቶ አርባ ሰባት')
        self.assertEqual(num2words(1111111111111111111, lang='am'), 'አንድ quintሚሊዮን, አንድ መቶ አሥራ አንድ quadrሚሊዮን, አንድ መቶ አሥራ አንድ trሚሊዮን, አንድ መቶ አሥራ አንድ bቢሊዮን, አንድ መቶ አሥራ አንድ mሚሊዮን, አንድ መቶ አሥራ አንድ ሺህ, አንድ መቶ አሥራ አንድ')
        self.assertEqual(num2words(999999999, lang='am'), 'ዘጠኝ መቶ ዘጠና ዘጠኝ mሚሊዮን, ዘጠኝ መቶ ዘጠና ዘጠኝ ሺህ, ዘጠኝ መቶ ዘጠና ዘጠኝ')
        self.assertEqual(num2words(29498237468376240, lang="am"), 'ሃያ ዘጠኝ quadrሚሊዮን, አራት መቶ ዘጠና ስምንት trሚሊዮን, ሁለት መቶ ሠላሳ ሰባት bቢሊዮን, አራት መቶ ስድሳ ስምንት mሚሊዮን, ሦስት መቶ ሰባ ስድስት ሺህ, ሁለት መቶ አርባ')
        self.assertEqual(num2words(110110, lang='am'), 'አንድ መቶ አሥር ሺህ, አንድ መቶ አሥር')

    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='am'), 'አንድ መቶ ዘጠና ዘጠኝ')

    def test_to_ordinal(self):
        self.assertEqual(
            num2words(1, lang='am', to='ordinal'),
            'አንደኛ'
        )
        self.assertEqual(
            num2words(13, lang='am', to='ordinal'),
            'አሥራ ሦስተኛ'
        )
        self.assertEqual(
            num2words(22, lang='am', to='ordinal'),
            'ሃያ ሁለተኛ'
        )
        self.assertEqual(
            num2words(10000, lang='am', to='ordinal'),
            'አሥር ሺህኛ'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(num2words(10, lang='am', to='ordinal_num'), '10ኛ')
        self.assertEqual(num2words(21, lang='am', to='ordinal_num'), '21ኛ')
        self.assertEqual(num2words(102, lang='am', to='ordinal_num'), '102ኛ')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='am'), 'አሥራ ሁለት ነጥብ አምስት')
        self.assertEqual(num2words(12.51, lang='am'), 'አሥራ ሁለት ነጥብ አምስት አንድ')
        self.assertEqual(num2words(12.53, lang='am'), 'አሥራ ሁለት ነጥብ አምስት ሦስት')

    def test_to_overflow(self):
        with self.assertRaises(OverflowError):
            num2words('1000000000000000000000000000000000000000000000000000000'
                      '0000000000000000000000000000000000000000000000000000000'
                      '0000000000000000000000000000000000000000000000000000000'
                      '0000000000000000000000000000000000000000000000000000000'
                      '0000000000000000000000000000000000000000000000000000000'
                      '00000000000000000000000000000000', lang='am')

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='am', to='currency', cents=False,
                      currency='ETB'), 'ሠላሳ ስምንት ብር ከ 40 ሳንቲም'
        )
        self.assertEqual(
            num2words('0', lang='am', to='currency', separator=' እና',
                      cents=True, currency='ETB'), 'ዜሮ ብር እና ዜሮ ሳንቲም'
        )

        self.assertEqual(
            num2words('1.50', lang='am', to='currency', cents=True,
                      currency='ETB'), 'አንድ ብር ከ አምሳ ሳንቲም'
        )

    def test_to_year(self):
        self.assertEqual(num2words(1990, lang='am', to='year'),
                         'አሥራ ዘጠኝ መቶ ዘጠና')
        self.assertEqual(num2words(5555, lang='am', to='year'),
                         'አምሳ አምስት መቶ አምሳ አምስት')
        self.assertEqual(num2words(2017, lang='am', to='year'),
                         'ሁለት ሺህ አሥራ ሰባት')
        self.assertEqual(num2words(1066, lang='am', to='year'),
                         'አንድ ሺህ ስድሳ ስድስት')
        self.assertEqual(num2words(1865, lang='am', to='year'),
                         'አሥራ ስምንት መቶ ስድሳ አምስት')
