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


class Num2WordsRMPUTERTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="rm_puter")
        neg_crd = num2words(-number, lang="rm_puter")
        pos_ord = num2words(+number, lang="rm_puter", ordinal=True)
        neg_ord = num2words(-number, lang="rm_puter", ordinal=True)
        self.assertEqual("minus " + pos_crd, neg_crd)
        self.assertEqual("minus " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_puter"),
            "trais comma ün quatter ün tschinch")
        self.assertEqual(
            num2words(-5.15, lang="rm_puter"),
            "minus tschinch comma ün tschinch")
        self.assertEqual(
            num2words(-0.15, lang="rm_puter"),
            "minus nolla comma ün tschinch")

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_puter", ordinal=True),
            "terz comma ün quatter ün tschinch")
        self.assertEqual(
            num2words(-5.15, lang="rm_puter", ordinal=True),
            "minus tschinchevel comma ün tschinch")
        self.assertEqual(
            num2words(-0.15, lang="rm_puter", ordinal=True),
            "minus nolla comma ün tschinch")

    def test_0(self):
        self.assertEqual(num2words(0, lang="rm_puter"), "nolla")
        self.assertEqual(num2words(0, lang="rm_puter", ordinal=True),
                         "nolla")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="rm_puter"), "ün")
        self.assertEqual(num2words(2, lang="rm_puter"), "duos")
        self.assertEqual(num2words(3, lang="rm_puter"), "trais")
        self.assertEqual(num2words(5, lang="rm_puter"), "tschinch")
        self.assertEqual(num2words(7, lang="rm_puter"), "set")
        self.assertEqual(num2words(8, lang="rm_puter"), "och")
        self.assertEqual(num2words(10, lang="rm_puter"), "desch")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="rm_puter"), "ündesch")
        self.assertEqual(num2words(13, lang="rm_puter"), "tredesch")
        self.assertEqual(num2words(15, lang="rm_puter"), "quindesch")
        self.assertEqual(num2words(16, lang="rm_puter"), "saidesch")
        self.assertEqual(num2words(17, lang="rm_puter"), "dischset")
        self.assertEqual(num2words(18, lang="rm_puter"), "dischdoch")
        self.assertEqual(num2words(19, lang="rm_puter"), "dischnouv")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="rm_puter"), "vainch")
        self.assertEqual(num2words(21, lang="rm_puter"), "vainchün")
        self.assertEqual(num2words(22, lang="rm_puter"), "vainchaduos")
        self.assertEqual(num2words(23, lang="rm_puter"), "vainchatrais")
        self.assertEqual(num2words(28, lang="rm_puter"), "vainchoch")
        self.assertEqual(num2words(30, lang="rm_puter"), "trenta")
        self.assertEqual(num2words(31, lang="rm_puter"), "trentün")
        self.assertEqual(num2words(34, lang="rm_puter"), "trentaquatter")
        self.assertEqual(num2words(38, lang="rm_puter"), "trentoch")
        self.assertEqual(num2words(40, lang="rm_puter"), "quaraunta")
        self.assertEqual(num2words(50, lang="rm_puter"), "tschinquaunta")
        self.assertEqual(num2words(59, lang="rm_puter"), "tschinquauntanouv")
        self.assertEqual(num2words(66, lang="rm_puter"), "sesauntases")
        self.assertEqual(num2words(77, lang="rm_puter"), "settauntaset")
        self.assertEqual(num2words(81, lang="rm_puter"), "ochauntün")
        self.assertEqual(num2words(92, lang="rm_puter"), "nonauntaduos")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_puter"), "tschient")
        self.assertEqual(num2words(101, lang="rm_puter"), "tschientedün")
        self.assertEqual(num2words(102, lang="rm_puter"), "tschienteduos")
        self.assertEqual(num2words(103, lang="rm_puter"), "tschientetrais")
        self.assertEqual(num2words(104, lang="rm_puter"),
                         "tschientequatter")
        self.assertEqual(num2words(105, lang="rm_puter"),
                         "tschientetschinch")
        self.assertEqual(num2words(106, lang="rm_puter"), "tschienteses")
        self.assertEqual(num2words(107, lang="rm_puter"), "tschienteset")
        self.assertEqual(num2words(108, lang="rm_puter"), "tschientedoch")
        self.assertEqual(num2words(109, lang="rm_puter"), "tschientenouv")
        self.assertEqual(num2words(110, lang="rm_puter"), "tschientedesch")
        self.assertEqual(num2words(111, lang="rm_puter"),
                         "tschientedündesch")
        self.assertEqual(num2words(112, lang="rm_puter"),
                         "tschientedudesch")
        self.assertEqual(num2words(113, lang="rm_puter"),
                         "tschientetredesch")
        self.assertEqual(num2words(114, lang="rm_puter"),
                         "tschientquattordesch")
        self.assertEqual(num2words(115, lang="rm_puter"),
                         "tschientequindesch")
        self.assertEqual(num2words(116, lang="rm_puter"),
                         "tschientesaidesch")
        self.assertEqual(num2words(117, lang="rm_puter"),
                         "tschientdischset")
        self.assertEqual(num2words(118, lang="rm_puter"),
                         "tschientdischdoch")
        self.assertEqual(num2words(119, lang="rm_puter"),
                         "tschientdischnouv")
        self.assertEqual(num2words(120, lang="rm_puter"),
                         "tschientevainch")
        self.assertEqual(num2words(121, lang="rm_puter"),
                         "tschientvainchün")
        self.assertEqual(num2words(122, lang="rm_puter"),
                         "tschientvainchaduos")
        self.assertEqual(num2words(123, lang="rm_puter"),
                         "tschientvainchatrais")
        self.assertEqual(num2words(124, lang="rm_puter"),
                         "tschientvainchaquatter")
        self.assertEqual(num2words(125, lang="rm_puter"),
                         "tschientvainchatschinch")
        self.assertEqual(num2words(126, lang="rm_puter"),
                         "tschientvainchases")
        self.assertEqual(num2words(127, lang="rm_puter"),
                         "tschientvainchaset")
        self.assertEqual(num2words(128, lang="rm_puter"),
                         "tschientvainchoch")
        self.assertEqual(num2words(129, lang="rm_puter"),
                         "tschientvainchanouv")
        self.assertEqual(num2words(130, lang="rm_puter"),
                         "tschientetrenta")
        self.assertEqual(num2words(131, lang="rm_puter"),
                         "tschienttrentün")
        self.assertEqual(num2words(150, lang="rm_puter"),
                         "tschienttschinquaunta")
        self.assertEqual(num2words(196, lang="rm_puter"),
                         "tschientnonauntases")
        self.assertEqual(num2words(200, lang="rm_puter"),
                         "duatschient")
        self.assertEqual(num2words(208, lang="rm_puter"),
                         "duatschientedoch")
        self.assertEqual(num2words(210, lang="rm_puter"),
                         "duatschientedesch")
        self.assertEqual(num2words(271, lang="rm_puter"),
                         "duatschientsettauntün")
        self.assertEqual(num2words(300, lang="rm_puter"),
                         "trajatschient")
        self.assertEqual(num2words(308, lang="rm_puter"),
                         "trajatschientedoch")
        self.assertEqual(num2words(311, lang="rm_puter"),
                         "trajatschientedündesch")
        self.assertEqual(
            num2words(375, lang="rm_puter"),
            "trajatschientsettauntatschinch")
        self.assertEqual(num2words(400, lang="rm_puter"),
                         "quattertschient")
        self.assertEqual(num2words(409, lang="rm_puter"),
                         "quattertschientenouv")
        self.assertEqual(num2words(410, lang="rm_puter"),
                         "quattertschientedesch")
        self.assertEqual(num2words(472, lang="rm_puter"),
                         "quattertschientsettauntaduos")
        self.assertEqual(num2words(701, lang="rm_puter"),
                         "settschientedün")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="rm_puter"), "milli")
        self.assertEqual(num2words(1001, lang="rm_puter"), "milliedün")
        self.assertEqual(num2words(1010, lang="rm_puter"), "milliedesch")
        self.assertEqual(num2words(1100, lang="rm_puter"),
                         "millietschient")
        self.assertEqual(num2words(1101, lang="rm_puter"),
                         "millitschientedün")
        self.assertEqual(num2words(1132, lang="rm_puter"),
                         "millitschienttrentaduos")
        self.assertEqual(num2words(1500, lang="rm_puter"),
                         "millitschinchtschient")
        self.assertEqual(
            num2words(7378, lang="rm_puter"),
            "setmillitrajatschientsettauntoch")
        self.assertEqual(num2words(2000, lang="rm_puter"), "duamilli")
        self.assertEqual(num2words(2001, lang="rm_puter"), "duamilliedün")
        self.assertEqual(num2words(2020, lang="rm_puter"),
                         "duamillievainch")
        self.assertEqual(num2words(2100, lang="rm_puter"),
                         "duamillietschient")
        self.assertEqual(num2words(2101, lang="rm_puter"),
                         "duamillitschientedün")
        self.assertEqual(num2words(3000, lang="rm_puter"), "trajamilli")
        self.assertEqual(num2words(3012, lang="rm_puter"),
                         "trajamilliedudesch")
        self.assertEqual(
            num2words(6870, lang="rm_puter"), "sesmilliochtschientsettaunta"
        )
        self.assertEqual(num2words(10000, lang="rm_puter"), "deschmilli")
        self.assertEqual(num2words(10001, lang="rm_puter"),
                         "deschmilliedün")
        self.assertEqual(
            num2words(98765, lang="rm_puter"),
            "nonauntochmillisettschientsesauntatschinch")
        self.assertEqual(num2words(100000, lang="rm_puter"),
                         "tschientmilli")
        self.assertEqual(
            num2words(523456, lang="rm_puter"),
            "tschinchtschientvainchatrajamilliquattertschienttschinquauntases")

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="rm_puter"), "ün milliun")
        self.assertEqual(num2words(1000007, lang="rm_puter"),
                         "ün milliun e set")
        self.assertEqual(num2words(1000008, lang="rm_puter"),
                         "ün milliun ed och")
        self.assertEqual(
            num2words(1200000, lang="rm_puter"),
            "ün milliun duatschientmilli")
        self.assertEqual(num2words(2000000, lang="rm_puter"),
                         "duos milliuns")
        self.assertEqual(num2words(2000004, lang="rm_puter"),
                         "duos milliuns e quatter")
        self.assertEqual(num2words(2000009, lang="rm_puter"),
                         "duos milliuns e nouv")
        self.assertEqual(
            num2words(2200311, lang="rm_puter"),
            "duos milliuns duatschientmillitrajatschientedündesch")
        self.assertEqual(
            num2words(2300000, lang="rm_puter"),
            "duos milliuns trajatschientmilli")
        self.assertEqual(num2words(3000000, lang="rm_puter"),
                         "trais milliuns")
        self.assertEqual(
            num2words(3000005, lang="rm_puter"),
            "trais milliuns e tschinch")
        self.assertEqual(
            num2words(3800000, lang="rm_puter"),
            "trais milliuns ochtschientmilli")
        self.assertEqual(num2words(1000000000, lang="rm_puter"),
                         "ün milliard")
        self.assertEqual(
            num2words(1000000017, lang="rm_puter"),
            "ün milliard e dischset")
        self.assertEqual(num2words(2000000000, lang="rm_puter"),
                         "duos milliards")
        self.assertEqual(
            num2words(2000001000, lang="rm_puter"),
            "duos milliards e milli")
        self.assertEqual(
            num2words(3000000100, lang="rm_puter"),
            "trais milliards e tschient")
        self.assertEqual(
            num2words(3000002000, lang="rm_puter"),
            "trais milliards e duamilli")
        self.assertEqual(
            num2words(3002000100, lang="rm_puter"),
            "trais milliards duos milliuns e tschient")
        self.assertEqual(
            num2words(3002000101, lang="rm_puter"),
            "trais milliards duos milliuns e tschientedün")
        self.assertEqual(num2words(21000000000, lang="rm_puter"),
                         "vainchün milliards")
        self.assertEqual(num2words(22000000000, lang="rm_puter"),
                         "vainchaduos milliards")
        self.assertEqual(
            num2words(1234567890, lang="rm_puter"),
            "ün milliard duatschienttrentaquatter milliuns "
            "tschinchtschientsesauntasetmilliochtschientnonaunta")
        self.assertEqual(num2words(1000000000000, lang="rm_puter"),
                         "ün billiun")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="rm_puter"),
            "tschientvainchatrais quadrilliards "
            "quattertschienttschinquauntases"
            " quadrilliuns settschientochauntanouv trilliards dudesch "
            "trilliuns trajatschientquarauntatschinch billiards "
            "sestschientsettauntoch billiuns nouvtschientedün milliards "
            "duatschienttrentaquatter milliuns "
            "tschinchtschientsesauntasetmilliochtschientnonaunta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="rm_puter", ordinal=True),
                         "prüm")
        self.assertEqual(num2words(7, lang="rm_puter", ordinal=True),
                         "settevel")
        self.assertEqual(num2words(8, lang="rm_puter", ordinal=True),
                         "ochevel")
        self.assertEqual(num2words(17, lang="rm_puter", ordinal=True),
                         "dischsettevel")
        self.assertEqual(num2words(18, lang="rm_puter", ordinal=True),
                         "dischdochevel")
        self.assertEqual(num2words(20, lang="rm_puter", ordinal=True),
                         "vainchevel")
        self.assertEqual(num2words(21, lang="rm_puter", ordinal=True),
                         "vainchünevel")
        self.assertEqual(
            num2words(27, lang="rm_puter", ordinal=True),
            "vainchasettevel")
        self.assertEqual(
            num2words(48, lang="rm_puter", ordinal=True),
            "quarauntochevel")
        self.assertEqual(num2words(60, lang="rm_puter", ordinal=True),
                         "sesauntevel")
        self.assertEqual(
            num2words(99, lang="rm_puter", ordinal=True),
            "nonauntanouvevel")

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_puter", ordinal=True),
                         "tschientevel")
        self.assertEqual(
            num2words(112, lang="rm_puter", ordinal=True),
            "tschientedudeschevel")
        self.assertEqual(
            num2words(137, lang="rm_puter", ordinal=True),
            "tschienttrentasettevel")
        self.assertEqual(
            num2words(700, lang="rm_puter", ordinal=True),
            "settschientevel")

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="rm_puter", ordinal=True),
                         "millievel")
        self.assertEqual(
            num2words(1001, lang="rm_puter", ordinal=True),
            "milliedünevel")
        self.assertEqual(
            num2words(1200, lang="rm_puter", ordinal=True),
            "milliduatschientevel")
        self.assertEqual(
            num2words(8640, lang="rm_puter", ordinal=True),
            "ochmillisestschientquarauntevel")
        self.assertEqual(
            num2words(14000, lang="rm_puter", ordinal=True),
            "quattordeschmillievel")
        self.assertEqual(
            num2words(123456, lang="rm_puter", ordinal=True),
            "tschientvainchatrajamilliquattertschienttschinquauntasesevel"
        )
        self.assertEqual(
            num2words(987655, lang="rm_puter", ordinal=True),
            "nouvtschientochauntasetmillisestschienttschinquauntatschinchevel")

    def test_with_decimals(self):
        self.assertAlmostEqual(
            num2words(1.0, lang="rm_puter"),
            "ün comma nolla")
        self.assertAlmostEqual(
            num2words(1.1, lang="rm_puter"),
            "ün comma ün")
