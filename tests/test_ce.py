# -*- coding: utf-8 -*-

# Copyright (c) 2023, Johannes Heinecke.  All Rights Reserved.

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

TEST_CASES_CARDINAL = [
    (1, "obl", "б", "цхьана"),
    (2, "comp", "в", "шиннал"),
    (3, "mat", "д", "кхааннах"),
    (4, "mat", "в", "веаннах"),
    (5, "abs", "й", "пхиъ"),
    (6, "dat", "д", "ялханна"),
    (7, "erg", "в", "ворхӀамма"),
    (8, "comp", "й", "бархӀаннал"),
    (9, "dat", "й", "иссанна"),
    (10, "erg", "б", "иттамма"),
    (11, "dat", "б", "цхьайттанна"),
    (12, "instr", "й", "шийттанца"),
    (13, "erg", "б", "кхойттамма"),
    (14, "all", "в", "вейттанга"),
    (15, "dat", "б", "пхийттанна"),
    (16, "dat", "й", "ялхиттанна"),
    (17, "dat", "в", "вуьрхӀиттанна"),
    (18, "attr", "й", "берхӀитта"),
    (19, "all", "й", "ткъайеснанга"),
    (20, "attr", "б", "ткъе"),
    (21, "all", "в", "ткъе цхаьнга"),
    (22, "obl", "в", "ткъе шина"),
    (23, "attr", "б", "ткъе кхо"),
    (24, "dat", "й", "ткъе йеанна"),
    (25, "attr", "й", "ткъе пхи"),
    (26, "abs", "б", "ткъе ялх"),
    (27, "abs", "в", "ткъе ворхӀ"),
    (28, "all", "б", "ткъе бархӀанга"),
    (29, "mat", "д", "ткъе иссаннах"),
    (30, "gen", "й", "ткъе иттаннан"),
    (31, "dat", "в", "ткъе цхьайттанна"),
    (32, "comp", "й", "ткъе шийттаннал"),
    (33, "instr", "в", "ткъе кхойттанца"),
    (34, "instr", "в", "ткъе вейттанца"),
    (35, "comp", "в", "ткъе пхийттаннал"),
    (36, "dat", "й", "ткъе ялхиттанна"),
    (37, "obl", "в", "ткъе вуьрхӀиттан"),
    (38, "dat", "й", "ткъе берхӀиттанна"),
    (39, "mat", "й", "ткъе ткъайеснаннах"),
    (40, "all", "д", "шовзткъанга"),
    (41, "obl", "в", "шовзткъе цхьана"),
    (42, "dat", "в", "шовзткъе шинна"),
    (43, "erg", "й", "шовзткъе кхаамма"),
    (44, "erg", "й", "шовзткъе йеамма"),
    (45, "comp", "д", "шовзткъе пхеаннал"),
    (46, "mat", "б", "шовзткъе ялханнах"),
    (47, "erg", "б", "шовзткъе ворхӀамма"),
    (48, "erg", "в", "шовзткъе бархӀамма"),
    (49, "all", "б", "шовзткъе иссанга"),
    (50, "mat", "й", "шовзткъе иттаннах"),
    (51, "comp", "в", "шовзткъе цхьайттаннал"),
    (52, "erg", "в", "шовзткъе шийттамма"),
    (53, "attr", "д", "шовзткъе кхойтта"),
    (54, "gen", "б", "шовзткъе бейттаннан"),
    (55, "attr", "д", "шовзткъе пхийтта"),
    (56, "instr", "й", "шовзткъе ялхиттанца"),
    (57, "obl", "б", "шовзткъе вуьрхӀиттан"),
    (58, "attr", "б", "шовзткъе берхӀитта"),
    (59, "all", "й", "шовзткъе ткъайеснанга"),
    (60, "all", "й", "кхузткъанга"),
    (61, "gen", "й", "кхузткъе цхьаннан"),
    (62, "all", "б", "кхузткъе шинга"),
    (63, "instr", "б", "кхузткъе кхаанца"),
    (64, "dat", "й", "кхузткъе йеанна"),
    (65, "instr", "й", "кхузткъе нхеанца"),
    (66, "all", "б", "кхузткъе ялханга"),
    (67, "erg", "д", "кхузткъе ворхӀамма"),
    (68, "instr", "д", "кхузткъе бархӀанца"),
    (69, "mat", "й", "кхузткъе иссаннах"),
    (70, "attr", "б", "кхузткъе итт"),
    (71, "gen", "б", "кхузткъе цхьайттаннан"),
    (72, "abs", "й", "кхузткъе шийтта"),
    (73, "mat", "д", "кхузткъе кхойттаннах"),
    (74, "instr", "й", "кхузткъе йейттанца"),
    (75, "mat", "в", "кхузткъе пхийттаннах"),
    (76, "instr", "б", "кхузткъе ялхиттанца"),
    (77, "dat", "в", "кхузткъе вуьрхӀиттанна"),
    (78, "erg", "д", "кхузткъе берхӀиттамма"),
    (79, "gen", "б", "кхузткъе ткъайеснаннан"),
    (80, "dat", "б", "дезткъанна"),
    (81, "gen", "б", "дезткъе цхьаннан"),
    (82, "dat", "б", "дезткъе шинна"),
    (83, "obl", "д", "дезткъе кхона"),
    (84, "erg", "в", "дезткъе веамма"),
    (85, "all", "в", "дезткъе пхеанга"),
    (86, "erg", "д", "дезткъе ялхамма"),
    (87, "comp", "б", "дезткъе ворхӀаннал"),
    (88, "dat", "д", "дезткъе бархӀанна"),
    (89, "erg", "б", "дезткъе иссамма"),
    (90, "obl", "й", "дезткъе иттан"),
    (91, "obl", "б", "дезткъе цхьайттан"),
    (92, "abs", "б", "дезткъе шийтта"),
    (93, "gen", "в", "дезткъе кхойттаннан"),
    (94, "comp", "б", "дезткъе бейттаннал"),
    (95, "all", "б", "дезткъе пхийттанга"),
    (96, "instr", "д", "дезткъе ялхиттанца"),
    (97, "erg", "д", "дезткъе вуьрхӀиттамма"),
    (98, "instr", "й", "дезткъе берхӀиттанца"),
    (99, "instr", "б", "дезткъе ткъайеснанца"),
    (0, "gen", "б", "нолан"),
    (100, "mat", "б", "бӀеннах"),
    (200, "attr", "д", "ши бӀе"),
    (300, "obl", "в", "кхо бӀен"),
    (400, "abs", "в", "ви бӀе"),
    (500, "all", "й", "пхи бӀенга"),
    (600, "abs", "й", "ялх бӀе"),
    (700, "mat", "й", "ворхӀ бӀеннах"),
    (800, "gen", "б", "бархӀ бӀеннан"),
    (900, "mat", "в", "исс бӀеннах"),
    (1000, "gen", "д", "эзарнан"),
    (1100, "instr", "д", "эзар бӀенца"),
    (1200, "instr", "д", "эзар ши бӀенца"),
    (1300, "comp", "б", "эзар кхо бӀеннал"),
    (1400, "instr", "д", "эзар ди бӀенца"),
    (1500, "comp", "б", "эзар пхи бӀеннал"),
    (1600, "erg", "б", "эзар ялх бӀемма"),
    (1700, "attr", "д", "эзар ворхӀ бӀе"),
    (1800, "obl", "д", "эзар бархӀ бӀен"),
    (1900, "gen", "й", "эзар исс бӀеннан"),
    (2000, "comp", "д", "ши эзарнал"),
    (2022, "comp", "д", "ши эзар ткъе шиннал"),
    (2100, "obl", "в", "ши эзар бӀен"),
    (423000, "erg", "в", "ви бӀе ткъе кхо эзарно"),
]

