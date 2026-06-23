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

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsSWTest(TestCase):
    def test_zero(self):
        self.assertEqual(num2words(0, lang="sw"), "sifuri")

    def test_units(self):
        self.assertEqual(num2words(1, lang="sw"), "moja")
        self.assertEqual(num2words(2, lang="sw"), "mbili")
        self.assertEqual(num2words(3, lang="sw"), "tatu")
        self.assertEqual(num2words(4, lang="sw"), "nne")
        self.assertEqual(num2words(5, lang="sw"), "tano")
        self.assertEqual(num2words(6, lang="sw"), "sita")
        self.assertEqual(num2words(7, lang="sw"), "saba")
        self.assertEqual(num2words(8, lang="sw"), "nane")
        self.assertEqual(num2words(9, lang="sw"), "tisa")

    def test_ten_and_teens(self):
        self.assertEqual(num2words(10, lang="sw"), "kumi")
        self.assertEqual(num2words(11, lang="sw"), "kumi na moja")
        self.assertEqual(num2words(12, lang="sw"), "kumi na mbili")
        self.assertEqual(num2words(15, lang="sw"), "kumi na tano")
        self.assertEqual(num2words(16, lang="sw"), "kumi na sita")
        self.assertEqual(num2words(19, lang="sw"), "kumi na tisa")

    def test_tens(self):
        self.assertEqual(num2words(20, lang="sw"), "ishirini")
        self.assertEqual(num2words(30, lang="sw"), "thelathini")
        self.assertEqual(num2words(40, lang="sw"), "arobaini")
        self.assertEqual(num2words(50, lang="sw"), "hamsini")
        self.assertEqual(num2words(60, lang="sw"), "sitini")
        self.assertEqual(num2words(70, lang="sw"), "sabini")
        self.assertEqual(num2words(80, lang="sw"), "themanini")
        self.assertEqual(num2words(90, lang="sw"), "tisini")

    def test_compound_tens(self):
        self.assertEqual(num2words(21, lang="sw"), "ishirini na moja")
        self.assertEqual(num2words(33, lang="sw"), "thelathini na tatu")
        self.assertEqual(num2words(47, lang="sw"), "arobaini na saba")
        self.assertEqual(num2words(55, lang="sw"), "hamsini na tano")
        self.assertEqual(num2words(99, lang="sw"), "tisini na tisa")

    def test_hundreds(self):
        self.assertEqual(num2words(100, lang="sw"), "mia moja")
        self.assertEqual(num2words(200, lang="sw"), "mia mbili")
        self.assertEqual(num2words(300, lang="sw"), "mia tatu")
        self.assertEqual(num2words(900, lang="sw"), "mia tisa")

    def test_hundreds_with_remainder(self):
        # When the hundred multiplier is one and a remainder follows, the
        # "moja" is dropped: "mia na ...".
        self.assertEqual(num2words(101, lang="sw"), "mia na moja")
        self.assertEqual(num2words(110, lang="sw"), "mia na kumi")
        self.assertEqual(num2words(111, lang="sw"), "mia na kumi na moja")
        self.assertEqual(
            num2words(121, lang="sw"), "mia na ishirini na moja"
        )
        self.assertEqual(num2words(301, lang="sw"), "mia tatu na moja")
        self.assertEqual(
            num2words(256, lang="sw"), "mia mbili na hamsini na sita"
        )
        self.assertEqual(
            num2words(656, lang="sw"), "mia sita na hamsini na sita"
        )
        self.assertEqual(
            num2words(999, lang="sw"), "mia tisa na tisini na tisa"
        )

    def test_thousands(self):
        self.assertEqual(num2words(1000, lang="sw"), "elfu moja")
        self.assertEqual(num2words(2000, lang="sw"), "elfu mbili")
        self.assertEqual(num2words(10000, lang="sw"), "elfu kumi")
        self.assertEqual(num2words(100000, lang="sw"), "elfu mia moja")
        self.assertEqual(num2words(1001, lang="sw"), "elfu moja na moja")
        self.assertEqual(
            num2words(1430, lang="sw"),
            "elfu moja na mia nne na thelathini",
        )
        self.assertEqual(
            num2words(1234, lang="sw"),
            "elfu moja na mia mbili na thelathini na nne",
        )

    def test_millions_and_billions(self):
        self.assertEqual(num2words(1000000, lang="sw"), "milioni moja")
        self.assertEqual(num2words(2000000, lang="sw"), "milioni mbili")
        self.assertEqual(
            num2words(1000008, lang="sw"), "milioni moja na nane"
        )
        self.assertEqual(
            num2words(1000000000, lang="sw"), "bilioni moja"
        )
        self.assertEqual(
            num2words(1234567, lang="sw"),
            "milioni moja na elfu mia mbili na thelathini na nne na "
            "mia tano na sitini na saba",
        )

    def test_negative(self):
        self.assertEqual(num2words(-7, lang="sw"), "kasoro saba")
        self.assertEqual(
            num2words(-256, lang="sw"),
            "kasoro mia mbili na hamsini na sita",
        )

    def test_float(self):
        self.assertEqual(
            num2words(12.5, lang="sw"), "kumi na mbili pointi tano"
        )
        self.assertEqual(
            num2words(3.14, lang="sw"), "tatu pointi moja nne"
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang="sw", to="ordinal"), "ya kwanza")
        self.assertEqual(num2words(2, lang="sw", to="ordinal"), "ya pili")
        self.assertEqual(num2words(3, lang="sw", to="ordinal"), "ya tatu")
        self.assertEqual(num2words(5, lang="sw", to="ordinal"), "ya tano")
        self.assertEqual(
            num2words(21, lang="sw", to="ordinal"), "ya ishirini na moja"
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(5, lang="sw", to="ordinal_num"), "ya 5")
        self.assertEqual(num2words(42, lang="sw", to="ordinal_num"), "ya 42")

    def test_year(self):
        self.assertEqual(
            num2words(2024, lang="sw", to="year"),
            "elfu mbili na ishirini na nne",
        )

    def test_currency(self):
        self.assertEqual(
            num2words(12.50, lang="sw", to="currency"),
            "kumi na mbili shilingi na hamsini senti",
        )
        self.assertEqual(
            num2words(5, lang="sw", to="currency", currency="USD"),
            "tano dola",
        )

    def test_ordinal_invalid(self):
        with self.assertRaises(TypeError):
            num2words(2.5, lang="sw", to="ordinal")
        with self.assertRaises(TypeError):
            num2words(-3, lang="sw", to="ordinal")
