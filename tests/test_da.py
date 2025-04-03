# coding: utf-8
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
from num2words.lang_DA import Num2Word_DA


class Num2WordsDKTest(TestCase):
    def test_ordinal(self):
        self.assertEqual(num2words(1, to="ordinal", lang="da"), "første")
        self.assertEqual(num2words(5, to="ordinal", lang="da"), "femte")

    def test_cardinal(self):
        self.assertEqual(num2words(0, to="cardinal", lang="da"), "nul")
        self.assertEqual(num2words(1, to="cardinal", lang="da"), "et")
        self.assertEqual(num2words(2, to="cardinal", lang="da"), "to")
        self.assertEqual(num2words(5, to="cardinal", lang="da"), "fem")
        self.assertEqual(num2words(8, to="cardinal", lang="da"), "otte")
        self.assertEqual(num2words(18, to="cardinal", lang="da"), "atten")
        self.assertEqual(num2words(45, to="cardinal", lang="da"), "femogfyrre")

    def test_to_ordinal_num(self):
        num2words_dk = Num2Word_DA()
        self.assertEqual(num2words_dk.to_ordinal_num(1), "1te")
        self.assertEqual(num2words_dk.to_ordinal_num(2), "2en")
        self.assertEqual(num2words_dk.to_ordinal_num(5), "5te")
        self.assertEqual(num2words_dk.to_ordinal_num(10), "10ende")