TEST_CASES_ORDINAL = [
    (1, "all", "б", "цхьалгӀа"),
    (2, "dat", "в", "шолгӀа"),
    (3, "obl", "й", "кхоалгӀа"),
    (4, "dat", "б", "боьалгӀа"),
    (5, "dat", "в", "пхоьалгӀа"),
    (6, "abs", "в", "йолхалгӀа"),
    (7, "abs", "в", "ворхӀалгӀа"),
    (8, "abs", "д", "борхӀалӀа"),
    (9, "comp", "д", "уьссалгӀа"),
    (10, "erg", "д", "уьтталгӀа"),
    (11, "all", "б", "цхьайтталгӀа"),
    (12, "abs", "й", "шийтталга"),
    (13, "gen", "в", "кхойтталгӀа"),
    (14, "gen", "в", "вейтталгӀа"),
    (15, "mat", "й", "пхийтталгӀа"),
    (16, "dat", "й", "ялхитталгӀа"),
    (17, "erg", "д", "вуьрхӀитталгӀа"),
    (18, "erg", "й", "берхитталӀа"),
    (19, "obl", "в", "ткъаесналгӀа"),
    (20, "abs", "в", "ткъолгӀа"),
    (21, "mat", "б", "ткъе цхьалгӀа"),
    (22, "erg", "б", "ткъе шолгӀа"),
    (23, "mat", "й", "ткъе кхоалгӀа"),
    (24, "obl", "б", "ткъе боьалгӀа"),
    (25, "abs", "д", "ткъе пхоьалгӀа"),
    (26, "all", "й", "ткъе йолхалгӀа"),
    (27, "mat", "в", "ткъе ворхӀалгӀа"),
    (28, "instr", "д", "ткъе борхӀалӀа"),
    (29, "obl", "б", "ткъе уьссалгӀа"),
    (30, "dat", "б", "ткъе уьтталгӀа"),
    (31, "obl", "й", "ткъе цхьайтталгӀа"),
    (32, "comp", "д", "ткъе шийтталга"),
    (33, "attr", "д", "ткъе кхойтталгӀа"),
    (34, "gen", "в", "ткъе вейтталгӀа"),
    (35, "erg", "д", "ткъе пхийтталгӀа"),
    (36, "all", "в", "ткъе ялхитталгӀа"),
    (37, "attr", "й", "ткъе вуьрхӀитталгӀа"),
    (38, "erg", "б", "ткъе берхитталӀа"),
    (39, "gen", "д", "ткъе ткъаесналгӀа"),
    (40, "abs", "й", "шовзткъалгІа"),
    (41, "erg", "й", "шовзткъе цхьалгӀа"),
    (42, "comp", "й", "шовзткъе шолгӀа"),
    (43, "obl", "д", "шовзткъе кхоалгӀа"),
    (44, "all", "й", "шовзткъе йоьалгӀа"),
    (45, "abs", "д", "шовзткъе пхоьалгӀа"),
    (46, "comp", "д", "шовзткъе йолхалгӀа"),
    (47, "comp", "й", "шовзткъе ворхӀалгӀа"),
    (48, "attr", "б", "шовзткъе борхӀалӀа"),
    (49, "comp", "й", "шовзткъе уьссалгӀа"),
    (50, "abs", "д", "шовзткъе уьтталгӀа"),
    (51, "dat", "б", "шовзткъе цхьайтталгӀа"),
    (52, "comp", "в", "шовзткъе шийтталга"),
    (53, "mat", "б", "шовзткъе кхойтталгӀа"),
    (54, "all", "д", "шовзткъе дейтталгӀа"),
    (55, "dat", "в", "шовзткъе пхийтталгӀа"),
    (56, "erg", "б", "шовзткъе ялхитталгӀа"),
    (57, "comp", "й", "шовзткъе вуьрхӀитталгӀа"),
    (58, "instr", "в", "шовзткъе берхитталӀа"),
    (59, "mat", "б", "шовзткъе ткъаесналгӀа"),
    (60, "all", "в", "кхузткъалгІа"),
    (61, "obl", "д", "кхузткъе цхьалгӀа"),
    (62, "instr", "д", "кхузткъе шолгӀа"),
    (63, "erg", "й", "кхузткъе кхоалгӀа"),
    (64, "dat", "д", "кхузткъе доьалгӀа"),
    (65, "gen", "д", "кхузткъе пхоьалгӀа"),
    (66, "mat", "в", "кхузткъе йолхалгӀа"),
    (67, "gen", "в", "кхузткъе ворхӀалгӀа"),
    (68, "attr", "б", "кхузткъе борхӀалӀа"),
    (69, "all", "д", "кхузткъе уьссалгӀа"),
    (70, "mat", "в", "кхузткъе уьтталгӀа"),
    (71, "gen", "й", "кхузткъе цхьайтталгӀа"),
    (72, "obl", "й", "кхузткъе шийтталга"),
    (73, "attr", "в", "кхузткъе кхойтталгӀа"),
    (74, "dat", "б", "кхузткъе бейтталгӀа"),
    (75, "instr", "в", "кхузткъе пхийтталгӀа"),
    (76, "gen", "в", "кхузткъе ялхитталгӀа"),
    (77, "erg", "д", "кхузткъе вуьрхӀитталгӀа"),
    (78, "all", "й", "кхузткъе берхитталӀа"),
    (79, "instr", "д", "кхузткъе ткъаесналгӀа"),
    (80, "dat", "в", "дезткъалгІа"),
    (81, "mat", "в", "дезткъе цхьалгӀа"),
    (82, "abs", "д", "дезткъе шолгӀа"),
    (83, "abs", "д", "дезткъе кхоалгӀа"),
    (84, "erg", "в", "дезткъе воьалгӀа"),
    (85, "obl", "й", "дезткъе пхоьалгӀа"),
    (86, "instr", "д", "дезткъе йолхалгӀа"),
    (87, "all", "в", "дезткъе ворхӀалгӀа"),
    (88, "dat", "д", "дезткъе борхӀалӀа"),
    (89, "obl", "б", "дезткъе уьссалгӀа"),
    (90, "instr", "в", "дезткъе уьтталгӀа"),
    (91, "abs", "й", "дезткъе цхьайтталгӀа"),
    (92, "comp", "в", "дезткъе шийтталга"),
    (93, "erg", "д", "дезткъе кхойтталгӀа"),
    (94, "obl", "й", "дезткъе йейтталгӀа"),
    (95, "comp", "б", "дезткъе пхийтталгӀа"),
    (96, "obl", "б", "дезткъе ялхитталгӀа"),
    (97, "gen", "й", "дезткъе вуьрхӀитталгӀа"),
    (98, "dat", "б", "дезткъе берхитталӀа"),
    (99, "abs", "д", "дезткъе ткъаесналгӀа"),
    (100, "abs", "в", "бІолгІа"),
    (200, "obl", "й", "ши бІолгІа"),
    (300, "mat", "в", "кхо бІолгІа"),
    (400, "gen", "б", "би бІолгІа"),
    (500, "erg", "й", "пхи бІолгІа"),
    (600, "gen", "д", "ялх бІолгІа"),
    (700, "instr", "й", "ворхӀ бІолгІа"),
    (800, "all", "б", "бархӀ бІолгІа"),
    (900, "comp", "б", "исс бІолгІа"),
    (1000, "dat", "д", "эзарлагІа"),
    (107, "gen", "в", "бӀе ворхӀалгӀа"),
    (214, "attr", "д", "ши бӀе дейтталгӀа"),
    (321, "comp", "д", "кхо бӀе ткъе цхьалгӀа"),
    (428, "dat", "в", "ви бӀе ткъе борхӀалӀа"),
    (535, "erg", "й", "пхи бӀе ткъе пхийтталгӀа"),
    (642, "all", "й", "ялх бӀе шовзткъе шолгӀа"),
    (749, "mat", "в", "ворхӀ бӀе шовзткъе уьссалгӀа"),
    (856, "attr", "й", "бархӀ бӀе шовзткъе ялхитталгӀа"),
    (963, "mat", "б", "исс бӀе кхузткъе кхоалгӀа"),
    (1070, "comp", "в", "эзар кхузткъе уьтталгӀа"),
    (1177, "dat", "в", "эзар бӀе кхузткъе вуьрхӀитталгӀа"),
    (1284, "abs", "д", "эзар ши бӀе дезткъе доьалгӀа"),
    (1391, "dat", "в", "эзар кхо бӀе дезткъе цхьайтталгӀа"),
    (1498, "abs", "в", "эзар ви бӀе дезткъе берхитталӀа"),
    (1605, "obl", "б", "эзар ялх бӀе пхоьалгӀа"),
    (1712, "erg", "й", "эзар ворхӀ бӀе шийтталга"),
    (1819, "all", "б", "эзар бархӀ бӀе ткъаесналгӀа"),
    (1926, "abs", "б", "эзар исс бӀе ткъе йолхалгӀа"),
    (2033, "all", "д", "ши эзар ткъе кхойтталгӀа"),
    (2140, "dat", "б", "ши эзар бӀе шовзткъалгІа"),
    (423000, "dat", "д", "ди бӀе ткъе кхо эзарлагІа"),
]

