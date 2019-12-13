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

        self.assertEqual(num2words(1, lang="tr", to="ordinal"), u"birinci")
        self.assertEqual(num2words(2, lang="tr", to="ordinal"), u"ikinci")
        self.assertEqual(num2words(9, lang="tr", to="ordinal"), u"dokuzuncu")
        self.assertEqual(num2words(10, lang="tr", to="ordinal"), u"onuncu")
        self.assertEqual(num2words(11, lang="tr", to="ordinal"), u"onbirinci")
        self.assertEqual(num2words(44, lang="tr", to="ordinal"), u"kırkdördüncü")
        self.assertEqual(num2words(100, lang="tr", to="ordinal"), u"yüzüncü")
        self.assertEqual(num2words(101, lang="tr", to="ordinal"), u"yüzbirinci")
        self.assertEqual(num2words(103, lang="tr", to="ordinal"), u"yüzüçüncü")
        self.assertEqual(num2words(110, lang="tr", to="ordinal"), u"yüzonuncu")
        self.assertEqual(num2words(111, lang="tr", to="ordinal"), u"yüzonbirinci")
        self.assertEqual(num2words(1000, lang="tr", to="ordinal"), u"bininci")
        self.assertEqual(num2words(1001, lang="tr", to="ordinal"), u"binbirinci")
        self.assertEqual(num2words(1010, lang="tr", to="ordinal"), u"binonuncu")
        self.assertEqual(num2words(1011, lang="tr", to="ordinal"), u"binonbirinci")
        self.assertEqual(num2words(1100, lang="tr", to="ordinal"), u"binyüzüncü")
        self.assertEqual(num2words(1110, lang="tr", to="ordinal"), u"binyüzonuncu")
        self.assertEqual(
            num2words(2341, lang="tr", to="ordinal"), u"ikibinüçyüzkırkbirinci"
        )
        self.assertEqual(num2words(10000, lang="tr", to="ordinal"), u"onbininci")
        self.assertEqual(num2words(10010, lang="tr", to="ordinal"), u"onbinonuncu")
        self.assertEqual(num2words(10100, lang="tr", to="ordinal"), u"onbinyüzüncü")
        self.assertEqual(num2words(10110, lang="tr", to="ordinal"), u"onbinyüzonuncu")
        self.assertEqual(num2words(11000, lang="tr", to="ordinal"), u"onbirbininci")
        self.assertEqual(num2words(35000, lang="tr", to="ordinal"), u"otuzbeşbininci")
        self.assertEqual(
            num2words(116331, lang="tr", to="ordinal"), u"yüzonaltıbinüçyüzotuzbirinci"
        )
        self.assertEqual(
            num2words(116330, lang="tr", to="ordinal"), u"yüzonaltıbinüçyüzotuzuncu"
        )
        self.assertEqual(num2words(100000, lang="tr", to="ordinal"), u"yüzbininci")
        self.assertEqual(num2words(501000, lang="tr", to="ordinal"), u"beşyüzbirbininci")
        self.assertEqual(
            num2words(1000111, lang="tr", to="ordinal"), u"birmilyonyüzonbirinci"
        )
        self.assertEqual(
            num2words(111000111, lang="tr", to="ordinal"), u"yüzonbirmilyonyüzonbirinci"
        )
        self.assertEqual(
            num2words(111001111, lang="tr", to="ordinal"), u"yüzonbirmilyonbinyüzonbirinci"
        )
        self.assertEqual(
            num2words(111111111, lang="tr", to="ordinal"),
            u"yüzonbirmilyonyüzonbirbinyüzonbirinci"
        )
        self.assertEqual(num2words(100001000, lang="tr", to="ordinal"), u"yüzmilyonbininci")
        self.assertEqual(
            num2words(100001001, lang="tr", to="ordinal"), u"yüzmilyonbinbirinci"
        )
        self.assertEqual(
            num2words(100010000, lang="tr", to="ordinal"), u"yüzmilyononbininci"
        )
        self.assertEqual(
            num2words(100010001, lang="tr", to="ordinal"), u"yüzmilyononbinbirinci"
        )
        self.assertEqual(
            num2words(100011000, lang="tr", to="ordinal"), u"yüzmilyononbirbininci"
        )
        self.assertEqual(
            num2words(100011001, lang="tr", to="ordinal"), u"yüzmilyononbirbinbirinci"
        )
        self.assertEqual(
            num2words(101011001, lang="tr", to="ordinal"), u"yüzbirmilyononbirbinbirinci"
        )
        self.assertEqual(
            num2words(101011010, lang="tr", to="ordinal"), u"yüzbirmilyononbirbinonuncu"
        )
        self.assertEqual(
            num2words(1101011010, lang="tr", to="ordinal"),
            u"birmilyaryüzbirmilyononbirbinonuncu"
        )
        self.assertEqual(
            num2words(101101011010, lang="tr", to="ordinal"),
            u"yüzbirmilyaryüzbirmilyononbirbinonuncu"
        )
        self.assertEqual(
            num2words(1000000000001, lang="tr", to="ordinal"), u"birtrilyonbirinci"
        )

        self.assertEqual(num2words(1, lang="tr", to="cardinal"), u"bir")
        self.assertEqual(num2words(2, lang="tr", to="cardinal"), u"iki")
        self.assertEqual(num2words(9, lang="tr", to="cardinal"), u"dokuz")
        self.assertEqual(num2words(10, lang="tr", to="cardinal"), u"on")
        self.assertEqual(num2words(11, lang="tr", to="cardinal"), u"onbir")
        self.assertEqual(num2words(44, lang="tr", to="cardinal"), u"kırkdört")
        self.assertEqual(num2words(100, lang="tr", to="cardinal"), u"yüz")
        self.assertEqual(num2words(101, lang="tr", to="cardinal"), u"yüzbir")
        self.assertEqual(num2words(103, lang="tr", to="cardinal"), u"yüzüç")
        self.assertEqual(num2words(110, lang="tr", to="cardinal"), u"yüzon")
        self.assertEqual(num2words(111, lang="tr", to="cardinal"), u"yüzonbir")
        self.assertEqual(num2words(1000, lang="tr", to="cardinal"), u"bin")
        self.assertEqual(num2words(1001, lang="tr", to="cardinal"), u"binbir")
        self.assertEqual(num2words(1010, lang="tr", to="cardinal"), u"binon")
        self.assertEqual(num2words(1011, lang="tr", to="cardinal"), u"binonbir")
        self.assertEqual(num2words(1100, lang="tr", to="cardinal"), u"binyüz")
        self.assertEqual(num2words(1110, lang="tr", to="cardinal"), u"binyüzon")
        self.assertEqual(num2words(2341, lang="tr", to="cardinal"), u"ikibinüçyüzkırkbir")
        self.assertEqual(num2words(10000, lang="tr", to="cardinal"), u"onbin")
        self.assertEqual(num2words(10010, lang="tr", to="cardinal"), u"onbinon")
        self.assertEqual(num2words(10100, lang="tr", to="cardinal"), u"onbinyüz")
        self.assertEqual(num2words(10110, lang="tr", to="cardinal"), u"onbinyüzon")
        self.assertEqual(num2words(11000, lang="tr", to="cardinal"), u"onbirbin")
        self.assertEqual(num2words(35000, lang="tr", to="cardinal"), u"otuzbeşbin")
        self.assertEqual(
            num2words(116331, lang="tr", to="cardinal"), u"yüzonaltıbinüçyüzotuzbir"
        )
        self.assertEqual(
            num2words(116330, lang="tr", to="cardinal"), u"yüzonaltıbinüçyüzotuz"
        )
        self.assertEqual(num2words(500000, lang="tr", to="cardinal"), u"beşyüzbin")
        self.assertEqual(num2words(501000, lang="tr", to="cardinal"), u"beşyüzbirbin")
        self.assertEqual(num2words(1000111, lang="tr", to="cardinal"), u"birmilyonyüzonbir")
        self.assertEqual(
            num2words(111000111, lang="tr", to="cardinal"), u"yüzonbirmilyonyüzonbir"
        )
        self.assertEqual(
            num2words(111001111, lang="tr", to="cardinal"), u"yüzonbirmilyonbinyüzonbir"
        )
        self.assertEqual(
            num2words(111111111, lang="tr", to="cardinal"),
            u"yüzonbirmilyonyüzonbirbinyüzonbir"
        )
        self.assertEqual(num2words(100001000, lang="tr", to="cardinal"), u"yüzmilyonbin")
        self.assertEqual(num2words(100001001, lang="tr", to="cardinal"), u"yüzmilyonbinbir")
        self.assertEqual(num2words(100010000, lang="tr", to="cardinal"), u"yüzmilyononbin")
        self.assertEqual(
            num2words(100010001, lang="tr", to="cardinal"), u"yüzmilyononbinbir"
        )
        self.assertEqual(
            num2words(100011000, lang="tr", to="cardinal"), u"yüzmilyononbirbin"
        )
        self.assertEqual(
            num2words(100011001, lang="tr", to="cardinal"), u"yüzmilyononbirbinbir"
        )
        self.assertEqual(
            num2words(101011001, lang="tr", to="cardinal"), u"yüzbirmilyononbirbinbir"
        )
        self.assertEqual(
            num2words(101011010, lang="tr", to="cardinal"), u"yüzbirmilyononbirbinon"
        )
        self.assertEqual(
            num2words(1101011010, lang="tr", to="cardinal"),
            u"birmilyaryüzbirmilyononbirbinon"
        )
        self.assertEqual(
            num2words(101101011010, lang="tr", to="cardinal"),
            u"yüzbirmilyaryüzbirmilyononbirbinon"
        )
        self.assertEqual(
            num2words(1000000000001, lang="tr", to="cardinal"), u"birtrilyonbir"
        )
        self.assertEqual(num2words(0.01, lang="tr", to="cardinal"), u"sıfırvirgülbir")
        self.assertEqual(num2words(0.1, lang="tr", to="cardinal"), u"sıfırvirgülon")
        self.assertEqual(num2words(0.21, lang="tr", to="cardinal"), u"sıfırvirgülyirmibir")
        self.assertEqual(num2words(1.01, lang="tr", to="cardinal"), u"birvirgülbir")
        self.assertEqual(num2words(1.1, lang="tr", to="cardinal"), u"birvirgülon")
        self.assertEqual(num2words(1.21, lang="tr", to="cardinal"), u"birvirgülyirmibir")
        self.assertEqual(
            num2words(101101011010.02, lang="tr", to="cardinal"),
            u"yüzbirmilyaryüzbirmilyononbirbinonvirgüliki"
        )
        self.assertEqual(
            num2words(101101011010.2, lang="tr", to="cardinal"),
            u"yüzbirmilyaryüzbirmilyononbirbinonvirgülyirmi"
        )
        self.assertEqual(num2words(0, lang="tr", to="currency"), u'sıfırlira')
        self.assertEqual(num2words(1.1, lang="tr", to="currency"), u'birliraonkuruş')
        self.assertEqual(num2words(1.2, lang="tr", to="ordinal"), u'')
        self.assertEqual(num2words(1.3, lang="tr", to="ordinal"), u'')
        self.assertEqual(num2words(2000, lang="tr", to="currency"), u'ikibinlira')
        self.assertEqual(num2words(3000, lang="tr", to="ordinal"), u'üçbininci')
        self.assertEqual(num2words(110000, lang="tr", to="currency"), u'yüzonbinlira')
        self.assertEqual(num2words(120000, lang="tr", to="ordinal"), u'yüzyirmibininci')
        self.assertEqual(num2words(1002000, lang="tr", to="currency"), u'birmilyonikibinlira')
        self.assertEqual(num2words(1002001, lang="tr", to="currency"), u'birmilyonikibinbirlira')
        self.assertEqual(num2words(1002002, lang="tr", to="ordinal"), u'birmilyonikibinikinci')
        self.assertEqual(num2words(1003000, lang="tr", to="ordinal"), u'birmilyonüçbininci')
        self.assertEqual(num2words(1100000, lang="tr", to="currency"), u'birmilyonyüzbin')
        self.assertEqual(num2words(1200000, lang="tr", to="ordinal"), u'birmilyonikiyüzbininci')
