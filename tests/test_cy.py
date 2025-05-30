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

TEST_CASES_CARDINAL = (
    (0, "dim"),
    (1, "un"),
    (1, "un"),
    (2, "dau"),
    (3, "tri"),
    (4, "pedwar"),
    (5, "pump"),
    (6, "chwech"),
    (7, "saith"),
    (8, "wyth"),
    (9, "naw"),
    (10, "deg"),
    (11, "un ar ddeg"),
    (12, "deuddeg"),
    (13, "tri ar ddeg"),
    (14, "pedwar ar ddeg"),
    (15, "pymtheg"),
    (16, "un ar bymtheg"),
    (17, "dau ar bymtheg"),
    (18, "deunaw"),
    (19, "pedwar ar bymtheg"),
    (20, "ugain"),
    (21, "un ar hugain"),
    (22, "dau ar hugain"),
    (23, "tri ar hugain"),
    (24, "pedwar ar hugain"),
    (25, "pump ar hugain"),
    (26, "chwech ar hugain"),
    (27, "saith ar hugain"),
    (28, "wyth ar hugain"),
    (29, "naw ar hugain"),
    (30, "deg ar hugain"),
    (31, "un ar ddeg ar hugain"),
    (32, "deuddeg ar hugain"),
    (33, "tri ar ddeg ar hugain"),
    (34, "pedwar ar ddeg ar hugain"),
    (35, "pymtheg ar hugain"),
    (36, "un ar bymtheg ar hugain"),
    (37, "dau ar bymtheg ar hugain"),
    (38, "deunaw ar hugain"),
    (39, "pedwar ar bymtheg ar hugain"),
    (40, "deugain"),
    (41, "un a deugain"),
    (42, "dau a deugain"),
    (43, "tri a deugain"),
    (44, "pedwar a deugain"),
    (45, "pump a deugain"),
    (46, "chwech a deugain"),
    (47, "saith a deugain"),
    (48, "wyth a deugain"),
    (49, "naw a deugain"),
    (50, "hanner cant"),
    (51, "hanner cant ac un"),
    (52, "hanner cant a dau"),
    (53, "hanner cant a thri"),
    (54, "hanner cant a phedwar"),
    (55, "hanner cant a phump"),
    (56, "hanner cant a chwech"),
    (57, "hanner cant a saith"),
    (58, "hanner cant a wyth"),
    (59, "hanner cant a naw"),
    (60, "trigain"),
    (61, "un a thrigain"),
    (62, "dau a thrigain"),
    (63, "tri a thrigain"),
    (64, "pedwar a thrigain"),
    (65, "pump a thrigain"),
    (66, "chwech a thrigain"),
    (67, "saith a thrigain"),
    (68, "wyth a thrigain"),
    (69, "naw a thrigain"),
    (70, "deg a thrigain"),
    (71, "un ar ddeg a thrigain"),
    (72, "deuddeg a thrigain"),
    (73, "tri ar ddeg a thrigain"),
    (74, "pedwar ar ddeg a thrigain"),
    (75, "pymtheg a thrigain"),
    (76, "un ar bymtheg a thrigain"),
    (77, "dau ar bymtheg a thrigain"),
    (78, "deunaw a thrigain"),
    (79, "pedwar ar bymtheg a thrigain"),
    (80, "pedwar ugain"),
    (81, "un a phedwar ugain"),
    (82, "dau a phedwar ugain"),
    (83, "tri a phedwar ugain"),
    (84, "pedwar a phedwar ugain"),
    (85, "pump a phedwar ugain"),
    (86, "chwech a phedwar ugain"),
    (87, "saith a phedwar ugain"),
    (88, "wyth a phedwar ugain"),
    (89, "naw a phedwar ugain"),
    (90, "deg a phedwar ugain"),
    (91, "un ar ddeg a phedwar ugain"),
    (92, "deuddeg a phedwar ugain"),
    (93, "tri ar ddeg a phedwar ugain"),
    (94, "pedwar ar ddeg a phedwar ugain"),
    (95, "pymtheg a phedwar ugain"),
    (96, "un ar bymtheg a phedwar ugain"),
    (97, "dau ar bymtheg a phedwar ugain"),
    (98, "deunaw a phedwar ugain"),
    (99, "pedwar ar bymtheg a phedwar ugain"),
    (100, "cant"),
    (101, "cant ac un"),
    (102, "cant a dau"),
    (103, "cant a thri"),
    (104, "cant a phedwar"),
    (105, "cant a phump"),
    (106, "cant a chwech"),
    (107, "cant a saith"),
    (108, "cant ac wyth"),
    (109, "cant a naw"),
    (110, "cant a deg"),
    (111, "cant ac un ar ddeg"),
    (112, "cant a deuddeg"),
    (113, "cant a thri ar ddeg"),
    (114, "cant a phedwar ar ddeg"),
    (115, "cant a phymtheg"),
    (116, "cant ac un ar bymtheg"),
    (117, "cant a dau ar bymtheg"),
    (118, "cant a deunaw"),
    (119, "cant a phedwar ar bymtheg"),
    (120, "cant ac ugain"),
    (121, "cant ac un ar hugain"),
    (122, "cant a dau ar hugain"),
    (100, "cant"),
    (217, "dau gant a dau ar bymtheg"),
    (334, "tri chant a phedwar ar ddeg ar hugain"),
    (451, "pedwar cant a hanner ac un"),
    (568, "pump cant ac wyth a thrigain"),
    (685, "chwech chant a phump a phedwar ugain"),
    (802, "wyth cant a dau"),
    (919, "naw cant a phedwar ar bymtheg"),
    (100, "cant"),
    (150, "cant a hanner"),
    (200, "dau gant"),
    (300, "tri chant"),
    (400, "pedwar cant"),
    (500, "pump cant"),
    (600, "chwech chant"),
    (700, "saith cant"),
    (800, "wyth cant"),
    (900, "naw cant"),
    (1000, "mil"),
    (1000, "mil"),
    (12111, "deuddeg mil cant ac un ar ddeg"),
    (23222, "tair ar hugain mil dau gant a dau ar hugain"),
    (
        34333,
        "pedair ar ddeg ar hugain mil tri chant a thri ar ddeg ar hugain",
    ),
    (45444, "pump a deugain mil pedwar cant a phedwar a deugain"),
    (56555, "hanner cant a chwech mil pump cant a hanner a phump"),
    (67666, "saith a thrigain mil chwech chant a chwech a thrigain"),
    (78777, "deunaw a thrigain mil saith cant a dau ar bymtheg a thrigain"),
    (89888, "naw a phedwar ugain mil wyth cant ac wyth a phedwar ugain"),
    (100999, "cant mil naw cant a phedwar ar bymtheg a phedwar ugain"),
    (112110, "cant a deuddeg mil cant a deg"),
    (123221, "cant a thair ar hugain mil dau gant ac un ar hugain"),
    (
        134332,
        "cant a phedair ar ddeg ar hugain mil tri chant a deuddeg ar hugain",
    ),
    (145443, "cant a phump a deugain mil pedwar cant a thri a deugain"),
    (156554, "cant a hanner a chwech mil pump cant a hanner a phedwar"),
    (123, "cant a thri ar hugain"),
    (2345, "dwy fil tri chant a phump a deugain"),
    (34567, "pedair ar ddeg ar hugain mil pump cant a saith a thrigain"),
    (654321, "chwech chant a hanner a phedair mil tri chant ac un ar hugain"),
    (
        7654321,
        "saith miliwn chwech chant a hanner a "
        "phedair mil tri chant ac un ar hugain",
    ),
    (
        987654321,
        "naw cant a saith a phedwar ugain miliwn chwech chant a "
        "hanner a phedair mil tri chant ac un ar hugain",
    ),
    (
        123456789012,
        "cant a thri ar hugain biliwn pedwar cant a hanner a chwech miliwn "
        "saith cant a naw a phedwar ugain mil deuddeg",
    ),
    (2023, "dwy fil tri ar hugain"),
    (-40123, "meinws deugain mil cant a thri ar hugain"),
    (12340000000000000, "deuddeg cwadriliwn tri chant a deugain triliwn"),
    (3000000000000000, "tri chwadriliwn"),
    (2500000000000000000000000000000000, "dau ddengiliwn pump cant noniliwn"),
)


