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


def n2zh_hk(*args, **kwargs):
    return num2words(*args, lang='zh_HK', **kwargs)


class Num2WordsZHTest(TestCase):
    def test_currency(self):
        self.assertEqual(n2zh_hk('0', to="currency", reading="capital"),
                        "零圓整")
        self.assertEqual(n2zh_hk(5.00, to="currency", reading="capital"),
                        "伍圓整")
        self.assertEqual(n2zh_hk('0', to="currency"),
                        "零元")
        self.assertEqual(n2zh_hk(5.00, to="currency"),
                        "五元")
        self.assertEqual(n2zh_hk(10.05, to="currency", reading="capital"),
                        "壹拾圓伍分")
        self.assertEqual(n2zh_hk(10.05, to="currency"),
                        "十元零五仙")
        self.assertEqual(n2zh_hk(12.12, to="currency", reading="capital"),
                        "壹拾貳圓壹角貳分")
        self.assertEqual(n2zh_hk(1235678, to="currency", reading="capital"),
                        "壹佰貳拾叁萬伍仟陸佰柒拾捌圓整")
        self.assertEqual(n2zh_hk('1234567890.123', to="currency", reading="capital"),
                        "壹拾貳億叁仟肆佰伍拾陸萬柒仟捌佰玖拾圓壹角貳分")
        self.assertEqual(n2zh_hk(67890.126, to="currency"),
                        "六萬七千八百九十元一毫三仙")
        self.assertEqual(n2zh_hk(987654.3, to="currency", currency = 'USD', reading="capital"),
                        "美元玖拾捌萬柒仟陸佰伍拾肆圓叁角")
        self.assertEqual(n2zh_hk(987654.3, to="currency", currency = 'USD'),
                        "美元九十八萬七千六百五十四元三毫")
        self.assertEqual(n2zh_hk(135.79, to="currency", currency = 'EUR'),
                        "歐羅一百三十五元七毫九仙")
        