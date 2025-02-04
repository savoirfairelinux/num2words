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


def n2zh_cn(*args, **kwargs):
    return num2words(*args, lang='zh_CN', **kwargs)


class Num2WordsZHTest(TestCase):
    def test_currency(self):
        self.assertEqual(n2zh_cn('0', to="currency", capital=True),
                        "零圆整")
        self.assertEqual(n2zh_cn(5.00, to="currency", capital=True),
                        "伍圆整")
        self.assertEqual(n2zh_cn('0', to="currency"),
                        "零元")
        self.assertEqual(n2zh_cn(5.00, to="currency"),
                        "五元")
        self.assertEqual(n2zh_cn(10.05, to="currency", capital=True),
                        "壹拾圆零伍分")
        self.assertEqual(n2zh_cn(10.05, to="currency"),
                        "十元零五毫")
        self.assertEqual(n2zh_cn(12.12, to="currency", capital=True),
                        "壹拾贰圆壹角贰分")
        self.assertEqual(n2zh_cn(1235678, to="currency", capital=True),
                        "壹佰贰拾叁万伍仟陆佰柒拾捌圆整")
        self.assertEqual(n2zh_cn('1234567890.123', to="currency", capital=True),
                        "壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾圆壹角贰分")
        self.assertEqual(n2zh_cn(67890.126, to="currency"),
                        "六万七千八百九十元一角三分")
        self.assertEqual(n2zh_cn(987654.3, to="currency", currency = 'USD', capital=True),
                        "美元玖拾捌万柒仟陆佰伍拾肆圆叁角")
        self.assertEqual(n2zh_cn(987654.3, to="currency", currency = 'USD'),
                        "美元九十八万七千六百五十四元三角")
        self.assertEqual(n2zh_cn(135.79, to="currency", currency = 'EUR'),
                        "欧元一百三十五元七角九分")
        