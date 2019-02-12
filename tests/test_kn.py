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


class Num2WordsKNTest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(42, lang="kn"), u"ನಲವತ್ತ್ ಎರಡು")
        self.assertEqual(num2words(893, lang="kn"), u"ಎಂಟು ನೂರು ತೊಂಬತ್ತ ಮೂರು")
        self.assertEqual(
            num2words(1729, lang="kn"), u"ಒಂದು ಸಾವಿರ ಏಳು ನೂರು ಇಪ್ಪತ್ತ್ಒಂಬತ್ತು"
        )

    def test_ordinals(self):
        self.assertEqual(num2words(2, lang="kn", ordinal=True), u"ಎರಡನೇ")
        self.assertEqual(num2words(5, lang="kn", ordinal=True), u"ಐದನೇ")
        self.assertEqual(num2words(16, lang="kn", ordinal=True), u"ಹದಿನಾರನೇ")
