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


class Num2WordsHETest(TestCase):
    maxDiff = None

    def test_0(self):
        self.assertEqual(num2words(0, lang="he"), u'אפס')

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="he"), u'אחת')
        self.assertEqual(num2words(2, lang="he"), u'שתים')
        self.assertEqual(num2words(7, lang="he"), u'שבע')
        self.assertEqual(num2words(10, lang="he"), u'עשר')

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="he"), u'אחת עשרה')
        self.assertEqual(num2words(13, lang="he"), u'שלש עשרה')
        self.assertEqual(num2words(15, lang="he"), u'חמש עשרה')
        self.assertEqual(num2words(16, lang="he"), u'שש עשרה')
        self.assertEqual(num2words(19, lang="he"), u'תשע עשרה')

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="he"), u'עשרים')
        self.assertEqual(num2words(23, lang="he"), u'עשרים ושלש')
        self.assertEqual(num2words(28, lang="he"), u'עשרים ושמונה')
        self.assertEqual(num2words(31, lang="he"), u'שלשים ואחת')
        self.assertEqual(num2words(40, lang="he"), u'ארבעים')
        self.assertEqual(num2words(66, lang="he"), u'ששים ושש')
        self.assertEqual(num2words(92, lang="he"), u'תשעים ושתים')

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="he"), u'מאה')
        self.assertEqual(num2words(111, lang="he"), u'מאה ואחת עשרה')
        self.assertEqual(num2words(150, lang="he"), u'מאה וחמישים')
        self.assertEqual(num2words(196, lang="he"), u'מאה תשעים ושש')
        self.assertEqual(num2words(200, lang="he"), u'מאתיים')
        self.assertEqual(num2words(210, lang="he"), u'מאתיים ועשר')
        self.assertEqual(num2words(701, lang="he"), u'שבע מאות ואחת')

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="he"), u'אלף')
        self.assertEqual(num2words(1001, lang="he"), u'אלף ואחת')
        self.assertEqual(num2words(1500, lang="he"), u'אלף וחמש מאות')
        self.assertEqual(
            num2words(7378, lang="he"), u'שבעת אלפים שלש מאות שבעים ושמונה'
        )
        self.assertEqual(num2words(2000, lang="he"), u'אלפיים')
        self.assertEqual(num2words(2100, lang="he"), u'אלפיים ומאה')
        self.assertEqual(
            num2words(6870, lang="he"), u'ששת אלפים שמונה מאות ושבעים'
        )
