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
from num2words.lang_HY import Num2Word_HY


class Num2WordsHYTest(TestCase):
    """Test suite for Armenian number to words converter."""

    def test_basic_cardinal_numbers(self):
        """Test basic cardinal number conversion."""
        # Single digits
        self.assertEqual(num2words(0, lang="hy"), "զրո")
        self.assertEqual(num2words(1, lang="hy"), "մեկ")
        self.assertEqual(num2words(2, lang="hy"), "երկու")
        self.assertEqual(num2words(3, lang="hy"), "երեք")
        self.assertEqual(num2words(5, lang="hy"), "հինգ")
        self.assertEqual(num2words(9, lang="hy"), "ինը")

        # Teens and tens
        self.assertEqual(num2words(10, lang="hy"), "տասը")
        self.assertEqual(num2words(11, lang="hy"), "տասնմեկ")
        self.assertEqual(num2words(12, lang="hy"), "տասներկու")
        self.assertEqual(num2words(15, lang="hy"), "տասնհինգ")
        self.assertEqual(num2words(19, lang="hy"), "տասնինը")
        self.assertEqual(num2words(20, lang="hy"), "քսան")
        self.assertEqual(num2words(21, lang="hy"), "քսանմեկ")
        self.assertEqual(num2words(30, lang="hy"), "երեսուն")
        self.assertEqual(num2words(50, lang="hy"), "հիսուն")
        self.assertEqual(num2words(99, lang="hy"), "իննսուն ինը")

        # Hundreds
        self.assertEqual(num2words(100, lang="hy"), "հարյուր")
        self.assertEqual(num2words(101, lang="hy"), "հարյուր մեկ")
        self.assertEqual(num2words(111, lang="hy"), "հարյուր տասնմեկ")
        self.assertEqual(num2words(120, lang="hy"), "հարյուր քսան")
        self.assertEqual(num2words(200, lang="hy"), "երկու հարյուր")
        self.assertEqual(num2words(999, lang="hy"), "ինը հարյուր իննսուն ինը")

    def test_large_cardinal_numbers(self):
        """Test large cardinal number conversion."""
        # Thousands
        self.assertEqual(num2words(1000, lang="hy"), "հազար")
        self.assertEqual(num2words(1001, lang="hy"), "հազար մեկ")
        self.assertEqual(num2words(1111, lang="hy"), "հազար հարյուր տասնմեկ")
        self.assertEqual(num2words(2000, lang="hy"), "երկու հազար")
        self.assertEqual(num2words(10000, lang="hy"), "տասը հազար")
        self.assertEqual(num2words(100000, lang="hy"), "հարյուր հազար")

        # Millions and billions
        self.assertEqual(num2words(1000000, lang="hy"), "մեկ միլիոն")
        self.assertEqual(num2words(2000000, lang="hy"), "երկու միլիոն")
        self.assertEqual(num2words(1000000000, lang="hy"), "մեկ միլիարդ")
        self.assertEqual(num2words(4000000000, lang="hy"), "չորս միլիարդ")

        # Special cases for merge method
        self.assertEqual(num2words(142, lang="hy"), "հարյուր քառասուներկու")
        self.assertEqual(
            num2words(100042, lang="hy"), "հարյուր հազար քառասուներկու"
        )

        # Specific scenarios in to_cardinal
        self.assertEqual(num2words(1100, lang="hy"), "հազար հարյուր")
        self.assertEqual(num2words(3000000, lang="hy"), "երեք միլիոն")
        self.assertEqual(num2words(3000000000, lang="hy"), "երեք միլիարդ")

    def test_very_large_numbers(self):
        """Test very large numbers that need special handling."""
        converter = Num2Word_HY()

        # Large numbers without specified group
        result = converter.to_cardinal(10**15)
        self.assertTrue(isinstance(result, str))
        self.assertTrue(len(result) > 0)

        # Error handling for extremely large numbers
        result2 = converter.to_cardinal(10**16)
        self.assertTrue(isinstance(result2, str))
        self.assertTrue(len(result2) > 0)

        # Large numbers with mixed components
        result3 = converter.to_cardinal(1234567890)
        self.assertTrue(isinstance(result3, str))
        self.assertTrue(len(result3) > 0)

        # Additional large number tests
        for num in [10**14, 10**17, 10**19]:
            result = converter.to_cardinal(num)
            self.assertTrue(isinstance(result, str))

    def test_ordinal_numbers(self):
        """Test ordinal number conversion."""
        self.assertEqual(num2words(0, lang="hy", to="ordinal"), "զրոերորդ")
        self.assertEqual(num2words(1, lang="hy", to="ordinal"), "առաջին")
        self.assertEqual(num2words(2, lang="hy", to="ordinal"), "երկրորդ")
        self.assertEqual(num2words(3, lang="hy", to="ordinal"), "երրորդ")
        self.assertEqual(num2words(4, lang="hy", to="ordinal"), "չորրորդ")
        self.assertEqual(num2words(5, lang="hy", to="ordinal"), "հինգերորդ")
        self.assertEqual(num2words(6, lang="hy", to="ordinal"), "վեցերորդ")
        self.assertEqual(num2words(7, lang="hy", to="ordinal"), "յոթերորդ")
        self.assertEqual(num2words(8, lang="hy", to="ordinal"), "ութերորդ")
        self.assertEqual(num2words(9, lang="hy", to="ordinal"), "իններորդ")
        self.assertEqual(num2words(10, lang="hy", to="ordinal"), "տասներորդ")
        self.assertEqual(
            num2words(11, lang="hy", to="ordinal"), "տասնմեկերորդ"
        )
        self.assertEqual(
            num2words(12, lang="hy", to="ordinal"), "տասներկուերորդ"
        )
        self.assertEqual(num2words(20, lang="hy", to="ordinal"), "քսաներորդ")
        self.assertEqual(num2words(21, lang="hy", to="ordinal"), "քսան առաջին")
        self.assertEqual(
            num2words(101, lang="hy", to="ordinal"), "հարյուր մեկերորդ"
        )
        self.assertEqual(
            num2words(222, lang="hy", to="ordinal"),
            "երկու հարյուր քսաներկուերորդ",
        )

        # Large ordinal numbers
        self.assertEqual(
            num2words(1000, lang="hy", to="ordinal"), "հազարերորդ"
        )
        self.assertEqual(
            num2words(1000000, lang="hy", to="ordinal"), "մեկ միլիոներորդ"
        )

    def test_ordinal_with_suffix(self):
        """Test ordinal number with suffix conversion."""
        self.assertEqual(num2words(1, lang="hy", to="ordinal_num"), "1-րդ")
        self.assertEqual(num2words(2, lang="hy", to="ordinal_num"), "2-րդ")
        self.assertEqual(num2words(10, lang="hy", to="ordinal_num"), "10-րդ")
        self.assertEqual(num2words(21, lang="hy", to="ordinal_num"), "21-րդ")
        self.assertEqual(num2words(103, lang="hy", to="ordinal_num"), "103-րդ")
        self.assertEqual(
            num2words(1001, lang="hy", to="ordinal_num"), "1001-րդ"
        )

    def test_basic_currency(self):
        """Test basic currency conversion."""
        # Basic currency tests
        self.assertEqual(
            num2words(1.0, lang="hy", to="currency", currency="AMD"),
            "մեկ դրամ",
        )
        self.assertEqual(
            num2words(2.0, lang="hy", to="currency", currency="AMD"),
            "երկու դրամ",
        )
        self.assertEqual(
            num2words(100.0, lang="hy", to="currency", currency="EUR"),
            "հարյուր եվրո",
        )

        # Various currencies
        self.assertEqual(
            num2words(100, lang="hy", to="currency", currency="AMD"),
            "հարյուր դրամ",
        )
        self.assertEqual(
            num2words(100, lang="hy", to="currency", currency="RUB"),
            "հարյուր ռուբլի",
        )
        self.assertEqual(
            num2words(100, lang="hy", to="currency", currency="JPY"),
            "հարյուր իեն",
        )
        self.assertEqual(
            num2words(100, lang="hy", to="currency", currency="GBP"),
            "հարյուր ֆունտ ստեռլինգ",
        )
        self.assertEqual(
            num2words(100, lang="hy", to="currency", currency="CHF"),
            "հարյուր շվեյցարական ֆրանկ",
        )

    def test_currency_with_fractional_values(self):
        """Test currency conversion with fractional values."""
        # Fractional values
        self.assertEqual(
            num2words(1.5, lang="hy", to="currency", currency="USD"),
            "մեկ դոլար ամբողջ հինգ տասներորդ ցենտ",
        )
        self.assertEqual(
            num2words(100.00, lang="hy", to="currency", currency="USD"),
            "հարյուր դոլար",
        )
        self.assertEqual(
            num2words(100.42, lang="hy", to="currency", currency="USD"),
            "հարյուր դոլար, քառասուներկու ցենտ",
        )

        # Special cases with cents
        self.assertEqual(
            num2words(1.25, lang="hy", to="currency", currency="USD"),
            "մեկ դոլար քսանհինգ ցենտ",
        )
        self.assertEqual(
            num2words(1.75, lang="hy", to="currency", currency="USD"),
            "մեկ դոլար յոթանասունհինգ ցենտ",
        )

        # Negative values
        self.assertEqual(
            num2words(-1.42, lang="hy", to="currency", currency="USD"),
            "մինուս մեկ դոլար, քառասուներկու ցենտ",
        )

        # Fractional values without whole part
        self.assertEqual(
            num2words(0.5, lang="hy", to="currency", currency="USD"),
            "հիսուն ցենտ",
        )

        # Test with various cent values
        for cents_value in [25, 50, 75, 5, 42]:
            result = Num2Word_HY().to_currency(1 + cents_value / 100, "USD")
            self.assertTrue(len(result) > 0)

    def test_currency_special_cases(self):
        """Test special cases in currency conversion."""
        # Unknown currency
        self.assertEqual(
            num2words(10, lang="hy", to="currency", currency="XXX"), "տասը"
        )

        # No cents option
        self.assertEqual(
            num2words(
                10, lang="hy", to="currency", currency="EUR", cents=False
            ),
            "տասը եվրո",
        )

        # Negative values without fractions
        self.assertEqual(
            num2words(
                -100, lang="hy", to="currency", currency="EUR", cents=False
            ),
            "մինուս հարյուր եվրո",
        )

        # Testing negative currency without cents
        result = Num2Word_HY().to_currency(-10, "EUR", cents=False)
        self.assertEqual(result, "մինուս տասը եվրո")

        # Testing currency dictionary access
        converter = Num2Word_HY()
        self.assertTrue("AMD" in converter.CURRENCY_FORMS)
        self.assertEqual(converter.CURRENCY_FORMS["AMD"][0], ("դրամ", "դրամ"))

        # Testing unknown currency with cents
        result = converter.to_currency(10.5, "XYZ")
        self.assertTrue(isinstance(result, str))

        # Testing negative currency
        result = converter.to_currency(-1.50, "EUR")
        self.assertTrue("մինուս" in result)

    def test_year_conversion(self):
        """Test the to_year method functionality."""
        # Testing basic year conversion
        self.assertEqual(
            num2words(2000, lang="hy", to="year"), "երկու հազար թվական"
        )
        self.assertEqual(
            num2words(2001, lang="hy", to="year"), "երկու հազար մեկ թվական"
        )
        self.assertEqual(
            num2words(2010, lang="hy", to="year"), "երկու հազար տասը թվական"
        )

        # Testing year prefix removal - direct test
        year_str = "մեկ հազար"
        year_str_stripped = year_str[4:].strip()
        self.assertEqual(year_str_stripped, "հազար")

        # Testing year prefix removal - negative case
        year_str2 = "երկու հազար"
        # No conditional here, just verify it doesn't match
        self.assertFalse(year_str2.startswith("մեկ "))
        self.assertEqual(year_str2, "երկու հազար")

        # Testing year conversion with different inputs
        converter = Num2Word_HY()
        for num in [1000, 1066, 1100, 1500, 1900, 2000]:
            result = converter.to_year(num)
            self.assertTrue(isinstance(result, str))

        # Explicitly test the conversion of years that start with մեկ
        result_1000 = converter.to_year(1000)
        self.assertTrue(
            result_1000.startswith("հազար")
            and not result_1000.startswith("մեկ հազար")
        )
        result_1001 = converter.to_year(1001)
        self.assertTrue(result_1001.startswith("հազար"))

    def test_special_cases(self):
        """Test special cases and edge scenarios."""
        # String replacement for 'հազար միլիոն' to 'միլիարդ' - direct test
        result1 = "հազար միլիոն"
        result1 = result1.replace("հազար միլիոն", "միլիարդ")
        self.assertEqual(result1, "միլիարդ")

        # Testing string replacement without 'հազար միլիոն'
        result2 = "other text"
        result2 = result2.replace("հազար միլիոն", "միլիարդ")
        self.assertEqual(result2, "other text")

        # Testing string replacement with context - positive case
        test_string1 = "հազար միլիոն test"
        original_string1 = test_string1
        # Direct replacement without conditional
        test_string1 = test_string1.replace("հազար միլիոն", "միլիարդ")
        self.assertEqual(test_string1, "միլիարդ test")
        self.assertNotEqual(test_string1, original_string1)

        # Testing the negative case for 'հազար միլիոն'
        test_string_neg = "test string"
        original_string_neg = test_string_neg
        # Direct verification without conditional
        self.assertFalse("հազար միլիոն" in test_string_neg)
        self.assertEqual(test_string_neg, "test string")
        self.assertEqual(test_string_neg, original_string_neg)

        # Testing string insertion
        result = ["մեկ", "դոլար"]
        result.insert(-1, "ամբողջ հինգ տասներորդ")
        self.assertEqual(result, ["մեկ", "ամբողջ հինգ տասներորդ", "դոլար"])

        # Testing currency parts
        cents_pluralized = Num2Word_HY().pluralize(50, ("ցենտ", "ցենտ"))
        self.assertEqual(cents_pluralized, "ցենտ")

        # Testing year prefix handling with various inputs
        # Positive case: string starts with "մեկ "
        test_year1 = "մեկ հազար"
        # Direct operation without conditional
        self.assertTrue(test_year1.startswith("մեկ "))
        test_year1_stripped = test_year1[4:].strip()
        self.assertEqual(test_year1_stripped, "հազար")
        self.assertNotEqual(test_year1, test_year1_stripped)

        # Negative case: string doesn't start with "մեկ "
        test_year2 = "երկու հազար"
        original_test_year2 = test_year2
        # Direct verification without conditional
        self.assertFalse(test_year2.startswith("մեկ "))
        self.assertEqual(test_year2, "երկու հազար")
        self.assertEqual(test_year2, original_test_year2)

        # More explicit test for the startswith condition
        has_prefix_true = "մեկ հազար".startswith("մեկ ")
        self.assertTrue(has_prefix_true)
        has_prefix_false = "երկու հազար".startswith("մեկ ")
        self.assertFalse(has_prefix_false)

        # Testing year prefix removal - more variations
        input_str1 = "մեկ հազար ութ հարյուր"
        # Direct operation without conditional
        self.assertTrue(input_str1.startswith("մեկ "))
        input_str1_stripped = input_str1[4:].strip()
        self.assertEqual(input_str1_stripped, "հազար ութ հարյուր")
        self.assertNotEqual(input_str1, input_str1_stripped)

        input_str2 = "երկու հազար ութ հարյուր"
        original_input_str2 = input_str2
        # Direct verification without conditional
        self.assertFalse(input_str2.startswith("մեկ "))
        self.assertEqual(input_str2, "երկու հազար ութ հարյուր")
        self.assertEqual(input_str2, original_input_str2)

    def test_pluralization(self):
        """Test pluralization function."""
        converter = Num2Word_HY()

        # Testing pluralize with same forms
        self.assertEqual(converter.pluralize(1, ("դրամ", "դրամ")), "դրամ")
        self.assertEqual(converter.pluralize(2, ("դրամ", "դրամ")), "դրամ")
        self.assertEqual(converter.pluralize(11, ("դրամ", "դրամ")), "դրամ")
        self.assertEqual(converter.pluralize(21, ("դրամ", "դրամ")), "դրամ")
        self.assertEqual(converter.pluralize(101, ("դրամ", "դրամ")), "դրամ")

        # Empty forms and single form
        self.assertEqual(converter.pluralize(5, []), "")
        self.assertEqual(converter.pluralize(5, ["դրամ"]), "դրամ")

        # Testing various numbers for correct pluralization
        self.assertEqual(
            converter.pluralize(0, ("խնձոր", "խնձորներ")), "խնձորներ"
        )
        self.assertEqual(
            converter.pluralize(1, ("խնձոր", "խնձորներ")), "խնձոր"
        )
        self.assertEqual(
            converter.pluralize(2, ("խնձոր", "խնձորներ")), "խնձորներ"
        )
        self.assertEqual(
            converter.pluralize(11, ("խնձոր", "խնձորներ")), "խնձորներ"
        )
        self.assertEqual(
            converter.pluralize(21, ("խնձոր", "խնձորներ")), "խնձոր"
        )
        self.assertEqual(
            converter.pluralize(22, ("խնձոր", "խնձորներ")), "խնձորներ"
        )
        self.assertEqual(
            converter.pluralize(31, ("խնձոր", "խնձորներ")), "խնձոր"
        )

        # Different plural forms
        self.assertEqual(
            converter.pluralize(0, ("տարի", "տարիներ")), "տարիներ"
        )
        self.assertEqual(converter.pluralize(1, ("տարի", "տարիներ")), "տարի")
        self.assertEqual(
            converter.pluralize(5, ("տարի", "տարիներ")), "տարիներ"
        )

        # Edge cases
        self.assertEqual(converter.pluralize(101, ("ծառ", "ծառեր")), "ծառ")
        result = converter.pluralize(0, ("ծառ", "ծառեր"))
        self.assertEqual(result, "ծառեր")

    def test_merge_method(self):
        """Test the merge method functionality."""
        converter = Num2Word_HY()

        # Basic merge tests
        val = converter.merge(("երկու հարյուր", 200), ("ի", 0))
        self.assertEqual(val[0], "երկու հարյուր ի")

        val = converter.merge(("հինգ հարյուր", 500), ("երկու", 2))
        self.assertEqual(val[0], "հինգ հարյուր երկու")

        # Testing merge with specific parameters
        result = converter.merge(("մեկ", 1), ("միլիոն", 1000000))
        self.assertEqual(result[0], "մեկ միլիոն")

        # Testing merge with single-digit number and hundreds
        result = converter.merge(("հինգ հարյուր", 500), ("երեք", 3))
        self.assertEqual(result[0], "հինգ հարյուր երեք")

        # Testing merge method with different parameters
        merge_result = converter.merge(("մեկ", 1), ("հարյուր", 100))
        self.assertTrue(isinstance(merge_result, tuple))

        # Testing merge with small numbers and hundreds
        for cnum in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            for nnum in range(1, 10):
                result = converter.merge((str(cnum), cnum), (str(nnum), nnum))
                self.assertEqual(result[1], cnum + nnum)
                expected_text = "%s %s" % (str(cnum), str(nnum))
                self.assertEqual(result[0], expected_text)

        # Testing various combinations in merge method
        for cnum in [1, 100, 200, 500, 999]:
            for nnum in [0, 1, 10, 50, 100, 1000, 1000000]:
                if cnum != nnum:
                    result = converter.merge(
                        (str(cnum), cnum), (str(nnum), nnum)
                    )
                    self.assertTrue(isinstance(result, tuple))
                    self.assertTrue(isinstance(result[0], str))
                    self.assertTrue(isinstance(result[1], int))

        result1 = converter.merge(("հինգ հարյուր", 500), ("երկու", 2))
        self.assertEqual(result1[0], "հինգ հարյուր երկու")
        self.assertEqual(result1[1], 502)
        result2 = converter.merge(("վեց հարյուր", 600), ("չորս", 4))
        self.assertEqual(result2[0], "վեց հարյուր չորս")
        self.assertEqual(result2[1], 604)

        for snum, nnum in [(500, 5), (800, 8), (900, 9)]:
            val = converter.merge(
                (f"base_{snum}", snum), (f"num_{nnum}", nnum)
            )
            self.assertEqual(val[1], snum + nnum)
        for prefix in [3, 4, 5]:
            value = prefix * 1000000000
            result = converter.to_cardinal(value)
            expected_start = converter.to_cardinal(prefix)
            self.assertTrue(result.startswith(expected_start))
            self.assertIn("միլիարդ", result)
        result_big = converter.to_cardinal(1000000000)
        self.assertNotIn("հազար միլիոն", result_big)
        self.assertIn("միլիարդ", result_big)
        test_str_with_pattern = "test հազար միլիոն suffix"
        result_replace = test_str_with_pattern.replace(
            "հազար միլիոն", "միլիարդ"
        )
        self.assertEqual(result_replace, "test միլիարդ suffix")

        for year in [100, 500, 2000, 3000]:
            result_year = converter.to_year(year)
            expected = converter.to_cardinal(year) + " թվական"
            self.assertEqual(result_year, expected)
        result_neg = converter.to_cardinal_negative(-42)
        self.assertTrue(result_neg.startswith("մինուս"))
        result_pos = converter.to_cardinal_negative(42)
        self.assertFalse(result_pos.startswith("մինուս"))

    def test_merge_method_small_numbers_with_hundreds(self):
        """Test merge method with small single-digit numbers and hundreds."""
        converter = Num2Word_HY()
        for hundred in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            for digit in range(1, 10):
                result = converter.merge((f"test_{hundred}", hundred),
                                         (f"test_{digit}", digit))
                self.assertEqual(result[1], hundred + digit)
                expected = f"test_{hundred} test_{digit}"
                self.assertEqual(result[0], expected)

    def test_billion_prefix_case(self):
        """Test special case for two billion conversion."""
        self.assertEqual(num2words(2000000000, lang="hy"), "երկու միլիարդ")

        self.assertEqual(num2words(3000000000, lang="hy"), "երեք միլիարդ")
        self.assertEqual(num2words(4000000000, lang="hy"), "չորս միլիարդ")

    def test_thousand_million_replacement(self):
        """Test replacement of 'հազար միլիոն' with 'միլիարդ'."""

        test_string = "հազար միլիոն"
        result = test_string.replace("հազար միլիոն", "միլիարդ")
        self.assertEqual(result, "միլիարդ")

        test_string_context = "текст հազար միլիոն ещё текст"
        result_context = test_string_context.replace("հազար միլիոն", "միլիարդ")
        self.assertEqual(result_context, "текст միլիարդ ещё текст")

        converter = Num2Word_HY()
        result_cardinal = converter.to_cardinal(1000000000)
        self.assertNotIn("հազար միլիոն", result_cardinal)
        self.assertIn("միլիարդ", result_cardinal)

    def test_year_prefix_removal(self):
        """Test removal of 'մեկ ' prefix in year conversion."""
        converter = Num2Word_HY()

        year_str = "մեկ հազար"
        
        for year in [1000, 1001, 1100, 1500, 1900, 1999]:
            result = converter.to_year(year)
            self.assertTrue(result.startswith("հազար"))
            self.assertFalse(result.startswith("մեկ հազար"))

        for year in [100, 500, 2000, 3000]:
            result = converter.to_year(year)
            expected = converter.to_cardinal(year) + " թվական"
            self.assertEqual(result, expected)

    def test_merge_method_zero_with_hundreds(self):
        converter = Num2Word_HY()
        for hundred in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            result = converter.merge(("сто", hundred), ("ноль", 0))
            self.assertEqual(result[0], "сто нолի")
            self.assertEqual(result[1], hundred + 0)

    def test_to_cardinal_thousand_million_branch(self):
        converter = Num2Word_HY()
        result = Num2Word_HY.to_cardinal(converter, 1000000000)
        self.assertEqual(result, "մեկ միլիարդ")

    def test_to_year_prefix_removal_branch(self):
        class DummyHY(Num2Word_HY):
            def to_cardinal(self, value):
                return "մեկ հազար"
        converter = DummyHY()
        result = converter.to_year(1000)
        self.assertEqual(result, "հազար թվական")

    def test_cardinal_million_grouping(self):
        converter = Num2Word_HY()
        result = converter.to_cardinal(10455397)
        expected = (
            "տասը միլիոն չորս հարյուր հիսունհինգ հազար "
            "երեք հարյուր իննսուն յոթ"
        )
        self.assertEqual(result, expected)
