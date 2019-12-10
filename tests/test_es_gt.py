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

TEST_GTQ = (
    (1.0, 'un quetzal con cero centavos'),
    (2.0, 'dos quetzales con cero centavos'),
    (8.0, 'ocho quetzales con cero centavos'),
    (12.0, 'doce quetzales con cero centavos'),
    (21.0, 'veintiun quetzales con cero centavos'),
    (81.25, 'ochenta y un quetzales con veinticinco centavos'),
    (100.00, 'cien quetzales con cero centavos')
)


class Num2WordsESGTTest(test_es.Num2WordsESTest):

    def test_currency(self):
        for test in TEST_GTQ:
            self.assertEqual(
                num2words(test[0], lang='es_GT', to='currency'),
                test[1]
            )
