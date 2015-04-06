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
        # ref https://github.com/savoirfairelinux/num2words/issues/18
        self.assertEqual(num2words(5, ordinal=True, lang='fr'), "cinquième")
        self.assertEqual(num2words(35, ordinal=True, lang='fr'), "trente-cinquième")
        self.assertEqual(num2words(9, ordinal=True, lang='fr'), "neuvième")
        self.assertEqual(num2words(49, ordinal=True, lang='fr'), "quarante-neuvième")

