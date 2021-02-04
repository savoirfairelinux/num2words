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


class Num2WordsRMTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="rm")
        neg_crd = num2words(-number, lang="rm")
        pos_ord = num2words(+number, lang="rm", ordinal=True)
        neg_ord = num2words(-number, lang="rm", ordinal=True)
        self.assertEqual("minus " + pos_crd, neg_crd)
        self.assertEqual("minus " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm"), "trais comma in quatter in tschintg"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm"), "minus tschintg comma in tschintg"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm"), "minus nulla comma in tschintg"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm", ordinal=True),
            "terz comma in quatter in tschintg"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm", ordinal=True),
            "minus tschintgavel comma in tschintg"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm", ordinal=True),
            "minus nulla comma in tschintg"
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="rm"), "nulla")
        self.assertEqual(num2words(0, lang="rm", ordinal=True), "nulla")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="rm"), "in")
        self.assertEqual(num2words(2, lang="rm"), "dus")
        self.assertEqual(num2words(3, lang="rm"), "trais")
        self.assertEqual(num2words(5, lang="rm"), "tschintg")
        self.assertEqual(num2words(7, lang="rm"), "set")
        self.assertEqual(num2words(8, lang="rm"), "otg")
        self.assertEqual(num2words(10, lang="rm"), "diesch")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="rm"), "indesch")
        self.assertEqual(num2words(13, lang="rm"), "tredesch")
        self.assertEqual(num2words(15, lang="rm"), "quindesch")
        self.assertEqual(num2words(16, lang="rm"), "sedesch")
        self.assertEqual(num2words(17, lang="rm"), "deschset")
        self.assertEqual(num2words(18, lang="rm"), "deschdotg")
        self.assertEqual(num2words(19, lang="rm"), "deschnov")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="rm"), "ventg")
        self.assertEqual(num2words(21, lang="rm"), "ventgin")
        self.assertEqual(num2words(22, lang="rm"), "ventgadus")
        self.assertEqual(num2words(23, lang="rm"), "ventgatrais")
        self.assertEqual(num2words(28, lang="rm"), "ventgotg")
        self.assertEqual(num2words(30, lang="rm"), "trenta")
        self.assertEqual(num2words(31, lang="rm"), "trentin")
        self.assertEqual(num2words(34, lang="rm"), "trentaquatter")
        self.assertEqual(num2words(38, lang="rm"), "trentotg")
        self.assertEqual(num2words(40, lang="rm"), "quaranta")
        self.assertEqual(num2words(50, lang="rm"), "tschuncanta")
        self.assertEqual(num2words(59, lang="rm"), "tschuncantanov")
        self.assertEqual(num2words(66, lang="rm"), "sessantasis")
        self.assertEqual(num2words(77, lang="rm"), "settantaset")
        self.assertEqual(num2words(81, lang="rm"), "otgantin")
        self.assertEqual(num2words(92, lang="rm"), "novantadus")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm"), "tschient")
        self.assertEqual(num2words(101, lang="rm"), "tschientedin")
        self.assertEqual(num2words(102, lang="rm"), "tschientedus")
        self.assertEqual(num2words(103, lang="rm"), "tschientetrais")
        self.assertEqual(num2words(104, lang="rm"), "tschientequatter")
        self.assertEqual(num2words(105, lang="rm"), "tschientetschintg")
        self.assertEqual(num2words(106, lang="rm"), "tschientesis")
        self.assertEqual(num2words(107, lang="rm"), "tschienteset")
        self.assertEqual(num2words(108, lang="rm"), "tschientedotg")
        self.assertEqual(num2words(109, lang="rm"), "tschientenov")
        self.assertEqual(num2words(110, lang="rm"), "tschientediesch")
        self.assertEqual(num2words(111, lang="rm"), "tschientedindesch")

        self.assertEqual(num2words(112, lang="rm"), "tschientedudesch")

        self.assertEqual(num2words(113, lang="rm"), "tschientetredesch")

        self.assertEqual(num2words(114, lang="rm"), "tschientquattordesch")
        self.assertEqual(num2words(115, lang="rm"), "tschientequindesch")
        self.assertEqual(num2words(116, lang="rm"), "tschientesedesch")
        self.assertEqual(num2words(117, lang="rm"), "tschientdeschset")
        self.assertEqual(num2words(118, lang="rm"), "tschientdeschdotg")
        self.assertEqual(num2words(119, lang="rm"), "tschientdeschnov")
        self.assertEqual(num2words(120, lang="rm"), "tschienteventg")

        self.assertEqual(num2words(121, lang="rm"), "tschientventgin")
        self.assertEqual(num2words(122, lang="rm"), "tschientventgadus")
        self.assertEqual(num2words(123, lang="rm"), "tschientventgatrais")
        self.assertEqual(num2words(124, lang="rm"), "tschientventgaquatter")
        self.assertEqual(num2words(125, lang="rm"), "tschientventgatschintg")
        self.assertEqual(num2words(126, lang="rm"), "tschientventgasis")
        self.assertEqual(num2words(127, lang="rm"), "tschientventgaset")
        self.assertEqual(num2words(128, lang="rm"), "tschientventgotg")
        self.assertEqual(num2words(129, lang="rm"), "tschientventganov")

        self.assertEqual(num2words(130, lang="rm"), "tschientetrenta")
        self.assertEqual(num2words(131, lang="rm"), "tschienttrentin")
        self.assertEqual(num2words(150, lang="rm"), "tschienttschuncanta")
        self.assertEqual(num2words(196, lang="rm"), "tschientnovantasis")
        self.assertEqual(num2words(200, lang="rm"), "duatschient")
        self.assertEqual(num2words(208, lang="rm"), "duatschientedotg")
        self.assertEqual(num2words(210, lang="rm"), "duatschientediesch")
        self.assertEqual(num2words(271, lang="rm"), "duatschientsettantin")
        self.assertEqual(num2words(300, lang="rm"), "traitschient")
        self.assertEqual(num2words(308, lang="rm"), "traitschientedotg")
        self.assertEqual(num2words(311, lang="rm"), "traitschientedindesch")
        self.assertEqual(
            num2words(375, lang="rm"), "traitschientsettantatschintg"
        )
        self.assertEqual(num2words(400, lang="rm"), "quattertschient")
        self.assertEqual(num2words(409, lang="rm"), "quattertschientenov")
        self.assertEqual(num2words(410, lang="rm"), "quattertschientediesch")
        self.assertEqual(
            num2words(472, lang="rm"), "quattertschientsettantadus")
        self.assertEqual(num2words(701, lang="rm"), "settschientedin")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="rm"), "milli")
        self.assertEqual(num2words(1001, lang="rm"), "milliedin")
        self.assertEqual(num2words(1010, lang="rm"), "milliediesch")
        self.assertEqual(num2words(1100, lang="rm"), "millietschient")
        self.assertEqual(num2words(1101, lang="rm"), "millitschientedin")
        self.assertEqual(num2words(1132, lang="rm"), "millitschienttrentadus")
        self.assertEqual(num2words(1500, lang="rm"), "millitschintgtschient")
        self.assertEqual(
            num2words(7378, lang="rm"), "setmillitraitschientsettantotg"
        )
        self.assertEqual(num2words(2000, lang="rm"), "duamilli")
        self.assertEqual(num2words(2001, lang="rm"), "duamilliedin")
        self.assertEqual(num2words(2020, lang="rm"), "duamillieventg")
        self.assertEqual(num2words(2100, lang="rm"), "duamillietschient")
        self.assertEqual(num2words(2101, lang="rm"), "duamillitschientedin")
        self.assertEqual(num2words(3000, lang="rm"), "traimilli")
        self.assertEqual(num2words(3012, lang="rm"), "traimilliedudesch")
        self.assertEqual(
            num2words(6870, lang="rm"), "sismilliotgtschientsettanta"
        )
        self.assertEqual(num2words(10000, lang="rm"), "dieschmilli")
        self.assertEqual(num2words(10001, lang="rm"), "dieschmilliedin")
        self.assertEqual(
            num2words(98765, lang="rm"),
            "novantotgmillisettschientsessantatschintg"
        )
        self.assertEqual(num2words(100000, lang="rm"), "tschientmilli")
        self.assertEqual(
            num2words(523456, lang="rm"),
            "tschintgtschientventgatraimilliquattertschienttschuncantasis"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="rm"), "in milliun")
        self.assertEqual(num2words(1000007, lang="rm"), "in milliun e set")
        self.assertEqual(num2words(1000008, lang="rm"), "in milliun ed otg")
        self.assertEqual(
            num2words(1200000, lang="rm"), "in milliun duatschientmilli"
        )
        self.assertEqual(num2words(2000000, lang="rm"), "dus milliuns")
        self.assertEqual(
            num2words(2000004, lang="rm"), "dus milliuns e quatter")
        self.assertEqual(num2words(2000009, lang="rm"), "dus milliuns e nov")
        self.assertEqual(
            num2words(2200311, lang="rm"),
            "dus milliuns duatschientmillitraitschientedindesch")
        self.assertEqual(
            num2words(2300000, lang="rm"), "dus milliuns traitschientmilli")
        self.assertEqual(num2words(3000000, lang="rm"), "trais milliuns")
        self.assertEqual(
            num2words(3000005, lang="rm"), "trais milliuns e tschintg")
        self.assertEqual(
            num2words(3800000, lang="rm"), "trais milliuns otgtschientmilli")
        self.assertEqual(num2words(1000000000, lang="rm"), "ina milliarda")
        self.assertEqual(
            num2words(1000000017, lang="rm"), "ina milliarda e deschset")
        self.assertEqual(num2words(2000000000, lang="rm"), "duas milliardas")
        self.assertEqual(
            num2words(2000001000, lang="rm"), "duas milliardas e milli")
        self.assertEqual(
            num2words(3000000100, lang="rm"), "trais milliardas e tschient")
        self.assertEqual(
            num2words(3000002000, lang="rm"), "trais milliardas e duamilli")
        self.assertEqual(
            num2words(3002000100, lang="rm"),
            "trais milliardas dus milliuns e tschient")
        self.assertEqual(
            num2words(3002000101, lang="rm"),
            "trais milliardas dus milliuns e tschientedin")
        self.assertEqual(num2words(21000000000, lang="rm"),
                         "ventgin milliardas")
        self.assertEqual(num2words(22000000000, lang="rm"),
                         "ventgaduas milliardas")
        self.assertEqual(
            num2words(1234567890, lang="rm"),
            "ina milliarda duatschienttrentaquatter milliuns "
            "tschintgtschientsessantasetmilliotgtschientnovanta"
        )
        self.assertEqual(num2words(1000000000000, lang="rm"), "in billiun")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="rm"),
            "tschientventgatrais quadrilliardas quattertschienttschuncantasis"
            " quadrilliuns settschientotgantanov trilliardas dudesch "
            "trilliuns traitschientquarantatschintg billiardas "
            "sistschientsettantotg billiuns novtschientedin milliardas "
            "duatschienttrentaquatter milliuns "
            "tschintgtschientsessantasetmilliotgtschientnovanta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="rm", ordinal=True), "emprim")
        self.assertEqual(num2words(7, lang="rm", ordinal=True), "settavel")
        self.assertEqual(num2words(8, lang="rm", ordinal=True), "otgavel")
        self.assertEqual(num2words(20, lang="rm", ordinal=True), "ventgavel")
        self.assertEqual(num2words(21, lang="rm", ordinal=True), "ventginavel")
        self.assertEqual(
            num2words(27, lang="rm", ordinal=True), "ventgasettavel")
        self.assertEqual(
            num2words(48, lang="rm", ordinal=True), "quarantotgavel")
        self.assertEqual(num2words(60, lang="rm", ordinal=True), "sessantavel")
        self.assertEqual(
            num2words(99, lang="rm", ordinal=True), "novantanovavel")

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm", ordinal=True),
                         "tschientavel")
        self.assertEqual(
            num2words(112, lang="rm", ordinal=True), "tschientedudeschavel")
        self.assertEqual(
            num2words(137, lang="rm", ordinal=True), "tschienttrentasettavel")
        self.assertEqual(
            num2words(700, lang="rm", ordinal=True), "settschientavel")

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="rm", ordinal=True), "milliavel")
        self.assertEqual(
            num2words(1001, lang="rm", ordinal=True), "milliedinavel")
        self.assertEqual(
            num2words(1200, lang="rm", ordinal=True), "milliduatschientavel")
        self.assertEqual(
            num2words(8640, lang="rm", ordinal=True),
            "otgmillisistschientquarantavel")
        self.assertEqual(
            num2words(14000, lang="rm", ordinal=True), "quattordeschmilliavel")
        self.assertEqual(
            num2words(123456, lang="rm", ordinal=True),
            "tschientventgatraimilliquattertschienttschuncantasisavel")
        self.assertEqual(
            num2words(987655, lang="rm", ordinal=True),
            "novtschientotgantasetmillisistschienttschuncantatschintgavel")

    def test_with_decimals(self):
        self.assertAlmostEqual(
            num2words(1.0, lang="rm"), "in comma nulla")
        self.assertAlmostEqual(
            num2words(1.1, lang="rm"), "in comma in")
