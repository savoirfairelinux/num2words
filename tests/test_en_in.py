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
        self.assertEqual(num2words(1e5, lang="en_IN"), "one lakh")
        self.assertEqual(num2words(1e6, lang="en_IN"), "ten lakh")
        self.assertEqual(num2words(1e7, lang="en_IN"), "one crore")

    def test_negative_decimals(self):
        # Comprehensive test for negative decimals including -0.4
        self.assertEqual(num2words(-0.4, lang="en_IN"), "minus zero point four")
        self.assertEqual(num2words(-0.5, lang="en_IN"), "minus zero point five")
        self.assertEqual(num2words(-1.4, lang="en_IN"), "minus one point four")
        self.assertEqual(num2words(-10.25, lang="en_IN"), "minus ten point two five")
