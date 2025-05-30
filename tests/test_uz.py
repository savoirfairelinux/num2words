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

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, "bir"),
    (2, "ikki"),
    (3, "uch"),
    (4, "toʻrt"),
    (5, "besh"),
    (6, "olti"),
    (7, "yetti"),
    (8, "sakkiz"),
    (9, "toʻqqiz"),
    (10, "oʻn"),
    (10.01, "oʻn butun nol bir"),
    (11, "oʻn bir"),
    (12, "oʻn ikki"),
    (12.50, "oʻn ikki butun besh"),
    (13, "oʻn uch"),
    (14, "oʻn toʻrt"),
    (14.13, "oʻn toʻrt butun oʻn uch"),
    (15, "oʻn besh"),
    (16, "oʻn olti"),
    (17, "oʻn yetti"),
    (17.31, "oʻn yetti butun oʻttiz bir"),
    (18, "oʻn sakkiz"),
    (19, "oʻn toʻqqiz"),
    (20, "yigirma"),
    (21, "yigirma bir"),
    (21.20, "yigirma bir butun ikki"),
    (30, "oʻttiz"),
    (32, "oʻttiz ikki"),
    (40, "qirq"),
    (43, "qirq uch"),
    (43.007, "qirq uch butun nol nol yetti"),
    (50, "ellik"),
    (54, "ellik toʻrt"),
    (60, "oltmish"),
    (60.059, "oltmish butun nol ellik toʻqqiz"),
    (65, "oltmish besh"),
    (70, "yetmish"),
    (76, "yetmish olti"),
    (80, "sakson"),
    (87, "sakson yetti"),
    (90, "toʻqson"),
    (98, "toʻqson sakkiz"),
    (99, "toʻqson toʻqqiz"),
    (100, "bir yuz"),
    (101, "bir yuz bir"),
    (199, "bir yuz toʻqson toʻqqiz"),
    (200, "ikki yuz"),
    (203, "ikki yuz uch"),
    (300, "uch yuz"),
    (356, "uch yuz ellik olti"),
    (400, "toʻrt yuz"),
    (434, "toʻrt yuz oʻttiz toʻrt"),
    (500, "besh yuz"),
    (578, "besh yuz yetmish sakkiz"),
    (600, "olti yuz"),
    (689, "olti yuz sakson toʻqqiz"),
    (700, "yettiyuz"),
    (729, "yetti yuz yigirma toʻqqiz"),
    (800, "sakkiz yuz"),
    (894, "sakkiz yuz toʻqson toʻrt"),
    (900, "toʻqqiz yuz"),
    (999, "toʻqqiz yuz toʻqson toʻqqiz"),
    (1000, "bir ming"),
    (1001, "bir ming bir"),
    (2012, "ikki ming oʻn ikki"),
    (2025, "ikki ming yigirma besh"),
    (1234, "bir ming ikki yuz oʻttiz toʻrt"),
    (12345.65, "oʻn ikki ming uch yuz qirq besh butun oltmish besh"),
    (-260000, "minus ikki yuz oltmish ming"),
    (777777, "yetti yuz yetmish yetti ming yetti yuz yetmish yetti"),
    (999999, "toʻqqiz yuz toʻqson toʻqqiz ming toʻqqiz yuz toʻqson toʻqqiz"),
    (1000000, "bir million"),
    (1000000000, "bir milliard"),
    (1234567890, "bir milliard ikki yuz oʻttiz toʻrt million besh yuz oltmish yetti ming sakkiz yuz toʻqson"),
    (1000000000000000, "bir kvadrillion"),
    (1000000000000000000, "bir kvintillion"),
    (1000000000000000000000, "bir sextillion"),
    (1000000000000000000000000, "bir septillion"),
    (1000000000000000000000000000, "bir oktilion"),
    (1000000000000000000000000000000, "bir nonillion"),
    (215461407892039002157189883901676,
     "ikki yuz oʻn besh nonillion toʻrt yuz oltmish bir oktilion toʻrt yuz "
     "yetti septillion sakkiz yuz toʻqson ikki sextillion oʻttiz toʻqqiz kvintillion "
     "ikki kvadrillion bir yuz ellik yetti trillion bir yuz sakson toʻqqiz milliard sakkiz "
     "yuz sakson uch million toʻqqiz yuz bir ming olti yuz yetmish olti"),
    (719094234693663034822824384220291,
     "yetti yuz oʻn toʻqqiz nonillion toʻqson toʻrt oktilion ikki yuz oʻttiz toʻrt septillion "
     "olti yuz toʻqson uch sextillion olti yuz oltmish uch kvintillion oʻttiz toʻrt kvadrillion "
     "sakkiz yuz yigirma ikki trillion sakkiz yuz yigirma toʻrt milliard uch yuz sakson toʻrt "
     "million ikki yuz yigirma ming ikki yuz toʻqson bir"),
)

