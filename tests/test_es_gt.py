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

from num2words import num2words

from . import test_es

TEST_CASES_TO_CURRENCY = (
    (1, 'un quetzal'),
    (2, 'dos quetzales'),
    (8, 'ocho quetzales'),
    (12, 'doce quetzales'),
    (21, 'veintiun quetzales'),
    (81.25, 'ochenta y un quetzales y veinticinco centavos'),
    (100, 'cien quetzales'),
)


class Num2WordsESGTTest(test_es.Num2WordsESTest):

    def test_number(self):
        for test in test_es.TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='es_GT'), test[1])

    def test_ordinal(self):
        for test in test_es.TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='es_GT', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in test_es.TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='es_GT', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='es_GT', to='currency'),
                test[1]
            )
