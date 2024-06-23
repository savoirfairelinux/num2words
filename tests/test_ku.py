# -*- coding: utf-8 -*-
# Copyright (c) 2024, Karwan Khalid.  All Rights Reserved.

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


class Num2WordsKUTest(TestCase):
    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='ku'), "سەد و نەوەت و نۆ")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ku', to='ordinal'),
            'سفرەم'
        )
        self.assertEqual(
            num2words(1, lang='ku', to='ordinal'),
            'یەکەم'
        )
        self.assertEqual(
            num2words(13, lang='ku', to='ordinal'),
            'سێزدم'
        )
        self.assertEqual(
            num2words(23, lang='ku', to='ordinal'),
            'بیست و سێەم'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ku'), "سەد و سی هەزار")
        self.assertEqual(num2words(242, lang='ku'), "دوو سەد و چل و دوو")
        self.assertEqual(num2words(800, lang='ku'), "هەشت سەد")
        self.assertEqual(num2words(-203, lang='ku'), "سالب دوو سەد و سێ")


    def test_year(self):
        self.assertEqual(num2words(1398, lang='ku', to='year'),
                         "ساڵی هەزار و سێ سەد و نەوەت و هەشت")
        self.assertEqual(num2words(1399, lang='ku', to='year'),
                         "ساڵی هەزار و سێ سەد و نەوەت و نۆ")
        self.assertEqual(
            num2words(1400, lang='ku', to='year'), "ساڵی هەزار و چوار سەد")

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ku', to='currency'), 'هەزار دینار')
        self.assertEqual(
            num2words(1500000, lang='ku', to='currency'),
            'پازدە ملیۆن و پێنج سەد هەزار دینار'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ku', to='ordinal_num'), '10م')
        self.assertEqual(num2words(21, lang='ku', to='ordinal_num'), '21م')
        self.assertEqual(num2words(102, lang='ku', to='ordinal_num'), '102م')
        self.assertEqual(num2words(73, lang='ku', to='ordinal_num'), '73م')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='ku'), "دوازدە پۆینت پێنج")
        self.assertEqual(num2words(0.75, lang='ku'), "سفر پۆینت حەفتا و پێنج")
        self.assertEqual(num2words(12.51, lang='ku'),
                         "دوازدە پۆینت پەنجا و یەک")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
