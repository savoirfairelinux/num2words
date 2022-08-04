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


class Num2WordsMSTest(TestCase):
    def test_cardinal_for_natural_number(self):
        self.assertEqual(num2words(10, lang='ms'), "sepuluh")
        self.assertEqual(num2words(11, lang='ms'), "sebelas")
        self.assertEqual(num2words(100, lang='ms'), "seratus")
        self.assertEqual(num2words(1000, lang='ms'), "seribu")
        self.assertEqual(num2words(10000, lang='ms'), "sepuluh ribu")
        self.assertEqual(num2words(100000, lang='ms'), "seratus ribu")
        self.assertEqual(num2words(1000000, lang='ms'), "satu juta")
        self.assertEqual(num2words(10000000, lang='ms'), "sepuluh juta")
        self.assertEqual(num2words(100000000, lang='ms'), "seratus juta")
        self.assertEqual(num2words(1000000000, lang='ms'), "satu bilion")
        self.assertEqual(num2words(108, lang='ms'), "seratus lapan")
        self.assertEqual(num2words(1075, lang='ms'), "seribu tujuh puluh lima")
        self.assertEqual(
            num2words(1087231, lang='ms'),
            "satu juta lapan puluh tujuh ribu dua ratus tiga puluh satu"
        )
        self.assertEqual(
            num2words(1000000408, lang='ms'),
            "satu bilion empat ratus lapan"
        )

        self.assertEqual(
            num2words(765432, lang='ms'),
            "tujuh ratus enam puluh lima ribu empat ratus tiga puluh dua"
        )

    def test_cardinal_for_decimal_number(self):
        self.assertEqual(
            num2words(12.234, lang='ms'), "dua belas perpuluhan dua tiga empat"
        )
        self.assertEqual(
            num2words(9.07, lang='ms'), "sembilan perpuluhan kosong tujuh"
        )

    def test_cardinal_for_negative_number(self):
        self.assertEqual(
            num2words(-923, lang='ms'), "negatif sembilan ratus dua puluh tiga"
        )
        self.assertEqual(
            num2words(-2.23, lang='ms'), "negatif dua perpuluhan dua tiga"
        )

    def test_ordinal_for_natural_number(self):
        self.assertEqual(num2words(1, ordinal=True, lang='ms'), "pertama")
        self.assertEqual(num2words(10, ordinal=True, lang='ms'), "kesepuluh")

    def test_ordinal_for_negative_number(self):
        self.assertRaises(TypeError, num2words, -12, ordinal=True, lang='ms')

    def test_ordinal_for_floating_number(self):
        self.assertRaises(TypeError, num2words, 3.243, ordinal=True, lang='ms')
