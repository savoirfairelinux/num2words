# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2020, Hamidreza Kalbasi.  All Rights Reserved.

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


class Num2WordsFATest(TestCase):
    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='fa'), "صد و نود و نه")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='fa', to='ordinal'),
            'صفرم'
        )
        self.assertEqual(
            num2words(1, lang='fa', to='ordinal'),
            'یکم'
        )
        self.assertEqual(
            num2words(13, lang='fa', to='ordinal'),
            'سیزدهم'
        )
        self.assertEqual(
            num2words(23, lang='fa', to='ordinal'),
            'بیست و سوم'
        )
        self.assertEqual(
            num2words(12, lang='fa', to='ordinal'),
            'دوازدهم'
        )
        self.assertEqual(
            num2words(113, lang='fa', to='ordinal'),
            'صد و سیزدهم'
        )
        self.assertEqual(
            num2words(103, lang='fa', to='ordinal'),
            'صد و سوم'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='fa'), "صد و سی هزار")
        self.assertEqual(num2words(242, lang='fa'), "دویست و چهل و دو")
        self.assertEqual(num2words(800, lang='fa'), "هشتصد")
        self.assertEqual(num2words(-203, lang='fa'), "منفی دویست و سه")
        self.assertEqual(
            num2words(1234567890, lang='fa'),
            "یک میلیارد و دویست و سی و چهار میلیون و"
            " پانصد و شصت و هفت هزار و هشتصد و نود"
        )

    def test_year(self):
        self.assertEqual(num2words(1398, lang='fa', to='year'),
                         "هزار و سیصد و نود و هشت")
        self.assertEqual(num2words(1399, lang='fa', to='year'),
                         "هزار و سیصد و نود و نه")
        self.assertEqual(
            num2words(1400, lang='fa', to='year'), "هزار و چهارصد")

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='fa', to='currency'), 'هزار تومان')
        self.assertEqual(
            num2words(1500000, lang='fa', to='currency'),
            'یک میلیون و پانصد هزار تومان'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='fa', to='ordinal_num'), '10م')
        self.assertEqual(num2words(21, lang='fa', to='ordinal_num'), '21م')
        self.assertEqual(num2words(102, lang='fa', to='ordinal_num'), '102م')
        self.assertEqual(num2words(73, lang='fa', to='ordinal_num'), '73م')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='fa'), "دوازده و نیم")
        self.assertEqual(num2words(0.75, lang='fa'), "هفتاد و پنج صدم")
        self.assertEqual(num2words(12.51, lang='fa'),
                         "دوازده و پنجاه و یک صدم")
        self.assertEqual(num2words(12.53, lang='fa'),
                         "دوازده و پنجاه و سه صدم")
        self.assertEqual(num2words(12.59, lang='fa'),
                         "دوازده و پنجاه و نه صدم")
        self.assertEqual(num2words(0.000001, lang='fa'), "یک میلیونیم")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