TEST_CASES_YEAR = [
    (1719, "abs", "эзар ворхӀ бӀе ткъайесна"),
    (1812, "abs", "эзар бархӀ бӀе шийтта"),
    (1926, "abs", "эзар исс бӀе ткъе ялх"),
]

TEST_CASES_DECIMALS = [(123.4567, "бӀе ткъе кхоъ а диъ пхиъ ялх ворхӀ")]

TEST_CASES_MILLIONS = [
    (200020, "ши бӀе эзар ткъа"),
    (4000400, "ди миллион ди бӀе"),
    (60006000, "кхузткъе миллион ялх эзар"),
    (800080000, "бархӀ бӀе миллион дезткъе эзар"),
    (10001000000, "итт миллиард цхьа миллион"),
    (120012000000, "бӀе ткъе миллиард шийтта миллион"),
    (1400140000000, "цхьа биллион ди бӀе миллиард бӀе шовзткъе миллион"),
    (16001600000000, "ялхитта биллион цхьа миллиард ялх бӀе миллион"),
    (180018000000000, "бӀе дезткъе биллион берхӀитта миллиард"),
    (2000200000000000, "ши биллиард ши бӀе миллиард"),
    (22002200000000000, "ткъе ши биллиард ши биллион ши бӀе миллиард"),
    (240024000000000000, "ши бӀе шовзткъе биллиард ткъе ди биллион"),
    (
        2600260000000000000,
        "ши триллион ялх бӀе биллиард ши бӀе кхузткъе биллион",
    ),
    (
        28002800000000000000,
        "ткъе бархӀ триллион ши биллиард бархӀ бӀе биллион",
    ),
    (300030000000000000000, "кхо бӀе триллион ткъе итт биллиард"),
    (
        3200320000000000000000,
        "кхо триллиард ши бӀе триллион кхо бӀе ткъе биллиард",
    ),
    (
        34003400000000000000000,
        "ткъе дейтта триллиард кхо триллион ди бӀе биллиард",
    ),
    (
        360036000000000000000000,
        "кхо бӀе кхузткъе триллиард ткъе ялхитта триллион",
    ),
    (
        3800380000000000000000000,
        "кхо квадриллион бархӀ бӀе триллиард кхо бӀе дезткъе триллион",
    ),
    (40004000000000000000000000, "шовзткъе квадриллион ди триллиард"),
    (
        420042000000000000000000000,
        "ди бӀе ткъе квадриллион шовзткъе ши триллиард",
    ),
    (
        4400440000000000000000000000,
        "ди квадриллиард ди бӀе квадриллион ди бӀе шовзткъе триллиард",
    ),
    (
        46004600000000000000000000000,
        "шовзткъе ялх квадриллиард ди квадриллион ялх бӀе триллиард",
    ),
    (
        480048000000000000000000000000,
        "ди бӀе дезткъе квадриллиард шовзткъе бархӀ квадриллион",
    ),
    (5000500000000000000000000000000, "пхи квинтиллион пхи бӀе квадриллион"),
    (
        52005200000000000000000000000000,
        "шовзткъе шийтта квинтиллион пхи квадриллиард ши бӀе квадриллион",
    ),
    (
        540054000000000000000000000000000,
        "пхи бӀе шовзткъе квинтиллион шовзткъе дейтта квадриллиард",
    ),
    (
        5600560000000000000000000000000000,
        "пхи квинтиллиард ялх бӀе квинтиллион пхи бӀе кхузткъе квадриллиард",
    ),
    (10**56, "NOT IMPLEMENTED")
]

