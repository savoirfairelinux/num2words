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


class Num2WordsRMSUTSILVTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="rm_sutsilv")
        neg_crd = num2words(-number, lang="rm_sutsilv")
        pos_ord = num2words(+number, lang="rm_sutsilv", ordinal=True)
        neg_ord = num2words(-number, lang="rm_sutsilv", ordinal=True)
        self.assertEqual("minus " + pos_crd, neg_crd)
        self.assertEqual("minus " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_sutsilv"),
            "tres coma egn quater egn tschentg"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_sutsilv"),
            "minus tschentg coma egn tschentg"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_sutsilv"),
            "minus nola coma egn tschentg"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="rm_sutsilv", ordinal=True),
            "tearz coma egn quater egn tschentg"
        )
        self.assertEqual(
            num2words(-5.15, lang="rm_sutsilv", ordinal=True),
            "minus tschentgavel coma egn tschentg"
        )
        self.assertEqual(
            num2words(-0.15, lang="rm_sutsilv", ordinal=True),
            "minus nola coma egn tschentg"
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="rm_sutsilv"), "nola")
        self.assertEqual(num2words(0, lang="rm_sutsilv", ordinal=True),
                         "nola")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="rm_sutsilv"), "egn")
        self.assertEqual(num2words(2, lang="rm_sutsilv"), "dus")
        self.assertEqual(num2words(3, lang="rm_sutsilv"), "tres")
        self.assertEqual(num2words(5, lang="rm_sutsilv"), "tschentg")
        self.assertEqual(num2words(7, lang="rm_sutsilv"), "seat")
        self.assertEqual(num2words(8, lang="rm_sutsilv"), "otg")
        self.assertEqual(num2words(10, lang="rm_sutsilv"), "diesch")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="rm_sutsilv"), "endesch")
        self.assertEqual(num2words(13, lang="rm_sutsilv"), "tredesch")
        self.assertEqual(num2words(15, lang="rm_sutsilv"), "quendesch")
        self.assertEqual(num2words(16, lang="rm_sutsilv"), "sedesch")
        self.assertEqual(num2words(17, lang="rm_sutsilv"), "gisseat")
        self.assertEqual(num2words(18, lang="rm_sutsilv"), "schotg")
        self.assertEqual(num2words(19, lang="rm_sutsilv"), "schenev")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="rm_sutsilv"), "veintg")
        self.assertEqual(num2words(21, lang="rm_sutsilv"), "veintgegn")
        self.assertEqual(num2words(22, lang="rm_sutsilv"), "veintgadus")
        self.assertEqual(num2words(23, lang="rm_sutsilv"), "veintgatres")
        self.assertEqual(num2words(28, lang="rm_sutsilv"), "veintgotg")
        self.assertEqual(num2words(30, lang="rm_sutsilv"), "trainta")
        self.assertEqual(num2words(31, lang="rm_sutsilv"), "traintegn")
        self.assertEqual(num2words(34, lang="rm_sutsilv"), "traintaquater")
        self.assertEqual(num2words(38, lang="rm_sutsilv"), "traintotg")
        self.assertEqual(num2words(40, lang="rm_sutsilv"), "curànta")
        self.assertEqual(num2words(50, lang="rm_sutsilv"), "tschuncànta")
        self.assertEqual(num2words(59, lang="rm_sutsilv"), "tschuncàntanov")
        self.assertEqual(num2words(66, lang="rm_sutsilv"), "sissàntasis")
        self.assertEqual(num2words(77, lang="rm_sutsilv"), "satàntaseat")
        self.assertEqual(num2words(81, lang="rm_sutsilv"), "otgàntegn")
        self.assertEqual(num2words(92, lang="rm_sutsilv"), "novàntadus")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_sutsilv"),
                         "tschient")
        self.assertEqual(num2words(101, lang="rm_sutsilv"),
                         "tschientadegn")
        self.assertEqual(num2words(102, lang="rm_sutsilv"),
                         "tschientadus")
        self.assertEqual(num2words(103, lang="rm_sutsilv"),
                         "tschientatres")
        self.assertEqual(num2words(104, lang="rm_sutsilv"),
                         "tschientaquater")
        self.assertEqual(num2words(105, lang="rm_sutsilv"),
                         "tschientatschentg")
        self.assertEqual(num2words(106, lang="rm_sutsilv"),
                         "tschientasis")
        self.assertEqual(num2words(107, lang="rm_sutsilv"),
                         "tschientaseat")
        self.assertEqual(num2words(108, lang="rm_sutsilv"),
                         "tschientadotg")
        self.assertEqual(num2words(109, lang="rm_sutsilv"),
                         "tschientanov")
        self.assertEqual(num2words(110, lang="rm_sutsilv"),
                         "tschientadiesch")
        self.assertEqual(num2words(111, lang="rm_sutsilv"),
                         "tschientadendesch")
        self.assertEqual(num2words(112, lang="rm_sutsilv"),
                         "tschientadudesch")
        self.assertEqual(num2words(113, lang="rm_sutsilv"),
                         "tschientatredesch")
        self.assertEqual(num2words(114, lang="rm_sutsilv"),
                         "tschientquitordesch")
        self.assertEqual(num2words(115, lang="rm_sutsilv"),
                         "tschientaquendesch")
        self.assertEqual(num2words(116, lang="rm_sutsilv"),
                         "tschientasedesch")
        self.assertEqual(num2words(117, lang="rm_sutsilv"),
                         "tschientgisseat")
        self.assertEqual(num2words(118, lang="rm_sutsilv"),
                         "tschientschotg")
        self.assertEqual(num2words(119, lang="rm_sutsilv"),
                         "tschientschenev")
        self.assertEqual(num2words(120, lang="rm_sutsilv"),
                         "tschientaveintg")
        self.assertEqual(num2words(121, lang="rm_sutsilv"),
                         "tschientveintgegn")
        self.assertEqual(num2words(122, lang="rm_sutsilv"),
                         "tschientveintgadus")
        self.assertEqual(num2words(123, lang="rm_sutsilv"),
                         "tschientveintgatres")
        self.assertEqual(num2words(124, lang="rm_sutsilv"),
                         "tschientveintgaquater")
        self.assertEqual(num2words(125, lang="rm_sutsilv"),
                         "tschientveintgatschentg")
        self.assertEqual(num2words(126, lang="rm_sutsilv"),
                         "tschientveintgasis")
        self.assertEqual(num2words(127, lang="rm_sutsilv"),
                         "tschientveintgaseat")
        self.assertEqual(num2words(128, lang="rm_sutsilv"),
                         "tschientveintgotg")
        self.assertEqual(num2words(129, lang="rm_sutsilv"),
                         "tschientveintganov")
        self.assertEqual(num2words(130, lang="rm_sutsilv"),
                         "tschientatrainta")
        self.assertEqual(num2words(131, lang="rm_sutsilv"),
                         "tschienttraintegn")
        self.assertEqual(num2words(150, lang="rm_sutsilv"),
                         "tschienttschuncànta")
        self.assertEqual(num2words(196, lang="rm_sutsilv"),
                         "tschientnovàntasis")
        self.assertEqual(num2words(200, lang="rm_sutsilv"),
                         "dutschient")
        self.assertEqual(num2words(208, lang="rm_sutsilv"),
                         "dutschientadotg")
        self.assertEqual(num2words(210, lang="rm_sutsilv"),
                         "dutschientadiesch")
        self.assertEqual(num2words(271, lang="rm_sutsilv"),
                         "dutschientsatàntegn")
        self.assertEqual(num2words(300, lang="rm_sutsilv"),
                         "tretschient")
        self.assertEqual(num2words(308, lang="rm_sutsilv"),
                         "tretschientadotg")
        self.assertEqual(num2words(311, lang="rm_sutsilv"),
                         "tretschientadendesch")
        self.assertEqual(
            num2words(375, lang="rm_sutsilv"),
            "tretschientsatàntatschentg"
        )
        self.assertEqual(num2words(400, lang="rm_sutsilv"),
                         "quatertschient")
        self.assertEqual(num2words(409, lang="rm_sutsilv"),
                         "quatertschientanov")
        self.assertEqual(num2words(410, lang="rm_sutsilv"),
                         "quatertschientadiesch")
        self.assertEqual(num2words(472, lang="rm_sutsilv"),
                         "quatertschientsatàntadus")
        self.assertEqual(num2words(701, lang="rm_sutsilv"),
                         "seattschientadegn")

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="rm_sutsilv"),
                         "meli")
        self.assertEqual(num2words(1001, lang="rm_sutsilv"),
                         "meliadegn")
        self.assertEqual(num2words(1010, lang="rm_sutsilv"),
                         "meliadiesch")
        self.assertEqual(num2words(1100, lang="rm_sutsilv"),
                         "meliatschient")
        self.assertEqual(num2words(1101, lang="rm_sutsilv"),
                         "melitschientadegn")
        self.assertEqual(num2words(1132, lang="rm_sutsilv"),
                         "melitschienttraintadus")
        self.assertEqual(num2words(1500, lang="rm_sutsilv"),
                         "melitschentgtschient")
        self.assertEqual(
            num2words(7378, lang="rm_sutsilv"),
            "seatmelitretschientsatàntotg"
        )
        self.assertEqual(num2words(2000, lang="rm_sutsilv"),
                         "dumeli")
        self.assertEqual(num2words(2001, lang="rm_sutsilv"),
                         "dumeliadegn")
        self.assertEqual(num2words(2020, lang="rm_sutsilv"),
                         "dumeliaveintg")
        self.assertEqual(num2words(2100, lang="rm_sutsilv"),
                         "dumeliatschient")
        self.assertEqual(num2words(2101, lang="rm_sutsilv"),
                         "dumelitschientadegn")
        self.assertEqual(num2words(3000, lang="rm_sutsilv"),
                         "tremeli")
        self.assertEqual(num2words(3012, lang="rm_sutsilv"),
                         "tremeliadudesch")
        self.assertEqual(
            num2words(6870, lang="rm_sutsilv"),
            "sismeliotgtschientsatànta"
        )
        self.assertEqual(num2words(10000, lang="rm_sutsilv"),
                         "dieschmeli")
        self.assertEqual(num2words(10001, lang="rm_sutsilv"),
                         "dieschmeliadegn")
        self.assertEqual(
            num2words(98765, lang="rm_sutsilv"),
            "novàntotgmeliseattschientsissàntatschentg"
        )
        self.assertEqual(num2words(100000, lang="rm_sutsilv"),
                         "tschientmeli")
        self.assertEqual(
            num2words(523456, lang="rm_sutsilv"),
            "tschentgtschientveintgatremeliquatertschienttschuncàntasis"
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="rm_sutsilv"),
                         "egn miliùn")
        self.assertEqual(num2words(1000007, lang="rm_sutsilv"),
                         "egn miliùn a seat")
        self.assertEqual(num2words(1000008, lang="rm_sutsilv"),
                         "egn miliùn ad otg")
        self.assertEqual(
            num2words(1200000, lang="rm_sutsilv"),
            "egn miliùn dutschientmeli")
        self.assertEqual(num2words(2000000, lang="rm_sutsilv"),
                         "dus miliùns")
        self.assertEqual(num2words(2000004, lang="rm_sutsilv"),
                         "dus miliùns a quater")
        self.assertEqual(num2words(2000009, lang="rm_sutsilv"),
                         "dus miliùns a nov")
        self.assertEqual(
            num2words(2200311, lang="rm_sutsilv"),
            "dus miliùns dutschientmelitretschientadendesch")
        self.assertEqual(
            num2words(2300000, lang="rm_sutsilv"),
            "dus miliùns tretschientmeli")
        self.assertEqual(num2words(3000000, lang="rm_sutsilv"),
                         "tres miliùns")
        self.assertEqual(
            num2words(3000005, lang="rm_sutsilv"),
            "tres miliùns a tschentg")
        self.assertEqual(
            num2words(3800000, lang="rm_sutsilv"),
            "tres miliùns otgtschientmeli")
        self.assertEqual(num2words(1000000000, lang="rm_sutsilv"),
                         "egna miliarda")
        self.assertEqual(
            num2words(1000000017, lang="rm_sutsilv"),
            "egna miliarda a gisseat")
        self.assertEqual(num2words(2000000000, lang="rm_sutsilv"),
                         "duas miliardas")
        self.assertEqual(
            num2words(2000001000, lang="rm_sutsilv"),
            "duas miliardas a meli")
        self.assertEqual(
            num2words(3000000100, lang="rm_sutsilv"),
            "tres miliardas a tschient")
        self.assertEqual(
            num2words(3000002000, lang="rm_sutsilv"),
            "tres miliardas a dumeli")
        self.assertEqual(
            num2words(3002000100, lang="rm_sutsilv"),
            "tres miliardas dus miliùns a tschient")
        self.assertEqual(
            num2words(3002000101, lang="rm_sutsilv"),
            "tres miliardas dus miliùns a tschientadegn")
        self.assertEqual(num2words(21000000000, lang="rm_sutsilv"),
                         "veintgegn miliardas")
        self.assertEqual(num2words(22000000000, lang="rm_sutsilv"),
                         "veintgaduas miliardas")
        self.assertEqual(
            num2words(1234567890, lang="rm_sutsilv"),
            "egna miliarda dutschienttraintaquater miliùns "
            "tschentgtschientsissàntaseatmeliotgtschientnovànta")
        self.assertEqual(num2words(1000000000000, lang="rm_sutsilv"),
                         "egn biliùn")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="rm_sutsilv"),
            "tschientveintgatres quadriliardas quatertschienttschuncàntasis"
            " quadriliùns seattschientotgàntanov triliardas dudesch "
            "triliùns tretschientcuràntatschentg biliardas "
            "sistschientsatàntotg biliùns novtschientadegn miliardas "
            "dutschienttraintaquater miliùns "
            "tschentgtschientsissàntaseatmeliotgtschientnovànta"
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="rm_sutsilv", ordinal=True),
                         "amprem")
        self.assertEqual(num2words(7, lang="rm_sutsilv", ordinal=True),
                         "seatavel")
        self.assertEqual(num2words(8, lang="rm_sutsilv", ordinal=True),
                         "otgavel")
        self.assertEqual(num2words(20, lang="rm_sutsilv", ordinal=True),
                         "veintgavel")
        self.assertEqual(num2words(21, lang="rm_sutsilv", ordinal=True),
                         "veintgegnavel")
        self.assertEqual(
            num2words(27, lang="rm_sutsilv", ordinal=True),
            "veintgaseatavel")
        self.assertEqual(
            num2words(48, lang="rm_sutsilv", ordinal=True),
            "curàntotgavel")
        self.assertEqual(num2words(60, lang="rm_sutsilv", ordinal=True),
                         "sissàntavel")
        self.assertEqual(
            num2words(99, lang="rm_sutsilv", ordinal=True),
            "novàntanovavel")

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="rm_sutsilv", ordinal=True),
                         "tschientavel")
        self.assertEqual(
            num2words(112, lang="rm_sutsilv", ordinal=True),
            "tschientadudeschavel")
        self.assertEqual(
            num2words(137, lang="rm_sutsilv", ordinal=True),
            "tschienttraintaseatavel")
        self.assertEqual(
            num2words(700, lang="rm_sutsilv", ordinal=True),
            "seattschientavel")

    def test_nth_1000_to_999999(self):
        self.assertEqual(num2words(1000, lang="rm_sutsilv", ordinal=True),
                         "meliavel")
        self.assertEqual(
            num2words(1001, lang="rm_sutsilv", ordinal=True),
            "meliadegnavel")
        self.assertEqual(
            num2words(1200, lang="rm_sutsilv", ordinal=True),
            "melidutschientavel")
        self.assertEqual(
            num2words(8640, lang="rm_sutsilv", ordinal=True),
            "otgmelisistschientcuràntavel")
        self.assertEqual(
            num2words(14000, lang="rm_sutsilv", ordinal=True),
            "quitordeschmeliavel")
        self.assertEqual(
            num2words(123456, lang="rm_sutsilv", ordinal=True),
            "tschientveintgatremeliquatertschienttschuncàntasisavel")
        self.assertEqual(
            num2words(987655, lang="rm_sutsilv", ordinal=True),
            "novtschientotgàntaseatmelisistschienttschuncàntatschentgavel")

    def test_with_decimals(self):
        self.assertAlmostEqual(
            num2words(1.0, lang="rm_sutsilv"),
            "egn coma nola")
        self.assertAlmostEqual(
            num2words(1.1, lang="rm_sutsilv"),
            "egn coma egn")
