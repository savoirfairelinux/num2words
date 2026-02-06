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


class Num2WordsNETest(TestCase):
    def test_zero(self):
        self.assertEqual(num2words(0, lang='ne'), 'शून्य')

    def test_ones(self):
        """Test numbers 1-9"""
        self.assertEqual(num2words(1, lang='ne'), 'एक')
        self.assertEqual(num2words(2, lang='ne'), 'दुई')
        self.assertEqual(num2words(3, lang='ne'), 'तीन')
        self.assertEqual(num2words(4, lang='ne'), 'चार')
        self.assertEqual(num2words(5, lang='ne'), 'पाँच')
        self.assertEqual(num2words(6, lang='ne'), 'छ')
        self.assertEqual(num2words(7, lang='ne'), 'सात')
        self.assertEqual(num2words(8, lang='ne'), 'आठ')
        self.assertEqual(num2words(9, lang='ne'), 'नौ')

    def test_tens(self):
        """Test numbers 10-19"""
        self.assertEqual(num2words(10, lang='ne'), 'दस')
        self.assertEqual(num2words(11, lang='ne'), 'एघार')
        self.assertEqual(num2words(12, lang='ne'), 'बाह्र')
        self.assertEqual(num2words(13, lang='ne'), 'तेह्र')
        self.assertEqual(num2words(14, lang='ne'), 'चौध')
        self.assertEqual(num2words(15, lang='ne'), 'पन्ध्र')
        self.assertEqual(num2words(16, lang='ne'), 'सोह्र')
        self.assertEqual(num2words(17, lang='ne'), 'सत्र')
        self.assertEqual(num2words(18, lang='ne'), 'अठार')
        self.assertEqual(num2words(19, lang='ne'), 'उन्नाइस')

    def test_sixties(self):
        """Test numbers 60-69"""
        self.assertEqual(num2words(60, lang='ne'), 'साठी')
        self.assertEqual(num2words(61, lang='ne'), 'एकसट्ठी')
        self.assertEqual(num2words(62, lang='ne'), 'बैसट्ठी')
        self.assertEqual(num2words(63, lang='ne'), 'त्रिसट्ठी')
        self.assertEqual(num2words(64, lang='ne'), 'चौंसट्ठी')
        self.assertEqual(num2words(65, lang='ne'), 'पैंसट्ठी')
        self.assertEqual(num2words(66, lang='ne'), 'छैसट्ठी')
        self.assertEqual(num2words(67, lang='ne'), 'सतसट्ठी')
        self.assertEqual(num2words(68, lang='ne'), 'अठसट्ठी')
        self.assertEqual(num2words(69, lang='ne'), 'उनन्सत्तरी')

    def test_seventies(self):
        """Test numbers 70-79"""
        self.assertEqual(num2words(70, lang='ne'), 'सत्तरी')
        self.assertEqual(num2words(71, lang='ne'), 'एकहत्तर')
        self.assertEqual(num2words(72, lang='ne'), 'बहत्तर')
        self.assertEqual(num2words(73, lang='ne'), 'त्रिहत्तर')
        self.assertEqual(num2words(74, lang='ne'), 'चौहत्तर')
        self.assertEqual(num2words(75, lang='ne'), 'पचहत्तर')
        self.assertEqual(num2words(76, lang='ne'), 'छयहत्तर')
        self.assertEqual(num2words(77, lang='ne'), 'सतहत्तर')
        self.assertEqual(num2words(78, lang='ne'), 'अठहत्तर')
        self.assertEqual(num2words(79, lang='ne'), 'उनासी')

    def test_hundreds(self):
        """Test hundreds"""
        self.assertEqual(num2words(100, lang='ne'), 'एक सय')
        self.assertEqual(num2words(200, lang='ne'), 'दुई सय')
        self.assertEqual(num2words(500, lang='ne'), 'पाँच सय')
        self.assertEqual(num2words(999, lang='ne'), 'नौ सय उनान्सय')

    def test_hundreds_with_remainder(self):
        self.assertEqual(num2words(101, lang='ne'), 'एक सय एक')
        self.assertEqual(num2words(111, lang='ne'), 'एक सय एघार')
        self.assertEqual(num2words(150, lang='ne'), 'एक सय पचास')
        self.assertEqual(num2words(256, lang='ne'), 'दुई सय छपन्न')
        self.assertEqual(num2words(789, lang='ne'), 'सात सय उनान्नब्बे')

    def test_thousands(self):
        """Test thousands (10^3)"""
        self.assertEqual(num2words(1000, lang='ne'), 'एक हजार')
        self.assertEqual(num2words(2000, lang='ne'), 'दुई हजार')
        self.assertEqual(num2words(5000, lang='ne'), 'पाँच हजार')
        self.assertEqual(num2words(50000, lang='ne'), 'पचास हजार')
        self.assertEqual(
            num2words(99999, lang='ne'), 'उनान्सय हजार नौ सय उनान्सय')

    def test_thousands_with_remainder(self):
        self.assertEqual(num2words(1001, lang='ne'), 'एक हजार एक')
        self.assertEqual(num2words(1234, lang='ne'), 'एक हजार दुई सय चौतिस')
        self.assertEqual(num2words(5678, lang='ne'), 'पाँच हजार छ सय अठहत्तर')
        self.assertEqual(
            num2words(99999, lang='ne'), 'उनान्सय हजार नौ सय उनान्सय')

    def test_lakhs(self):
        """Test lakhs (10^5)"""
        self.assertEqual(num2words(100000, lang='ne'), 'एक लाख')
        self.assertEqual(num2words(200000, lang='ne'), 'दुई लाख')
        self.assertEqual(num2words(500000, lang='ne'), 'पाँच लाख')
        self.assertEqual(num2words(1000000, lang='ne'), 'दस लाख')
        self.assertEqual(num2words(5000000, lang='ne'), 'पचास लाख')

    def test_lakhs_with_remainder(self):
        self.assertEqual(num2words(100001, lang='ne'), 'एक लाख एक')
        self.assertEqual(
            num2words(123456, lang='ne'), 'एक लाख तेइस हजार चार सय छपन्न')
        self.assertEqual(
            num2words(999999, lang='ne'), 'नौ लाख उनान्सय हजार नौ सय उनान्सय')

    def test_crores(self):
        """Test crores (10^7)"""
        self.assertEqual(num2words(10000000, lang='ne'), 'एक करोड')
        self.assertEqual(num2words(20000000, lang='ne'), 'दुई करोड')
        self.assertEqual(num2words(50000000, lang='ne'), 'पाँच करोड')
        self.assertEqual(num2words(100000000, lang='ne'), 'दस करोड')
        self.assertEqual(num2words(500000000, lang='ne'), 'पचास करोड')

    def test_crores_with_remainder(self):
        self.assertEqual(
            num2words(10000001, lang='ne'), 'एक करोड एक'
            )
        self.assertEqual(
            num2words(12345678, lang='ne'),
            'एक करोड तेइस लाख पैँतालिस हजार छ सय अठहत्तर'
            )

    def test_arba(self):
        """Test arba (10^9)"""
        self.assertEqual(num2words(1000000000, lang='ne'), 'एक अर्ब')
        self.assertEqual(num2words(2000000000, lang='ne'), 'दुई अर्ब')
        self.assertEqual(num2words(5000000000, lang='ne'), 'पाँच अर्ब')
        self.assertEqual(num2words(10000000000, lang='ne'), 'दस अर्ब')
        self.assertEqual(num2words(50000000000, lang='ne'), 'पचास अर्ब')
        self.assertEqual(num2words(99000000000, lang='ne'), 'उनान्सय अर्ब')

    def test_arba_with_remainder(self):
        self.assertEqual(num2words(1000000001, lang='ne'), 'एक अर्ब एक')
        self.assertEqual(
            num2words(1234567890, lang='ne'),
            'एक अर्ब तेइस करोड पैँतालिस लाख सतसट्ठी हजार आठ सय नब्बे'
            )

    def test_kharba(self):
        """Test kharba (10^11)"""
        self.assertEqual(num2words(100000000000, lang='ne'), 'एक खर्ब')
        self.assertEqual(num2words(1000000000000, lang='ne'), 'दस खर्ब')
        self.assertEqual(num2words(5000000000000, lang='ne'), 'पचास खर्ब')
        self.assertEqual(num2words(10000000000000, lang='ne'), 'एक सय खर्ब')

    def test_kharba_with_remainder(self):
        self.assertEqual(num2words(100000000001, lang='ne'), 'एक खर्ब एक')

    def test_complex_numbers(self):
        # 123,456,789,012 is 1,23,45,67,89,012 in Nepali currency format
        # Reading: 1 kharba, 23 arba, 45 crore, 67 lakh, 89 thousand, 12
        self.assertEqual(
            num2words(123456789123, lang='ne'),
            'एक खर्ब तेइस अर्ब पैँतालिस करोड '
            'सतसट्ठी लाख उनान्नब्बे हजार '
            'एक सय तेइस'
        )

        # 12,34,56,78,90,123
        self.assertEqual(
            num2words(1234567890123, lang='ne'),
            'बाह्र खर्ब चौतिस अर्ब छपन्न '
            'करोड अठहत्तर लाख नब्बे हजार '
            'एक सय तेइस'
        )

        # 9,99,99,99,99,999
        self.assertEqual(
            num2words(999999999999, lang='ne'),
            'नौ खर्ब उनान्सय अर्ब उनान्सय करोड '
            'उनान्सय लाख उनान्सय हजार '
            'नौ सय उनान्सय'
        )

    def test_negative_numbers(self):
        """Test negative numbers."""
        self.assertEqual(num2words(-1, lang='ne'), 'माइनस एक')
        self.assertEqual(num2words(-100, lang='ne'), 'माइनस एक सय')
        self.assertEqual(num2words(-1000, lang='ne'), 'माइनस एक हजार')
        self.assertEqual(num2words(-1000000000, lang='ne'), 'माइनस एक अर्ब')

    def test_ordinals(self):
        """Test ordinal numbers."""
        self.assertEqual(num2words(1, lang='ne', to='ordinal'), 'पहिलो')
        self.assertEqual(num2words(2, lang='ne', to='ordinal'), 'दोस्रो')
        self.assertEqual(num2words(3, lang='ne', to='ordinal'), 'तेस्रो')
        self.assertEqual(num2words(4, lang='ne', to='ordinal'), 'चौथो')
        self.assertEqual(num2words(5, lang='ne', to='ordinal'), 'पाँचौं')
        self.assertEqual(num2words(8, lang='ne', to='ordinal'), 'आठौं')
        self.assertEqual(num2words(9, lang='ne', to='ordinal'), 'नवौं')
        self.assertEqual(num2words(10, lang='ne', to='ordinal'), 'दशौं')
        self.assertEqual(num2words(12, lang='ne', to='ordinal'), 'बाह्रौं')
        self.assertEqual(num2words(20, lang='ne', to='ordinal'), 'बीसौं')
        self.assertEqual(num2words(21, lang='ne', to='ordinal'), 'एक्काइसौं')
        self.assertEqual(num2words(23, lang='ne', to='ordinal'), 'तेइसौं')
        self.assertEqual(num2words(100, lang='ne', to='ordinal'), 'एक सयऔं')

    def test_currency_npr(self):
        """Test NPR (Nepalese Rupee) currency conversion."""
        result = num2words(1, lang='ne', to='currency', currency='NPR')
        self.assertIn('रुपैयाँ', result)

        result = num2words(5, lang='ne', to='currency', currency='NPR')
        self.assertIn('रुपैयाँ', result)

        # Test arba in currency
        result = num2words(
            5000000000, lang='ne', to='currency', currency='NPR'
            )
        self.assertIn('अर्ब', result)
        self.assertIn('रुपैयाँ', result)

        # Test with paisa (fractional)
        result = num2words(5.50, lang='ne', to='currency', currency='NPR')
        self.assertIn('रुपैयाँ', result)
        self.assertIn('पैसा', result)

    def test_currency_other(self):
        """Test USD conversion"""
        result = num2words(100, lang='ne', to='currency', currency='USD')
        self.assertIn('डलर', result)

        result = num2words(1, lang='ne', to='currency', currency='USD')
        self.assertIn('डलर', result)

        result = num2words(2, lang='ne', to='currency', currency='USD')
        self.assertIn('डलर', result)

        """Test EUR conversion."""
        result = num2words(1, lang='ne', to='currency', currency='EUR')
        self.assertEqual(result, 'एक युरो')

        result = num2words(50, lang='ne', to='currency', currency='EUR')
        self.assertIn('पचास', result)
        self.assertIn('युरो', result)

    def test_string_input(self):
        self.assertEqual(num2words('123', lang='ne'), 'एक सय तेइस')
        self.assertEqual(num2words('1000', lang='ne'), 'एक हजार')

    def test_float_input(self):
        """Test float input (truncated to integer for cardinal)"""
        self.assertEqual(num2words(123.45, lang='ne'), 'एक सय तेइस')
        self.assertEqual(num2words(99.99, lang='ne'), 'उनान्सय')
