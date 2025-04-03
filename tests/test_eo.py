# -*- coding: utf-8 -*-
# Copyright (c) 2021, Savoir-faire Linux inc.  All Rights Reserved.

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
    (1, "unu"),
    (2, "du"),
    (3, "tri"),
    (5.5, "kvin komo kvin"),
    (11, "dek unu"),
    (12, "dek du"),
    (16, "dek ses"),
    (17.42, "dek sep komo kvar du"),
    (19, "dek naŭ"),
    (20, "dudek"),
    (21, "dudek unu"),
    (26, "dudek ses"),
    (27.312, "dudek sep komo tri unu du"),
    (28, "dudek ok"),
    (30, "tridek"),
    (31, "tridek unu"),
    (40, "kvardek"),
    (44, "kvardek kvar"),
    (50, "kvindek"),
    (53.486, "kvindek tri komo kvar ok ses"),
    (55, "kvindek kvin"),
    (60, "sesdek"),
    (67, "sesdek sep"),
    (70, "sepdek"),
    (79, "sepdek naŭ"),
    (89, "okdek naŭ"),
    (95, "naŭdek kvin"),
    (100, "cent"),
    (101, "cent unu"),
    (199, "cent naŭdek naŭ"),
    (203, "ducent tri"),
    (287, "ducent okdek sep"),
    (300.42, "tricent komo kvar du"),
    (356, "tricent kvindek ses"),
    (400, "kvarcent"),
    (434, "kvarcent tridek kvar"),
    (578, "kvincent sepdek ok"),
    (689, "sescent okdek naŭ"),
    (729, "sepcent dudek naŭ"),
    (894, "okcent naŭdek kvar"),
    (999, "naŭcent naŭdek naŭ"),
    (1000, "mil"),
    (1001, "mil unu"),
    (1097, "mil naŭdek sep"),
    (1104, "mil cent kvar"),
    (1243, "mil ducent kvardek tri"),
    (2385, "du mil tricent okdek kvin"),
    (3766, "tri mil sepcent sesdek ses"),
    (4196, "kvar mil cent naŭdek ses"),
    (4196.42, "kvar mil cent naŭdek ses komo kvar du"),
    (5846, "kvin mil okcent kvardek ses"),
    (6459, "ses mil kvarcent kvindek naŭ"),
    (7232, "sep mil ducent tridek du"),
    (8569, "ok mil kvincent sesdek naŭ"),
    (9539, "naŭ mil kvincent tridek naŭ"),
    (1000000, "unu miliono"),
    (1000001, "unu miliono unu"),
    (4000000, "kvar milionoj"),
    (4000004, "kvar milionoj kvar"),
    (4300000, "kvar milionoj tricent mil"),
    (80000000, "okdek milionoj"),
    (300000000, "tricent milionoj"),
    (10000000000000, "dek bilionoj"),
    (10000000000010, "dek bilionoj dek"),
    (100000000000000, "cent bilionoj"),
    (1000000000000000000, "unu triliono"),
    (1000000000000000000000, "unu triliardo"),
    (10000000000000000000000000, "dek kvarilionoj")
)

TEST_CASES_ORDINAL = (
    (1, "unua"),
    (8, "oka"),
    (12, "dek dua"),
    (14, "dek kvara"),
    (28, "dudek oka"),
    (100, "centa"),
    (1000, "mila"),
    (1000000, "unu miliona"),
    (1000000000000000, "unu biliarda"),
    (1000000000000000000, "unu triliona")
)

TEST_CASES_ORDINAL_NUM = (
    (1, "1a"),
    (8, "8a"),
    (11, "11a"),
    (12, "12a"),
    (14, "14a"),
    (21, "21a"),
    (28, "28a"),
    (100, "100a"),
    (101, "101a"),
    (1000, "1000a"),
    (1000000, "1000000a")
)

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, "unu eŭro kaj nul centimo"),
    (2.01, "du eŭroj kaj unu centimo"),
    (8.10, "ok eŭroj kaj dek centimoj"),
    (12.26, "dek du eŭroj kaj dudek ses centimoj"),
    (21.29, "dudek unu eŭroj kaj dudek naŭ centimoj"),
    (81.25, "okdek unu eŭroj kaj dudek kvin centimoj"),
    (100.00, "cent eŭroj kaj nul centimo"),
)

TEST_CASES_TO_CURRENCY_FRF = (
    (1.00, "unu franko kaj nul centimo"),
    (2.01, "du frankoj kaj unu centimo"),
    (8.10, "ok frankoj kaj dek centimoj"),
    (12.27, "dek du frankoj kaj dudek sep centimoj"),
    (21.29, "dudek unu frankoj kaj dudek naŭ centimoj"),
    (81.25, "okdek unu frankoj kaj dudek kvin centimoj"),
    (100.00, "cent frankoj kaj nul centimo"),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, "unu dolaro kaj nul cendo"),
    (2.01, "du dolaroj kaj unu cendo"),
    (8.10, "ok dolaroj kaj dek cendoj"),
    (12.26, "dek du dolaroj kaj dudek ses cendoj"),
    (21.29, "dudek unu dolaroj kaj dudek naŭ cendoj"),
    (81.25, "okdek unu dolaroj kaj dudek kvin cendoj"),
    (100.00, "cent dolaroj kaj nul cendo"),
)


class Num2WordsEOTest(TestCase):
    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang="eo"), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang="eo", ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang="eo", to="ordinal_num"),
                test[1]
            )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang="eo", to="currency", currency="EUR"),
                test[1]
            )

    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_FRF:
            self.assertEqual(
                num2words(test[0], lang="eo", to="currency", currency="FRF"),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang="eo", to="currency", currency="USD"),
                test[1]
            )
