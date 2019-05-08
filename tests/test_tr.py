# -*- coding: utf-8 -*-
# Copyright (c) 2017, Tufan Kaynak, Framras.  All Rights Reserved.
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

from unittest import TestCase

from num2words import num2words


class Num2WordsTRTest(TestCase):
    def test_tr(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/8

        self.assertEqual(num2words(1, True, "tr"), u"birinci")
        self.assertEqual(num2words(2, True, "tr"), u"ikinci")
        self.assertEqual(num2words(9, True, "tr"), u"dokuzuncu")
        self.assertEqual(num2words(10, True, "tr"), u"onuncu")
        self.assertEqual(num2words(11, True, "tr"), u"onbirinci")
        self.assertEqual(num2words(44, True, "tr"), u"kırkdördüncü")
        self.assertEqual(num2words(100, True, "tr"), u"yüzüncü")
        self.assertEqual(num2words(101, True, "tr"), u"yüzbirinci")
        self.assertEqual(num2words(103, True, "tr"), u"yüzüçüncü")
        self.assertEqual(num2words(110, True, "tr"), u"yüzonuncu")
        self.assertEqual(num2words(111, True, "tr"), u"yüzonbirinci")
        self.assertEqual(num2words(1000, True, "tr"), u"bininci")
        self.assertEqual(num2words(1001, True, "tr"), u"binbirinci")
        self.assertEqual(num2words(1010, True, "tr"), u"binonuncu")
        self.assertEqual(num2words(1011, True, "tr"), u"binonbirinci")
        self.assertEqual(num2words(1100, True, "tr"), u"binyüzüncü")
        self.assertEqual(num2words(1110, True, "tr"), u"binyüzonuncu")
        self.assertEqual(
            num2words(2341, True, "tr"), u"ikibinüçyüzkırkbirinci"
        )
        self.assertEqual(num2words(10000, True, "tr"), u"onbininci")
        self.assertEqual(num2words(10010, True, "tr"), u"onbinonuncu")
        self.assertEqual(num2words(10100, True, "tr"), u"onbinyüzüncü")
        self.assertEqual(num2words(10110, True, "tr"), u"onbinyüzonuncu")
        self.assertEqual(num2words(11000, True, "tr"), u"onbirbininci")
        self.assertEqual(num2words(35000, True, "tr"), u"otuzbeşbininci")
        self.assertEqual(
            num2words(116331, True, "tr"), u"yüzonaltıbinüçyüzotuzbirinci"
        )
        self.assertEqual(
            num2words(116330, True, "tr"), u"yüzonaltıbinüçyüzotuzuncu"
        )
        self.assertEqual(num2words(100000, True, "tr"), u"yüzbininci")
        self.assertEqual(num2words(501000, True, "tr"), u"beşyüzbirbininci")
        self.assertEqual(
            num2words(1000111, True, "tr"), u"birmilyonyüzonbirinci"
        )
        self.assertEqual(
            num2words(111000111, True, "tr"), u"yüzonbirmilyonyüzonbirinci"
        )
        self.assertEqual(
            num2words(111001111, True, "tr"), u"yüzonbirmilyonbinyüzonbirinci"
        )
        self.assertEqual(
            num2words(111111111, True, "tr"),
            u"yüzonbirmilyonyüzonbirbinyüzonbirinci"
        )
        self.assertEqual(num2words(100001000, True, "tr"), u"yüzmilyonbininci")
        self.assertEqual(
            num2words(100001001, True, "tr"), u"yüzmilyonbinbirinci"
        )
        self.assertEqual(
            num2words(100010000, True, "tr"), u"yüzmilyononbininci"
        )
        self.assertEqual(
            num2words(100010001, True, "tr"), u"yüzmilyononbinbirinci"
        )
        self.assertEqual(
            num2words(100011000, True, "tr"), u"yüzmilyononbirbininci"
        )
        self.assertEqual(
            num2words(100011001, True, "tr"), u"yüzmilyononbirbinbirinci"
        )
        self.assertEqual(
            num2words(101011001, True, "tr"), u"yüzbirmilyononbirbinbirinci"
        )
        self.assertEqual(
            num2words(101011010, True, "tr"), u"yüzbirmilyononbirbinonuncu"
        )
        self.assertEqual(
            num2words(1101011010, True, "tr"),
            u"birmilyaryüzbirmilyononbirbinonuncu"
        )
        self.assertEqual(
            num2words(101101011010, True, "tr"),
            u"yüzbirmilyaryüzbirmilyononbirbinonuncu"
        )
        self.assertEqual(
            num2words(1000000000001, True, "tr"), u"birtrilyonbirinci"
        )

        self.assertEqual(num2words(1, False, "tr"), u"bir")
        self.assertEqual(num2words(2, False, "tr"), u"iki")
        self.assertEqual(num2words(9, False, "tr"), u"dokuz")
        self.assertEqual(num2words(10, False, "tr"), u"on")
        self.assertEqual(num2words(11, False, "tr"), u"onbir")
        self.assertEqual(num2words(44, False, "tr"), u"kırkdört")
        self.assertEqual(num2words(100, False, "tr"), u"yüz")
        self.assertEqual(num2words(101, False, "tr"), u"yüzbir")
        self.assertEqual(num2words(103, False, "tr"), u"yüzüç")
        self.assertEqual(num2words(110, False, "tr"), u"yüzon")
        self.assertEqual(num2words(111, False, "tr"), u"yüzonbir")
        self.assertEqual(num2words(1000, False, "tr"), u"bin")
        self.assertEqual(num2words(1001, False, "tr"), u"binbir")
        self.assertEqual(num2words(1010, False, "tr"), u"binon")
        self.assertEqual(num2words(1011, False, "tr"), u"binonbir")
        self.assertEqual(num2words(1100, False, "tr"), u"binyüz")
        self.assertEqual(num2words(1110, False, "tr"), u"binyüzon")
        self.assertEqual(num2words(2341, False, "tr"), u"ikibinüçyüzkırkbir")
        self.assertEqual(num2words(10000, False, "tr"), u"onbin")
        self.assertEqual(num2words(10010, False, "tr"), u"onbinon")
        self.assertEqual(num2words(10100, False, "tr"), u"onbinyüz")
        self.assertEqual(num2words(10110, False, "tr"), u"onbinyüzon")
        self.assertEqual(num2words(11000, False, "tr"), u"onbirbin")
        self.assertEqual(num2words(35000, False, "tr"), u"otuzbeşbin")
        self.assertEqual(
            num2words(116331, False, "tr"), u"yüzonaltıbinüçyüzotuzbir"
        )
        self.assertEqual(
            num2words(116330, False, "tr"), u"yüzonaltıbinüçyüzotuz"
        )
        self.assertEqual(num2words(500000, False, "tr"), u"beşyüzbin")
        self.assertEqual(num2words(501000, False, "tr"), u"beşyüzbirbin")
        self.assertEqual(num2words(1000111, False, "tr"), u"birmilyonyüzonbir")
        self.assertEqual(
            num2words(111000111, False, "tr"), u"yüzonbirmilyonyüzonbir"
        )
        self.assertEqual(
            num2words(111001111, False, "tr"), u"yüzonbirmilyonbinyüzonbir"
        )
        self.assertEqual(
            num2words(111111111, False, "tr"),
            u"yüzonbirmilyonyüzonbirbinyüzonbir"
        )
        self.assertEqual(num2words(100001000, False, "tr"), u"yüzmilyonbin")
        self.assertEqual(num2words(100001001, False, "tr"), u"yüzmilyonbinbir")
        self.assertEqual(num2words(100010000, False, "tr"), u"yüzmilyononbin")
        self.assertEqual(
            num2words(100010001, False, "tr"), u"yüzmilyononbinbir"
        )
        self.assertEqual(
            num2words(100011000, False, "tr"), u"yüzmilyononbirbin"
        )
        self.assertEqual(
            num2words(100011001, False, "tr"), u"yüzmilyononbirbinbir"
        )
        self.assertEqual(
            num2words(101011001, False, "tr"), u"yüzbirmilyononbirbinbir"
        )
        self.assertEqual(
            num2words(101011010, False, "tr"), u"yüzbirmilyononbirbinon"
        )
        self.assertEqual(
            num2words(1101011010, False, "tr"),
            u"birmilyaryüzbirmilyononbirbinon"
        )
        self.assertEqual(
            num2words(101101011010, False, "tr"),
            u"yüzbirmilyaryüzbirmilyononbirbinon"
        )
        self.assertEqual(
            num2words(1000000000001, False, "tr"), u"birtrilyonbir"
        )
        self.assertEqual(num2words(0.01, False, "tr"), u"sıfırvirgülbir")
        self.assertEqual(num2words(0.1, False, "tr"), u"sıfırvirgülon")
        self.assertEqual(num2words(0.21, False, "tr"), u"sıfırvirgülyirmibir")
        self.assertEqual(num2words(1.01, False, "tr"), u"birvirgülbir")
        self.assertEqual(num2words(1.1, False, "tr"), u"birvirgülon")
        self.assertEqual(num2words(1.21, False, "tr"), u"birvirgülyirmibir")
        self.assertEqual(
            num2words(101101011010.02, False, "tr"),
            u"yüzbirmilyaryüzbirmilyononbirbinonvirgüliki"
        )
        self.assertEqual(
            num2words(101101011010.2, False, "tr"),
            u"yüzbirmilyaryüzbirmilyononbirbinonvirgülyirmi"
        )