TEST_CASES_CARDINAL_FEM = (
    (2, "dwy"),
    (3, "tair"),
    (4, "pedair"),
    (5, "pump"),
    (6, "chwech"),
    (7, "saith"),
    (8, "wyth"),
    (9, "naw"),
    (10, "deg"),
    (11, "un ar ddeg"),
    (12, "deuddeg"),
    (13, "tair ar ddeg"),
    (14, "pedair ar ddeg"),
    (15, "pymtheg"),
    (16, "un ar bymtheg"),
    (17, "dwy ar bymtheg"),
    (18, "deunaw"),
    (19, "pedair ar bymtheg"),
    (20, "ugain"),
    (21, "un ar hugain"),
    (22, "dwy ar hugain"),
    (23, "tair ar hugain"),
    (24, "pedair ar hugain"),
    (25, "pump ar hugain"),
    (26, "chwech ar hugain"),
    (27, "saith ar hugain"),
    (28, "wyth ar hugain"),
    (29, "naw ar hugain"),
    (30, "deg ar hugain"),
    (31, "un ar ddeg ar hugain"),
    (32, "deuddeg ar hugain"),
    (33, "tair ar ddeg ar hugain"),
    (34, "pedair ar ddeg ar hugain"),
    (35, "pymtheg ar hugain"),
    (36, "un ar bymtheg ar hugain"),
    (37, "dwy ar bymtheg ar hugain"),
    (38, "deunaw ar hugain"),
    (39, "pedair ar bymtheg ar hugain"),
    (40, "deugain"),
    (41, "un a deugain"),
    (42, "dwy a deugain"),
    (43, "tair a deugain"),
    (44, "pedair a deugain"),
    (45, "pump a deugain"),
    (46, "chwech a deugain"),
    (47, "saith a deugain"),
    (48, "wyth a deugain"),
    (49, "naw a deugain"),
    (50, "hanner cant"),
    (51, "hanner cant ac un"),
    (52, "hanner cant a dwy"),
    (53, "hanner cant a thair"),
    (54, "hanner cant a phedair"),
    (55, "hanner cant a phump"),
    (56, "hanner cant a chwech"),
    (57, "hanner cant a saith"),
    (58, "hanner cant a wyth"),
    (59, "hanner cant a naw"),
    (60, "trigain"),
    (61, "un a thrigain"),
    (62, "dwy a thrigain"),
)