TEST_CURRENCY = [
    (143.55, "abs", "RUB", "бӀе шовзткъе кхо Сом, шовзткъе пхийтта Кепек"),
    (243.15, "dat", "RUB", "ши бӀе шовзткъе кхона Сом, пхийттан Кепек"),
]


class Num2WordsCETest(TestCase):
    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(
                num2words(test[0], lang="ce", case=test[1], clazz=test[2]),
                test[3],
            )

    def test_millions(self):
        for test in TEST_CASES_MILLIONS:
            self.assertEqual(num2words(test[0], lang="ce"), test[1])

    def test_ordinal_number(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang="ce", to="ordinal", clazz=test[2]),
                test[3],
            )
        self.assertEqual(num2words(3, to="ordinal_num", lang='ce'), "3-й")
        self.assertEqual(num2words(5, to="ordinal_num", lang='ce'), "5-й")
        self.assertEqual(num2words(82, to="ordinal_num", lang='ce'), "82-й")

    def test_year(self):
        for test in TEST_CASES_YEAR:
            self.assertEqual(
                num2words(test[0], lang="ce", to="year", case=test[1]), test[2]
            )

    def test_currency(self):
        for test in TEST_CURRENCY:
            self.assertEqual(
                num2words(
                    test[0],
                    lang="ce",
                    to="currency",
                    currency=test[2],
                    case=test[1],
                ),
                test[3],
            )

    def test_currency_missing(self):
        with self.assertRaises(NotImplementedError):
            num2words(2.45, to="currency", lang='cy', currency="DEM")

    def test_decimals(self):
        for test in TEST_CASES_DECIMALS:
            self.assertEqual(num2words(test[0], lang="ce"), test[1])
