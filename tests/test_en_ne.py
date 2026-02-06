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


class Num2WordsENNETest(TestCase):
    def test_cardinal(self):
        # Basic powers of 100 progression
        self.assertEqual(num2words(1e5, lang="en_NE"), "one lakh")
        self.assertEqual(num2words(1e6, lang="en_NE"), "ten lakh")
        self.assertEqual(num2words(1e7, lang="en_NE"), "one crore")
        self.assertEqual(num2words(1e8, lang="en_NE"), "ten crore")
        self.assertEqual(num2words(1e9, lang="en_NE"), "one arba")
        self.assertEqual(num2words(1e10, lang="en_NE"), "ten arba")
        self.assertEqual(num2words(1e11, lang="en_NE"), "one kharba")
        self.assertEqual(num2words(1e12, lang="en_NE"), "ten kharba")
        self.assertEqual(num2words(1e13, lang="en_NE"), "one neel")
        self.assertEqual(num2words(1e14, lang="en_NE"), "ten neel")
        self.assertEqual(num2words(1e15, lang="en_NE"), "one padam")
        self.assertEqual(num2words(1e16, lang="en_NE"), "ten padam")
        self.assertEqual(num2words(1e17, lang="en_NE"), "one shankha")
        self.assertEqual(num2words(1e18, lang="en_NE"), "ten shankha")

    def test_intermediate_values(self):
        # Test intermediate values to ensure proper grouping
        self.assertEqual(
            num2words(150000, lang="en_NE"),
            "one lakh, fifty thousand"
        )
        self.assertEqual(
            num2words(250000, lang="en_NE"),
            "two lakh, fifty thousand"
        )
        self.assertEqual(
            num2words(1250000, lang="en_NE"),
            "twelve lakh, fifty thousand"
        )
        self.assertEqual(
            num2words(15000000, lang="en_NE"),
            "one crore, fifty lakh"
        )
        self.assertEqual(
            num2words(12345567, lang="en_NE"),
            "one crore, twenty-three lakh, forty-five thousand, "
            "five hundred and sixty-seven"
        )
        self.assertEqual(
            num2words(125000000, lang="en_NE"), "twelve crore, "
            "fifty lakh"
        )

    def test_small_numbers(self):
        # Ensure small numbers still work correctly
        self.assertEqual(num2words(0, lang="en_NE"), "zero")
        self.assertEqual(num2words(1, lang="en_NE"), "one")
        self.assertEqual(num2words(99, lang="en_NE"), "ninety-nine")
        self.assertEqual(
            num2words(999, lang="en_NE"),
            "nine hundred and ninety-nine"
        )
        self.assertEqual(
            num2words(9999, lang="en_NE"),
            "nine thousand, nine hundred and ninety-nine"
        )
        self.assertEqual(
            num2words(99999, lang="en_NE"),
            "ninety-nine thousand, nine hundred and ninety-nine"
        )

    def test_complex_values(self):
        # Real-world complex numbers
        self.assertEqual(
            num2words(12345678, lang="en_NE"),
            "one crore, twenty-three lakh, forty-five thousand, "
            "six hundred and seventy-eight"
        )
        self.assertEqual(
            num2words(987654321, lang="en_NE"),
            "ninety-eight crore, seventy-six lakh, "
            "fifty-four thousand, three hundred and twenty-one"
        )
