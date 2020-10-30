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


def n2zh(*args, **kwargs):
    return num2words(*args, lang='zh', **kwargs)


class Num2WordsJATest(TestCase):
    def test_low(self):
        self.assertEqual(n2zh(0), "零")
        self.assertEqual(n2zh(0, capital=True), "零")
        self.assertEqual(n2zh(1), "一")
        self.assertEqual(n2zh(1, capital=True), "壹")
        self.assertEqual(n2zh(2), "二")
        self.assertEqual(n2zh(2, capital=True), "贰")
        self.assertEqual(n2zh(3), "三")
        self.assertEqual(n2zh(3, capital=True), "叁")
        self.assertEqual(n2zh(4), "四")
        self.assertEqual(n2zh(4, capital=True), "肆")
        self.assertEqual(n2zh(5), "五")
        self.assertEqual(n2zh(5, capital=True), "伍")
        self.assertEqual(n2zh(6), "六")
        self.assertEqual(n2zh(6, capital=True), "陆")
        self.assertEqual(n2zh(7), "七")
        self.assertEqual(n2zh(7, capital=True), "柒")
        self.assertEqual(n2zh(8), "八")
        self.assertEqual(n2zh(8, capital=True), "捌")
        self.assertEqual(n2zh(9), "九")
        self.assertEqual(n2zh(9, capital=True), "玖")
        self.assertEqual(n2zh(10), "十")
        self.assertEqual(n2zh(10, capital=True), "拾")
        self.assertEqual(n2zh(11), "十一")
        self.assertEqual(n2zh(11, capital=True), "拾壹")
        self.assertEqual(n2zh(12), "十二")
        self.assertEqual(n2zh(12, capital=True), "拾贰")
        self.assertEqual(n2zh(13), "十三")
        self.assertEqual(n2zh(13, capital=True), "拾叁")
        self.assertEqual(n2zh(14), "十四")
        self.assertEqual(n2zh(14, capital=True), "拾肆")
        self.assertEqual(n2zh(15), "十五")
        self.assertEqual(n2zh(15, capital=True), "拾伍")
        self.assertEqual(n2zh(16), "十六")
        self.assertEqual(n2zh(16, capital=True), "拾陆")
        self.assertEqual(n2zh(17), "十七")
        self.assertEqual(n2zh(17, capital=True), "拾柒")
        self.assertEqual(n2zh(18), "十八")
        self.assertEqual(n2zh(18, capital=True), "拾捌")
        self.assertEqual(n2zh(19), "十九")
        self.assertEqual(n2zh(19, capital=True), "拾玖")
        self.assertEqual(n2zh(20), "二十")
        self.assertEqual(n2zh(20, capital=True), "贰拾")

    def test_mid(self):
        self.assertEqual(n2zh(100), "一百")
        self.assertEqual(n2zh(100, capital=True), "壹佰")
        self.assertEqual(n2zh(-123), "负一百二十三")
        self.assertEqual(n2zh(123, capital=True), "壹佰贰拾叁")
        self.assertEqual(n2zh(300), "三百")
        self.assertEqual(n2zh('300', capital=True), "叁佰")
        self.assertEqual(n2zh(1000), "壹千")
        self.assertEqual(n2zh(-1000, capital=True), "负壹仟")
        self.assertEqual(n2zh('8000', capital=True), "捌仟")

    def test_high(self):
        self.assertEqual(n2zh(10000), "一万")
        self.assertEqual(n2zh('10000', capital=True), "壹万")
        self.assertEqual(n2zh(12345), "一万二千三百四十五")
        self.assertEqual(n2zh('12345', capital=True),"壹万贰仟叁佰肆拾伍")
        self.assertEqual(n2zh(10**8), "一亿")
        self.assertEqual(n2zh(10**8, capital=True), "壹亿")
        self.assertEqual(n2zh(1234567890), "一十二亿三千四百五十六万七千八百九十")
        self.assertEqual(n2zh(1234567890, capital=True),"壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾")
        self.assertEqual(n2zh(12345678901234567890), "一千二百三十四亿五千六百七十八万九千零一十二亿三千四百五十六万七千八百九十")
        self.assertEqual(n2zh(120078900500090), "一百二十万零七百八十九亿零五十万零九十")


    def test_cardinal_float(self):
        self.assertEqual(n2zh(0.123456789),"零点一二三四五六七八九")
        self.assertEqual(n2zh('10.012345678901234567890123456789'),"一十点零一二三四五六七八九零一二三四五六七八九零一二三四五六七八九")
        self.assertEqual(n2zh(10**8 + 0.01), "一亿点零一")
        self.assertEqual(n2zh(10**8 + 0.01, capital=True),"壹亿点零壹")

    def test_ordinal(self):
        self.assertEqual(n2zh(0, to="ordinal"), "第〇")
        self.assertEqual(n2zh(2, to="ordinal"), "第二")
        self.assertEqual(n2zh(10, to="ordinal"), "第十")
        self.assertEqual(n2zh(11, to="ordinal"), "第十一")
        self.assertEqual(n2zh('19', to="ordinal"), "第十九")
        self.assertEqual(n2zh(109, to="ordinal"), "第一百〇九")
        self.assertEqual(n2zh(100909, to="ordinal"), "第十万〇九百〇九")
        
    def test_ordinal_num(self):
        self.assertEqual(n2zh(120, to="ordinal_num"), "第120")

    def test_currency(self):
        self.assertEqual(n2zh('0', to="currency"),
                         "零元整")
        self.assertEqual(n2zh(5.00, to="currency"),
                         "伍圆整")
        self.assertEqual(n2zh(10.05, to="currency"),
                         "壹拾圆零伍分")
        self.assertEqual(n2zh(12.12, to="currency"),
                         "壹拾贰圆壹角贰分")
        self.assertEqual(n2zh(1235678, to="currency"),
                         "壹佰贰拾叁万伍仟陆佰柒拾捌圆整")
        self.assertEqual(n2zh('1234567890.123', to="currency"),
                         "壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾圆壹角贰分")
        self.assertEqual(n2zh(67890.126, to="currency", capital=False),
                         "六万七千八百九十元一角三分")
        self.assertEqual(n2zh(987654.3, to="currency", currency = 'USD'),
                         "玖拾捌万柒仟陆佰伍拾肆美圆叁拾美分")
        self.assertEqual(n2zh(1234.26, to="currency", currency = 'USD', capital=False),
                         "一千二百三十四美元二十六美分")
        self.assertEqual(n2zh(314.87, to="currency", currency = 'EUR', capital=False),
                         "三百一十四欧元八十七分")
        
    def test_year(self):
        self.assertEqual(n2zh(2017, to="year"), "二〇二〇年")
        
