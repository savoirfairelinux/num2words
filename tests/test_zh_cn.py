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
    def test_low(self):
        self.assertEqual(n2zh_cn(2), "二")
        self.assertEqual(n2zh_cn(2, reading="capital"), "贰")
        self.assertEqual(n2zh_cn(6), "六")
        self.assertEqual(n2zh_cn(6, reading="capital"), "陆")

    def test_high(self):
        self.assertEqual(n2zh_cn(10000), "一万")
        self.assertEqual(n2zh_cn('10000', reading="capital"), "壹万")
        self.assertEqual(n2zh_cn(12345), "一万二千三百四十五")
        self.assertEqual(n2zh_cn('12345', reading="capital"),"壹万贰仟叁佰肆拾伍")
        self.assertEqual(n2zh_cn(10**8), "一亿")
        self.assertEqual(n2zh_cn(10**8, reading="capital"), "壹亿")
        self.assertEqual(n2zh_cn(1234567890), "十二亿三千四百五十六万七千八百九十")
        self.assertEqual(n2zh_cn(1234567890, reading="capital"),"壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾")
        self.assertEqual(n2zh_cn(12345678901234567890), "一千二百三十四京五千六百七十八兆九千零一十二亿三千四百五十六万七千八百九十")
        self.assertEqual(n2zh_cn(120078900500090), "一百二十兆零七百八十九亿零五十万零九十")
        
    def test_mid(self):
        self.assertEqual(n2zh_cn(-123), "负一百二十三")
        self.assertEqual(n2zh_cn(-1000, reading="capital"), "负壹仟")

    def test_cardinal_float(self):
        self.assertEqual(n2zh_cn(0.123456789),"零点一二三四五六七八九")
        # self.assertEqual(n2zh_cn('10.012345678901234567890123456789'),"十点零一二三四五六七八九零一二三四五六七八九零一二三四五六七八九")
        self.assertEqual(n2zh_cn(10**8 + 0.01), "一亿点零一")
        self.assertEqual(n2zh_cn(10**8 + 0.01, reading="capital"),"壹亿点零壹")

    def test_currency(self):
        self.assertEqual(n2zh_cn('0', to="currency", reading="capital"),
                        "零圆正")
        self.assertEqual(n2zh_cn(5.00, to="currency", reading="capital"),
                        "伍圆正")
        self.assertEqual(n2zh_cn('0', to="currency"),
                        "零元")
        self.assertEqual(n2zh_cn(5.00, to="currency"),
                        "五元")
        self.assertEqual(n2zh_cn(10.05, to="currency", reading="capital"),
                        "壹拾圆伍分")
        self.assertEqual(n2zh_cn(10.05, to="currency"),
                        "十元零五分")
        self.assertEqual(n2zh_cn(12.12, to="currency", reading="capital"),
                        "壹拾贰圆壹角贰分")
        self.assertEqual(n2zh_cn(1235678, to="currency", reading="capital"),
                        "壹佰贰拾叁万伍仟陆佰柒拾捌圆正")
        self.assertEqual(n2zh_cn('1234567890.123', to="currency", reading="capital"),
                        "壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾圆壹角贰分")
        self.assertEqual(n2zh_cn(67890.126, to="currency"),
                        "六万七千八百九十元一角三分")
        self.assertEqual(n2zh_cn(987654.3, to="currency", currency = 'USD', reading="capital"),
                        "美元玖拾捌万柒仟陆佰伍拾肆圆叁角")
        self.assertEqual(n2zh_cn(987654.3, to="currency", currency = 'USD'),
                        "美元九十八万七千六百五十四元三角")
        self.assertEqual(n2zh_cn(135.79, to="currency", currency = 'EUR'),
                        "欧元一百三十五元七角九分")
        