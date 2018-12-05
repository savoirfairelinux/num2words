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

from __future__ import division, print_function, unicode_literals

from unittest import TestCase

from num2words import num2words


def n2k(*args, **kwargs):
    return num2words(*args, lang='ko', **kwargs)


class Num2WordsKOTest(TestCase):
    def test_low(self):
        cases = [(0, "영"), (1, "일"), (2, "이"), (3, "삼"), (4, "사"), (5, "오"),
                 (6, "육"), (7, "칠"), (8, "팔"), (9, "구"), (10, "십"),
                 (11, "십일"), (12, "십이"), (13, "십삼"), (14, "십사"),
                 (15, "십오"), (16, "십육"), (17, "십칠"),
                 (18, "십팔"), (19, "십구"), (20, "이십"), (25, "이십오"),
                 (31, "삼십일"), (42, "사십이"), (54, "오십사"), (63, "육십삼"),
                 (76, "칠십육"), (89, "팔십구"), (98, "구십팔")]
        for num, out in cases:
            self.assertEqual(n2k(num), out)

    def test_mid(self):
        cases = [(100, "백"), (121, "백이십일"), (160, "백육십"), (256, "이백오십육"),
                 (285, "이백팔십오"), (486, "사백팔십육"), (627, "육백이십칠"),
                 (808, "팔백팔"), (999, "구백구십구"), (1004, "천사"),
                 (2018, "이천십팔"), (7063, "칠천육십삼")]
        for num, out in cases:
            self.assertEqual(n2k(num), out)

    def test_high(self):
        cases = [(10000, "만"), (11020, "만 천이십"), (25891, "이만 오천팔백구십일"),
                 (64237, "육만 사천이백삼십칠"), (241572, "이십사만 천오백칠십이"),
                 (100000000, "일억"), (5000500000000, "오조 오억")]
        for num, out in cases:
            self.assertEqual(n2k(num), out)

    def test_negative(self):
        cases = [(-11, "마이너스 십일"), (-15, "마이너스 십오"),
                 (-18, "마이너스 십팔"), (-241572, "마이너스 이십사만 천오백칠십이")]
        for num, out in cases:
            self.assertEqual(n2k(num), out)

    def test_year(self):
        cases = [(2000, "이천년"), (2002, "이천이년"), (2018, "이천십팔년"),
                 (1954, "천구백오십사년"), (1910, "천구백십년"), (-1000, "기원전 천년")]
        for num, out in cases:
            self.assertEqual(n2k(num, to="year"), out)

    def test_currency(self):
        cases_krw = [(8350, "팔천삼백오십원"), (14980, "만사천구백팔십원"),
                     (250004000, "이억오천만사천원")]
        cases_usd = [(4, "사달러 영센트"), (19.55, "십구달러 오십오센트")]
        cases_jpy = [(15, "십오엔"), (50, "오십엔")]
        for num, out in cases_krw:
            self.assertEqual(n2k(num, to="currency"), out)
        for num, out in cases_usd:
            self.assertEqual(n2k(num, to="currency", currency="USD"), out)
        for num, out in cases_jpy:
            self.assertEqual(n2k(num, to="currency", currency="JPY"), out)
        with self.assertRaises(ValueError):
            n2k(190.55, to="currency")
        with self.assertRaises(NotImplementedError):
            n2k(4, to="currency", currency="EUR")

    def test_ordinal(self):
        cases = [(1, "첫 번째"), (101, "백 한 번째"), (2, "두 번째"), (5, "다섯 번째"),
                 (10, "열 번째"), (25, "스물다섯 번째"), (137, "백 서른일곱 번째")]
        for num, out in cases:
            self.assertEqual(n2k(num, to="ordinal"), out)

    def test_ordinal_num(self):
        cases = [(1, "1 번째"), (101, "101 번째"), (25, "25 번째")]
        for num, out in cases:
            self.assertEqual(n2k(num, to="ordinal_num"), out)
