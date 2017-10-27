# -*- encoding: utf-8 -*-
# Copyright (c) 2015, Savoir-faire Linux inc.  All Rights Reserved.

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


class Num2WordsENTest(TestCase):
    def test_ordinal_special_joins(self):
        self.assertEqual(
            num2words(5, ordinal=True, lang='fr_CH'), "cinquième"
        )
        self.assertEqual(
            num2words(6, ordinal=True, lang='fr_CH'), "sixième"
        )
        self.assertEqual(
            num2words(35, ordinal=True, lang='fr_CH'), "trente-cinquième"
        )
        self.assertEqual(num2words(9, ordinal=True, lang='fr_CH'), "neuvième")
        self.assertEqual(
            num2words(49, ordinal=True, lang='fr_CH'), "quarante-neuvième"
        )
        self.assertEqual(num2words(71, lang='fr_CH'), "septante et un")
        self.assertEqual(num2words(81, lang='fr_CH'), "huitante et un")
        self.assertEqual(num2words(80, lang='fr_CH'), "huitante")
        self.assertEqual(num2words(880, lang='fr_CH'), "huit cents huitante")
        self.assertEqual(
            num2words(91, ordinal=True, lang='fr_CH'), "nonante et unième"
        )
        self.assertEqual(num2words(53, lang='fr_CH'), "cinquante-trois")
