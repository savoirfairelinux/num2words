# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2020, Virginie Holm, recapp IT AG.  All Rights Reserved.

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


class Num2WordsRMVALLADERTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="rm_vallader")
        neg_crd = num2words(-number, lang="rm_vallader")
        pos_ord = num2words(+number, lang="rm_vallader", ordinal=True)
        neg_ord = num2words(-number, lang="rm_vallader", ordinal=True)
        self.assertEqual("minus " + pos_crd, neg_crd)
        self.assertEqual("minus " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_vallader"), "trais comma ün quatter ün tschinch"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_vallader"), "minus tschinch comma ün tschinch"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_vallader"), "minus nolla comma ün tschinch"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_vallader", ordinal=True),
            "terz comma ün quatter ün tschinch"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_vallader", ordinal=True),
            "minus tschinchavel comma ün tschinch"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_vallader", ordinal=True),
            "minus nolla comma ün tschinch"
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="rm_vallader"), "nolla")
        self.assertEqual(num2words(0, lang="rm_vallader", ordinal=True), "nolla")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="rm_vallader"), "ün")
        self.assertEqual(num2words(2, lang="rm_vallader"), "duos")
        self.assertEqual(num2words(3, lang="rm_vallader"), "trais")
        self.assertEqual(num2words(5, lang="rm_vallader"), "tschinch")
        self.assertEqual(num2words(7, lang="rm_vallader"), "set")
        self.assertEqual(num2words(8, lang="rm_vallader"), "ot")
        self.assertEqual(num2words(10, lang="rm_vallader"), "desch")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="rm_vallader"), "ündesch")
        self.assertEqual(num2words(13, lang="rm_vallader"), "traidesch")
        self.assertEqual(num2words(15, lang="rm_vallader"), "quindesch")
        self.assertEqual(num2words(16, lang="rm_vallader"), "saidesch")
        self.assertEqual(num2words(17, lang="rm_vallader"), "deschset")
        self.assertEqual(num2words(18, lang="rm_vallader"), "deschdot")
        self.assertEqual(num2words(19, lang="rm_vallader"), "deschnouv")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="rm_vallader"), "vainch")
        self.assertEqual(num2words(21, lang="rm_vallader"), "vainchün")
        self.assertEqual(num2words(22, lang="rm_vallader"), "vaincheduos")
        self.assertEqual(num2words(23, lang="rm_vallader"), "vainchetrais")
        self.assertEqual(num2words(28, lang="rm_vallader"), "vainchot")
        self.assertEqual(num2words(30, lang="rm_vallader"), "trenta")
        self.assertEqual(num2words(31, lang="rm_vallader"), "trentün")
        self.assertEqual(num2words(34, lang="rm_vallader"), "trentaquatter")
        self.assertEqual(num2words(38, lang="rm_vallader"), "trentot")
        self.assertEqual(num2words(40, lang="rm_vallader"), "quaranta")
        self.assertEqual(num2words(50, lang="rm_vallader"), "tschinquanta")
        self.assertEqual(num2words(59, lang="rm_vallader"), "tschinquantanouv")
        self.assertEqual(num2words(66, lang="rm_vallader"), "sesantases")
        self.assertEqual(num2words(77, lang="rm_vallader"), "settantaset")
        self.assertEqual(num2words(81, lang="rm_vallader"), "ottantün")
        self.assertEqual(num2words(92, lang="rm_vallader"), "novantaduos")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_vallader"), "tschient")
        self.assertEqual(num2words(101, lang="rm_vallader"), "tschientedün")
        self.assertEqual(num2words(102, lang="rm_vallader"), "tschienteduos")
        self.assertEqual(num2words(103, lang="rm_vallader"), "tschientetrais")
        self.assertEqual(num2words(104, lang="rm_vallader"), "tschientequatter")
        self.assertEqual(num2words(105, lang="rm_vallader"), "tschientetschinch")
        self.assertEqual(num2words(106, lang="rm_vallader"), "tschienteses")
        self.assertEqual(num2words(107, lang="rm_vallader"), "tschienteset")
        self.assertEqual(num2words(108, lang="rm_vallader"), "tschientedot")
        self.assertEqual(num2words(109, lang="rm_vallader"), "tschientenouv")
        self.assertEqual(num2words(110, lang="rm_vallader"), "tschientedesch")
        self.assertEqual(num2words(111, lang="rm_vallader"), "tschientedündesch")
        self.assertEqual(num2words(112, lang="rm_vallader"), "tschientedudesch")
        self.assertEqual(num2words(113, lang="rm_vallader"), "tschientetraidesch")
        self.assertEqual(num2words(114, lang="rm_vallader"), "tschientquattordesch")
        self.assertEqual(num2words(115, lang="rm_vallader"), "tschientequindesch")
        self.assertEqual(num2words(116, lang="rm_vallader"), "tschientesaidesch")
        self.assertEqual(num2words(117, lang="rm_vallader"), "tschientdeschset")
        self.assertEqual(num2words(118, lang="rm_vallader"), "tschientdeschdot")
        self.assertEqual(num2words(119, lang="rm_vallader"), "tschientdeschnouv")
        self.assertEqual(num2words(120, lang="rm_vallader"), "tschientevainch")
        self.assertEqual(num2words(121, lang="rm_vallader"), "tschientvainchün")
        self.assertEqual(num2words(122, lang="rm_vallader"), "tschientvaincheduos")
        self.assertEqual(num2words(123, lang="rm_vallader"), "tschientvainchetrais")
        self.assertEqual(num2words(124, lang="rm_vallader"), "tschientvainchequatter")
        self.assertEqual(num2words(125, lang="rm_vallader"), "tschientvainchetschinch")
        self.assertEqual(num2words(126, lang="rm_vallader"), "tschientvaincheses")
        self.assertEqual(num2words(127, lang="rm_vallader"), "tschientvaincheset")
        self.assertEqual(num2words(128, lang="rm_vallader"), "tschientvainchot")
        self.assertEqual(num2words(129, lang="rm_vallader"), "tschientvainchenouv")
        self.assertEqual(num2words(130, lang="rm_vallader"), "tschientetrenta")
        self.assertEqual(num2words(131, lang="rm_vallader"), "tschienttrentün")
        self.assertEqual(num2words(150, lang="rm_vallader"), "tschienttschinquanta")
        self.assertEqual(num2words(196, lang="rm_vallader"), "tschientnovantases")
        self.assertEqual(num2words(200, lang="rm_vallader"), "duatschient")
        self.assertEqual(num2words(208, lang="rm_vallader"), "duatschientedot")
        self.assertEqual(num2words(210, lang="rm_vallader"), "duatschientedesch")
        self.assertEqual(num2words(271, lang="rm_vallader"), "duatschientsettantün")
        self.assertEqual(num2words(300, lang="rm_vallader"), "trajatschient")
        self.assertEqual(num2words(308, lang="rm_vallader"), "trajatschientedot")
        self.assertEqual(num2words(311, lang="rm_vallader"), "trajatschientedündesch")
        self.assertEqual(
            num2words(375, lang="rm_vallader"), "trajatschientsettantatschinch"
        )
        self.assertEqual(num2words(400, lang="rm_vallader"), "quattertschient")
        self.assertEqual(num2words(409, lang="rm_vallader"), "quattertschientenouv")
        self.assertEqual(num2words(410, lang="rm_vallader"), "quattertschientedesch")
        self.assertEqual(num2words(472, lang="rm_vallader"), "quattertschientsettantaduos")
        self.assertEqual(num2words(701, lang="rm_vallader"), "settschientedün")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="rm_vallader"), "milli")
        self.assertEqual(num2words(1001, lang="rm_vallader"), "milliedün")
        self.assertEqual(num2words(1010, lang="rm_vallader"), "milliedesch")
        self.assertEqual(num2words(1100, lang="rm_vallader"), "millietschient")
        self.assertEqual(num2words(1101, lang="rm_vallader"), "millitschientedün")
        self.assertEqual(num2words(1132, lang="rm_vallader"), "millitschienttrentaduos")
        self.assertEqual(num2words(1500, lang="rm_vallader"), "millitschinchtschient")
        self.assertEqual(
            num2words(7378, lang="rm_vallader"), "setmillitrajatschientsettantot"
        )
        self.assertEqual(num2words(2000, lang="rm_vallader"), "duamilli")
        self.assertEqual(num2words(2001, lang="rm_vallader"), "duamilliedün")
        self.assertEqual(num2words(2020, lang="rm_vallader"), "duamillievainch")
        self.assertEqual(num2words(2100, lang="rm_vallader"), "duamillietschient")
        self.assertEqual(num2words(2101, lang="rm_vallader"), "duamillitschientedün")
        self.assertEqual(num2words(3000, lang="rm_vallader"), "trajamilli")
        self.assertEqual(num2words(3012, lang="rm_vallader"), "trajamilliedudesch")
        self.assertEqual(
            num2words(6870, lang="rm_vallader"), "sesmilliottschientsettanta"
        )
        self.assertEqual(num2words(10000, lang="rm_vallader"), "deschmilli")
        self.assertEqual(num2words(10001, lang="rm_vallader"), "deschmilliedün")
        self.assertEqual(
            num2words(98765, lang="rm_vallader"),
            "novantotmillisettschientsesantatschinch"
        )
        self.assertEqual(num2words(100000, lang="rm_vallader"), "tschientmilli")
        self.assertEqual(
            num2words(523456, lang="rm_vallader"),
            "tschinchtschientvainchetrajamilliquattertschienttschinquantases"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="rm_vallader"), "ün milliun")
        self.assertEqual(num2words(1000007, lang="rm_vallader"), "ün milliun e set")
        self.assertEqual(num2words(1000008, lang="rm_vallader"), "ün milliun ed ot")
        self.assertEqual(
            num2words(1200000, lang="rm_vallader"), "ün milliun duatschientmilli"
        )
        self.assertEqual(num2words(2000000, lang="rm_vallader"), "duos milliuns")
        self.assertEqual(num2words(2000004, lang="rm_vallader"), "duos milliuns e quatter")
        self.assertEqual(num2words(2000009, lang="rm_vallader"), "duos milliuns e nouv")
        self.assertEqual(
            num2words(2200311, lang="rm_vallader"), "duos milliuns duatschientmillitrajatschientedündesch"
        )
        self.assertEqual(
            num2words(2300000, lang="rm_vallader"), "duos milliuns trajatschientmilli"
        )
        self.assertEqual(num2words(3000000, lang="rm_vallader"), "trais milliuns")
        self.assertEqual(
            num2words(3000005, lang="rm_vallader"), "trais milliuns e tschinch"
        )
        self.assertEqual(
            num2words(3800000, lang="rm_vallader"), "trais milliuns ottschientmilli"
        )
        self.assertEqual(num2words(1000000000, lang="rm_vallader"), "ün milliard")
        self.assertEqual(
            num2words(1000000017, lang="rm_vallader"), "ün milliard e deschset"
        )
        self.assertEqual(num2words(2000000000, lang="rm_vallader"), "duos milliards")
        self.assertEqual(
            num2words(2000001000, lang="rm_vallader"), "duos milliards e milli"
        )
        self.assertEqual(
            num2words(3000000100, lang="rm_vallader"), "trais milliards e tschient"
        )
        self.assertEqual(
            num2words(3000002000, lang="rm_vallader"), "trais milliards e duamilli"
        )
        self.assertEqual(
            num2words(3002000100, lang="rm_vallader"), "trais milliards duos milliuns e tschient"
        )
        self.assertEqual(
            num2words(3002000101, lang="rm_vallader"), "trais milliards duos milliuns e tschientedün"
        )
        self.assertEqual(num2words(21000000000, lang="rm_vallader"), "vainchün milliards")
        self.assertEqual(num2words(22000000000, lang="rm_vallader"), "vaincheduos milliards")
        self.assertEqual(
            num2words(1234567890, lang="rm_vallader"),
            "ün milliard duatschienttrentaquatter milliuns "
            "tschinchtschientsesantasetmilliottschientnovanta"
        )
        self.assertEqual(num2words(1000000000000, lang="rm_vallader"), "ün billiun")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="rm_vallader"),
            "tschientvainchetrais quadrilliards quattertschienttschinquantases"
            " quadrilliuns settschientottantanouv trilliards dudesch "
            "trilliuns trajatschientquarantatschinch billiards "
            "sestschientsettantot billiuns nouvtschientedün milliards "
            "duatschienttrentaquatter milliuns "
            "tschinchtschientsesantasetmilliottschientnovanta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="rm_vallader", ordinal=True), "prüm")
        self.assertEqual(num2words(7, lang="rm_vallader", ordinal=True), "settavel")
        self.assertEqual(num2words(8, lang="rm_vallader", ordinal=True), "ottavel")
        self.assertEqual(num2words(17, lang="rm_vallader", ordinal=True), "deschsettavel")
        self.assertEqual(num2words(18, lang="rm_vallader", ordinal=True), "deschdottavel")
        self.assertEqual(num2words(20, lang="rm_vallader", ordinal=True), "vainchavel")
        self.assertEqual(num2words(21, lang="rm_vallader", ordinal=True), "vainchünavel")
        self.assertEqual(
            num2words(27, lang="rm_vallader", ordinal=True), "vainchesettavel"
        )
        self.assertEqual(
            num2words(48, lang="rm_vallader", ordinal=True), "quarantottavel"
        )
        self.assertEqual(num2words(60, lang="rm_vallader", ordinal=True), "sesantavel")
        self.assertEqual(
            num2words(99, lang="rm_vallader", ordinal=True), "novantanouvavel"
        )

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_vallader", ordinal=True), "tschientavel")
        self.assertEqual(
            num2words(112, lang="rm_vallader", ordinal=True), "tschientedudeschavel"
        )
        self.assertEqual(
            num2words(137, lang="rm_vallader", ordinal=True), "tschienttrentasettavel"
        )
        self.assertEqual(
            num2words(700, lang="rm_vallader", ordinal=True), "settschientavel"
        )

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="rm_vallader", ordinal=True), "milliavel")
        self.assertEqual(
            num2words(1001, lang="rm_vallader", ordinal=True), "milliedünavel"
        )
        self.assertEqual(
            num2words(1200, lang="rm_vallader", ordinal=True), "milliduatschientavel"
        )
        self.assertEqual(
            num2words(8640, lang="rm_vallader", ordinal=True),
            "otmillisestschientquarantavel"
        )
        self.assertEqual(
            num2words(14000, lang="rm_vallader", ordinal=True), "quattordeschmilliavel"
        )
        self.assertEqual(
            num2words(123456, lang="rm_vallader", ordinal=True),
            "tschientvainchetrajamilliquattertschienttschinquantasesavel"
        )
        self.assertEqual(
            num2words(987655, lang="rm_vallader", ordinal=True),
            "nouvtschientottantasetmillisestschienttschinquantatschinchavel"
        )

    def test_with_decimals(self):
        self.assertAlmostEqual(
            num2words(1.0, lang="rm_vallader"), "ün comma nolla"
        )
        self.assertAlmostEqual(
            num2words(1.1, lang="rm_vallader"), "ün comma ün"
        )
