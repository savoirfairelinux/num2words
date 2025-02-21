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


class Num2WordsZHTest(TestCase):
    def test_low(self):
        self.assertEqual(n2zh(0), "零")
        self.assertEqual(n2zh(0, capital=True), "零")
        self.assertEqual(n2zh(1), "一")
        self.assertEqual(n2zh(1, capital=True), "壹")
        self.assertEqual(n2zh(2), "二")
        self.assertEqual(n2zh(2, capital=True), "貳")
        self.assertEqual(n2zh(3), "三")
        self.assertEqual(n2zh(3, capital=True), "叁")
        self.assertEqual(n2zh(4), "四")
        self.assertEqual(n2zh(4, capital=True), "肆")
        self.assertEqual(n2zh(5), "五")
        self.assertEqual(n2zh(5, capital=True), "伍")
        self.assertEqual(n2zh(6), "六")
        self.assertEqual(n2zh(6, capital=True), "陸")
        self.assertEqual(n2zh(7), "七")
        self.assertEqual(n2zh(7, capital=True), "柒")
        self.assertEqual(n2zh(8), "八")
        self.assertEqual(n2zh(8, capital=True), "捌")
        self.assertEqual(n2zh(9), "九")
        self.assertEqual(n2zh(9, capital=True), "玖")
        self.assertEqual(n2zh(10), "十")
        self.assertEqual(n2zh(10, capital=True), "壹拾")
        self.assertEqual(n2zh(11), "十一")
        self.assertEqual(n2zh(11, capital=True), "壹拾壹")
        self.assertEqual(n2zh(12), "十二")
        self.assertEqual(n2zh(12, capital=True), "壹拾貳")
        self.assertEqual(n2zh(13), "十三")
        self.assertEqual(n2zh(13, capital=True), "壹拾叁")
        self.assertEqual(n2zh(14), "十四")
        self.assertEqual(n2zh(14, capital=True), "壹拾肆")
        self.assertEqual(n2zh(15), "十五")
        self.assertEqual(n2zh(15, capital=True), "壹拾伍")
        self.assertEqual(n2zh(16), "十六")
        self.assertEqual(n2zh(16, capital=True), "壹拾陸")
        self.assertEqual(n2zh(17), "十七")
        self.assertEqual(n2zh(17, capital=True), "壹拾柒")
        self.assertEqual(n2zh(18), "十八")
        self.assertEqual(n2zh(18, capital=True), "壹拾捌")
        self.assertEqual(n2zh(19), "十九")
        self.assertEqual(n2zh(19, capital=True), "壹拾玖")
        self.assertEqual(n2zh(20), "二十")
        self.assertEqual(n2zh(20, capital=True), "貳拾")

    def test_mid(self):
        self.assertEqual(n2zh(100), "一百")
        self.assertEqual(n2zh(100, capital=True), "壹佰")
        self.assertEqual(n2zh(-123), "負一百二十三")
        self.assertEqual(n2zh(123, capital=True), "壹佰貳拾叁")
        self.assertEqual(n2zh(300), "三百")
        self.assertEqual(n2zh('300', capital=True), "叁佰")
        self.assertEqual(n2zh(1000), "一千")
        self.assertEqual(n2zh(-1000, capital=True), "負壹仟")
        self.assertEqual(n2zh('8000', capital=True), "捌仟")

    def test_high(self):
        self.assertEqual(n2zh(10000), "一萬")
        self.assertEqual(n2zh('10000', capital=True), "壹萬")
        self.assertEqual(n2zh(12345), "一萬二千三百四十五")
        self.assertEqual(n2zh('12345', capital=True),"壹萬貳仟叁佰肆拾伍")
        self.assertEqual(n2zh(10**8), "一億")
        self.assertEqual(n2zh(10**8, capital=True), "壹億")
        self.assertEqual(n2zh(1234567890), "十二億三千四百五十六萬七千八百九十")
        self.assertEqual(n2zh(1234567890, capital=True),"壹拾貳億叁仟肆佰伍拾陸萬柒仟捌佰玖拾")
        self.assertEqual(n2zh(12345678901234567890), "一千二百三十四京五千六百七十八兆九千零一十二億三千四百五十六萬七千八百九十")
        self.assertEqual(n2zh(120078900500090), "一百二十兆零七百八十九億零五十萬零九十")

    def test_stuff_zero(self):
        self.assertEqual(n2zh(1203405, stuff_zero=1), "一百二十萬零三千四百零五")
        self.assertEqual(n2zh(1203405, stuff_zero=2), "一百二十萬三千四百零五")
        self.assertEqual(n2zh(1203405, stuff_zero=3), "一百二十萬三千四百五")
        self.assertEqual(n2zh(908070605, stuff_zero=1), "九億零八百零七萬零六百零五")
        self.assertEqual(n2zh(908070605, stuff_zero=2), "九億零八百零七萬零六百零五")
        self.assertEqual(n2zh(908070605, stuff_zero=3), "九億八百七萬六百五")
        self.assertEqual(n2zh(1200034005, stuff_zero=1), "十二億零三萬四千零五")
        self.assertEqual(n2zh(1200034005, stuff_zero=2), "十二億零三萬四千零五")
        self.assertEqual(n2zh(1200034005, stuff_zero=3), "十二億三萬四千五")
        self.assertEqual(n2zh(5000006, stuff_zero=1), "五百萬零六")
        self.assertEqual(n2zh(5000006, stuff_zero=2), "五百萬零六")
        self.assertEqual(n2zh(5000006, stuff_zero=3), "五百萬六")
        self.assertEqual(n2zh(102003040000000, stuff_zero=1), "一百零二兆零三十億零四千萬")
        self.assertEqual(n2zh(102003040000000, stuff_zero=2), "一百零二兆零三十億四千萬")
        self.assertEqual(n2zh(102003040000000, stuff_zero=3), "一百二兆三十億四千萬")

    def test_cardinal_float(self):
        self.assertEqual(n2zh(0.123456789),"零點一二三四五六七八九")
        # self.assertEqual(n2zh('10.012345678901234567890123456789'),"一十點零一二三四五六七八九零一二三四五六七八九零一二三四五六七八九")
        self.assertEqual(n2zh(10**8 + 0.01), "一億點零一")
        self.assertEqual(n2zh(10**8 + 0.01, capital=True),"壹億點零壹")

    def test_ordinal(self):
        self.assertEqual(n2zh(0, to="ordinal"), "第零")
        self.assertEqual(n2zh(2, to="ordinal"), "第二")
        self.assertEqual(n2zh(10, to="ordinal"), "第十")
        self.assertEqual(n2zh(11, to="ordinal"), "第十一")
        self.assertEqual(n2zh('19', to="ordinal"), "第十九")
        self.assertEqual(n2zh(109, to="ordinal"), "第一百零九")
        self.assertEqual(n2zh(2, to="ordinal", counter="名"), "第二名")
        self.assertEqual(n2zh(3, to="ordinal", counter="位"), "第三位")
        
    def test_ordinal_num(self):
        self.assertEqual(n2zh(1.5, to="ordinal_num"), "第1.5")
        self.assertEqual(n2zh(120, to="ordinal_num"), "第120")
        
    def test_currency(self):
        self.assertEqual(n2zh('0', to="currency", capital=True),
                        "零圓整")
        self.assertEqual(n2zh(5.00, to="currency", capital=True),
                        "伍圓整")
        self.assertEqual(n2zh('0', to="currency"),
                        "零元")
        self.assertEqual(n2zh(5.00, to="currency"),
                        "五元")
        self.assertEqual(n2zh(10.05, to="currency", capital=True),
                        "壹拾圓伍分")
        self.assertEqual(n2zh(10.05, to="currency"),
                        "十元零五分")
        self.assertEqual(n2zh(12.12, to="currency", capital=True),
                        "壹拾貳圓壹角貳分")
        self.assertEqual(n2zh(1235678, to="currency", capital=True),
                        "壹佰貳拾叁萬伍仟陸佰柒拾捌圓整")
        self.assertEqual(n2zh('1234567890.123', to="currency", capital=True),
                        "壹拾貳億叁仟肆佰伍拾陸萬柒仟捌佰玖拾圓壹角貳分")
        self.assertEqual(n2zh(67890.126, to="currency"),
                        "六萬七千八百九十元一角三分")
        self.assertEqual(n2zh(987654.3, to="currency", currency = 'USD', capital=True),
                        "美元玖拾捌萬柒仟陸佰伍拾肆圓叁角")
        self.assertEqual(n2zh(987654.3, to="currency", currency = 'USD'),
                        "美元九十八萬七千六百五十四元三角")
        self.assertEqual(n2zh(135.79, to="currency", currency = 'EUR'),
                        "歐元一百三十五元七角九分")
        
    def test_year(self):
        self.assertEqual(n2zh(2020, to="year"), "二零二零年")
        self.assertEqual(n2zh(2020.0, to="year"), "二零二零年")
        self.assertEqual(n2zh(2020, to="year", capital=True), "公元二零二零年")
        self.assertEqual(n2zh(-1, to="year"), "公元前一年")
        with self.assertRaises(TypeError):
            n2zh(2020.1, to="year")
