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

import unittest
from unittest import TestCase

from num2words import num2words

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
    # (53.486, 'cinquante-trois virgule quatre huit six'),
    (55, 'pemp ha hanter-kant'),
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
    # (203, 'deux cent trois'),
    # (287, 'deux cent quatre-vingt-sept'),
    # (300.42, 'trois cents virgule quatre deux'),
    # (356, 'trois cent cinquante-six'),
    # (400, 'quatre cents'),
    # (434, 'quatre cent trente-quatre'),
    # (578, 'cinq cent soixante-dix-huit'),
    # (689, 'six cent quatre-vingt-neuf'),
    # (729, 'sept cent vingt-neuf'),
    (851, "eizh kant unan ha hanter-kant"),
    # (999, 'neuf cent quatre-vingt-dix-neuf'),
    (1000, 'mil'),
    # (1001, 'mille un'),
    # (1097, 'mille quatre-vingt-dix-sept'),
    (1984, "mil nav c'hant pevar ha pevar-ugent"),
    (1995, "mil nav c'hant pemzek ha pevar-ugent"),
    (2007, "daou vil seizh"),
    # (2385, 'deux mille trois cent quatre-vingt-cinq'),
    # (3766, 'trois mille sept cent soixante-six'),
    # (4196, 'quatre mille cent quatre-vingt-seize'),
    # (4196.42, 'quatre mille cent quatre-vingt-seize virgule quatre deux'),
    # (5846, 'cinq mille huit cent quarante-six'),
    # (6459, 'six mille quatre cent cinquante-neuf'),
    (7777, "seizh mil seizh kant seitek ha tri-ugent"),
    (7847, "seizh mil eizh kant seizh ha daou-ugent"),
    (1000000, 'unan milion'),
    (2000000, 'daou vilion'),
    (4000000, 'pevar milion'),
    (11000000, 'unnek milion'),
    (200000000, "daou c'hant milion"),
    (208000000, "daou c'hant eizh milion"),
    (2000000000, 'daou viliard'),
    (10000000000000, 'dek bilion'),
    (10000000000010, 'dek bilion dek'),
    (100000000000000, 'kant bilion'),
    (1000000000000000000, 'unan trilion'),
    # (1000000000000000000000, 'un trilliard'),
    # (10000000000000000000000000, 'dek perlion')
)

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
    (21, 'unanvet warn-ugent'),
    (28, 'eizhvet warn-ugent'),
    (73, 'trizekvet ha tri-ugent'),
    (100, 'kantvet'),
    (101, 'kant unanvet'),
    (1000, 'milvet'),
    (1000000, 'milionvet')
)

TEST_CASES_ORDINAL_NUM = (
    (1, 'kentañ'),
    (2, 'eil'),
    (3, 'trede'),
    (4, 'pevare'),
    (5, 'pempvet'),
    (6, "cʼhwecʼhvet"),
    (7, 'seizhvet'),
    (8, 'eizhvet'),
    (9, 'navvet'),
    (11, 'unnekvet'),
    (12, 'douzekvet'),
    (14, 'pevarzekvet'),
    (15, 'pemzekvet'),
    (21, 'unanvet warn-ugent'),
    (28, 'eizhvet warn-ugent'),
    (73, 'trizekvet ha tri-ugent'),
    (100, 'kantvet'),
    (101, 'kant unanvet'),
    (1000, 'milvet'),
    (1000000, 'milionvet')
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
    (252.90, "daou c'hant daou euro ha hanter-kant, dek santim ha pevar-ugent"),
    (566.37, "pemp kant c'hwec'h euro ha tri-ugent, seizh santim ha tregont"),
    (100000.00, 'kant mil euro, zero santim'),
)

TEST_CASES_TO_CURRENCY_FRF = (
    (1.00, 'un franc et zéro centimes'),
    (2.01, 'deux francs et un centime'),
    (8.10, 'huit francs et dix centimes'),
    (12.27, 'douze francs et vingt-sept centimes'),
    (21.29, 'vingt et un francs et vingt-neuf centimes'),
    (81.25, 'quatre-vingt-un francs et vingt-cinq centimes'),
    (100.00, 'cent francs et zéro centimes'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'un dollar et zéro cents'),
    (2.01, 'deux dollars et un cent'),
    (8.10, 'huit dollars et dix cents'),
    (12.26, 'douze dollars et vingt-six cents'),
    (21.29, 'vingt et un dollars et vingt-neuf cents'),
    (81.25, 'quatre-vingt-un dollars et vingt-cinq cents'),
    (100.00, 'cent dollars et zéro cents'),
    (10000.00, "dek mil dollar ha zero sent")
)

class Num2WordsENTest(TestCase):
    def test_ordinal_special_joins(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/18
        self.assertEqual(
            num2words(5, ordinal=True, lang='br'), "cinquième"
        )
        self.assertEqual(
            num2words(35, ordinal=True, lang='br'), "trente-cinquième"
        )
        self.assertEqual(
            num2words(9, ordinal=True, lang='br'), "neuvième"
        )
        self.assertEqual(
            num2words(49, ordinal=True, lang='br'), "quarante-neuvième"
        )

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='br'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='br', ordinal=True),
                test[1]
            )

    @unittest.expectedFailure
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

    @unittest.expectedFailure
    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang='br', to='currency', currency='FRF'),
                test[1]
            )

    @unittest.expectedFailure
    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='br', to='currency', currency='USD'),
                test[1]
            )
