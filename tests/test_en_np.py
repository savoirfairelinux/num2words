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


class Num2WordsENINTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(1e5, lang="en_NP"), "one lakh")
        self.assertEqual(num2words(1e6, lang="en_NP"), "ten lakh")
        self.assertEqual(num2words(1e7, lang="en_NP"), "one crore")
        self.assertEqual(num2words(1e8, lang="en_NP"), "ten crore")
        self.assertEqual(num2words(1e9, lang="en_NP"), "one arba")
        self.assertEqual(num2words(1e10, lang="en_NP"), "ten arba")
        self.assertEqual(num2words(1e11, lang="en_NP"), "one kharba")
        self.assertEqual(num2words(1e12, lang="en_NP"), "ten kharba")
        self.assertEqual(num2words(1e13, lang="en_NP"), "one neel")
        self.assertEqual(num2words(1e14, lang="en_NP"), "ten neel")
        self.assertEqual(num2words(1e15, lang="en_NP"), "one padam")
        self.assertEqual(num2words(1e16, lang="en_NP"), "ten padam")
        self.assertEqual(num2words(1e17, lang="en_NP"), "one shankha")
        self.assertEqual(num2words(1e18, lang="en_NP"), "ten shankha")
      
