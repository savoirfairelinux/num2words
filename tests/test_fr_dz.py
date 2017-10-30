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

from num2words.lang_FR_DZ import to_currency


class Num2WordsPLTest(TestCase):
    def test_currency(self):
        self.assertEqual(
            to_currency(1234.12),
            "mille deux cent trente-quatre dinards virgule douze centimes"
        )
        self.assertEqual(
            to_currency(45689.89),
            "quarante-cinq mille six cent quatre-vingt-neuf dinards virgule "
            "quatre-vingt-neuf centimes"
        )
