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


class Num2WordsCKBTest(TestCase):
    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='ckb'), "سەد و نەوەد و نۆ")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ckb', to='ordinal'),
            'سفر'
        )
        self.assertEqual(
            num2words(1, lang='ckb', to='ordinal'),
            'یه‌کەم'
        )
        self.assertEqual(
            num2words(13, lang='ckb', to='ordinal'),
            'سیانزدەیەم'
        )
        self.assertEqual(
            num2words(23, lang='ckb', to='ordinal'),
            'بیست و سێیەم'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ckb'), "سەد و سی هەزار")
        self.assertEqual(num2words(242, lang='ckb'), "دوو سەد و چل و دوو")
        self.assertEqual(num2words(800, lang='ckb'), "هەشت سەد")
        self.assertEqual(num2words(-203, lang='ckb'), "سالب دوو سەد و سێ")


    def test_year(self):
        self.assertEqual(num2words(1398, lang='ckb', to='year'),
                         "ساڵی هەزار و سێ سەد و نەوەد و هەشت")
        self.assertEqual(num2words(1399, lang='ckb', to='year'),
                         "ساڵی هەزار و سێ سەد و نەوەد و نۆ")
        self.assertEqual(
            num2words(1400, lang='ckb', to='year'), "ساڵی هەزار و چوار سەد")

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ckb', to='currency'), 'هەزار دینار')
        self.assertEqual(
            num2words(1500000, lang='ckb', to='currency'),
            'یه‌ک میلیۆن و پێنج سەد هەزار دینار'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ckb', to='ordinal_num'), '10یەم')
        self.assertEqual(num2words(21, lang='ckb', to='ordinal_num'), '21یەم')
        self.assertEqual(num2words(102, lang='ckb', to='ordinal_num'), '102یەم')
        self.assertEqual(num2words(73, lang='ckb', to='ordinal_num'), '73یەم')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='ckb'), "دوازدە پۆینت پێنج")
        self.assertEqual(num2words(0.75, lang='ckb'), "سفر پۆینت حەفتا و پێنج")
        self.assertEqual(num2words(12.51, lang='ckb'),
                         "دوازدە پۆینت پەنجا و یه‌ک")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
