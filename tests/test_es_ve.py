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


class Num2WordsESVETest(TestCase):

    def test_number(self):

        test_cases = (
            (1, 'uno'),
            (2, 'dos'),
            (3, 'tres'),
            (11, 'once'),
            (12, 'doce'),
            (16, 'dieciseis'),
            (19, 'diecinueve'),
            (20, 'veinte'),
            (21, 'veintiuno'),
            (26, 'veintiséis'),
            (28, 'veintiocho'),
            (30, 'treinta'),
            (31, 'treinta y uno'),
            (40, 'cuarenta'),
            (43, 'cuarenta y tres'),
            (50, 'cincuenta'),
            (55, 'cincuenta y cinco'),
            (60, 'sesenta'),
            (67, 'sesenta y siete'),
            (70, 'setenta'),
            (79, 'setenta y nueve'),
            (100, 'cien'),
            (101, 'ciento uno'),
            (199, 'ciento noventa y nueve'),
            (203, 'doscientos tres'),
            (287, 'doscientos ochenta y siete'),
            (300, 'trescientos'),
            (356, 'trescientos cincuenta y seis'),
            (410, 'cuatrocientos diez'),
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
            (5846, 'cinco mil ochocientos cuarenta y seis'),
            (6459, 'seis mil cuatrocientos cincuenta y nueve'),
            (7232, 'siete mil doscientos treinta y dos'),
            (8569, 'ocho mil quinientos sesenta y nueve'),
            (9539, 'nueve mil quinientos treinta y nueve'),
            (1000000, 'un millón'),
            (1000001, 'un millón uno'),
        )

        for test in test_cases:
            self.assertEqual(num2words(test[0], lang='es_VE'), test[1])
