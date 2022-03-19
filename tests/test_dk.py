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


class Num2WordsDKTest(TestCase):
    def test_ordinal(self):
        self.assertEqual(num2words(1, to="ordinal", lang="dk"), "første")
        self.assertEqual(num2words(5, to="ordinal", lang="dk"), "femte")

    def test_cardinal(self):
        self.assertEqual(num2words(0, to="cardinal", lang="dk"), "nul")
        self.assertEqual(num2words(1, to="cardinal", lang="dk"), "et")
        self.assertEqual(num2words(2, to="cardinal", lang="dk"), "to")
        self.assertEqual(num2words(5, to="cardinal", lang="dk"), "fem")
        self.assertEqual(num2words(8, to="cardinal", lang="dk"), "otte")
        self.assertEqual(num2words(18, to="cardinal", lang="dk"), "atten")
        self.assertEqual(num2words(45, to="cardinal", lang="dk"), "femogfyrre")
