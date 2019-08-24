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
    (1, 'un bolívar'),
    (2, 'dos bolívares'),
    (8, 'ocho bolívares'),
    (12, 'doce bolívares'),
    (21, 'veintiun bolívares'),
    (81.25, 'ochenta y un bolívares y veinticinco centavos'),
    (100, 'cien bolívares'),
)


class Num2WordsESVETest(test_es.Num2WordsESTest):

    def test_number(self):
        for test in test_es.TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='es_VE'), test[1])

    def test_ordinal(self):
        for test in test_es.TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='es_VE', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in test_es.TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='es', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='es_VE', to='currency', old=True),
                test[1]
            )
