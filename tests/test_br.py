# -*- coding: utf-8 -*-
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
from num2words import num2words

import unittest
from unittest import TestCase

TEST_CASES_CARDINAL = (
    (0, "zero"),
    (1, 'unan'),
    (2, 'daou'),
    (3, 'tri'),
    (5.5, 'pemp skej pemp'),
    (10, 'dek'),
    (11, 'unnek'),
    (16, "c'hwezek"),
    (17.42, 'seitek skej pevar daou'),
    (19, 'naontek'),
    (20, 'ugent'),
    (21, 'unan warn ugent'),
    (26, "c'hwec'h warn ugent"),
    (27.312, 'seizh warn ugent skej tri unan daou'),
    (28, 'eizh warn ugent'),
    (30, 'tregont'),
    (31, 'unan ha tregont'),
    (40, 'daou-ugent'),
    (44, 'pevar ha daou-ugent'),
    (50, 'hanter-kant'),
    (55, 'pemp hag hanter-kant'),
    (60, 'tri-ugent'),
    (67, 'seizh ha tri-ugent'),
    (70, 'dek ha tri-ugent'),
    (79, 'naontek ha tri-ugent'),
    (89, 'nav ha pevar-ugent'),
    (95, 'pemzek ha pevar-ugent'),
    (100, 'kant'),
    (101, 'kant unan'),
    (110, 'kant dek'),
    (150, 'kant hanter-kant'),
    (200, "daou c'hant"),
    (201, "daou c'hant unan"),
    (237, "daou c'hant seizh ha tregont"),
    (302, "tri c'hant daou"),
    (338, "tri c'hant eizh ha tregont"),
    (453, "pevar c'hant tri hag hanter-kant"),
    (599, "pemp kant naontek ha pevar-ugent"),
    (655, "c'hwec'h kant pemp hag hanter-kant"),
    (774, "seizh kant pevarzek ha tri-ugent"),
    (851, "eizh kant unan hag hanter-kant"),
    (1000, 'mil'),
    (1984, "mil nav c'hant pevar ha pevar-ugent"),
    (1995, "mil nav c'hant pemzek ha pevar-ugent"),
    (2007, "daou vil seizh"),
    (2100, "daou vil kant"),
    (3001, "tri mil unan"),
    (7777, "seizh mil seizh kant seitek ha tri-ugent"),
    (7847, "seizh mil eizh kant seizh ha daou-ugent"),
    (1000000, 'unan milion'),
    (2000000, 'daou vilion'),
    (3010100, "tri milion dek mil kant"),
    (4000000, 'pevar milion'),
    (11000000, 'unnek milion'),
    (200000000, "daou c'hant milion"),
    (208000000, "daou c'hant eizh milion"),
    (2000000000, 'daou viliard'),
    (10000000000000, 'dek bilion'),
    (10000000000010, 'dek bilion dek'),
    (100000000000000, 'kant bilion'),
    (1000000000000000000, 'unan trilion'),
)

# Some tests adapted from https://www.webklas.org/IMG/odt/kartou_niverin_CE1.odt

TEST_CASES_ORDINAL = (
    (1, 'kentañ'),
    (2, 'eil'),
    (3, 'trede'),
    (4, 'pevare'),
    (5, 'pempvet'),
    (6, "c'hwec'hvet"),
    (7, 'seizhvet'),
    (8, 'eizhvet'),
    (9, 'navvet'),
    (11, 'unnekvet'),
    (12, 'daouzekvet'),
    (14, 'pevarzekvet'),
    (15, 'pemzekvet'),
    (21, 'unanvet warn ugent'),
    (28, 'eizhvet warn ugent'),
    (73, 'trizekvet ha tri-ugent'),
    (100, 'kantvet'),
    (101, 'kant unanvet'),
    (1000, 'milvet'),
    (1000000, 'unan milionvet')
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1añ'),
    (2, '2l'),
    (3, '3e'),
    (4, '4e'),
    (5, '5vet'),
    (6, "6vet"),
    (7, '7vet'),
    (8, '8vet'),
    (9, '9vet'),
    (11, '11vet'),
    (12, '12vet'),
    (14, '14vet'),
    (15, '15vet'),
    (21, '21vet'),
    (28, '28vet'),
    (73, '73vet'),
    (100, '100vet'),
    (101, '101vet'),
    (1000, '1000vet'),
    (1000000, '1000000vet')
)

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'un euro, zero santim'),
    (2.01, 'daou euro, un santim'),
    (8.10, 'eizh euro, dek santim'),
    (12.26, "daouzek euro, c'hwec'h santim warn ugent"),
    (21.29, 'un euro warn ugent, nav santim warn ugent'),
    (77.00, 'seitek euro ha tri-ugent, zero santim'),
    (81.25, 'un euro ha pevar-ugent, pemp santim warn ugent'),
    (90.25, 'dek euro ha pevar-ugent, pemp santim warn ugent'),
    (100.00, 'kant euro, zero santim'),
    (252.90, "daou c'hant daou euro hag hanter-kant, dek santim ha pevar-ugent"),
    (566.37, "pemp kant c'hwec'h euro ha tri-ugent, seizh santim ha tregont"),
    (100000.00, 'kant mil euro, zero santim'),
)

TEST_CASES_TO_CURRENCY_FRF = (
    (1.00, 'un lur, zero santim'),
    (2.01, 'daou lur, un santim'),
    (8.10, 'eizh lur, dek santim'),
    (12.26, "daouzek lur, c'hwec'h santim warn ugent"),
    (21.29, 'un lur warn ugent, nav santim warn ugent'),
    (77.00, 'seitek lur ha tri-ugent, zero santim'),
    (81.25, 'un lur ha pevar-ugent, pemp santim warn ugent'),
    (90.25, 'dek lur ha pevar-ugent, pemp santim warn ugent'),
    (100.00, 'kant lur, zero santim'),
    (252.90, "daou c'hant daou lur hag hanter-kant, dek santim ha pevar-ugent"),
    (566.37, "pemp kant c'hwec'h lur ha tri-ugent, seizh santim ha tregont"),
    (100000.00, 'kant mil lur, zero santim'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'un dollar, zero sent'),
    (2.01, 'daou dollar, un sent'),
    (8.10, 'eizh dollar, dek sent'),
    (12.26, "daouzek dollar, c'hwec'h sent warn ugent"),
    (21.29, 'un dollar warn ugent, nav sent warn ugent'),
    (77.00, 'seitek dollar ha tri-ugent, zero sent'),
    (81.25, 'un dollar ha pevar-ugent, pemp sent warn ugent'),
    (90.25, 'dek dollar ha pevar-ugent, pemp sent warn ugent'),
    (100.00, 'kant dollar, zero sent'),
    (252.90, "daou c'hant daou dollar hag hanter-kant, dek sent ha pevar-ugent"),
    (566.37, "pemp kant c'hwec'h dollar ha tri-ugent, seizh sent ha tregont"),
    (100000.00, 'kant mil dollar, zero sent'),
)


class Num2WordsENTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='br'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='br', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='br', to='ordinal_num'),
                test[1]
            )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='br', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='br', to='currency', currency='FRF'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='br', to='currency', currency='USD'),
                test[1]
            )


if __name__ == '__main__':
    unittest.main()
