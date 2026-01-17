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

from unittest import TestCase

from num2words import num2words


class Num2WordsSNTest(TestCase):
    """Test cases for Shona language (sn)."""

    def test_cardinal_zero(self):
        self.assertEqual(num2words(0, lang='sn'), 'chiposhi')

    def test_cardinal_ones(self):
        self.assertEqual(num2words(1, lang='sn'), 'motsi')
        self.assertEqual(num2words(2, lang='sn'), 'piri')
        self.assertEqual(num2words(3, lang='sn'), 'tatu')
        self.assertEqual(num2words(4, lang='sn'), 'ina')
        self.assertEqual(num2words(5, lang='sn'), 'shanu')
        self.assertEqual(num2words(6, lang='sn'), 'tanhatu')
        self.assertEqual(num2words(7, lang='sn'), 'nomwe')
        self.assertEqual(num2words(8, lang='sn'), 'sere')
        self.assertEqual(num2words(9, lang='sn'), 'pfumbamwe')

    def test_cardinal_teens(self):
        self.assertEqual(num2words(10, lang='sn'), 'gumi')
        self.assertEqual(num2words(11, lang='sn'), 'gumi nemotsi')
        self.assertEqual(num2words(12, lang='sn'), 'gumi nepiri')
        self.assertEqual(num2words(13, lang='sn'), 'gumi netatu')
        self.assertEqual(num2words(14, lang='sn'), 'gumi neina')
        self.assertEqual(num2words(15, lang='sn'), 'gumi neshanu')
        self.assertEqual(num2words(16, lang='sn'), 'gumi netanhatu')
        self.assertEqual(num2words(17, lang='sn'), 'gumi nenomwe')
        self.assertEqual(num2words(18, lang='sn'), 'gumi nesere')
        self.assertEqual(num2words(19, lang='sn'), 'gumi nepfumbamwe')

    def test_cardinal_tens(self):
        self.assertEqual(num2words(20, lang='sn'), 'makumi maviri')
        self.assertEqual(num2words(30, lang='sn'), 'makumi matatu')
        self.assertEqual(num2words(40, lang='sn'), 'makumi mana')
        self.assertEqual(num2words(50, lang='sn'), 'makumi mashanu')
        self.assertEqual(num2words(60, lang='sn'), 'makumi matanhatu')
        self.assertEqual(num2words(70, lang='sn'), 'makumi manomwe')
        self.assertEqual(num2words(80, lang='sn'), 'makumi masere')
        self.assertEqual(num2words(90, lang='sn'), 'makumi mapfumbamwe')

    def test_cardinal_compound(self):
        self.assertEqual(num2words(21, lang='sn'), 'makumi maviri nemotsi')
        self.assertEqual(num2words(35, lang='sn'), 'makumi matatu neshanu')
        self.assertEqual(num2words(42, lang='sn'), 'makumi mana nepiri')
        self.assertEqual(num2words(99, lang='sn'),
                         'makumi mapfumbamwe nepfumbamwe')

    def test_cardinal_hundreds(self):
        self.assertEqual(num2words(100, lang='sn'), 'zana')
        self.assertEqual(num2words(101, lang='sn'), 'zana nemotsi')
        self.assertEqual(num2words(110, lang='sn'), 'zana negumi')
        self.assertEqual(num2words(123, lang='sn'),
                         'zana nemakumi maviri netatu')
        self.assertEqual(num2words(200, lang='sn'), 'mazana piri')
        self.assertEqual(num2words(500, lang='sn'), 'mazana shanu')
        self.assertEqual(num2words(999, lang='sn'),
                         'mazana pfumbamwe nemakumi mapfumbamwe nepfumbamwe')

    def test_cardinal_thousands(self):
        self.assertEqual(num2words(1000, lang='sn'), 'chiuru')
        self.assertEqual(num2words(1001, lang='sn'), 'chiuru nemotsi')
        self.assertEqual(num2words(1100, lang='sn'), 'chiuru nezana')
        self.assertEqual(num2words(2000, lang='sn'), 'zviuru piri')
        self.assertEqual(num2words(5000, lang='sn'), 'zviuru shanu')
        self.assertEqual(num2words(10000, lang='sn'), 'zviuru gumi')
        self.assertEqual(num2words(12345, lang='sn'),
                         'zviuru gumi nepiri nemazana tatu '
                         'nemakumi mana neshanu')

    def test_cardinal_millions(self):
        self.assertEqual(num2words(1000000, lang='sn'), 'miriyoni')
        self.assertEqual(num2words(2000000, lang='sn'), 'mamiriyoni piri')
        self.assertEqual(num2words(1234567, lang='sn'),
                         'miriyoni nezviuru mazana piri nemakumi matatu neina '
                         'nemazana shanu nemakumi matanhatu nenomwe')

    def test_cardinal_billions(self):
        self.assertEqual(num2words(1000000000, lang='sn'), 'bhiriyoni')
        self.assertEqual(num2words(2000000000, lang='sn'), 'mabhiriyoni piri')

    def test_ordinal_basic(self):
        self.assertEqual(num2words(1, lang='sn', to='ordinal'), 'wokutanga')
        self.assertEqual(num2words(2, lang='sn', to='ordinal'), 'wechipiri')
        self.assertEqual(num2words(3, lang='sn', to='ordinal'), 'wechitatu')
        self.assertEqual(num2words(4, lang='sn', to='ordinal'), 'wechina')
        self.assertEqual(num2words(5, lang='sn', to='ordinal'), 'wechishanu')
        self.assertEqual(num2words(10, lang='sn', to='ordinal'), 'wechigumi')

    def test_ordinal_compound(self):
        # For compound numbers, the last word gets the ordinal suffix
        self.assertEqual(num2words(21, lang='sn', to='ordinal'),
                         'makumi maviri wechinemotsi')
        self.assertEqual(num2words(100, lang='sn', to='ordinal'), 'wechizana')

    def test_ordinal_num(self):
        self.assertEqual(num2words(1, lang='sn', to='ordinal_num'), '1ga')
        self.assertEqual(num2words(2, lang='sn', to='ordinal_num'), '2ri')
        self.assertEqual(num2words(10, lang='sn', to='ordinal_num'), '10mi')

    def test_cardinal_float(self):
        self.assertEqual(num2words(12.5, lang='sn'),
                         'gumi nepiri poindi shanu')
        self.assertEqual(num2words(0.75, lang='sn'),
                         'chiposhi poindi nomwe shanu')
        self.assertEqual(num2words(123.45, lang='sn'),
                         'zana nemakumi maviri netatu poindi ina shanu')

    def test_negative(self):
        self.assertEqual(num2words(-1, lang='sn'), 'mainasi motsi')
        self.assertEqual(num2words(-42, lang='sn'),
                         'mainasi makumi mana nepiri')

    def test_to_currency(self):
        self.assertEqual(
            num2words('1.50', lang='sn', to='currency', currency='ZWL'),
            'motsi dora, makumi mashanu masendi'
        )
        self.assertEqual(
            num2words('10.00', lang='sn', to='currency', currency='ZWL'),
            'gumi madora, chiposhi masendi'
        )

    def test_to_year(self):
        self.assertEqual(num2words(2024, lang='sn', to='year'),
                         'zviuru piri nemakumi maviri neina')
        self.assertEqual(num2words(1990, lang='sn', to='year'),
                         'chiuru nemazana pfumbamwe nemakumi mapfumbamwe')

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words(10 ** 16, lang='sn')
