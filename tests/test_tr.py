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
            {"number": 0, "lang": "tr", "to": "currency", "response": u"bedelsiz"},
            {"number": 1.1, "lang": "tr", "to": "currency", "response": u"birliraonkuruş"},
            {"number": 2000, "lang": "tr", "to": "currency", "response": u"ikibinlira"},
            {"number": 110000, "lang": "tr", "to": "currency", "response": u"yüzonbinlira"},
            {"number": 1002000, "lang": "tr", "to": "currency", "response": u"birmilyonikibinlira"},
            {"number": 1002001, "lang": "tr", "to": "currency", "response": u"birmilyonikibinbirlira"},
            {"number": 1100000, "lang": "tr", "to": "currency", "response": u"birmilyonyüzbinlira"},
            {"number": 1, "lang": "tr", "to": "ordinal", "response": u"birinci"},
            {"number": 2, "lang": "tr", "to": "ordinal", "response": u"ikinci"},
            {"number": 9, "lang": "tr", "to": "ordinal", "response": u"dokuzuncu"},
            {"number": 10, "lang": "tr", "to": "ordinal", "response": u"onuncu"},
            {"number": 11, "lang": "tr", "to": "ordinal", "response": u"onbirinci"},
            {"number": 44, "lang": "tr", "to": "ordinal", "response": u"kırkdördüncü"},
            {"number": 100, "lang": "tr", "to": "ordinal", "response": u"yüzüncü"},
            {"number": 101, "lang": "tr", "to": "ordinal", "response": u"yüzbirinci"},
            {"number": 103, "lang": "tr", "to": "ordinal", "response": u"yüzüçüncü"},
            {"number": 110, "lang": "tr", "to": "ordinal", "response": u"yüzonuncu"},
            {"number": 111, "lang": "tr", "to": "ordinal", "response": u"yüzonbirinci"},
            {"number": 1000, "lang": "tr", "to": "ordinal", "response": u"bininci"},
            {"number": 1001, "lang": "tr", "to": "ordinal", "response": u"binbirinci"},
            {"number": 1010, "lang": "tr", "to": "ordinal", "response": u"binonuncu"},
            {"number": 1011, "lang": "tr", "to": "ordinal", "response": u"binonbirinci"},
            {"number": 1100, "lang": "tr", "to": "ordinal", "response": u"binyüzüncü"},
            {"number": 1110, "lang": "tr", "to": "ordinal", "response": u"binyüzonuncu"},
            {"number": 2341, "lang": "tr", "to": "ordinal", "response": u"ikibinüçyüzkırkbirinci"},
            {"number": 10000, "lang": "tr", "to": "ordinal", "response": u"onbininci"},
            {"number": 10010, "lang": "tr", "to": "ordinal", "response": u"onbinonuncu"},
            {"number": 10100, "lang": "tr", "to": "ordinal", "response": u"onbinyüzüncü"},
            {"number": 10110, "lang": "tr", "to": "ordinal", "response": u"onbinyüzonuncu"},
            {"number": 11000, "lang": "tr", "to": "ordinal", "response": u"onbirbininci"},
            {"number": 35000, "lang": "tr", "to": "ordinal", "response": u"otuzbeşbininci"},
            {"number": 116331, "lang": "tr", "to": "ordinal", "response": u"yüzonaltıbinüçyüzotuzbirinci"},
            {"number": 116330, "lang": "tr", "to": "ordinal", "response": u"yüzonaltıbinüçyüzotuzuncu"},
            {"number": 100000, "lang": "tr", "to": "ordinal", "response": u"yüzbininci"},
            {"number": 501000, "lang": "tr", "to": "ordinal", "response": u"beşyüzbirbininci"},
            {"number": 1000111, "lang": "tr", "to": "ordinal", "response": u"birmilyonyüzonbirinci"},
            {"number": 111000111, "lang": "tr", "to": "ordinal", "response": u"yüzonbirmilyonyüzonbirinci"},
            {"number": 111001111, "lang": "tr", "to": "ordinal", "response": u"yüzonbirmilyonbinyüzonbirinci"},
            {"number": 111111111, "lang": "tr", "to": "ordinal", "response": u"yüzonbirmilyonyüzonbirbinyüzonbirinci"},
            {"number": 100001000, "lang": "tr", "to": "ordinal", "response": u"yüzmilyonbininci"},
            {"number": 100001001, "lang": "tr", "to": "ordinal", "response": u"yüzmilyonbinbirinci"},
            {"number": 100010000, "lang": "tr", "to": "ordinal", "response": u"yüzmilyononbininci"},
            {"number": 100010001, "lang": "tr", "to": "ordinal", "response": u"yüzmilyononbinbirinci"},
            {"number": 100011000, "lang": "tr", "to": "ordinal", "response": u"yüzmilyononbirbininci"},
            {"number": 100011001, "lang": "tr", "to": "ordinal", "response": u"yüzmilyononbirbinbirinci"},
            {"number": 101011001, "lang": "tr", "to": "ordinal", "response": u"yüzbirmilyononbirbinbirinci"},
            {"number": 101011010, "lang": "tr", "to": "ordinal", "response": u"yüzbirmilyononbirbinonuncu"},
            {"number": 1101011010, "lang": "tr", "to": "ordinal", "response": u"birmilyaryüzbirmilyononbirbinonuncu"},
            {"number": 101101011010, "lang": "tr", "to": "ordinal",
             "response": u"yüzbirmilyaryüzbirmilyononbirbinonuncu"},
            {"number": 1000000000001, "lang": "tr", "to": "ordinal", "response": u"birtrilyonbirinci"},
            {"number": 1.2, "lang": "tr", "to": "ordinal", "response": u""},
            {"number": 1.3, "lang": "tr", "to": "ordinal", "response": u""},
            {"number": 3000, "lang": "tr", "to": "ordinal", "response": u"üçbininci"},
            {"number": 120000, "lang": "tr", "to": "ordinal", "response": u"yüzyirmibininci"},
            {"number": 1002002, "lang": "tr", "to": "ordinal", "response": u"birmilyonikibinikinci"},
            {"number": 1003000, "lang": "tr", "to": "ordinal", "response": u"birmilyonüçbininci"},
            {"number": 1200000, "lang": "tr", "to": "ordinal", "response": u"birmilyonikiyüzbininci"},
            {"number": 1, "lang": "tr", "to": "cardinal", "response": u"bir"},
            {"number": 2, "lang": "tr", "to": "cardinal", "response": u"iki"},
            {"number": 9, "lang": "tr", "to": "cardinal", "response": u"dokuz"},
            {"number": 10, "lang": "tr", "to": "cardinal", "response": u"on"},
            {"number": 11, "lang": "tr", "to": "cardinal", "response": u"onbir"},
            {"number": 44, "lang": "tr", "to": "cardinal", "response": u"kırkdört"},
            {"number": 100, "lang": "tr", "to": "cardinal", "response": u"yüz"},
            {"number": 101, "lang": "tr", "to": "cardinal", "response": u"yüzbir"},
            {"number": 103, "lang": "tr", "to": "cardinal", "response": u"yüzüç"},
            {"number": 110, "lang": "tr", "to": "cardinal", "response": u"yüzon"},
            {"number": 111, "lang": "tr", "to": "cardinal", "response": u"yüzonbir"},
            {"number": 1000, "lang": "tr", "to": "cardinal", "response": u"bin"},
            {"number": 1001, "lang": "tr", "to": "cardinal", "response": u"binbir"},
            {"number": 1010, "lang": "tr", "to": "cardinal", "response": u"binon"},
            {"number": 1011, "lang": "tr", "to": "cardinal", "response": u"binonbir"},
            {"number": 1100, "lang": "tr", "to": "cardinal", "response": u"binyüz"},
            {"number": 1110, "lang": "tr", "to": "cardinal", "response": u"binyüzon"},
            {"number": 2341, "lang": "tr", "to": "cardinal", "response": u"ikibinüçyüzkırkbir"},
            {"number": 10000, "lang": "tr", "to": "cardinal", "response": u"onbin"},
            {"number": 10010, "lang": "tr", "to": "cardinal", "response": u"onbinon"},
            {"number": 10100, "lang": "tr", "to": "cardinal", "response": u"onbinyüz"},
            {"number": 10110, "lang": "tr", "to": "cardinal", "response": u"onbinyüzon"},
            {"number": 11000, "lang": "tr", "to": "cardinal", "response": u"onbirbin"},
            {"number": 35000, "lang": "tr", "to": "cardinal", "response": u"otuzbeşbin"},
            {"number": 116331, "lang": "tr", "to": "cardinal", "response": u"yüzonaltıbinüçyüzotuzbir"},
            {"number": 116330, "lang": "tr", "to": "cardinal", "response": u"yüzonaltıbinüçyüzotuz"},
            {"number": 500000, "lang": "tr", "to": "cardinal", "response": u"beşyüzbin"},
            {"number": 501000, "lang": "tr", "to": "cardinal", "response": u"beşyüzbirbin"},
            {"number": 1000111, "lang": "tr", "to": "cardinal", "response": u"birmilyonyüzonbir"},
            {"number": 111000111, "lang": "tr", "to": "cardinal", "response": u"yüzonbirmilyonyüzonbir"},
            {"number": 111001111, "lang": "tr", "to": "cardinal", "response": u"yüzonbirmilyonbinyüzonbir"},
            {"number": 111111111, "lang": "tr", "to": "cardinal", "response": u"yüzonbirmilyonyüzonbirbinyüzonbir"},
            {"number": 100001000, "lang": "tr", "to": "cardinal", "response": u"yüzmilyonbin"},
            {"number": 100001001, "lang": "tr", "to": "cardinal", "response": u"yüzmilyonbinbir"},
            {"number": 100010000, "lang": "tr", "to": "cardinal", "response": u"yüzmilyononbin"},
            {"number": 100010001, "lang": "tr", "to": "cardinal", "response": u"yüzmilyononbinbir"},
            {"number": 100011000, "lang": "tr", "to": "cardinal", "response": u"yüzmilyononbirbin"},
            {"number": 100011001, "lang": "tr", "to": "cardinal", "response": u"yüzmilyononbirbinbir"},
            {"number": 101011001, "lang": "tr", "to": "cardinal", "response": u"yüzbirmilyononbirbinbir"},
            {"number": 101011010, "lang": "tr", "to": "cardinal", "response": u"yüzbirmilyononbirbinon"},
            {"number": 1101011010, "lang": "tr", "to": "cardinal", "response": u"birmilyaryüzbirmilyononbirbinon"},
            {"number": 101101011010, "lang": "tr", "to": "cardinal", "response": u"yüzbirmilyaryüzbirmilyononbirbinon"},
            {"number": 100001001, "lang": "tr", "to": "cardinal", "response": u"yüzmilyonbinbir"},
            {"number": 1000000000001, "lang": "tr", "to": "cardinal", "response": u"yüzmilyonbinbir"},
            {"number": 0.01, "lang": "tr", "to": "cardinal", "response": u"sıfırvirgülbir"},
            {"number": 0.21, "lang": "tr", "to": "cardinal", "response": u"sıfırvirgülyirmibir"},
            {"number": 0.1, "lang": "tr", "to": "cardinal", "response": u"sıfırvirgülon"},
            {"number": 1.01, "lang": "tr", "to": "cardinal", "response": u"birvirgülbir"},
            {"number": 1.1, "lang": "tr", "to": "cardinal", "response": u"birvirgülon"},
            {"number": 1.21, "lang": "tr", "to": "cardinal", "response": u"birvirgülyirmibir"},
            {"number": 101101011010.02, "lang": "tr", "to": "cardinal",
             "response": u"yüzbirmilyaryüzbirmilyononbirbinonvirgüliki"},
            {"number": 101101011010.2, "lang": "tr", "to": "cardinal",
             "response": u"yüzbirmilyaryüzbirmilyononbirbinonvirgülyirmi"},
        ]

        for casedata in testcases:
            self.assertEqual(num2words(casedata.number, lang=casedata.lang, to=casedata.to), casedata.response)
