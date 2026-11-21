# -*- coding: utf-8 -*-
# Copyright (c) 2026, num2words contributors. All Rights Reserved.

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

from decimal import Decimal
from unittest import TestCase

from num2words import num2words


class Num2WordsSLCurrencyTest(TestCase):
    def test_currency_float(self):
        self.assertEqual(
            num2words(502.12, lang='sl', to='currency'),
            'petsto dve euro in dvanajst cents',
        )

    def test_currency_integer_minor_units(self):
        self.assertEqual(
            num2words(50212, lang='sl', to='currency'),
            'petsto dve euro in dvanajst cents',
        )

    def test_currency_decimal_and_string(self):
        for value in (Decimal('502.12'), '502.12'):
            with self.subTest(value=value):
                self.assertEqual(
                    num2words(value, lang='sl', to='currency'),
                    'petsto dve euro in dvanajst cents',
                )

    def test_currency_negative(self):
        for value in (-502.12, -50212):
            with self.subTest(value=value):
                self.assertEqual(
                    num2words(value, lang='sl', to='currency'),
                    'minus petsto dve euro in dvanajst cents',
                )

    def test_currency_whole_minor_units(self):
        self.assertEqual(
            num2words(100, lang='sl', to='currency'), 'ena euro',
        )

    def test_currency_zero(self):
        self.assertEqual(
            num2words(0.0, lang='sl', to='currency'),
            'nič euro in nič cents',
        )

    def test_currency_abbreviated(self):
        for value in (502.12, 50212):
            with self.subTest(value=value):
                self.assertEqual(
                    num2words(value, lang='sl', to='currency', longval=False),
                    'petsto dve dvanajst',
                )

    def test_currency_legacy(self):
        self.assertEqual(
            num2words(1.01, lang='sl', to='currency', old=True),
            'ena evro in ena stotin',
        )
        self.assertEqual(
            num2words(1.01, lang='sl', to='currency', old=True, longval=False),
            'ena ena',
        )
