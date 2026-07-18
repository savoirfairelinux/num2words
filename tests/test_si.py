# -*- encoding: utf-8 -*-
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

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

# All expected forms verified by a native Sinhala speaker.
TEST_CASES_CARDINAL = (
    (0, "බින්දුව"),
    (1, "එක"),
    (2, "දෙක"),
    (3, "තුන"),
    (4, "හතර"),
    (5, "පහ"),
    (6, "හය"),
    (7, "හත"),
    (8, "අට"),
    (9, "නවය"),
    (10, "දහය"),
    (11, "එකොළහ"),
    (12, "දොළහ"),
    (13, "දහතුන"),
    (14, "දහහතර"),
    (15, "පහළොව"),
    (16, "දහසය"),
    (17, "දහහත"),
    (18, "දහඅට"),
    (19, "දහනවය"),
    (20, "විස්ස"),
    (21, "විසි එක"),
    (30, "තිහ"),
    (31, "තිස් එක"),
    (32, "තිස් දෙක"),
    (40, "හතළිහ"),
    (50, "පනහ"),
    (60, "හැට"),
    (70, "හැත්තෑව"),
    (80, "අසූව"),
    (90, "අනූව"),
    (99, "අනූ නවය"),
    (100, "සියය"),
    (122, "එකසිය විසි දෙක"),
    (200, "දෙසීය"),
    (205, "දෙසීය පහ"),
    (234, "දෙසීය තිස් හතර"),
    (250, "දෙසීය පනහ"),
    (400, "හාරසියය"),
    (543, "පන්සිය හතළිස් තුන"),
    (1000, "එක්දහස"),
    (1010, "එක්දහස් දහය"),
    (1250, "එක්දහස් දෙසීය පනහ"),
    (2000, "දෙදහස"),
    (4000, "හාරදහස"),
    (6543, "හයදහස් පන්සිය හතළිස් තුන"),
    (10000, "දසදහස"),
    (100000, "එක්ලක්ෂය"),
    (400000, "හාරලක්ෂය"),
    (1000000, "මිලියනය"),
    (2000000, "මිලියන දෙක"),
    (1000000000, "බිලියනය"),
    (-5, "සෘණ පහ"),
)

TEST_CASES_CARDINAL_FLOAT = (
    (3.14, "තුනයි දශම එකයි හතර"),
    (2.456, "දෙකයි දශම හතරයි පහයි හය"),
    (5.98762, "පහයි දශම නවයයි අටයි හතයි හයයි දෙක"),
)

TEST_CASES_ORDINAL = (
    (1, "පළමුවැනි"),
    (2, "දෙවැනි"),
    (3, "තුන්වැනි"),
    (4, "හතරවැනි"),
    (5, "පස්වැනි"),
    (10, "දහවැනි"),
    (20, "විසිවැනි"),
    (100, "සියවැනි"),
)


class Num2WordsSITest(TestCase):
    maxDiff = None

    def test_cardinal(self):
        for number, expected in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(number, lang="si"), expected)

    def test_cardinal_float(self):
        for number, expected in TEST_CASES_CARDINAL_FLOAT:
            self.assertEqual(num2words(number, lang="si"), expected)

    def test_ordinal(self):
        for number, expected in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(number, lang="si", to="ordinal"), expected
            )

    def test_ordinal_num(self):
        self.assertEqual(num2words(2, lang="si", to="ordinal_num"), "2වැනි")

    def test_currency(self):
        self.assertEqual(
            num2words(1250.50, lang="si", to="currency", currency="LKR"),
            "රුපියල් එක්දහස් දෙසීය පනහයි ශත පනහයි",
        )

    def test_year(self):
        self.assertEqual(
            num2words(1948, lang="si", to="year"),
            "එක්දහස් නවසිය හතළිස් අට",
        )

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words(10**12, lang="si")
