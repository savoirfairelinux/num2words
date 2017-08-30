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
    def test_and_join_100_tr(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/8

        self.assertEqual(num2words(1, True, "tr"), "birinci")
        self.assertEqual(num2words(2, True, "tr"), "ikinci")
        self.assertEqual(num2words(9, True, "tr"), "dokuzuncu")
        self.assertEqual(num2words(10, True, "tr"), "onuncu")
        self.assertEqual(num2words(11, True, "tr"), "onbirinci")
        self.assertEqual(num2words(44, True, "tr"), "kırkdördüncü")
        self.assertEqual(num2words(100, True, "tr"), "yüzüncü")
        self.assertEqual(num2words(101, True, "tr"), "yüzbirinci")
        self.assertEqual(num2words(103, True, "tr"), "yüzüçüncü")
        self.assertEqual(num2words(110, True, "tr"), "yüzonuncu")
        self.assertEqual(num2words(1000, True, "tr"), "bininci")
        self.assertEqual(num2words(1001, True, "tr"), "binbirinci")
        self.assertEqual(num2words(10000, True, "tr"), "onbininci")
        self.assertEqual(num2words(10100, True, "tr"), "onbinyüzüncü")
        self.assertEqual(num2words(11000, True, "tr"), "onbirbininci")
        self.assertEqual(num2words(35000, True, "tr"), "otuzbeşbininci")
        self.assertEqual(num2words(116331, True, "tr"), "yüzonaltıbinüçyüzotuzbirinci")
        self.assertEqual(num2words(116330, True, "tr"), "yüzonaltıbinüçyüzotuzuncu")
        self.assertEqual(num2words(100000, True, "tr"), "yüzbininci")
        self.assertEqual(num2words(501000, True, "tr"), "beşyüzbirbininci")
        self.assertEqual(num2words(1000111, True, "tr"), "birmilyonyüzonbirinci")
        self.assertEqual(num2words(111000111, True, "tr"), "yüzonbirmilyonyüzonbirinci")
        self.assertEqual(num2words(111001111, True, "tr"), "yüzonbirmilyonbinyüzonbirinci")
        self.assertEqual(num2words(111111111, True, "tr"), "yüzonbirmilyonyüzonbirbinyüzonbirinci")
        self.assertEqual(num2words(100001000, True, "tr"), "yüzmilyonbininci")
        self.assertEqual(num2words(100001001, True, "tr"), "yüzmilyonbinbirinci")
        self.assertEqual(num2words(100010000, True, "tr"), "yüzmilyononbininci")
        self.assertEqual(num2words(100010001, True, "tr"), "yüzmilyononbinbirinci")
        self.assertEqual(num2words(100011000, True, "tr"), "yüzmilyononbirbininci")
        self.assertEqual(num2words(100011001, True, "tr"), "yüzmilyononbirbinbirinci")
        self.assertEqual(num2words(101011001, True, "tr"), "yüzbirmilyononbirbinbirinci")
        self.assertEqual(num2words(101011010, True, "tr"), "yüzbirmilyononbirbinonuncu")
        self.assertEqual(num2words(1101011010, True, "tr"), "birmilyaryüzbirmilyononbirbinonuncu")
        self.assertEqual(num2words(101101011010, True, "tr"), "yüzbirmilyaryüzbirmilyononbirbinonuncu")
        self.assertEqual(num2words(1000000000001, True, "tr"), "birtrilyonbirinci")

        self.assertEqual(num2words(1, False, "tr"), "bir")
        self.assertEqual(num2words(2, False, "tr"), "iki")
        self.assertEqual(num2words(9, False, "tr"), "dokuz")
        self.assertEqual(num2words(10, False, "tr"), "on")
        self.assertEqual(num2words(11, False, "tr"), "onbir")
        self.assertEqual(num2words(44, False, "tr"), "kırkdört")
        self.assertEqual(num2words(100, False, "tr"), "yüz")
        self.assertEqual(num2words(101, False, "tr"), "yüzbir")
        self.assertEqual(num2words(103, False, "tr"), "yüzüç")
        self.assertEqual(num2words(110, False, "tr"), "yüzon")
        self.assertEqual(num2words(1000, False, "tr"), "bin")
        self.assertEqual(num2words(1001, False, "tr"), "binbir")
        self.assertEqual(num2words(10000, False, "tr"), "onbin")
        self.assertEqual(num2words(10100, False, "tr"), "onbinyüz")
        self.assertEqual(num2words(11000, False, "tr"), "onbirbin")
        self.assertEqual(num2words(35000, False, "tr"), "otuzbeşbin")
        self.assertEqual(num2words(116331, False, "tr"), "yüzonaltıbinüçyüzotuzbir")
        self.assertEqual(num2words(116330, False, "tr"), "yüzonaltıbinüçyüzotuz")
        self.assertEqual(num2words(500000, False, "tr"), "beşyüzbin")
        self.assertEqual(num2words(501000, False, "tr"), "beşyüzbirbin")
        self.assertEqual(num2words(1000111, False, "tr"), "birmilyonyüzonbir")
        self.assertEqual(num2words(111000111, False, "tr"), "yüzonbirmilyonyüzonbir")
        self.assertEqual(num2words(111001111, False, "tr"), "yüzonbirmilyonbinyüzonbir")
        self.assertEqual(num2words(111111111, False, "tr"), "yüzonbirmilyonyüzonbirbinyüzonbir")
        self.assertEqual(num2words(100001000, False, "tr"), "yüzmilyonbin")
        self.assertEqual(num2words(100001001, False, "tr"), "yüzmilyonbinbir")
        self.assertEqual(num2words(100010000, False, "tr"), "yüzmilyononbin")
        self.assertEqual(num2words(100010001, False, "tr"), "yüzmilyononbinbir")
        self.assertEqual(num2words(100011000, False, "tr"), "yüzmilyononbirbin")
        self.assertEqual(num2words(100011001, False, "tr"), "yüzmilyononbirbinbir")
        self.assertEqual(num2words(101011001, False, "tr"), "yüzbirmilyononbirbinbir")
        self.assertEqual(num2words(101011010, False, "tr"), "yüzbirmilyononbirbinon")
        self.assertEqual(num2words(1101011010, False, "tr"), "birmilyaryüzbirmilyononbirbinon")
        self.assertEqual(num2words(101101011010, False, "tr"), "yüzbirmilyaryüzbirmilyononbirbinon")
        self.assertEqual(num2words(1000000000001, False, "tr"), "birtrilyonbir")
        self.assertEqual(num2words(1.1, False, "tr"), "birvirgülon")
        self.assertEqual(num2words(1.21, False, "tr"), "birvirgülyirmibir")
        self.assertEqual(num2words(101101011010.02, False, "tr"), "yüzbirmilyaryüzbirmilyononbirbinonvirgüliki")
        self.assertEqual(num2words(101101011010.2, False, "tr"), "yüzbirmilyaryüzbirmilyononbirbinonvirgülyirmi")