TEST_CASES_ORDINAL = (
    (0, "dimfed"),
    (1, "cyntaf"),
    (2, "ail"),
    (3, "trydydd"),
    (4, "pedwerydd"),
    (5, "pumed"),
    (6, "chweched"),
    (7, "saithfed"),
    (8, "wythfed"),
    (9, "nawfed"),
    (10, "degfed"),
    (11, "unfed ar ddeg"),
    (12, "deuddegfed"),
    (13, "trydydd ar ddeg"),
    (14, "pedwerydd ar ddeg"),
    (15, "pymthegfed"),
    (16, "unfed ar bymtheg"),
    (17, "ail ar bymtheg"),
    (18, "deunawfed"),
    (19, "pedwerydd ar bymtheg"),
    (20, "ugainfed"),
    (21, "cyntaf ar hugain"),
    (22, "ail ar hugain"),
    (23, "trydydd ar hugain"),
    (24, "pedwerydd ar hugain"),
    (25, "pumed ar hugain"),
    (26, "chweched ar hugain"),
    (27, "saithfed ar hugain"),
    (28, "wythfed ar hugain"),
    (29, "nawfed ar hugain"),
    (30, "degfed ar hugain"),
    (31, "unfed ar ddeg ar hugain"),
    (32, "deuddegfed ar hugain"),
    (33, "trydydd ar ddeg ar hugain"),
    (34, "pedwerydd ar ddeg ar hugain"),
    (35, "pymthegfed ar hugain"),
    (36, "unfed ar bymtheg ar hugain"),
    (37, "ail ar bymtheg ar hugain"),
    (38, "deunawfed ar hugain"),
    (39, "pedwerydd ar bymtheg ar hugain"),
    (40, "deugainfed"),
    (41, "cyntaf a deugain"),
    (42, "ail a deugain"),
    (43, "trydydd a deugain"),
    (44, "pedwerydd a deugain"),
    (45, "pumed a deugain"),
    (46, "chweched a deugain"),
    (47, "saithfed a deugain"),
    (48, "wythfed a deugain"),
    (49, "nawfed a deugain"),
    (50, "degfed a deugain"),
    (51, "unfed ar ddeg a deugain"),
    (52, "deuddegfed a deugain"),
    (53, "trydydd ar ddeg a deugain"),
    (54, "pedwerydd ar ddeg a deugain"),
    (55, "pymthegfed a deugain"),
    (56, "unfed ar bymtheg a deugain"),
    (57, "ail ar bymtheg a deugain"),
    (58, "deunawfed a deugain"),
    (59, "pedwerydd ar bymtheg a deugain"),
    (60, "trigainfed"),
    (61, "cyntaf a thrigain"),
    (62, "ail a thrigain"),
    (63, "trydydd a thrigain"),
    (64, "pedwerydd a thrigain"),
    (65, "pumed a thrigain"),
    (66, "chweched a thrigain"),
    (67, "saithfed a thrigain"),
    (68, "wythfed a thrigain"),
    (69, "nawfed a thrigain"),
    (70, "degfed a thrigain"),
    (71, "unfed ar ddeg a thrigain"),
    (72, "deuddegfed a thrigain"),
    (73, "trydydd ar ddeg a thrigain"),
    (74, "pedwerydd ar ddeg a thrigain"),
    (75, "pymthegfed a thrigain"),
    (76, "unfed ar bymtheg a thrigain"),
    (77, "ail ar bymtheg a thrigain"),
    (78, "deunawfed a thrigain"),
    (79, "pedwerydd ar bymtheg a thrigain"),
    (80, "pedwar ugainfed"),
    (81, "cyntaf a phedwar ugain"),
    (82, "ail a phedwar ugain"),
    (83, "trydydd a phedwar ugain"),
    (84, "pedwerydd a phedwar ugain"),
    (85, "pumed a phedwar ugain"),
    (86, "chweched a phedwar ugain"),
    (87, "saithfed a phedwar ugain"),
    (88, "wythfed a phedwar ugain"),
    (89, "nawfed a phedwar ugain"),
    (90, "degfed a phedwar ugain"),
    (91, "unfed ar ddeg a phedwar ugain"),
    (92, "deuddegfed a phedwar ugain"),
    (93, "trydydd ar ddeg a phedwar ugain"),
    (94, "pedwerydd ar ddeg a phedwar ugain"),
    (95, "pymthegfed a phedwar ugain"),
    (96, "unfed ar bymtheg a phedwar ugain"),
    (97, "ail ar bymtheg a phedwar ugain"),
    (98, "deunawfed a phedwar ugain"),
    (99, "pedwerydd ar bymtheg a phedwar ugain"),
    (100, "canfed"),
)

