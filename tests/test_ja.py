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


def n2j(*args, **kwargs):
    return num2words(*args, lang='ja', **kwargs)


class Num2WordsJATest(TestCase):
    def test_low(self):
        self.assertEqual(n2j(0), "零")
        self.assertEqual(n2j(0, prefer=["〇"]), "〇")
        self.assertEqual(n2j(0, reading=True), "ゼロ")
        self.assertEqual(n2j(0, reading=True, prefer=["れい"]), "れい")
        self.assertEqual(n2j(1), "一")
        self.assertEqual(n2j(1, reading=True), "いち")
        self.assertEqual(n2j(2), "二")
        self.assertEqual(n2j(2, reading=True), "に")
        self.assertEqual(n2j(3), "三")
        self.assertEqual(n2j(3, reading=True), "さん")
        self.assertEqual(n2j(4), "四")
        self.assertEqual(n2j(4, reading=True), "よん")
        self.assertEqual(n2j(4, reading=True, prefer=["し"]), "し")
        self.assertEqual(n2j(5), "五")
        self.assertEqual(n2j(5, reading=True), "ご")
        self.assertEqual(n2j(6), "六")
        self.assertEqual(n2j(6, reading=True), "ろく")
        self.assertEqual(n2j(7), "七")
        self.assertEqual(n2j(7, reading=True), "なな")
        self.assertEqual(n2j(7, reading=True, prefer=["しち"]), "しち")
        self.assertEqual(n2j(8), "八")
        self.assertEqual(n2j(8, reading=True), "はち")
        self.assertEqual(n2j(9), "九")
        self.assertEqual(n2j(9, reading=True), "きゅう")
        self.assertEqual(n2j(10), "十")
        self.assertEqual(n2j(10, reading=True), "じゅう")
        self.assertEqual(n2j(11), "十一")
        self.assertEqual(n2j(11, reading=True), "じゅういち")
        self.assertEqual(n2j(12), "十二")
        self.assertEqual(n2j(12, reading=True), "じゅうに")
        self.assertEqual(n2j(13), "十三")
        self.assertEqual(n2j(13, reading=True), "じゅうさん")
        self.assertEqual(n2j(14), "十四")
        self.assertEqual(n2j(14, reading=True), "じゅうよん")
        self.assertEqual(n2j(14, reading=True, prefer=["し"]), "じゅうし")
        self.assertEqual(n2j(15), "十五")
        self.assertEqual(n2j(15, reading=True), "じゅうご")
        self.assertEqual(n2j(16), "十六")
        self.assertEqual(n2j(16, reading=True), "じゅうろく")
        self.assertEqual(n2j(17), "十七")
        self.assertEqual(n2j(17, reading=True), "じゅうなな")
        self.assertEqual(n2j(17, reading=True, prefer=["しち"]), "じゅうしち")
        self.assertEqual(n2j(18), "十八")
        self.assertEqual(n2j(18, reading=True), "じゅうはち")
        self.assertEqual(n2j(19), "十九")
        self.assertEqual(n2j(19, reading=True), "じゅうきゅう")
        self.assertEqual(n2j(20), "二十")
        self.assertEqual(n2j(20, reading=True), "にじゅう")

    def test_mid(self):
        self.assertEqual(n2j(100), "百")
        self.assertEqual(n2j(100, reading=True), "ひゃく")
        self.assertEqual(n2j(123), "百二十三")
        self.assertEqual(n2j(123, reading=True), "ひゃくにじゅうさん")
        self.assertEqual(n2j(300), "三百")
        self.assertEqual(n2j(300, reading=True), "さんびゃく")
        self.assertEqual(n2j(400), "四百")
        self.assertEqual(n2j(400, reading=True), "よんひゃく")
        # 400 --> しひゃく sounds weird, but can be generated with prefer
        self.assertEqual(n2j(600), "六百")
        self.assertEqual(n2j(600, reading=True), "ろっぴゃく")
        self.assertEqual(n2j(700, reading=True, prefer=["しち"]), "しちひゃく")
        self.assertEqual(n2j(800, reading=True), "はっぴゃく")
        self.assertEqual(n2j(1000), "千")
        self.assertEqual(n2j(1000, reading=True), "せん")
        self.assertEqual(n2j(3000, reading=True), "さんぜん")
        self.assertEqual(n2j(8000, reading=True), "はっせん")

    def test_high(self):
        self.assertEqual(n2j(10000), "一万")
        self.assertEqual(n2j(10000, reading=True), "いちまん")
        self.assertEqual(n2j(12345), "一万二千三百四十五")
        self.assertEqual(n2j(12345, reading=True),
                         "いちまん"
                         "にせん"
                         "さんびゃく"
                         "よんじゅうご")
        self.assertEqual(n2j(10**8), "一億")
        self.assertEqual(n2j(10**8, reading=True), "いちおく")
        self.assertEqual(n2j(123456789), "一億二千三百四十五万六千七百八十九")
        self.assertEqual(n2j(123456789, reading=True),
                         "いちおく"
                         "にせんさんびゃくよんじゅうごまん"
                         "ろくせんななひゃく"
                         "はちじゅうきゅう")
        self.assertEqual(n2j(10**12), "一兆")
        self.assertEqual(n2j(10**12, reading=True), "いっちょう")
        self.assertEqual(n2j(1234567890123),
                         "一兆二千三百四十五億六千七百八十九万百二十三")
        self.assertEqual(n2j(1234567890123, reading=True),
                         "いっちょう"
                         "にせんさんびゃくよんじゅうごおく"
                         "ろくせんななひゃくはちじゅうきゅうまん"
                         "ひゃくにじゅうさん")
        # TODO: tests for 10**16 and above

    def test_cardinal_float(self):
        self.assertEqual(n2j(0.0123456789, prefer=["〇"]),
                         "〇点〇一二三四五六七八九")
        self.assertEqual(n2j(0.0123456789, reading=True),
                         "れいてん"
                         "れいいち"
                         "にさん"
                         "よんご"
                         "ろくなな"
                         "はちきゅう")
        self.assertEqual(n2j(10**8 + 0.01), "一億点零一")
        self.assertEqual(n2j(10**8 + 0.01, reading=True),
                         "いちおくてんれいいち")

    def test_ordinal(self):
        self.assertEqual(n2j(0, to="ordinal"), "零番目")
        self.assertEqual(n2j(0, to="ordinal", reading=True, prefer=["れい"]),
                         "れいばんめ")
        self.assertEqual(n2j(2, to="ordinal", counter="人"), "二人目")
        self.assertEqual(n2j(3, to="ordinal", counter="つ"), "三つ目")
        with self.assertRaises(NotImplementedError):
            n2j(4, to="ordinal", reading=True, counter="人")

    def test_ordinal_num(self):
        self.assertEqual(n2j(0, to="ordinal_num"), "0番目")
        self.assertEqual(n2j(0, to="ordinal_num", reading=True), "0ばんめ")
        self.assertEqual(n2j(2, to="ordinal_num", counter="人"), "2人目")
        self.assertEqual(n2j(3, to="ordinal_num", counter="つ"), "3つ目")

    def test_currency(self):
        self.assertEqual(n2j(123456789, to="currency"),
                         "一億二千三百四十五万六千七百八十九円")
        self.assertEqual(n2j(123456789, to="currency", reading=True),
                         "いちおく"
                         "にせんさんびゃくよんじゅうごまん"
                         "ろくせんななひゃく"
                         "はちじゅうきゅうえん")

    def test_year(self):
        self.assertEqual(n2j(2017, to="year"), "平成二十九年")
        self.assertEqual(n2j(2017, to="year", reading=True),
                         "へいせいにじゅうくねん")
        self.assertEqual(n2j(2017, to="year", reading="arabic"),
                         "平成29年")
        self.assertEqual(n2j(2009, to="year", era=False), "二千九年")
        self.assertEqual(n2j(2009, to="year", reading=True, era=False),
                         "にせんくねん")
        self.assertEqual(n2j(2000, to="year", era=False), "二千年")
        self.assertEqual(n2j(2000, to="year", era=False, reading=True),
                         "にせんねん")
        self.assertEqual(n2j(645, to="year"), "大化元年")
        self.assertEqual(n2j(645, to="year", reading=True), "たいかがんねん")
        self.assertEqual(n2j(645, to="year"), "大化元年")
        self.assertEqual(n2j(645, to="year", reading=True), "たいかがんねん")
        self.assertEqual(n2j(-99, to="year", era=False), "紀元前九十九年")
        self.assertEqual(n2j(-99, to="year", era=False, reading=True),
                         "きげんぜんきゅうじゅうくねん")
        self.assertEqual(n2j(1375, to="year"), "天授元年")
        self.assertEqual(n2j(1375, to="year", prefer=["えいわ"]), "永和元年")
