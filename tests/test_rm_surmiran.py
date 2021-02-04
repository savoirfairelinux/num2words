# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2021, Virginie Holm, recapp IT AG.  All Rights Reserved.

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


class Num2WordsRMSURMIRANTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="rm_surmiran")
        neg_crd = num2words(-number, lang="rm_surmiran")
        pos_ord = num2words(+number, lang="rm_surmiran", ordinal=True)
        neg_ord = num2words(-number, lang="rm_surmiran", ordinal=True)
        self.assertEqual("minus " + pos_crd, neg_crd)
        self.assertEqual("minus " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_surmiran"), "treis comma en quatter en tschintg"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_surmiran"), "minus tschintg comma en tschintg"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_surmiran"), "minus nolla comma en tschintg"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_surmiran", ordinal=True),
            "terz comma en quatter en tschintg"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_surmiran", ordinal=True),
            "minus tschintgavel comma en tschintg"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_surmiran", ordinal=True),
            "minus nolla comma en tschintg"
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="rm_surmiran"), "nolla")
        self.assertEqual(num2words(0, lang="rm_surmiran", ordinal=True), "nolla")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="rm_surmiran"), "en")
        self.assertEqual(num2words(2, lang="rm_surmiran"), "dus")
        self.assertEqual(num2words(3, lang="rm_surmiran"), "treis")
        self.assertEqual(num2words(5, lang="rm_surmiran"), "tschintg")
        self.assertEqual(num2words(7, lang="rm_surmiran"), "set")
        self.assertEqual(num2words(8, lang="rm_surmiran"), "otg")
        self.assertEqual(num2words(10, lang="rm_surmiran"), "diesch")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="rm_surmiran"), "endesch")
        self.assertEqual(num2words(13, lang="rm_surmiran"), "tredesch")
        self.assertEqual(num2words(15, lang="rm_surmiran"), "quindesch")
        self.assertEqual(num2words(16, lang="rm_surmiran"), "sedesch")
        self.assertEqual(num2words(17, lang="rm_surmiran"), "dischset")
        self.assertEqual(num2words(18, lang="rm_surmiran"), "dischdotg")
        self.assertEqual(num2words(19, lang="rm_surmiran"), "dischnov")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="rm_surmiran"), "vantg")
        self.assertEqual(num2words(21, lang="rm_surmiran"), "vantgegn")
        self.assertEqual(num2words(22, lang="rm_surmiran"), "vantgadus")
        self.assertEqual(num2words(23, lang="rm_surmiran"), "vantgatreis")
        self.assertEqual(num2words(28, lang="rm_surmiran"), "vantgotg")
        self.assertEqual(num2words(30, lang="rm_surmiran"), "trenta")
        self.assertEqual(num2words(31, lang="rm_surmiran"), "trentegn")
        self.assertEqual(num2words(34, lang="rm_surmiran"), "trentaquatter")
        self.assertEqual(num2words(38, lang="rm_surmiran"), "trentotg")
        self.assertEqual(num2words(40, lang="rm_surmiran"), "curanta")
        self.assertEqual(num2words(50, lang="rm_surmiran"), "tschuncanta")
        self.assertEqual(num2words(59, lang="rm_surmiran"), "tschuncantanov")
        self.assertEqual(num2words(66, lang="rm_surmiran"), "sessantaseis")
        self.assertEqual(num2words(77, lang="rm_surmiran"), "settantaset")
        self.assertEqual(num2words(81, lang="rm_surmiran"), "otgantegn")
        self.assertEqual(num2words(92, lang="rm_surmiran"), "novantadus")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_surmiran"), "tschent")
        self.assertEqual(num2words(101, lang="rm_surmiran"), "tschentadegn")
        self.assertEqual(num2words(102, lang="rm_surmiran"), "tschentadus")
        self.assertEqual(num2words(103, lang="rm_surmiran"), "tschentatreis")
        self.assertEqual(num2words(104, lang="rm_surmiran"), "tschentaquatter")
        self.assertEqual(num2words(105, lang="rm_surmiran"), "tschentatschintg")
        self.assertEqual(num2words(106, lang="rm_surmiran"), "tschentaseis")
        self.assertEqual(num2words(107, lang="rm_surmiran"), "tschentaset")
        self.assertEqual(num2words(108, lang="rm_surmiran"), "tschentadotg")
        self.assertEqual(num2words(109, lang="rm_surmiran"), "tschentanov")
        self.assertEqual(num2words(110, lang="rm_surmiran"), "tschentadiesch")
        self.assertEqual(num2words(111, lang="rm_surmiran"), "tschentadendesch")

        self.assertEqual(num2words(112, lang="rm_surmiran"), "tschentadodesch")

        self.assertEqual(num2words(113, lang="rm_surmiran"), "tschentatredesch")

        self.assertEqual(num2words(114, lang="rm_surmiran"), "tschentquittordesch")
        self.assertEqual(num2words(115, lang="rm_surmiran"), "tschentaquindesch")
        self.assertEqual(num2words(116, lang="rm_surmiran"), "tschentasedesch")
        self.assertEqual(num2words(117, lang="rm_surmiran"), "tschentdischset")
        self.assertEqual(num2words(118, lang="rm_surmiran"), "tschentdischdotg")
        self.assertEqual(num2words(119, lang="rm_surmiran"), "tschentdischnov")
        self.assertEqual(num2words(120, lang="rm_surmiran"), "tschentavantg")

        self.assertEqual(num2words(121, lang="rm_surmiran"), "tschentvantgegn")
        self.assertEqual(num2words(122, lang="rm_surmiran"), "tschentvantgadus")
        self.assertEqual(num2words(123, lang="rm_surmiran"), "tschentvantgatreis")
        self.assertEqual(num2words(124, lang="rm_surmiran"), "tschentvantgaquatter")
        self.assertEqual(num2words(125, lang="rm_surmiran"), "tschentvantgatschintg")
        self.assertEqual(num2words(126, lang="rm_surmiran"), "tschentvantgaseis")
        self.assertEqual(num2words(127, lang="rm_surmiran"), "tschentvantgaset")
        self.assertEqual(num2words(128, lang="rm_surmiran"), "tschentvantgotg")
        self.assertEqual(num2words(129, lang="rm_surmiran"), "tschentvantganov")

        self.assertEqual(num2words(130, lang="rm_surmiran"), "tschentatrenta")
        self.assertEqual(num2words(131, lang="rm_surmiran"), "tschenttrentegn")
        self.assertEqual(num2words(150, lang="rm_surmiran"), "tschenttschuncanta")
        self.assertEqual(num2words(196, lang="rm_surmiran"), "tschentnovantaseis")
        self.assertEqual(num2words(200, lang="rm_surmiran"), "dutschent")
        self.assertEqual(num2words(208, lang="rm_surmiran"), "dutschentadotg")
        self.assertEqual(num2words(210, lang="rm_surmiran"), "dutschentadiesch")
        self.assertEqual(num2words(271, lang="rm_surmiran"), "dutschentsettantegn")
        self.assertEqual(num2words(300, lang="rm_surmiran"), "tretschent")
        self.assertEqual(num2words(308, lang="rm_surmiran"), "tretschentadotg")
        self.assertEqual(num2words(311, lang="rm_surmiran"), "tretschentadendesch")
        self.assertEqual(
            num2words(375, lang="rm_surmiran"), "tretschentsettantatschintg"
        )
        self.assertEqual(num2words(400, lang="rm_surmiran"), "quattertschent")
        self.assertEqual(num2words(409, lang="rm_surmiran"), "quattertschentanov")
        self.assertEqual(num2words(410, lang="rm_surmiran"), "quattertschentadiesch")
        self.assertEqual(num2words(472, lang="rm_surmiran"), "quattertschentsettantadus")
        self.assertEqual(num2words(701, lang="rm_surmiran"), "settschentadegn")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="rm_surmiran"), "mella")
        self.assertEqual(num2words(1001, lang="rm_surmiran"), "melladegn")
        self.assertEqual(num2words(1010, lang="rm_surmiran"), "melladiesch")
        self.assertEqual(num2words(1100, lang="rm_surmiran"), "mellatschent")
        self.assertEqual(num2words(1101, lang="rm_surmiran"), "mellatschentadegn")
        self.assertEqual(num2words(1132, lang="rm_surmiran"), "mellatschenttrentadus")
        self.assertEqual(num2words(1500, lang="rm_surmiran"), "mellatschintgtschent")
        self.assertEqual(
            num2words(7378, lang="rm_surmiran"), "setmellatretschentsettantotg"
        )
        self.assertEqual(num2words(2000, lang="rm_surmiran"), "dumella")
        self.assertEqual(num2words(2001, lang="rm_surmiran"), "dumelladegn")
        self.assertEqual(num2words(2020, lang="rm_surmiran"), "dumellavantg")
        self.assertEqual(num2words(2100, lang="rm_surmiran"), "dumellatschent")
        self.assertEqual(num2words(2101, lang="rm_surmiran"), "dumellatschentadegn")
        self.assertEqual(num2words(3000, lang="rm_surmiran"), "tremella")
        self.assertEqual(num2words(3012, lang="rm_surmiran"), "tremelladodesch")
        self.assertEqual(
            num2words(6870, lang="rm_surmiran"), "seismellaotgtschentsettanta"
        )
        self.assertEqual(num2words(10000, lang="rm_surmiran"), "dieschmella")
        self.assertEqual(num2words(10001, lang="rm_surmiran"), "dieschmelladegn")
        self.assertEqual(
            num2words(32000, lang="rm_surmiran"), "trentadumella"
        )
        self.assertEqual(
            num2words(98765, lang="rm_surmiran"),
            "novantotgmellasettschentsessantatschintg"
        )
        self.assertEqual(num2words(100000, lang="rm_surmiran"), "tschentmella")

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="rm_surmiran"), "en milliun")
        self.assertEqual(num2words(1000007, lang="rm_surmiran"), "en milliun a set")
        self.assertEqual(num2words(1000008, lang="rm_surmiran"), "en milliun ad otg")
        self.assertEqual(
            num2words(1200000, lang="rm_surmiran"), "en milliun dutschentmella"
        )
        self.assertEqual(num2words(2000000, lang="rm_surmiran"), "dus milliuns")
        self.assertEqual(num2words(2000004, lang="rm_surmiran"), "dus milliuns a quatter")
        self.assertEqual(num2words(2000009, lang="rm_surmiran"), "dus milliuns a nov")
        self.assertEqual(num2words(2000100, lang="rm_surmiran"), "dus milliuns a tschent")
        self.assertEqual(
            num2words(2200311, lang="rm_surmiran"), "dus milliuns dutschentmellatretschentadendesch"
        )
        self.assertEqual(
            num2words(2300000, lang="rm_surmiran"), "dus milliuns tretschentmella"
        )
        self.assertEqual(num2words(3000000, lang="rm_surmiran"), "treis milliuns")
        self.assertEqual(
            num2words(3000005, lang="rm_surmiran"), "treis milliuns a tschintg"
        )
        self.assertEqual(
            num2words(3000080, lang="rm_surmiran"), "treis milliuns ad otganta"
        )
        self.assertEqual(
            num2words(20300000, lang="rm_surmiran"), "vantg milliuns tretschentmella"
        )
        self.assertEqual(
            num2words(523456, lang="rm_surmiran"),
            "tschintgtschentvantgatremellaquattertschenttschuncantaseis"
        )
        self.assertEqual(
            num2words(3800000, lang="rm_surmiran"), "treis milliuns otgtschentmella"
        )
        self.assertEqual(num2words(1000000000, lang="rm_surmiran"), "ena milliarda")
        self.assertEqual(
            num2words(1000000017, lang="rm_surmiran"), "ena milliarda a dischset"
        )
        self.assertEqual(
            num2words(1020300000, lang="rm_surmiran"), "ena milliarda vantg milliuns tretschentmella"
        )
        self.assertEqual(num2words(2000000000, lang="rm_surmiran"), "dus milliardas")
        self.assertEqual(
            num2words(2000001000, lang="rm_surmiran"), "dus milliardas a mella"
        )
        self.assertEqual(
            num2words(2003000011, lang="rm_surmiran"), "dus milliardas treis milliuns ad endesch"
        )
        self.assertEqual(
            num2words(3000000100, lang="rm_surmiran"), "treis milliardas a tschent"
        )
        self.assertEqual(
            num2words(3000002000, lang="rm_surmiran"), "treis milliardas a dumella"
        )
        self.assertEqual(
            num2words(3002000100, lang="rm_surmiran"), "treis milliardas dus milliuns a tschent"
        )
        self.assertEqual(
            num2words(3003000001, lang="rm_surmiran"), "treis milliardas treis milliuns ad egn"
        )
        self.assertEqual(
            num2words(3002000101, lang="rm_surmiran"), "treis milliardas dus milliuns a tschentadegn"
        )
        self.assertEqual(num2words(21000000000, lang="rm_surmiran"), "vantgegn milliardas")
        self.assertEqual(num2words(22000000000, lang="rm_surmiran"), "vantgadus milliardas")
        self.assertEqual(
            num2words(1234567890, lang="rm_surmiran"),
            "ena milliarda dutschenttrentaquatter milliuns "
            "tschintgtschentsessantasetmellaotgtschentnovanta"
        )
        self.assertEqual(num2words(1000000000000, lang="rm_surmiran"), "en billiun")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="rm_surmiran"),
            "tschentvantgatreis quadrilliardas quattertschenttschuncantaseis"
            " quadrilliuns settschentotgantanov trilliardas dodesch "
            "trilliuns tretschentcurantatschintg billiardas "
            "seistschentsettantotg billiuns novtschentadegn milliardas "
            "dutschenttrentaquatter milliuns "
            "tschintgtschentsessantasetmellaotgtschentnovanta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="rm_surmiran", ordinal=True), "amprem")
        self.assertEqual(num2words(7, lang="rm_surmiran", ordinal=True), "settavel")
        self.assertEqual(num2words(8, lang="rm_surmiran", ordinal=True), "otgavel")
        self.assertEqual(num2words(20, lang="rm_surmiran", ordinal=True), "vantgavel")
        self.assertEqual(num2words(21, lang="rm_surmiran", ordinal=True), "vantgegnavel")
        self.assertEqual(
            num2words(27, lang="rm_surmiran", ordinal=True), "vantgasettavel"
        )
        self.assertEqual(
            num2words(48, lang="rm_surmiran", ordinal=True), "curantotgavel"
        )
        self.assertEqual(num2words(60, lang="rm_surmiran", ordinal=True), "sessantavel")
        self.assertEqual(
            num2words(99, lang="rm_surmiran", ordinal=True), "novantanovavel"
        )

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_surmiran", ordinal=True), "tschentavel")
        self.assertEqual(
            num2words(112, lang="rm_surmiran", ordinal=True), "tschentadodeschavel"
        )
        self.assertEqual(
            num2words(137, lang="rm_surmiran", ordinal=True), "tschenttrentasettavel"
        )
        self.assertEqual(
            num2words(700, lang="rm_surmiran", ordinal=True), "settschentavel"
        )

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="rm_surmiran", ordinal=True), "mellavel")
        self.assertEqual(
            num2words(1001, lang="rm_surmiran", ordinal=True), "melladegnavel"
        )
        self.assertEqual(
            num2words(1200, lang="rm_surmiran", ordinal=True), "melladutschentavel"
        )
        self.assertEqual(
            num2words(8640, lang="rm_surmiran", ordinal=True),
            "otgmellaseistschentcurantavel"
        )
        self.assertEqual(
            num2words(14000, lang="rm_surmiran", ordinal=True), "quittordeschmellavel"
        )
        self.assertEqual(
            num2words(123456, lang="rm_surmiran", ordinal=True),
            "tschentvantgatremellaquattertschenttschuncantaseisavel"
        )
        self.assertEqual(
            num2words(987655, lang="rm_surmiran", ordinal=True),
            "novtschentotgantasetmellaseistschenttschuncantatschintgavel"
        )

    def test_with_decimals(self):
        self.assertAlmostEqual(
            num2words(1.0, lang="rm_surmiran"), "en comma nolla"
        )
        self.assertAlmostEqual(
            num2words(1.1, lang="rm_surmiran"), "en comma en"
        )
