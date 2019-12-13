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

        testcases = [
            {"test": 0, "lang": "tr", "to": "currency", "expected": u"bedelsiz"},
            {"test": 1.1, "lang": "tr", "to": "currency", "expected": u"birliraonkuruş"},
            {"test": 2000, "lang": "tr", "to": "currency", "expected": u"ikibinlira"},
            {"test": 110000, "lang": "tr", "to": "currency", "expected": u"yüzonbinlira"},
            {"test": 1002000, "lang": "tr", "to": "currency", "expected": u"birmilyonikibinlira"},
            {"test": 1002001, "lang": "tr", "to": "currency", "expected": u"birmilyonikibinbirlira"},
            {"test": 1100000, "lang": "tr", "to": "currency", "expected": u"birmilyonyüzbinlira"},
            {"test": 1, "lang": "tr", "to": "ordinal", "expected": u"birinci"},
            {"test": 2, "lang": "tr", "to": "ordinal", "expected": u"ikinci"},
            {"test": 9, "lang": "tr", "to": "ordinal", "expected": u"dokuzuncu"},
            {"test": 10, "lang": "tr", "to": "ordinal", "expected": u"onuncu"},
            {"test": 11, "lang": "tr", "to": "ordinal", "expected": u"onbirinci"},
            {"test": 44, "lang": "tr", "to": "ordinal", "expected": u"kırkdördüncü"},
            {"test": 100, "lang": "tr", "to": "ordinal", "expected": u"yüzüncü"},
            {"test": 101, "lang": "tr", "to": "ordinal", "expected": u"yüzbirinci"},
            {"test": 103, "lang": "tr", "to": "ordinal", "expected": u"yüzüçüncü"},
            {"test": 110, "lang": "tr", "to": "ordinal", "expected": u"yüzonuncu"},
            {"test": 111, "lang": "tr", "to": "ordinal", "expected": u"yüzonbirinci"},
            {"test": 1000, "lang": "tr", "to": "ordinal", "expected": u"bininci"},
            {"test": 1001, "lang": "tr", "to": "ordinal", "expected": u"binbirinci"},
            {"test": 1010, "lang": "tr", "to": "ordinal", "expected": u"binonuncu"},
            {"test": 1011, "lang": "tr", "to": "ordinal", "expected": u"binonbirinci"},
            {"test": 1100, "lang": "tr", "to": "ordinal", "expected": u"binyüzüncü"},
            {"test": 1110, "lang": "tr", "to": "ordinal", "expected": u"binyüzonuncu"},
            {"test": 2341, "lang": "tr", "to": "ordinal", "expected": u"ikibinüçyüzkırkbirinci"},
            {"test": 10000, "lang": "tr", "to": "ordinal", "expected": u"onbininci"},
            {"test": 10010, "lang": "tr", "to": "ordinal", "expected": u"onbinonuncu"},
            {"test": 10100, "lang": "tr", "to": "ordinal", "expected": u"onbinyüzüncü"},
            {"test": 10110, "lang": "tr", "to": "ordinal", "expected": u"onbinyüzonuncu"},
            {"test": 11000, "lang": "tr", "to": "ordinal", "expected": u"onbirbininci"},
            {"test": 35000, "lang": "tr", "to": "ordinal", "expected": u"otuzbeşbininci"},
            {"test": 116331, "lang": "tr", "to": "ordinal", "expected": u"yüzonaltıbinüçyüzotuzbirinci"},
            {"test": 116330, "lang": "tr", "to": "ordinal", "expected": u"yüzonaltıbinüçyüzotuzuncu"},
            {"test": 100000, "lang": "tr", "to": "ordinal", "expected": u"yüzbininci"},
            {"test": 501000, "lang": "tr", "to": "ordinal", "expected": u"beşyüzbirbininci"},
            {"test": 1000111, "lang": "tr", "to": "ordinal", "expected": u"birmilyonyüzonbirinci"},
            {"test": 111000111, "lang": "tr", "to": "ordinal", "expected": u"yüzonbirmilyonyüzonbirinci"},
            {"test": 111001111, "lang": "tr", "to": "ordinal", "expected": u"yüzonbirmilyonbinyüzonbirinci"},
            {"test": 111111111, "lang": "tr", "to": "ordinal", "expected": u"yüzonbirmilyonyüzonbirbinyüzonbirinci"},
            {"test": 100001000, "lang": "tr", "to": "ordinal", "expected": u"yüzmilyonbininci"},
            {"test": 100001001, "lang": "tr", "to": "ordinal", "expected": u"yüzmilyonbinbirinci"},
            {"test": 100010000, "lang": "tr", "to": "ordinal", "expected": u"yüzmilyononbininci"},
            {"test": 100010001, "lang": "tr", "to": "ordinal", "expected": u"yüzmilyononbinbirinci"},
            {"test": 100011000, "lang": "tr", "to": "ordinal", "expected": u"yüzmilyononbirbininci"},
            {"test": 100011001, "lang": "tr", "to": "ordinal", "expected": u"yüzmilyononbirbinbirinci"},
            {"test": 101011001, "lang": "tr", "to": "ordinal", "expected": u"yüzbirmilyononbirbinbirinci"},
            {"test": 101011010, "lang": "tr", "to": "ordinal", "expected": u"yüzbirmilyononbirbinonuncu"},
            {"test": 1101011010, "lang": "tr", "to": "ordinal", "expected": u"birmilyaryüzbirmilyononbirbinonuncu"},
            {"test": 101101011010, "lang": "tr", "to": "ordinal",
             "response": u"yüzbirmilyaryüzbirmilyononbirbinonuncu"},
            {"test": 1000000000001, "lang": "tr", "to": "ordinal", "expected": u"birtrilyonbirinci"},
            {"test": 1.2, "lang": "tr", "to": "ordinal", "expected": u""},
            {"test": 1.3, "lang": "tr", "to": "ordinal", "expected": u""},
            {"test": 3000, "lang": "tr", "to": "ordinal", "expected": u"üçbininci"},
            {"test": 120000, "lang": "tr", "to": "ordinal", "expected": u"yüzyirmibininci"},
            {"test": 1002002, "lang": "tr", "to": "ordinal", "expected": u"birmilyonikibinikinci"},
            {"test": 1003000, "lang": "tr", "to": "ordinal", "expected": u"birmilyonüçbininci"},
            {"test": 1200000, "lang": "tr", "to": "ordinal", "expected": u"birmilyonikiyüzbininci"},
            {"test": 1, "lang": "tr", "to": "cardinal", "expected": u"bir"},
            {"test": 2, "lang": "tr", "to": "cardinal", "expected": u"iki"},
            {"test": 9, "lang": "tr", "to": "cardinal", "expected": u"dokuz"},
            {"test": 10, "lang": "tr", "to": "cardinal", "expected": u"on"},
            {"test": 11, "lang": "tr", "to": "cardinal", "expected": u"onbir"},
            {"test": 44, "lang": "tr", "to": "cardinal", "expected": u"kırkdört"},
            {"test": 100, "lang": "tr", "to": "cardinal", "expected": u"yüz"},
            {"test": 101, "lang": "tr", "to": "cardinal", "expected": u"yüzbir"},
            {"test": 103, "lang": "tr", "to": "cardinal", "expected": u"yüzüç"},
            {"test": 110, "lang": "tr", "to": "cardinal", "expected": u"yüzon"},
            {"test": 111, "lang": "tr", "to": "cardinal", "expected": u"yüzonbir"},
            {"test": 1000, "lang": "tr", "to": "cardinal", "expected": u"bin"},
            {"test": 1001, "lang": "tr", "to": "cardinal", "expected": u"binbir"},
            {"test": 1010, "lang": "tr", "to": "cardinal", "expected": u"binon"},
            {"test": 1011, "lang": "tr", "to": "cardinal", "expected": u"binonbir"},
            {"test": 1100, "lang": "tr", "to": "cardinal", "expected": u"binyüz"},
            {"test": 1110, "lang": "tr", "to": "cardinal", "expected": u"binyüzon"},
            {"test": 2341, "lang": "tr", "to": "cardinal", "expected": u"ikibinüçyüzkırkbir"},
            {"test": 10000, "lang": "tr", "to": "cardinal", "expected": u"onbin"},
            {"test": 10010, "lang": "tr", "to": "cardinal", "expected": u"onbinon"},
            {"test": 10100, "lang": "tr", "to": "cardinal", "expected": u"onbinyüz"},
            {"test": 10110, "lang": "tr", "to": "cardinal", "expected": u"onbinyüzon"},
            {"test": 11000, "lang": "tr", "to": "cardinal", "expected": u"onbirbin"},
            {"test": 35000, "lang": "tr", "to": "cardinal", "expected": u"otuzbeşbin"},
            {"test": 116331, "lang": "tr", "to": "cardinal", "expected": u"yüzonaltıbinüçyüzotuzbir"},
            {"test": 116330, "lang": "tr", "to": "cardinal", "expected": u"yüzonaltıbinüçyüzotuz"},
            {"test": 500000, "lang": "tr", "to": "cardinal", "expected": u"beşyüzbin"},
            {"test": 501000, "lang": "tr", "to": "cardinal", "expected": u"beşyüzbirbin"},
            {"test": 1000111, "lang": "tr", "to": "cardinal", "expected": u"birmilyonyüzonbir"},
            {"test": 111000111, "lang": "tr", "to": "cardinal", "expected": u"yüzonbirmilyonyüzonbir"},
            {"test": 111001111, "lang": "tr", "to": "cardinal", "expected": u"yüzonbirmilyonbinyüzonbir"},
            {"test": 111111111, "lang": "tr", "to": "cardinal", "expected": u"yüzonbirmilyonyüzonbirbinyüzonbir"},
            {"test": 100001000, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyonbin"},
            {"test": 100001001, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyonbinbir"},
            {"test": 100010000, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyononbin"},
            {"test": 100010001, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyononbinbir"},
            {"test": 100011000, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyononbirbin"},
            {"test": 100011001, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyononbirbinbir"},
            {"test": 101011001, "lang": "tr", "to": "cardinal", "expected": u"yüzbirmilyononbirbinbir"},
            {"test": 101011010, "lang": "tr", "to": "cardinal", "expected": u"yüzbirmilyononbirbinon"},
            {"test": 1101011010, "lang": "tr", "to": "cardinal", "expected": u"birmilyaryüzbirmilyononbirbinon"},
            {"test": 101101011010, "lang": "tr", "to": "cardinal", "expected": u"yüzbirmilyaryüzbirmilyononbirbinon"},
            {"test": 100001001, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyonbinbir"},
            {"test": 1000000000001, "lang": "tr", "to": "cardinal", "expected": u"yüzmilyonbinbir"},
            {"test": 0.01, "lang": "tr", "to": "cardinal", "expected": u"sıfırvirgülbir"},
            {"test": 0.21, "lang": "tr", "to": "cardinal", "expected": u"sıfırvirgülyirmibir"},
            {"test": 0.1, "lang": "tr", "to": "cardinal", "expected": u"sıfırvirgülon"},
            {"test": 1.01, "lang": "tr", "to": "cardinal", "expected": u"birvirgülbir"},
            {"test": 1.1, "lang": "tr", "to": "cardinal", "expected": u"birvirgülon"},
            {"test": 1.21, "lang": "tr", "to": "cardinal", "expected": u"birvirgülyirmibir"},
            {"test": 101101011010.02, "lang": "tr", "to": "cardinal",
             "response": u"yüzbirmilyaryüzbirmilyononbirbinonvirgüliki"},
            {"test": 101101011010.2, "lang": "tr", "to": "cardinal",
             "response": u"yüzbirmilyaryüzbirmilyononbirbinonvirgülyirmi"}
        ]

        for casedata in testcases:
            self.assertEqual(num2words(casedata.test, lang=casedata.lang, to=casedata.to), casedata.expected)
