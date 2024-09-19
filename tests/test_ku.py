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
        self.assertEqual(num2words(199, lang='ku'), "sed û nod û neh")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ku', to='ordinal'),
            'sifiryem'
        )
        self.assertEqual(
            num2words(1, lang='ku', to='ordinal'),
            'Yekyem'
        )
        self.assertEqual(
            num2words(13, lang='ku', to='ordinal'),
            'sêzdehyem'
        )
        self.assertEqual(
            num2words(23, lang='ku', to='ordinal'),
            'bîst û sêyem'
        )

    def test_cardinal(self):
        self.assertEqual(num2words(130000, lang='ku'), "sed û sî hezar")
        self.assertEqual(num2words(242, lang='ku'), "du sed û çil û du")
        self.assertEqual(num2words(800, lang='ku'), "heşt sed")
        self.assertEqual(num2words(-203, lang='ku'), "negatîf du sed û sê")


    def test_year(self):
        self.assertEqual(num2words(1398, lang='ku', to='year'),
                         "sala hezar û sê sed û nod û heşt")
        self.assertEqual(num2words(1399, lang='ku', to='year'),
                         "sala hezar û sê sed û nod û neh")
        self.assertEqual(
            num2words(1400, lang='ku', to='year'), "sala hezar û çar sed")

    def test_currency(self):
        self.assertEqual(
            num2words(1000, lang='ku', to='currency'), 'hezar lira')
        self.assertEqual(
            num2words(1500000, lang='ku', to='currency'),
            'Yek milyon û pênc sed hezar lira'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='ku', to='ordinal_num'), '10yem')
        self.assertEqual(num2words(21, lang='ku', to='ordinal_num'), '21yem')
        self.assertEqual(num2words(102, lang='ku', to='ordinal_num'), '102yem')
        self.assertEqual(num2words(73, lang='ku', to='ordinal_num'), '73yem')

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.5, lang='ku'), "dwanzdeh point pênc")
        self.assertEqual(num2words(0.75, lang='ku'), "sifir point heftê û pênc")
        self.assertEqual(num2words(12.51, lang='ku'),
                         "dwanzdeh point pêncî û Yek")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")
