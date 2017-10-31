# -*- encoding: utf-8 -*-
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


class Num2WordsRUTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(5, lang='ru'), "пять")
        self.assertEqual(num2words(15, lang='ru'), "пятнадцать")
        self.assertEqual(num2words(154, lang='ru'), "сто пятьдесят четыре")
        self.assertEqual(
            num2words(1135, lang='ru'), "одна тысяча сто тридцать пять"
        )
        self.assertEqual(
            num2words(418531, lang='ru'),
            "четыреста восемнадцать тысяч пятьсот тридцать один"
        )
        self.assertEqual(
            num2words(1000139, lang='ru'), "один миллион сто тридцать девять"
        )

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang='ru'), "пять запятая два")
        self.assertEqual(
            num2words(561.42, lang='ru'),
            "пятьсот шестьдесят один запятая сорок два"
        )

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='ru', to='currency', seperator=' и',
                      cents=False, currency='EUR'),
            "тридцать восемь евро и 40 центов"
        )
