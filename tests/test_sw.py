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

from unittest import TestCase

from num2words import num2words


class Num2WordsSWTest(TestCase):
    def test_0(self):
        self.assertEqual(num2words(0, lang='sw'), 'sifuri')

    def test_1_to_9(self):
        self.assertEqual(num2words(1, lang='sw'), 'moja')
        self.assertEqual(num2words(2, lang='sw'), 'mbili')
        self.assertEqual(num2words(9, lang='sw'), 'tisa')

    def test_tens_10_to_99(self):
        self.assertEqual(num2words(10, lang='sw'), 'kumi')
        self.assertEqual(num2words(11, lang='sw'), 'kumi na moja')
        self.assertEqual(num2words(20, lang='sw'), 'ishirini')
        self.assertEqual(num2words(27, lang='sw'), 'ishirini na saba')
        self.assertEqual(num2words(90, lang='sw'), 'tisini')
        self.assertEqual(num2words(99, lang='sw'), 'tisini na tisa')

    def test_hundreds_100_to_999(self):
        self.assertEqual(num2words(100, lang='sw'), 'mia moja')
        self.assertEqual(num2words(608, lang='sw'), 'mia sita na nane')
        self.assertEqual(num2words(500, lang='sw'), 'mia tano')
        self.assertEqual(num2words(572, lang='sw'), 'mia tano sabini na mbili')
        self.assertEqual(num2words(700, lang='sw'), 'mia saba')
        self.assertEqual(num2words(999, lang='sw'), 'mia tisa tisini na tisa')

    def test_thousands_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang='sw'), 'elfu moja')
        self.assertEqual(num2words(7000, lang='sw'), 'elfu saba')
        self.assertEqual(num2words(9000, lang='sw'), 'elfu tisa')
        self.assertEqual(
            num2words(1322, lang='sw'), 'moja elfu, mia tatu ishirini na mbili'
        )
        self.assertEqual(
            num2words(6987, lang='sw'), 'sita elfu, mia tisa themanini na saba'
        )
        self.assertEqual(
            num2words(9999, lang='sw'), 'tisa elfu, mia tisa tisini na tisa'
        )
