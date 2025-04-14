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
    return num2words(*args, lang='zh_TW', **kwargs)


class Num2WordsZhTWTest(TestCase):
    def test_low(self):
        self.assertEqual(n2zh_tw(-1), "負一")
        self.assertEqual(n2zh_tw(-1, reading=True), "ㄈㄨˋㄧ")

    def test_mid(self):
        self.assertEqual(n2zh_tw(100), "一百")
        self.assertEqual(n2zh_tw(100, reading=True), "ㄧㄅㄞˇ")
        self.assertEqual(n2zh_tw(101), "一百零一")
        self.assertEqual(n2zh_tw(101, reading=True), "ㄧㄅㄞˇㄌㄧㄥˊㄧ")
        self.assertEqual(n2zh_tw(123), "一百二十三")
        self.assertEqual(n2zh_tw(123, reading=True), "ㄧㄅㄞˇㄦˋㄕˊㄙㄢ")
        self.assertEqual(n2zh_tw(1000), "一千")
        self.assertEqual(n2zh_tw(1000, reading=True), "ㄧㄑㄧㄢ")
        self.assertEqual(n2zh_tw(1010), "一千零一十")
        self.assertEqual(n2zh_tw(1010, reading=True), "ㄧㄑㄧㄢㄌㄧㄥˊㄧㄕˊ")

    def test_high(self):
        self.assertEqual(n2zh_tw(10000), "一萬")
        self.assertEqual(n2zh_tw(10000, reading=True), "ㄧㄨㄢˋ")
        self.assertEqual(n2zh_tw(10001), "一萬零一")
        self.assertEqual(n2zh_tw(10001, reading=True), "ㄧㄨㄢˋㄌㄧㄥˊㄧ")
        self.assertEqual(n2zh_tw(100000), "十萬")
        self.assertEqual(n2zh_tw(100000, reading=True), "ㄕˊㄨㄢˋ")
        self.assertEqual(n2zh_tw(100001), "十萬零一")
        self.assertEqual(n2zh_tw(100001, reading=True), "ㄕˊㄨㄢˋㄌㄧㄥˊㄧ")
        self.assertEqual(n2zh_tw(12345), "一萬二千三百四十五")
        self.assertEqual(n2zh_tw(12345, reading=True),
                         "ㄧㄨㄢˋ"
                         "ㄦˋㄑㄧㄢ"
                         "ㄙㄢㄅㄞˇ"
                         "ㄙˋㄕˊㄨˇ")
        self.assertEqual(n2zh_tw(10**8), "一億")
        self.assertEqual(n2zh_tw(10**8, reading=True), "ㄧㄧˋ")
        self.assertEqual(n2zh_tw(5 * 10**8 + 80 * 10**4), "五億零八十萬")
        self.assertEqual(n2zh_tw(5 * 10**8 + 80 * 10**4, reading=True),
                         "ㄨˇㄧˋ"
                         "ㄌㄧㄥˊ"
                         "ㄅㄚㄕˊㄨㄢˋ")
        self.assertEqual(n2zh_tw(10**9), "十億")
        self.assertEqual(n2zh_tw(10**9, reading=True), "ㄕˊㄧˋ")
        self.assertEqual(n2zh_tw(123456789), "一億二千三百四十五萬六千七百八十九")
        self.assertEqual(n2zh_tw(123456789, reading=True),
                         "ㄧㄧˋ"
                         "ㄦˋㄑㄧㄢ"
                         "ㄙㄢㄅㄞˇㄙˋㄕˊㄨˇㄨㄢˋ"
                         "ㄌㄧㄡˋㄑㄧㄢ"
                         "ㄑㄧㄅㄞˇ"
                         "ㄅㄚㄕˊ"
                         "ㄐㄧㄡˇ")
        self.assertEqual(n2zh_tw(4080 * 10**8), "四千零八十億")
        self.assertEqual(n2zh_tw(4080 * 10**8, reading=True),
                         "ㄙˋㄑㄧㄢ"
                         "ㄌㄧㄥˊ"
                         "ㄅㄚㄕˊㄧˋ")
        with self.assertRaises(OverflowError):
            n2zh_tw(10**100)

    def test_cardinal_float(self):
        self.assertEqual(n2zh_tw(0.0123456789), "零點零一二三四五六七八九")
        self.assertEqual(n2zh_tw(0.0123456789, reading=True),
                         "ㄌㄧㄥˊ"
                         "ㄉㄧㄢˇ"
                         "ㄌㄧㄥˊ"
                         "ㄧㄦˋㄙㄢㄙˋㄨˇㄌㄧㄡˋㄑㄧㄅㄚㄐㄧㄡˇ")
        self.assertEqual(n2zh_tw(-0.0123456789), "負零點零一二三四五六七八九")
        self.assertEqual(n2zh_tw(-0.0123456789, reading=True),
                         "ㄈㄨˋ"
                         "ㄌㄧㄥˊ"
                         "ㄉㄧㄢˇ"
                         "ㄌㄧㄥˊ"
                         "ㄧㄦˋㄙㄢㄙˋㄨˇㄌㄧㄡˋㄑㄧㄅㄚㄐㄧㄡˇ")
        self.assertEqual(n2zh_tw(10**8 + 0.01), "一億點零一")
        self.assertEqual(n2zh_tw(10**8 + 0.01, reading=True),
                         "ㄧㄧˋㄉㄧㄢˇㄌㄧㄥˊㄧ")

    def test_ordinal(self):
        self.assertEqual(n2zh_tw(0, to="ordinal"), "第零")
        self.assertEqual(n2zh_tw(0, to="ordinal", reading=True), "ㄉㄧˋㄌㄧㄥˊ")
        self.assertEqual(
            n2zh_tw(
                0,
                to="ordinal",
                counter="個",
                reading=True),
            "ㄉㄧˋㄌㄧㄥˊ˙ㄍㄜ")
        self.assertEqual(n2zh_tw(2, to="ordinal", counter="名"), "第二名")
        self.assertEqual(n2zh_tw(3, to="ordinal", counter="位"), "第三位")
        with self.assertRaises(NotImplementedError):
            n2zh_tw(4, to="ordinal", reading=True, counter="隻")

    def test_ordinal_num(self):
        self.assertEqual(n2zh_tw(0, to="ordinal_num", reading=True), "ㄉㄧˋ0")
        self.assertEqual(
            n2zh_tw(
                0,
                to="ordinal_num",
                counter="個",
                reading=True),
            "ㄉㄧˋ0˙ㄍㄜ")
        with self.assertRaises(NotImplementedError):
            n2zh_tw(4, to="ordinal_num", reading=True, counter="隻")

    def test_year(self):
        self.assertEqual(n2zh_tw(1912, to="year", era=True), "民國元年")
        self.assertEqual(
            n2zh_tw(
                1912,
                to="year",
                era=True,
                reading="arabic"),
            "民國1年")
        self.assertEqual(n2zh_tw(1913, to="year", era=True), "民國二年")
        self.assertEqual(n2zh_tw(1932, to="year", era=True), "民國二十一年")
        self.assertEqual(n2zh_tw(2011, to="year", era=True), "民國一百年")
        self.assertEqual(n2zh_tw(2012, to="year", era=True), "民國一零一年")
        self.assertEqual(n2zh_tw(2025, to="year", era=True), "民國一一四年")
        self.assertEqual(
            n2zh_tw(
                2025,
                to="year",
                era=True,
                reading="arabic"),
            "民國114年")
        with self.assertRaises(ValueError):
            n2zh_tw(1911, to="year", era=True)

        self.assertEqual(n2zh_tw(2020, to="year"), "二零二零年")
        with self.assertRaises(TypeError):
            n2zh_tw(2020.1, to="year", era=True)
