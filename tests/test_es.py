# encoding: UTF-8
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

TEST_CASES_CARDINAL = (
    (1, 'uno'),
    (2, 'dos'),
    (3, 'tres'),
    (5.5, 'cinco punto cinco'),
    (11, 'once'),
    (12, 'doce'),
    (16, 'dieciseis'),
    (17.42, 'diecisiete punto cuatro dos'),
    (19, 'diecinueve'),
    (20, 'veinte'),
    (21, 'veintiuno'),
    (26, 'veintiséis'),
    (27.312, 'veintisiete punto tres uno dos'),
    (28, 'veintiocho'),
    (30, 'treinta'),
    (31, 'treinta y uno'),
    (40, 'cuarenta'),
    (44, 'cuarenta y cuatro'),
    (50, 'cincuenta'),
    (53.486, 'cincuenta y tres punto cuatro ocho seis'),
    (55, 'cincuenta y cinco'),
    (60, 'sesenta'),
    (67, 'sesenta y siete'),
    (70, 'setenta'),
    (79, 'setenta y nueve'),
    (89, 'ochenta y nueve'),
    (95, 'noventa y cinco'),
    (100, 'cien'),
    (101, 'ciento uno'),
    (199, 'ciento noventa y nueve'),
    (203, 'doscientos tres'),
    (287, 'doscientos ochenta y siete'),
    (300.42, 'trescientos punto cuatro dos'),
    (356, 'trescientos cincuenta y seis'),
    (400, 'cuatrocientos'),
    (434, 'cuatrocientos treinta y cuatro'),
    (578, 'quinientos setenta y ocho'),
    (689, 'seiscientos ochenta y nueve'),
    (729, 'setecientos veintinueve'),
    (894, 'ochocientos noventa y cuatro'),
    (999, 'novecientos noventa y nueve'),
    (1000, 'mil'),
    (1001, 'mil uno'),
    (1097, 'mil noventa y siete'),
    (1104, 'mil ciento cuatro'),
    (1243, 'mil doscientos cuarenta y tres'),
    (2385, 'dos mil trescientos ochenta y cinco'),
    (3766, 'tres mil setecientos sesenta y seis'),
    (4196, 'cuatro mil ciento noventa y seis'),
    (4196.42, 'cuatro mil ciento noventa y seis punto cuatro dos'),
    (5846, 'cinco mil ochocientos cuarenta y seis'),
    (6459, 'seis mil cuatrocientos cincuenta y nueve'),
    (7232, 'siete mil doscientos treinta y dos'),
    (8569, 'ocho mil quinientos sesenta y nueve'),
    (9539, 'nueve mil quinientos treinta y nueve'),
    (1000000, 'un millón'),
    (1000001, 'un millón uno'),
    (4000000, 'cuatro millones'),
    (10000000000000, 'diez billones'),
    (100000000000000, 'cien billones'),
    (1000000000000000000, 'un trillón'),
    (1000000000000000000000, 'mil trillones'),
    (10000000000000000000000000, 'diez cuatrillones')
)

TEST_CASES_ORDINAL = (
    (1, 'primero'),
    (8, 'octavo'),
    (12, 'décimosegundo'),
    (14, 'décimo cuarto'),
    (28, 'vigésimo octavo'),
    (100, 'centésimo'),
    (1000, 'milésimo'),
    (1000000, 'millonésimo'),
    (1000000000000000, 'cuadrillonésimo'),
    (1000000000000000000, 'un trillón')  # over 1e18 is not supported
)

TEST_CASES_ORDINAL_NUM = (
    (1, '1º'),
    (8, '8º'),
    (12, '12º'),
    (14, '14º'),
    (28, '28º'),
    (100, '100º'),
    (1000, '1000º'),
    (1000000, '1000000º')
)

TEST_CASES_TO_CURRENCY = (
    (1, 'un euro'),
    (2, 'dos euros'),
    (8, 'ocho euros'),
    (12, 'doce euros'),
    (21, 'veintiun euros'),
    (81.25, 'ochenta y un euros y veinticinco centavos'),
    (100, 'cien euros'),
)

TEST_CASES_TO_CURRENCY_OLD = (
    (1, 'un peso'),
    (2, 'dos pesos'),
    (8, 'ocho pesos'),
    (12, 'doce pesos'),
    (21, 'veintiun pesos'),
    (81.25, 'ochenta y un pesos y veinticinco pesetas'),
    (100, 'cien pesos'),
)


class Num2WordsESTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='es'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='es', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='es', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency'),
                test[1]
            )

    def test_currency_old(self):
        for test in TEST_CASES_TO_CURRENCY_OLD:
            self.assertEqual(
                num2words(test[0], lang='es', to='currency', old=True),
                test[1]
            )
