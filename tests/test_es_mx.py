# encoding: UTF-8
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
    (1, 'un peso, 00/100 M. N.'),
    (2, 'dos pesos, 00/100 M. N.'),
    (8, 'ocho pesos, 00/100 M. N.'),
    (12, 'doce pesos, 00/100 M. N.'),
    (21, 'veintiun pesos, 00/100 M. N.'),
    (81.25, 'ochenta y un pesos, 25/100 M. N.'),
    (100, 'cien pesos, 00/100 M. N.'),
)


class Num2WordsESMXTest(test_es.Num2WordsESTest):

    def test_number(self):
        for test in test_es.TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='es_MX'), test[1])

    def test_ordinal(self):
        for test in test_es.TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='es_MX', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in test_es.TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='es_MX', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='es_MX', to='currency'),
                test[1]
            )
