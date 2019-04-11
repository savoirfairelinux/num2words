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

from . import test_fr

TEST_CASES_TO_CURRENCY = (
    (1, 'un dinard'),
    (2, 'deux dinards'),
    (8, 'huit dinards'),
    (12, 'douze dinards'),
    (21, 'vingt et un dinards'),
    (81.25, 'quatre-vingt-un dinards et vingt-cinq centimes'),
    (100, 'cent dinards'),
)


class Num2WordsPLTest(TestCase):
    def test_currency(self):
        self.assertEqual(
            num2words(1234.12, lang='fr_DZ', to='currency'),
            "mille deux cent trente-quatre dinards et douze centimes"
        )
        self.assertEqual(
            num2words(45689.89, lang='fr_DZ', to='currency'),
            "quarante-cinq mille six cent quatre-vingt-neuf dinards et "
            "quatre-vingt-neuf centimes"
        )

    def test_number(self):
        for test in test_fr.TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='fr_DZ'), test[1])

    def test_ordinal(self):
        for test in test_fr.TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='fr_DZ', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in test_fr.TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='fr_DZ', to='ordinal_num'),
                test[1]
            )