TEST_CASES_YEAR = [
    (1922, "mil naw dau dau"),
    (1989, "mil naw wyth naw"),
    (1812, "mil wyth un dau"),
    (2012, "dwy fil deuddeg"),
    (2023, "dwy fil tri ar hugain")
    ]

TEST_CASES_DECIMALS = [
    (123.4567, "cant a thri ar hugain pwynt pedwar pump chwech saith")
]

TEST_CASES_TO_CURRENCY_GBP = (
    (0.00, "dim punt"),
    (0.23, "tri cheiniog ar hugain"),
    (2.04, "dwy bunt, pedwar ceiniog"),
    (3.50, "tair punt, hanner cant ceiniog"),
    (2002.15, "dwy fil dwy o bunnoedd, pymtheg ceiniog"),
    (100.01, "cant punt, ceiniog"),
    (50.00, "hanner cant punt"),
    (51.00, "hanner cant ac un punt"),
    (152.50, "cant a hanner a dwy o bunnoedd, hanner cant ceiniog"),
)

TEST_CASES_COUNTED = [
    (2, "ci", "masc", "dau gi"),
    (2, "ty", "masc", "dau dy"),
    (2, "llwy", "fem", "dwy lwy"),
    (2, "rhaglen", "masc", "dau raglen"),
    (11, "ci", "masc", "un ci ar ddeg"),
    (13, "ci", "masc", "tri chi ar ddeg"),
    (26, "ci", "masc", "chwech chi ar hugain"),
    (56, "ci", "masc", "hanner cant a chwech chi"),
    (100, "cwn", "masc", "cant o gwn"),
    (2000, "cathod", "fem", "dwy fil o gathod"),
    (11, "cath", "fem", "un cath ar ddeg"),
    (13, "cath", "fem", "tair cath ar ddeg"),
    (26, "cath", "fem", "chwech chath ar hugain"),
    (42, "cath", "fem", "dwy gath a deugain"),
    (56, "cath", "fem", "hanner cant a chwech chath"),
]


class Num2WordsCYTest(TestCase):
    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang="cy"), test[1])

    def test_number_fem(self):
        for test in TEST_CASES_CARDINAL_FEM:
            self.assertEqual(
                num2words(test[0], lang="cy", gender="fem"), test[1]
            )

    def test_number_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            num2words(10**66, lang='cy')

    def test_decimals(self):
        for test in TEST_CASES_DECIMALS:
            self.assertEqual(num2words(test[0], lang="cy"), test[1])

    def test_ordinals(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang="cy", to="ordinal"), test[1]
            )

    def test_ordinal_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            num2words(101, lang='cy', to="ordinal")

    def test_pounds(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang="cy", to="currency", currency="GBP"),
                test[1],
            )

    def test_other_cur(self):
        with self.assertRaises(NotImplementedError):
            num2words(10.23, lang="cy", to="currency", currency="DEM"),

    def test_counted(self):
        for test in TEST_CASES_COUNTED:
            self.assertEqual(
                num2words(
                    test[0], lang="cy", counted=test[1], gender=test[2]
                ),
                test[3],
            )

# TODO 'ordinal_num', 'year'
