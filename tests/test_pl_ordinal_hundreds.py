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


class Num2WordsPLOrdinalHundredsTest(TestCase):
    def test_compound_hundreds_before_thousands(self):
        cases = (
            (101000, 'stujednotysięczny'),
            (110000, 'studziesięciotysięczny'),
            (111000, 'stujedenastotysięczny'),
            (120000, 'studwudziestotysięczny'),
            (121000, 'studwudziestojednotysięczny'),
            (201000, 'dwustujednotysięczny'),
            (210000, 'dwustudziesięciotysięczny'),
            (212000, 'dwustudwunastotysięczny'),
            (220000, 'dwustudwudziestotysięczny'),
            (110000000, 'studziesięciomilionowy'),
            (1110000, 'milion studziesięciotysięczny'),
        )
        for number, expected in cases:
            with self.subTest(number=number):
                self.assertEqual(
                    num2words(number, lang='pl', to='ordinal'), expected)

    def test_hundreds_without_scale_keep_cardinal_prefix(self):
        self.assertEqual(
            num2words(110, lang='pl', to='ordinal'), 'sto dziesiąty')
        self.assertEqual(
            num2words(120, lang='pl', to='ordinal'), 'sto dwudziesty')
