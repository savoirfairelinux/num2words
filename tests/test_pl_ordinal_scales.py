# -*- coding: utf-8 -*-
# Copyright (c) 2026, Szymon Jędryczko.  All Rights Reserved.

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


class Num2WordsPLOrdinalScaleTest(TestCase):
    def test_large_scales(self):
        for power, expected in (
            (6, 'milionowy'),
            (9, 'miliardowy'),
            (12, 'bilionowy'),
            (15, 'biliardowy'),
            (18, 'trylionowy'),
            (63, 'decyliardowy'),
        ):
            with self.subTest(power=power):
                self.assertEqual(num2words(10**power, lang='pl', to='ordinal'),
                                 expected)

    def test_compound_large_scale(self):
        self.assertEqual(num2words(2 * 10**12, lang='pl', to='ordinal'),
                         'dwubilionowy')

    def test_compound_stems(self):
        for number, expected in (
            (30000, 'trzydziestotysięczny'),
            (500000, 'pięćsettysięczny'),
            (800000, 'osiemsettysięczny'),
            (30000000, 'trzydziestomilionowy'),
        ):
            with self.subTest(number=number):
                self.assertEqual(num2words(number, lang='pl', to='ordinal'),
                                 expected)
