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


def n2zh_tw(*args, **kwargs):
    return num2words(*args, lang='zh-hant', **kwargs)


class Num2WordsZhHantTest(TestCase):
    def test_low(self):
        self.assertEqual(n2zh_tw(0), "零")
        self.assertEqual(n2zh_tw(1), "一")
        self.assertEqual(n2zh_tw(2), "二")
        self.assertEqual(n2zh_tw(3), "三")
        self.assertEqual(n2zh_tw(4), "四")
        self.assertEqual(n2zh_tw(5), "五")
        self.assertEqual(n2zh_tw(6), "六")
        self.assertEqual(n2zh_tw(7), "七")
        self.assertEqual(n2zh_tw(8), "八")
        self.assertEqual(n2zh_tw(9), "九")
        self.assertEqual(n2zh_tw(10), "十")
        self.assertEqual(n2zh_tw(11), "十一")
        self.assertEqual(n2zh_tw(12), "十二")
        self.assertEqual(n2zh_tw(13), "十三")
        self.assertEqual(n2zh_tw(14), "十四")
        self.assertEqual(n2zh_tw(15), "十五")
        self.assertEqual(n2zh_tw(16), "十六")
        self.assertEqual(n2zh_tw(17), "十七")
        self.assertEqual(n2zh_tw(18), "十八")
        self.assertEqual(n2zh_tw(19), "十九")
        self.assertEqual(n2zh_tw(20), "二十")

    def test_mid(self):
        self.assertEqual(n2zh_tw(100), "百")
        self.assertEqual(n2zh_tw(100, reading=True), "ㄅㄞˇ")
        self.assertEqual(n2zh_tw(123), "百二十三")
        self.assertEqual(n2zh_tw(123, reading=True), "ㄧ ㄅㄞˇ ㄦˋ ㄕˊ ㄙㄢ")
        self.assertEqual(n2zh_tw(300), "三百")
        self.assertEqual(n2zh_tw(300, reading=True), "ㄙㄢ ㄅㄞˇ")
        self.assertEqual(n2zh_tw(400), "四百")
        self.assertEqual(n2zh_tw(400, reading=True), "ㄙˋ ㄅㄞˇ")
        self.assertEqual(n2zh_tw(600), "六百")
        self.assertEqual(n2zh_tw(600, reading=True), "ㄌㄧㄡˋ")
        self.assertEqual(n2zh_tw(700, reading=True, prefer=["しち"]), "しちひゃく")
        self.assertEqual(n2zh_tw(800, reading=True), "はっぴゃく")
        self.assertEqual(n2zh_tw(1000), "千")
        self.assertEqual(n2zh_tw(1000, reading=True), "せん")
        self.assertEqual(n2zh_tw(3000, reading=True), "さんぜん")
        self.assertEqual(n2zh_tw(8000, reading=True), "はっせん")

    def test_high(self):
        self.assertEqual(n2zh_tw(10000), "一万")
        self.assertEqual(n2zh_tw(10000, reading=True), "いちまん")
        self.assertEqual(n2zh_tw(12345), "一万二千三百四十五")
        self.assertEqual(n2zh_tw(12345, reading=True),
                         "いちまん"
                         "にせん"
                         "さんびゃく"
                         "よんじゅうご")
        self.assertEqual(n2zh_tw(10**8), "一億")
        self.assertEqual(n2zh_tw(10**8, reading=True), "いちおく")
        self.assertEqual(n2zh_tw(123456789), "一億二千三百四十五万六千七百八十九")
        self.assertEqual(n2zh_tw(123456789, reading=True),
                         "いちおく"
                         "にせんさんびゃくよんじゅうごまん"
                         "ろくせんななひゃく"
                         "はちじゅうきゅう")
        self.assertEqual(n2zh_tw(10**12), "一兆")
        self.assertEqual(n2zh_tw(10**12, reading=True), "いっちょう")
        self.assertEqual(n2zh_tw(1234567890123),
                         "一兆二千三百四十五億六千七百八十九万百二十三")
        self.assertEqual(n2zh_tw(1234567890123, reading=True),
                         "いっちょう"
                         "にせんさんびゃくよんじゅうごおく"
                         "ろくせんななひゃくはちじゅうきゅうまん"
                         "ひゃくにじゅうさん")
        # TODO: tests for 10**16 and above

    def test_cardinal_float(self):
        self.assertEqual(n2zh_tw(0.0123456789, prefer=["〇"]),
                         "〇点〇一二三四五六七八九")
        self.assertEqual(n2zh_tw(0.0123456789, reading=True),
                         "れいてん"
                         "れいいち"
                         "にさん"
                         "よんご"
                         "ろくなな"
                         "はちきゅう")
        self.assertEqual(n2zh_tw(10**8 + 0.01), "一億点零一")
        self.assertEqual(n2zh_tw(10**8 + 0.01, reading=True),
                         "いちおくてんれいいち")

    def test_ordinal(self):
        self.assertEqual(n2zh_tw(0, to="ordinal"), "零番目")
        self.assertEqual(n2zh_tw(0, to="ordinal", reading=True, prefer=["れい"]),
                         "れいばんめ")
        self.assertEqual(n2zh_tw(2, to="ordinal", counter="人"), "二人目")
        self.assertEqual(n2zh_tw(3, to="ordinal", counter="つ"), "三つ目")
        with self.assertRaises(NotImplementedError):
            n2zh_tw(4, to="ordinal", reading=True, counter="人")

    def test_ordinal_num(self):
        self.assertEqual(n2zh_tw(0, to="ordinal_num"), "第0個")
        self.assertEqual(n2zh_tw(0, to="ordinal_num", reading=True), "ㄉㄧˋㄌㄧㄥˊ˙ㄍㄜ")
        self.assertEqual(n2zh_tw(2, to="ordinal_num", counter="名"), "第2名")
        self.assertEqual(n2zh_tw(3, to="ordinal_num", counter="位"), "第3位")

    def test_currency(self):
        self.assertEqual(n2zh_tw(123456789, to="currency"),
                         "一億二千三百四十五万六千七百八十九元")

    def test_year(self):
        self.assertEqual(
            n2zh_tw(2020, to="year"),
            "西元二零二零年"
        )
        self.assertEqual(
            n2zh_tw(2017, to="year", reading="arabic"),
            "西元 2020 年"
        )
