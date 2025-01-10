# -*- coding: utf-8 -*-
# Author: Mehedi Hasan Khondoker
# Email: mehedihasankhondoker [at] gmail.com
# Copyright (c) 2024, Mehedi Hasan Khondoker.  All Rights Reserved.

# This library is build for Bangladesh format Number to Word conversion.
# You are welcome as contributor to the library.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.

from __future__ import unicode_literals

from decimal import Decimal
from unittest import TestCase

from num2words import num2words
from num2words.lang_BN import Num2Word_BN, NumberTooLargeError


class Num2WordsBNTest(TestCase):
    maxDiff = None

    def test_negative(self):
        self.assertEqual(num2words(-1, lang="bn"), u'এক')

    def test_0(self):
        self.assertEqual(num2words(0, lang="bn"), u'শূন্য')

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="bn"), u'এক')
        self.assertEqual(num2words(2, lang="bn"), u'দুই')
        self.assertEqual(num2words(7, lang="bn"), u'সাত')
        self.assertEqual(num2words(10, lang="bn"), u'দশ')

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="bn"), u'এগারো')
        self.assertEqual(num2words(13, lang="bn"), u'তেরো')
        self.assertEqual(num2words(15, lang="bn"), u'পনের')
        self.assertEqual(num2words(16, lang="bn"), u'ষোল')
        self.assertEqual(num2words(19, lang="bn"), u'উনিশ')

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="bn"), u'বিশ')
        self.assertEqual(num2words(23, lang="bn"), u'তেইশ')
        self.assertEqual(num2words(28, lang="bn"), u'আটাশ')
        self.assertEqual(num2words(31, lang="bn"), u'একত্রিশ')
        self.assertEqual(num2words(40, lang="bn"), u'চল্লিশ')
        self.assertEqual(num2words(66, lang="bn"), u'ছিষট্টি')
        self.assertEqual(num2words(92, lang="bn"), u'বিরানব্বই')

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="bn"), u'একশত')
        self.assertEqual(num2words(111, lang="bn"), u'একশত এগারো')
        self.assertEqual(num2words(150, lang="bn"), u'একশত পঞ্চাশ')
        self.assertEqual(num2words(196, lang="bn"), u'একশত ছিয়ানব্বই')
        self.assertEqual(num2words(200, lang="bn"), u'দুইশত')
        self.assertEqual(num2words(210, lang="bn"), u'দুইশত দশ')
        self.assertEqual(num2words(701, lang="bn"), u'সাতশত এক')
        self.assertEqual(num2words(999, lang="bn"), u'নয়শত নিরানব্বই')

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="bn"), u'এক হাজার')
        self.assertEqual(num2words(1001, lang="bn"), u'এক হাজার এক')
        self.assertEqual(num2words(1002, lang="bn"), u'এক হাজার দুই')
        self.assertEqual(num2words(1010, lang="bn"), u'এক হাজার দশ')
        self.assertEqual(num2words(1110, lang="bn"), u'এক হাজার একশত দশ')
        self.assertEqual(num2words(1111, lang="bn"), u'এক হাজার একশত এগারো')
        self.assertEqual(num2words(1500, lang="bn"), u'এক হাজার পাঁচশত')
        self.assertEqual(num2words(2000, lang="bn"), u'দুই হাজার')
        self.assertEqual(num2words(2042, lang="bn"), u'দুই হাজার বিয়াল্লিশ')
        self.assertEqual(num2words(3000, lang="bn"), u'তিন হাজার')
        self.assertEqual(num2words(3301, lang="bn"), u'তিন হাজার তিনশত এক')
        self.assertEqual(num2words(3108, lang="bn"), u'তিন হাজার একশত আট')
        self.assertEqual(num2words(6870, lang="bn"), u'ছয় হাজার আটশত সত্তর')
        self.assertEqual(num2words(7378, lang="bn"),
                         u'সাত হাজার তিনশত আটাত্তর')
        self.assertEqual(num2words(9999, lang="bn"),
                         u'নয় হাজার নয়শত নিরানব্বই')

    def test_10000_to_99999(self):
        self.assertEqual(num2words(10000, lang="bn"),
                         u'দশ হাজার')
        self.assertEqual(num2words(10501, lang="bn"),
                         u'দশ হাজার পাঁচশত এক')
        self.assertEqual(num2words(10999, lang="bn"),
                         u'দশ হাজার নয়শত নিরানব্বই')
        self.assertEqual(num2words(13000, lang="bn"), u'তেরো হাজার')
        self.assertEqual(num2words(15333, lang="bn"),
                         u'পনের হাজার তিনশত তেত্রিশ')
        self.assertEqual(num2words(21111, lang="bn"), u'একুশ হাজার একশত এগারো')
        self.assertEqual(num2words(21003, lang="bn"), u'একুশ হাজার তিন')
        self.assertEqual(num2words(25020, lang="bn"), u'পঁচিশ হাজার বিশ')
        self.assertEqual(num2words(68700, lang="bn"),
                         u'আটষট্টি হাজার সাতশত')
        self.assertEqual(num2words(73781, lang="bn"),
                         u'তিয়াত্তর হাজার সাতশত একাশি')
        self.assertEqual(num2words(99999, lang="bn"),
                         u'নিরানব্বই হাজার নয়শত নিরানব্বই')

    def test_100000_to_999999(self):
        self.assertEqual(num2words(100000, lang="bn"), u'এক লাখ')
        self.assertEqual(num2words('100000', lang="bn"), u'এক লাখ')
        self.assertEqual(num2words(199999, lang="bn"),
                         u'এক লাখ নিরানব্বই হাজার নয়শত নিরানব্বই')
        self.assertEqual(num2words(110000, lang="bn"), u'এক লাখ দশ হাজার')
        self.assertEqual(num2words(150010, lang="bn"),
                         u'এক লাখ পঞ্চাশ হাজার দশ')
        self.assertEqual(num2words('200200', lang="bn"), u'দুই লাখ দুইশত')
        self.assertEqual(num2words(737812, lang="bn"),
                         u'সাত লাখ সাতত্রিশ হাজার আটশত বারো')
        self.assertEqual(num2words('999999', lang="bn"),
                         u'নয় লাখ নিরানব্বই হাজার নয়শত নিরানব্বই')

    def test_1000000_to_9999999999999999(self):
        self.assertEqual(num2words(1000000, lang="bn"), u'দশ লাখ')
        self.assertEqual(num2words(20000000, lang="bn"), u'দুই কোটি')
        self.assertEqual(num2words(300000000, lang="bn"), u'ত্রিশ কোটি')
        self.assertEqual(num2words(4000000000, lang="bn"), u'চারশত কোটি')
        self.assertEqual(num2words(50000000000, lang="bn"), u'পাঁচ হাজার কোটি')
        self.assertEqual(num2words(600000000000, lang="bn"), u'ষাট হাজার কোটি')
        self.assertEqual(num2words(7000000000000, lang="bn"), u'সাত লাখ কোটি')
        self.assertEqual(num2words(80000000000000, lang="bn"), u'আশি লাখ কোটি')
        self.assertEqual(num2words
                         (900000000000000, lang="bn"), u'নয় কোটি কোটি')
        self.assertEqual(num2words(999999999999999, lang="bn"),
                         u'নয় কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই')  # noqa: E501
        self.assertEqual(num2words(9999999999999999, lang="bn"),
                         u'নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই')  # noqa: E501

    def test_dosomik_0_to_999999999999999999(self):
        self.assertEqual(num2words(0.56, lang="bn"), u'শূন্য দশমিক পাঁচ ছয়')
        self.assertEqual(num2words(1.11, lang="bn"), u'এক দশমিক এক এক')
        self.assertEqual(num2words(2.66, lang="bn"), u'দুই দশমিক ছয় ছয়')
        self.assertEqual(num2words(7.68, lang="bn"), u'সাত দশমিক ছয় আট')
        self.assertEqual(num2words('10.35', lang="bn"), u'দশ দশমিক তিন পাঁচ')
        self.assertEqual(num2words('11.47', lang="bn"), u'এগারো দশমিক চার সাত')
        self.assertEqual(num2words(13.69, lang="bn"), u'তেরো দশমিক ছয় নয়')
        self.assertEqual(num2words(15.96, lang="bn"), u'পনের দশমিক নয় ছয়')
        self.assertEqual(num2words(16.9999, lang="bn"),
                         u'ষোল দশমিক নয় নয় নয় নয়')
        self.assertEqual(num2words(19.56587, lang="bn"),
                         u'উনিশ দশমিক পাঁচ ছয় পাঁচ আট সাত')
        self.assertEqual(num2words(31.31, lang="bn"), u'একত্রিশ দশমিক তিন এক')
        self.assertEqual(num2words(40.85, lang="bn"), u'চল্লিশ দশমিক আট পাঁচ')
        self.assertEqual(num2words(66.66, lang="bn"), u'ছিষট্টি দশমিক ছয় ছয়')
        self.assertEqual(num2words(92.978, lang="bn"),
                         u'বিরানব্বই দশমিক নয় সাত আট')
        self.assertEqual(num2words(1000001.10, lang="bn"),
                         u'দশ লাখ এক দশমিক এক')
        self.assertEqual(num2words(20000000.22, lang="bn"),
                         u'দুই কোটি দশমিক দুই দুই')
        self.assertEqual(num2words(300030000.33, lang="bn"),
                         u'ত্রিশ কোটি ত্রিশ হাজার দশমিক তিন তিন')
        self.assertEqual(num2words('4004000444.44', lang="bn"),
                         u'চারশত কোটি চল্লিশ লাখ চারশত চৌচল্লিশ দশমিক চার চার')
        self.assertEqual(num2words(50000000001.50, lang="bn"),
                         u'পাঁচ হাজার কোটি এক দশমিক পাঁচ')
        self.assertEqual(num2words(600000000600.66, lang="bn"),
                         u'ষাট হাজার কোটি ছয়শত দশমিক ছয় ছয়')
        self.assertEqual(num2words(7000000000000.77, lang="bn"),
                         u'সাত লাখ কোটি দশমিক সাত সাত')
        self.assertEqual(num2words(80000000000888.88, lang="bn"),
                         u'আশি লাখ কোটি আটশত আটাশি দশমিক আট আট')
        self.assertEqual(num2words(900000000000000.9, lang="bn"),
                         u'নয় কোটি কোটি দশমিক নয়')
        self.assertEqual(num2words(999999999999999.9, lang="bn"),
                         u'নয় কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই দশমিক নয়')  # noqa: E501
        self.assertEqual(num2words(9999999999999999.99, lang="bn"),
                         u'একশত কোটি কোটি')
        self.assertEqual(num2words(99999999999999999.99, lang="bn"),
                         u'এক হাজার কোটি কোটি')
        self.assertEqual(num2words('999999999999999999.9', lang="bn"),
                         u'নয় হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই দশমিক নয়')  # noqa: E501

    def test_to_currency(self):
        n = Num2Word_BN()
        self.assertEqual(n.to_currency(20.0), u'বিশ টাকা')
        self.assertEqual(n.to_currency(20.50), u'বিশ টাকা পঞ্চাশ পয়সা')
        self.assertEqual(n.to_currency(33.51), u'তেত্রিশ টাকা একান্ন পয়সা')
        self.assertEqual(n.to_currency(99.99),
                         u'নিরানব্বই টাকা নিরানব্বই পয়সা')
        self.assertEqual(n.to_currency(10000.1),
                         u'দশ হাজার টাকা দশ পয়সা')
        self.assertEqual(n.to_currency(555555.50),
                         u'পাঁচ লাখ পঞ্চান্ন হাজার পাঁচশত পঞ্চান্ন টাকা পঞ্চাশ পয়সা')  # noqa: E501
        self.assertEqual(n.to_currency(6666676),
                         u'ছিষট্টি লাখ ছিষট্টি হাজার ছয়শত ছিয়াত্তর টাকা')
        self.assertEqual(n.to_currency(777777777),
                         u'সাতাত্তর কোটি সাতাত্তর লাখ সাতাত্তর হাজার সাতশত সাতাত্তর টাকা')  # noqa: E501
        self.assertEqual(n.to_currency(7777777778),
                         u'সাতশত সাতাত্তর কোটি সাতাত্তর লাখ সাতাত্তর হাজার সাতশত আটাত্তর টাকা')  # noqa: E501
        self.assertEqual(n.to_currency(97777777778),
                         u'নয় হাজার সাতশত সাতাত্তর কোটি সাতাত্তর লাখ সাতাত্তর হাজার সাতশত আটাত্তর টাকা')  # noqa: E501
        self.assertEqual(n.to_currency(977777777781),
                         u'সাতানব্বই হাজার সাতশত সাতাত্তর কোটি সাতাত্তর লাখ সাতাত্তর হাজার সাতশত একাশি টাকা')  # noqa: E501
        self.assertEqual(n.to_currency(9777777779781),
                         u'নয় লাখ সাতাত্তর হাজার সাতশত সাতাত্তর কোটি সাতাত্তর লাখ উনআশি হাজার সাতশত একাশি টাকা')  # noqa: E501

    def test_to_cardinal(self):
        n = Num2Word_BN()
        self.assertEqual(n.to_cardinal(0.56), u'শূন্য দশমিক পাঁচ ছয়')
        self.assertEqual(n.to_cardinal(1.11), u'এক দশমিক এক এক')
        self.assertEqual(n.to_cardinal(2.66), u'দুই দশমিক ছয় ছয়')
        self.assertEqual(n.to_cardinal(7.68), u'সাত দশমিক ছয় আট')
        self.assertEqual(n.to_cardinal('10.35'), u'দশ দশমিক তিন পাঁচ')
        self.assertEqual(n.to_cardinal('11.47'), u'এগারো দশমিক চার সাত')
        self.assertEqual(n.to_cardinal(13.69), u'তেরো দশমিক ছয় নয়')
        self.assertEqual(n.to_cardinal(15.96), u'পনের দশমিক নয় ছয়')
        self.assertEqual(n.to_cardinal(16.9999), u'ষোল দশমিক নয় নয় নয় নয়')
        self.assertEqual(n.to_cardinal(19.56587),
                         u'উনিশ দশমিক পাঁচ ছয় পাঁচ আট সাত')
        self.assertEqual(n.to_cardinal(31.31), u'একত্রিশ দশমিক তিন এক')
        self.assertEqual(n.to_cardinal(40.85), u'চল্লিশ দশমিক আট পাঁচ')
        self.assertEqual(n.to_cardinal(66.66), u'ছিষট্টি দশমিক ছয় ছয়')
        self.assertEqual(n.to_cardinal(92.978), u'বিরানব্বই দশমিক নয় সাত আট')
        self.assertEqual(n.to_cardinal(1000001.10), u'দশ লাখ এক দশমিক এক')
        self.assertEqual(n.to_cardinal(20000000.22), u'দুই কোটি দশমিক দুই দুই')
        self.assertEqual(n.to_cardinal(300030000.33),
                         u'ত্রিশ কোটি ত্রিশ হাজার দশমিক তিন তিন')
        self.assertEqual(n.to_cardinal('4004000444.44'),
                         u'চারশত কোটি চল্লিশ লাখ চারশত চৌচল্লিশ দশমিক চার চার')
        self.assertEqual(n.to_cardinal(50000000001.50),
                         u'পাঁচ হাজার কোটি এক দশমিক পাঁচ')
        self.assertEqual(n.to_cardinal(600000000600.66),
                         u'ষাট হাজার কোটি ছয়শত দশমিক ছয় ছয়')
        self.assertEqual(n.to_cardinal(7000000000000.77),
                         u'সাত লাখ কোটি দশমিক সাত সাত')
        self.assertEqual(n.to_cardinal(80000000000888.88),
                         u'আশি লাখ কোটি আটশত আটাশি দশমিক আট আট')
        self.assertEqual(n.to_cardinal(900000000000000.9),
                         u'নয় কোটি কোটি দশমিক নয়')
        self.assertEqual(n.to_cardinal(999999999999999.9),
                         u'নয় কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই দশমিক নয়')  # noqa: E501
        self.assertEqual(n.to_cardinal(9999999999999999.99),
                         u'একশত কোটি কোটি')
        self.assertEqual(n.to_cardinal(99999999999999999.99),
                         u'এক হাজার কোটি কোটি')
        self.assertEqual(n.to_cardinal('999999999999999999.99'),
                         u'নয় হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই দশমিক নয় নয়')  # noqa: E501

    def test_to_ordinal(self):
        n = Num2Word_BN()
        self.assertEqual(n.to_ordinal(0.56), u'শূন্য দশমিক পাঁচ ছয়')
        self.assertEqual(n.to_ordinal(1.11), u'এক দশমিক এক এক')
        self.assertEqual(n.to_ordinal(2.66), u'দুই দশমিক ছয় ছয়')
        self.assertEqual(n.to_ordinal(7.68), u'সাত দশমিক ছয় আট')
        self.assertEqual(n.to_ordinal('10.35'), u'দশ দশমিক তিন পাঁচ')
        self.assertEqual(n.to_ordinal('11.47'), u'এগারো দশমিক চার সাত')
        self.assertEqual(n.to_ordinal(13.69), u'তেরো দশমিক ছয় নয়')
        self.assertEqual(n.to_ordinal(15.96), u'পনের দশমিক নয় ছয়')
        self.assertEqual(n.to_ordinal(16.9999), u'ষোল দশমিক নয় নয় নয় নয়')
        self.assertEqual(n.to_ordinal(19.56587),
                         u'উনিশ দশমিক পাঁচ ছয় পাঁচ আট সাত')
        self.assertEqual(n.to_ordinal(31.31), u'একত্রিশ দশমিক তিন এক')
        self.assertEqual(n.to_ordinal(40.85), u'চল্লিশ দশমিক আট পাঁচ')
        self.assertEqual(n.to_ordinal(66.66), u'ছিষট্টি দশমিক ছয় ছয়')
        self.assertEqual(n.to_ordinal(92.978), u'বিরানব্বই দশমিক নয় সাত আট')
        self.assertEqual(n.to_ordinal(1000001.10), u'দশ লাখ এক দশমিক এক')
        self.assertEqual(n.to_ordinal(20000000.22), u'দুই কোটি দশমিক দুই দুই')
        self.assertEqual(n.to_ordinal(300030000.33),
                         u'ত্রিশ কোটি ত্রিশ হাজার দশমিক তিন তিন')
        self.assertEqual(n.to_ordinal('4004000444.44'),
                         u'চারশত কোটি চল্লিশ লাখ চারশত চৌচল্লিশ দশমিক চার চার')
        self.assertEqual(n.to_ordinal(50000000001.50),
                         u'পাঁচ হাজার কোটি এক দশমিক পাঁচ')
        self.assertEqual(n.to_ordinal(600000000600.66),
                         u'ষাট হাজার কোটি ছয়শত দশমিক ছয় ছয়')
        self.assertEqual(n.to_ordinal(7000000000000.77),
                         u'সাত লাখ কোটি দশমিক সাত সাত')
        self.assertEqual(n.to_ordinal(80000000000888.88),
                         u'আশি লাখ কোটি আটশত আটাশি দশমিক আট আট')
        self.assertEqual(n.to_ordinal(900000000000000.9),
                         u'নয় কোটি কোটি দশমিক নয়')
        self.assertEqual(n.to_ordinal(999999999999999.9),
                         u'নয় কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই দশমিক নয়')  # noqa: E501
        self.assertEqual(n.to_ordinal(9999999999999999.99),
                         u'একশত কোটি কোটি')
        self.assertEqual(n.to_ordinal(99999999999999999.99),
                         u'এক হাজার কোটি কোটি')
        self.assertEqual(n.to_ordinal('999999999999999999.99'),
                         u'নয় হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই দশমিক নয় নয়')  # noqa: E501

    def test_to_year(self):
        n = Num2Word_BN()
        self.assertEqual(n.to_year(1), u'এক সাল')
        self.assertEqual(n.to_year(1000), u'এক হাজার সাল')
        self.assertEqual(n.to_year(1500), u'এক হাজার পাঁচশত সাল')
        self.assertEqual(n.to_year(1820), u'এক হাজার আটশত বিশ সাল')
        self.assertEqual(n.to_year(1920), u'এক হাজার নয়শত বিশ সাল')
        self.assertEqual(n.to_year(2024), u'দুই হাজার চব্বিশ সাল')
        self.assertEqual(n.to_year(2004), u'দুই হাজার চার সাল')

    def test_to_ordinal_num(self):
        n = Num2Word_BN()
        self.assertEqual(n.to_ordinal_num(1), u'প্রথম')
        self.assertEqual(n.to_ordinal_num(1000), u'এক হাজারতম')
        self.assertEqual(n.to_ordinal_num(1500), u'এক হাজার পাঁচশতম')
        self.assertEqual(n.to_ordinal_num(1820), u'এক হাজার আটশত বিশতম')
        self.assertEqual(n.to_ordinal_num(1920), u'এক হাজার নয়শত বিশতম')
        self.assertEqual(n.to_ordinal_num(2024), u'দুই হাজার চব্বিশতম')
        self.assertEqual(n.to_ordinal_num(2004), u'দুই হাজার চারতম')

    def test_max_number_error(self):
        n = Num2Word_BN()

        with self.assertRaises(NumberTooLargeError):
            n.to_ordinal(
                99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991)  # noqa: E501

        with self.assertRaises(NumberTooLargeError):
            n.to_cardinal(
                99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991)  # noqa: E501

        with self.assertRaises(NumberTooLargeError):
            n.to_year(
                99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991)  # noqa: E501

        with self.assertRaises(NumberTooLargeError):
            n.to_ordinal_num(
                99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991)  # noqa: E501

        with self.assertRaises(NumberTooLargeError):
            n.to_currency(
                99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991)  # noqa: E501

        with self.assertRaises(NumberTooLargeError):
            num2words(
                99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991,  # noqa: E501
                lang="bn")

    def test_is_smaller_than_max_number(self):
        n = Num2Word_BN()
        self.assertEqual(n._is_smaller_than_max_number(55555), True)

    def test_is_smaller_than_max_number_error(self):
        with self.assertRaises(NumberTooLargeError):
            n = Num2Word_BN()
            n._is_smaller_than_max_number(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)  # noqa: E501

    def test_parse_number(self):
        n = Num2Word_BN()
        self.assertEqual(n.parse_number(Decimal(3.25)), (3, 25))
        self.assertEqual(n.parse_number(Decimal(300.2550)),
                         (300, 2549999999999954525264911353588104248046875))

    def test_parse_paisa(self):
        n = Num2Word_BN()
        self.assertEqual(n.parse_paisa(Decimal(3.25)), (3, 25))
        self.assertEqual(n.parse_paisa(300.2550), (300, 25))
        self.assertEqual(n.parse_paisa(100.5), (100, 50))

    def test_number_to_bengali_word(self):
        n = Num2Word_BN()
        self.assertEqual(n._number_to_bengali_word(3), "তিন")
        self.assertEqual(n._number_to_bengali_word(2550),
                         "দুই হাজার পাঁচশত পঞ্চাশ")
        self.assertEqual(n._number_to_bengali_word(9999999999999999),
                         "নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই কোটি নিরানব্বই লাখ নিরানব্বই হাজার নয়শত নিরানব্বই")  # noqa: E501
