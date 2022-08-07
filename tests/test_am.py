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
        self.assertEqual(num2words(199, lang='am'), "አንድ መቶ ዘጠና ዘጠኝ")

    def test_ordinal(self):
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

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='am', to='currency', cents=False, currency='ETB'),
            "ሠላሳ ስምንት ብር ከ 40 ሳንቲም"
        )
        self.assertEqual(
            num2words('0', lang='am', to='currency', separator=' እና', cents=True, currency='ETB'),
            "ዜሮ ብር እና ዜሮ ሳንቲም"
        )

        self.assertEqual(
            num2words('1.50', lang='am', to='currency', cents=True, currency='ETB'),
            "አንድ ብር ከ አምሳ ሳንቲም"
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