TEST_CASES_TO_CURRENCY_UZS = (
    (0.00, "nol soʻm, nol tiyin"),
    (1.00, "bir soʻm, nol tiyin"),
    (2.00, "ikki soʻm, nol tiyin"),
    (5.05, "besh soʻm, nol besh tiyin"),
    (7.77, "yetti soʻm, yetmish yetti tiyin"),
    (10.01, "oʻn soʻm, bir tiyin"),
    (100.0, "bir yuz soʻm, nol tiyin"),
    (1000.0, "ming soʻm, nol tiyin"),
    (10000.99, "oʻn ming soʻm, toʻqson toʻqqiz tiyin"),
    (200_000.0, "ikki yuz ming soʻm, nol tiyin"),
    (10_000_000.0, "oʻn million soʻm, nol tiyin"),
    (1_000_000_000.0, "bir milliard soʻm, nol tiyin"),
    (10_000_000_000.0, "oʻn milliard soʻm, nol tiyin"),
    (10_101_101_101.101, "oʻn milliard bir yuz bir million bir yuz bir ming bir yuz bir soʻm, oʻn tiyin"),
    (77_777_777.77, "yetmish yetti million yetti yuz yetmish yetti ming yetti yuz yetmish yetti soʻm, yetmish yetti tiyin"),
)

TEST_CASES_ORDINAL = (
    (1, "birinchi"),
    (2, "ikkinchi"),
    (3, "uchinchi"),
    (4, "toʻrtinchi"),
    (5, "beshinchi"),
    (6, "oltinchi"),
    (7, "yettinchi"),
    (8, "sakkizinchi"),
    (9, "toʻqqizinchi"),
    (10, "oʻninchi"),
    (11, "oʻn birinchi"),
    (12, "oʻn ikkinchi"),
    (20, "yigirmanchi"),
    (21, "yigirma birinchi"),
    (30, "oʻttizinchi"),
    (40, "qirqinchi"),
    (50, "ellikinchi"),
    (60, "oltmishinchi"),
    (70, "yetmishinchi"),
    (80, "saksoninchi"),
    (90, "toʻqsoninchi"),
    (100, "bir yuzinchi"),
    (101, "bir yuz birinchi"),
    (200, "ikki yuzinchi"),
    (1000, "bir minginchi"),
    (1001, "bir ming birinchi"),
    (1945, "bir ming toʻqqiz yuz qirq beshinchi"),
    (1990, "bir ming toʻqqiz yuz toʻqsoninchi"),
    (1991, "bir ming toʻqqiz yuz toʻqson birinchi"),
    (2019, "ikki ming oʻn toʻqqizinchi"),
    (2025, "ikki ming yigirma beshinchi"),
    (3333, "uch ming uch yuz oʻttiz uchinchi"),
    (3456, "uch ming toʻrt yuz ellik oltinchi"),
    (11111, "oʻn bir ming bir yuz oʻn birinchi"),
    (222222, "ikki yuz yigirma ikki ming ikki yuz yigirma ikkinchi"),
    (1000000, "bir millioninchi"),
    (1000001, "bir million birinchi"),
    (1001001, "bir million bir ming birinchi"),
    (1101010, "bir million bir yuz oʻn ming oʻninchi"),
    (2002002, "ikki million ikki ming ikkinchi"),
    (70707070, "yetmish million yetti yuz yetti ming yetmishinchi"),
    (777777777, 
    "yetti yuz yetmish yetti million yetti yuz "
    "yetmish yetti ming yetti yuz yetmish yettinchi"),
    (1234567890, 
    "bir milliard ikki yuz oʻttiz toʻrt million "
    "besh yuz oltmish yetti ming sakkiz yuz toʻqsoninchi"),
    (99999999999999999, 
     "toʻqqiz yuz toʻqson toʻqqiz trillion toʻqqiz yuz "
     "toʻqson toʻqqiz milliard toʻqqiz yuz toʻqson toʻqqiz million "
     "toʻqqiz yuz toʻqson toʻqqiz ming toʻqqiz yuz toʻqson toʻqqizinchi"),
    (12345678900987654321, 
     "oʻn ikki kvadrillion uch yuz qirq besh trillion "
    "yett yuz sakson yetti milliard toʻqqiz yuz toʻqqiz million "
    "sakson yetti ming toʻrt yuz oʻttiz birinchi"),
)

class TestNum2WordsUZ(TestCase):

    def test_cardinal(self):
        for number, expected in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(number, lang='uz'), expected)

    def test_currency(self):
        for number, expected in TEST_CASES_TO_CURRENCY_UZS:
            self.assertEqual(num2words(number, lang='uz', to='currency'), expected)

    def test_ordinal(self):
        for number, expected in TEST_CASES_ORDINAL:
            self.assertEqual(num2words(number, lang='uz', to='ordinal'), expected)