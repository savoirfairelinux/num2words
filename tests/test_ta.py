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


class Num2WordsTATest(TestCase):
    def test_numbers(self):
        self.assertEqual(num2words(42, lang="ta"), u"நாற்பத்தி இரண்டு")
        self.assertEqual(num2words(893, lang="ta"),
                         u"எட்டு நூறு தொண்ணூற்றி ஏழு,தொண்ணூற்று ஆறு")
        self.assertEqual(num2words(1729, lang="ta"), 
                         u"ஒன்று ஆயிரம் ஏழு நூறு இருபத்து ஒன்பது")
        self.assertEqual(num2words(123, lang="ta"),
                         u"ஒன்று நூறு இருபத்து மூன்று")
        self.assertEqual(num2words(32211, lang="ta"),
                         u"மூன்று முப்பத்தி இரண்டு ஆயிரம் இரண்டு நூறு பதினொரு")

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(3.14, lang="ta"),
                         u"மூன்று புள்ளி ஒன்று நான்கு")
        self.assertEqual(num2words(1.61803, lang="ta"),
                         u"ஒன்று புள்ளி ஆறு ஒன்று எட்டு பூஜ்யம் மூன்று")

    def test_ordinal(self):
        self.assertEqual(
            num2words(1, lang='ta', to='ordinal'),
            u'ஒன்றும்'
        )
        self.assertEqual(
            num2words(22, lang='ta', to='ordinal'),
            u'இருபத்து இரண்டும்'
        )
        self.assertEqual(
            num2words(12, lang='ta', to='ordinal'),
            u'பன்னிரண்டும்'
        )
        self.assertEqual(
            num2words(130, lang='ta', to='ordinal'),
            u'ஒன்று நூறு முப்பதும்'
        )
        self.assertEqual(
            num2words(1003, lang='ta', to='ordinal'),
            u'ஒன்று ஆயிரம் மூன்றும்'
        )
        self.assertEqual(num2words(2, lang="ta", ordinal=True), u"இரண்டும்")
        self.assertEqual(num2words(5, lang="ta", ordinal=True), u"ஐந்தும்")
        self.assertEqual(num2words(16, lang="ta", ordinal=True), u"பதினாறும்")
        self.assertEqual(num2words(113, lang="ta", ordinal=True),
                         u"ஒன்று நூறு பதின்மூன்றும்")

    def test_ordinal_num(self):
        self.assertEqual(
            num2words(2, lang="ta", to='ordinal_num'), u"2இரண்டும்")
        self.assertEqual(
            num2words(5, lang="ta", to='ordinal_num'), u"5ஐந்தும்")
        self.assertEqual(num2words(16, lang="ta", to='ordinal_num'),
                         u"16பதினாறும்")
        self.assertEqual(num2words(113, lang="ta", to='ordinal_num'),
                         u"113ஒன்று நூறு பதின்மூன்றும்")
