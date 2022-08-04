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


class Num2WordsRMSURSILVTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="rm_sursilv")
        neg_crd = num2words(-number, lang="rm_sursilv")
        pos_ord = num2words(+number, lang="rm_sursilv", ordinal=True)
        neg_ord = num2words(-number, lang="rm_sursilv", ordinal=True)
        self.assertEqual("minus " + pos_crd, neg_crd)
        self.assertEqual("minus " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_sursilv"),
            "treis comma in quater in tschun"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_sursilv"), "minus tschun comma in tschun"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_sursilv"), "minus nulla comma in tschun"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_sursilv", ordinal=True),
            "tierz comma in quater in tschun"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_sursilv", ordinal=True),
            "minus tschunavel comma in tschun"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_sursilv", ordinal=True),
            "minus nulla comma in tschun"
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="rm_sursilv"), "nulla")
        self.assertEqual(num2words(0, lang="rm_sursilv", ordinal=True),
                         "nulla")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="rm_sursilv"), "in")
        self.assertEqual(num2words(2, lang="rm_sursilv"), "dus")
        self.assertEqual(num2words(3, lang="rm_sursilv"), "treis")
        self.assertEqual(num2words(5, lang="rm_sursilv"), "tschun")
        self.assertEqual(num2words(7, lang="rm_sursilv"), "siat")
        self.assertEqual(num2words(8, lang="rm_sursilv"), "otg")
        self.assertEqual(num2words(10, lang="rm_sursilv"), "diesch")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="rm_sursilv"), "endisch")
        self.assertEqual(num2words(13, lang="rm_sursilv"), "tredisch")
        self.assertEqual(num2words(15, lang="rm_sursilv"), "quendisch")
        self.assertEqual(num2words(16, lang="rm_sursilv"), "sedisch")
        self.assertEqual(num2words(17, lang="rm_sursilv"), "gissiat")
        self.assertEqual(num2words(18, lang="rm_sursilv"), "schotg")
        self.assertEqual(num2words(19, lang="rm_sursilv"), "scheniv")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="rm_sursilv"), "vegn")
        self.assertEqual(num2words(21, lang="rm_sursilv"), "ventgin")
        self.assertEqual(num2words(22, lang="rm_sursilv"), "ventgadus")
        self.assertEqual(num2words(23, lang="rm_sursilv"), "ventgatreis")
        self.assertEqual(num2words(28, lang="rm_sursilv"), "ventgotg")
        self.assertEqual(num2words(30, lang="rm_sursilv"), "trenta")
        self.assertEqual(num2words(31, lang="rm_sursilv"), "trentin")
        self.assertEqual(num2words(34, lang="rm_sursilv"), "trentaquater")
        self.assertEqual(num2words(38, lang="rm_sursilv"), "trentotg")
        self.assertEqual(num2words(40, lang="rm_sursilv"), "curonta")
        self.assertEqual(num2words(50, lang="rm_sursilv"), "tschunconta")
        self.assertEqual(num2words(59, lang="rm_sursilv"), "tschuncontanov")
        self.assertEqual(num2words(66, lang="rm_sursilv"), "sissontasis")
        self.assertEqual(num2words(77, lang="rm_sursilv"), "siatontasiat")
        self.assertEqual(num2words(81, lang="rm_sursilv"), "otgontin")
        self.assertEqual(num2words(92, lang="rm_sursilv"), "navontadus")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_sursilv"), "tschien")
        self.assertEqual(num2words(101, lang="rm_sursilv"), "tschienedin")
        self.assertEqual(num2words(102, lang="rm_sursilv"), "tschienedus")
        self.assertEqual(num2words(103, lang="rm_sursilv"), "tschienetreis")
        self.assertEqual(num2words(104, lang="rm_sursilv"), "tschienequater")
        self.assertEqual(num2words(105, lang="rm_sursilv"), "tschienetschun")
        self.assertEqual(num2words(106, lang="rm_sursilv"), "tschienesis")
        self.assertEqual(num2words(107, lang="rm_sursilv"), "tschienesiat")
        self.assertEqual(num2words(108, lang="rm_sursilv"), "tschienedotg")
        self.assertEqual(num2words(109, lang="rm_sursilv"), "tschienenov")
        self.assertEqual(num2words(110, lang="rm_sursilv"), "tschienediesch")
        self.assertEqual(num2words(111, lang="rm_sursilv"), "tschienedendisch")
        self.assertEqual(num2words(112, lang="rm_sursilv"), "tschienedudisch")
        self.assertEqual(num2words(113, lang="rm_sursilv"), "tschienetredisch")
        self.assertEqual(num2words(114, lang="rm_sursilv"),
                         "tschienquitordisch")
        self.assertEqual(num2words(115, lang="rm_sursilv"),
                         "tschienequendisch")
        self.assertEqual(num2words(116, lang="rm_sursilv"), "tschienesedisch")
        self.assertEqual(num2words(117, lang="rm_sursilv"), "tschiengissiat")
        self.assertEqual(num2words(118, lang="rm_sursilv"), "tschienschotg")
        self.assertEqual(num2words(119, lang="rm_sursilv"), "tschienscheniv")
        self.assertEqual(num2words(120, lang="rm_sursilv"), "tschienevegn")
        self.assertEqual(num2words(121, lang="rm_sursilv"), "tschienventgin")
        self.assertEqual(num2words(122, lang="rm_sursilv"), "tschienventgadus")
        self.assertEqual(num2words(123, lang="rm_sursilv"),
                         "tschienventgatreis")
        self.assertEqual(num2words(124, lang="rm_sursilv"),
                         "tschienventgaquater")
        self.assertEqual(num2words(125, lang="rm_sursilv"),
                         "tschienventgatschun")
        self.assertEqual(num2words(126, lang="rm_sursilv"),
                         "tschienventgasis")
        self.assertEqual(num2words(127, lang="rm_sursilv"),
                         "tschienventgasiat")
        self.assertEqual(num2words(128, lang="rm_sursilv"), "tschienventgotg")
        self.assertEqual(num2words(129, lang="rm_sursilv"), "tschienventganov")
        self.assertEqual(num2words(130, lang="rm_sursilv"), "tschienetrenta")
        self.assertEqual(num2words(131, lang="rm_sursilv"), "tschientrentin")
        self.assertEqual(num2words(150, lang="rm_sursilv"),
                         "tschientschunconta")
        self.assertEqual(num2words(196, lang="rm_sursilv"),
                         "tschiennavontasis")
        self.assertEqual(num2words(200, lang="rm_sursilv"), "duatschien")
        self.assertEqual(num2words(208, lang="rm_sursilv"), "duatschienedotg")
        self.assertEqual(num2words(210, lang="rm_sursilv"),
                         "duatschienediesch")
        self.assertEqual(num2words(271, lang="rm_sursilv"),
                         "duatschiensiatontin")
        self.assertEqual(num2words(300, lang="rm_sursilv"), "treitschien")
        self.assertEqual(num2words(308, lang="rm_sursilv"),
                         "treitschienedotg")
        self.assertEqual(num2words(311, lang="rm_sursilv"),
                         "treitschienedendisch")
        self.assertEqual(
            num2words(375, lang="rm_sursilv"), "treitschiensiatontatschun"
        )
        self.assertEqual(num2words(400, lang="rm_sursilv"), "quatertschien")
        self.assertEqual(num2words(409, lang="rm_sursilv"),
                         "quatertschienenov")
        self.assertEqual(num2words(410, lang="rm_sursilv"),
                         "quatertschienediesch")
        self.assertEqual(num2words(472, lang="rm_sursilv"),
                         "quatertschiensiatontadus")
        self.assertEqual(num2words(701, lang="rm_sursilv"), "siattschienedin")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="rm_sursilv"), "melli")
        self.assertEqual(num2words(1001, lang="rm_sursilv"), "melliedin")
        self.assertEqual(num2words(1010, lang="rm_sursilv"), "melliediesch")
        self.assertEqual(num2words(1100, lang="rm_sursilv"), "mellietschien")
        self.assertEqual(num2words(1101, lang="rm_sursilv"),
                         "mellitschienedin")
        self.assertEqual(num2words(1132, lang="rm_sursilv"),
                         "mellitschientrentadus")
        self.assertEqual(num2words(1500, lang="rm_sursilv"),
                         "mellitschuntschien")
        self.assertEqual(
            num2words(7378, lang="rm_sursilv"),
            "siatmellitreitschiensiatontotg"
        )
        self.assertEqual(num2words(2000, lang="rm_sursilv"), "duamelli")
        self.assertEqual(num2words(2001, lang="rm_sursilv"), "duamelliedin")
        self.assertEqual(num2words(2020, lang="rm_sursilv"), "duamellievegn")
        self.assertEqual(num2words(2100, lang="rm_sursilv"),
                         "duamellietschien")
        self.assertEqual(num2words(2101, lang="rm_sursilv"),
                         "duamellitschienedin")
        self.assertEqual(num2words(3000, lang="rm_sursilv"), "treimelli")
        self.assertEqual(num2words(3012, lang="rm_sursilv"),
                         "treimelliedudisch")
        self.assertEqual(
            num2words(6870, lang="rm_sursilv"), "sismelliotgtschiensiatonta"
        )
        self.assertEqual(num2words(10000, lang="rm_sursilv"), "dieschmelli")
        self.assertEqual(num2words(10001, lang="rm_sursilv"),
                         "dieschmelliedin")
        self.assertEqual(
            num2words(98765, lang="rm_sursilv"),
            "navontotgmellisiattschiensissontatschun"
        )
        self.assertEqual(num2words(100000, lang="rm_sursilv"), "tschienmelli")
        self.assertEqual(
            num2words(523456, lang="rm_sursilv"),
            "tschuntschienventgatreimelliquatertschientschuncontasis"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="rm_sursilv"), "in milliun")
        self.assertEqual(num2words(1000007, lang="rm_sursilv"),
                         "in milliun e siat")
        self.assertEqual(num2words(1000008, lang="rm_sursilv"),
                         "in milliun ed otg")
        self.assertEqual(
            num2words(1200000, lang="rm_sursilv"),
            "in milliun duatschienmelli")
        self.assertEqual(num2words(2000000, lang="rm_sursilv"),
                         "dus milliuns")
        self.assertEqual(num2words(2000004, lang="rm_sursilv"),
                         "dus milliuns e quater")
        self.assertEqual(num2words(2000009, lang="rm_sursilv"),
                         "dus milliuns e nov")
        self.assertEqual(
            num2words(2200311, lang="rm_sursilv"),
            "dus milliuns duatschienmellitreitschienedendisch")
        self.assertEqual(
            num2words(2300000, lang="rm_sursilv"),
            "dus milliuns treitschienmelli")
        self.assertEqual(num2words(3000000, lang="rm_sursilv"),
                         "treis milliuns")
        self.assertEqual(
            num2words(3000005, lang="rm_sursilv"), "treis milliuns e tschun")
        self.assertEqual(
            num2words(3800000, lang="rm_sursilv"),
            "treis milliuns otgtschienmelli")
        self.assertEqual(num2words(1000000000, lang="rm_sursilv"),
                         "ina milliarda")
        self.assertEqual(
            num2words(1000000017, lang="rm_sursilv"),
            "ina milliarda e gissiat")
        self.assertEqual(num2words(2000000000, lang="rm_sursilv"),
                         "duas milliardas")
        self.assertEqual(
            num2words(2000001000, lang="rm_sursilv"),
            "duas milliardas e melli")
        self.assertEqual(
            num2words(3000000100, lang="rm_sursilv"),
            "treis milliardas e tschien")
        self.assertEqual(
            num2words(3000002000, lang="rm_sursilv"),
            "treis milliardas e duamelli")
        self.assertEqual(
            num2words(3002000100, lang="rm_sursilv"),
            "treis milliardas dus milliuns e tschien")
        self.assertEqual(
            num2words(3002000101, lang="rm_sursilv"),
            "treis milliardas dus milliuns e tschienedin")
        self.assertEqual(num2words(21000000000, lang="rm_sursilv"),
                         "ventgin milliardas")
        self.assertEqual(num2words(22000000000, lang="rm_sursilv"),
                         "ventgaduas milliardas")
        self.assertEqual(
            num2words(1234567890, lang="rm_sursilv"),
            "ina milliarda duatschientrentaquater milliuns "
            "tschuntschiensissontasiatmelliotgtschiennavonta")
        self.assertEqual(num2words(1000000000000, lang="rm_sursilv"),
                         "in billiun")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="rm_sursilv"),
            "tschienventgatreis quadrilliardas quatertschientschuncontasis"
            " quadrilliuns siattschienotgontanov trilliardas dudisch "
            "trilliuns treitschiencurontatschun billiardas "
            "sistschiensiatontotg billiuns novtschienedin milliardas "
            "duatschientrentaquater milliuns "
            "tschuntschiensissontasiatmelliotgtschiennavonta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="rm_sursilv", ordinal=True),
                         "emprem")
        self.assertEqual(num2words(7, lang="rm_sursilv", ordinal=True),
                         "siatavel")
        self.assertEqual(num2words(8, lang="rm_sursilv", ordinal=True),
                         "otgavel")
        self.assertEqual(num2words(20, lang="rm_sursilv", ordinal=True),
                         "vegnavel")
        self.assertEqual(num2words(21, lang="rm_sursilv", ordinal=True),
                         "ventginavel")
        self.assertEqual(
            num2words(27, lang="rm_sursilv", ordinal=True),
            "ventgasiatavel")
        self.assertEqual(
            num2words(48, lang="rm_sursilv", ordinal=True),
            "curontotgavel")
        self.assertEqual(num2words(60, lang="rm_sursilv", ordinal=True),
                         "sissontavel")
        self.assertEqual(
            num2words(99, lang="rm_sursilv", ordinal=True),
            "navontanovavel")

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_sursilv", ordinal=True),
                         "tschienavel")
        self.assertEqual(
            num2words(112, lang="rm_sursilv", ordinal=True),
            "tschienedudischavel")
        self.assertEqual(
            num2words(137, lang="rm_sursilv", ordinal=True),
            "tschientrentasiatavel")
        self.assertEqual(
            num2words(700, lang="rm_sursilv", ordinal=True),
            "siattschienavel")

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="rm_sursilv", ordinal=True),
                         "melliavel")
        self.assertEqual(
            num2words(1001, lang="rm_sursilv", ordinal=True),
            "melliedinavel")
        self.assertEqual(
            num2words(1200, lang="rm_sursilv", ordinal=True),
            "melliduatschienavel")
        self.assertEqual(
            num2words(8640, lang="rm_sursilv", ordinal=True),
            "otgmellisistschiencurontavel")
        self.assertEqual(
            num2words(14000, lang="rm_sursilv", ordinal=True),
            "quitordischmelliavel")
        self.assertEqual(
            num2words(123456, lang="rm_sursilv", ordinal=True),
            "tschienventgatreimelliquatertschientschuncontasisavel")
        self.assertEqual(
            num2words(987655, lang="rm_sursilv", ordinal=True),
            "novtschienotgontasiatmellisistschientschuncontatschunavel")

    def test_with_decimals(self):
        self.assertAlmostEqual(
            num2words(1.0, lang="rm_sursilv"), "in comma nulla")
        self.assertAlmostEqual(
            num2words(1.1, lang="rm_sursilv"), "in comma in")
