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


class Num2WordsHiTest(TestCase):
    def test_cardinal_for_integers(self):
        self.assertEqual(num2words(199, lang='hi'), 'एक सौ निन्यानवे')
        self.assertEqual(num2words(58, lang='hi'), 'अठावन')
        self.assertEqual(num2words(1214558, lang='hi'),
                         'बारह लाख चौदह हज़ार पांच सौ अठावन')
        self.assertEqual(num2words(521214558, lang='hi'),
                         'बावन करोड़ बारह लाख चौदह हज़ार पांच सौ अठावन')

    def test_cardinal_for_float_number(self):
        self.assertEqual(
          num2words(12.5, lang='hi'), "बारह दशमलव पांच")
        self.assertEqual(
          num2words(12.51, lang='hi'), "बारह दशमलव पांच एक")
