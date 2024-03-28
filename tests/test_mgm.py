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

from decimal import Decimal
from unittest import TestCase, skip

from num2words import num2words
from num2words.lang_MGM import Num2Word_MGM


class Num2WordsMGMTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_MGM()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='mgm'), 'id')
        self.assertEqual(num2words(2, lang='mgm'), 'ru')
        self.assertEqual(num2words(3, lang='mgm'), 'teil')
        self.assertEqual(num2words(4, lang='mgm'), 'haat')
        self.assertEqual(num2words(5, lang='mgm'), 'lima')
        self.assertEqual(num2words(6, lang='mgm'), 'neen')
        self.assertEqual(num2words(7, lang='mgm'), 'hitu')
        self.assertEqual(num2words(8, lang='mgm'), 'walu')
        self.assertEqual(num2words(9, lang='mgm'), 'sia')
        self.assertEqual(num2words(10, lang='mgm'), 'sanulu')
        self.assertEqual(num2words(11, lang='mgm'), 'sanulu resin ida')
        self.assertEqual(num2words(12, lang='mgm'), 'sanulu resin rua')
        self.assertEqual(num2words(13, lang='mgm'), 'sanulu resin tolu')
        self.assertEqual(num2words(14, lang='mgm'), 'sanulu resin haat')
        self.assertEqual(num2words(15, lang='mgm'), 'sanulu resin lima')
        self.assertEqual(num2words(16, lang='mgm'), 'sanulu resin neen')
        self.assertEqual(num2words(17, lang='mgm'), 'sanulu resin hitu')
        self.assertEqual(num2words(18, lang='mgm'), 'sanulu resin walu')
        self.assertEqual(num2words(19, lang='mgm'), 'sanulu resin sia')
        self.assertEqual(num2words(20, lang='mgm'), 'ruanulu')

        self.assertEqual(num2words(21, lang='mgm'), 'ruanulu resin ida')
        self.assertEqual(num2words(22, lang='mgm'), 'ruanulu resin rua')
        self.assertEqual(num2words(35, lang='mgm'), 'tolunulu resin lima')
        self.assertEqual(num2words(99, lang='mgm'), 'sianulu resin sia')

        self.assertEqual(num2words(100, lang='mgm'), 'atus ida')
        self.assertEqual(num2words(101, lang='mgm'), 'atus ida resin ida')
        self.assertEqual(num2words(107, lang='mgm'), 'atus ida resin hitu')
        self.assertEqual(num2words(110, lang='mgm'), 'atus ida sanulu')
        self.assertEqual(num2words(114, lang='mgm'), 'atus ida sanulu resin haat')
        self.assertEqual(num2words(128, lang='mgm'), 'atus ida ruanulu resin walu')
        self.assertEqual(num2words(151, lang='mgm'), 'atus ida limanulu resin ida')
        self.assertEqual(num2words(713, lang='mgm'), 'atus hitu sanulu resin tolu')
        self.assertEqual(num2words(999, lang='mgm'), 'atus sia sianulu resin sia')

        self.assertEqual(num2words(1000, lang='mgm'), 'rihun ida')
        self.assertEqual(num2words(1001, lang='mgm'), 'rihun ida resin ida')
        self.assertEqual(num2words(1011, lang='mgm'), 'rihun ida sanulu resin ida')
        self.assertEqual(num2words(1111, lang='mgm'), 'rihun ida atus ida sanulu resin ida')
        self.assertEqual(num2words(2357, lang='mgm'), 'rihun rua atus tolu limanulu resin hitu')
        self.assertEqual(
            num2words(2200, lang='mgm'),
            'rihun rua atus rua'
        )
        self.assertEqual(num2words(2230, lang='mgm'), 'rihun rua atus rua tolunulu')
        self.assertEqual(num2words(73400, lang='mgm'), 'rihun hitunulu resin tolu atus haat')
        self.assertEqual(num2words(73421, lang='mgm'), 'rihun hitunulu resin tolu atus haat ruanulu resin ida')
        self.assertEqual(num2words(100000, lang='mgm'), 'rihun atus ida')
        self.assertEqual(num2words(250050, lang='mgm'), 'rihun atus rua limanulu limanulu')
        self.assertEqual(
            num2words(6000000, lang='mgm'), 'miliaun neen'
        )
        self.assertEqual(
            num2words(100000000, lang='mgm'), 'miliaun atus ida'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm'), 'miliaun rihun sanulu resin sia'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm'),
            'miliaun rihun atus ida haatnulu resin lima resin rua'
        )
        self.assertEqual(
            num2words(4635102, lang='mgm'),
            'miliaun haat rihun atus neen tolunulu resin lima atus ida resin rua'
        )
        self.assertEqual(
            num2words(145254635102, lang='mgm'),
            'miliaun rihun atus ida haatnulu resin lima atus rua limanulu resin haat rihun atus neen tolunulu resin lima atus ida resin rua'
        )
        self.assertEqual(
            num2words(1000000000000, lang='mgm'),
            'biliaun ida'
        )
        self.assertEqual(
            num2words(2000000000000, lang='mgm'),
            'biliaun rua'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='mgm'),
            'biliaun rihun ida'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='mgm'),
            'biliaun rihun rua'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='mgm'),
            'triliaun ida'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='mgm'),
            'triliaun rua'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='mgm'), 'menus ida')
        self.assertEqual(
            num2words(-256, lang='mgm'), 'menus atus rua limanulu resin neen'
        )
        self.assertEqual(num2words(-1000, lang='mgm'), 'menus rihun ida')
        self.assertEqual(num2words(-1000000, lang='mgm'), 'menus miliaun ida')
        self.assertEqual(
            num2words(-1234567, lang='mgm'),
            'menus miliaun ida rihun atus rua tolunulu resin haat atus lima neenulu resin hitu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='mgm'), 'ida')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='mgm'), 'ida vírgula zero ida')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='mgm'), 'ida vírgula zero tolu lima'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='mgm'), 'ida vírgula tolu lima'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='mgm'),
            'tolu vírgula ida haat ida lima sia'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='mgm'),
            'atus ida resin ida vírgula rua rua'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='mgm'),
            'rihun rua atus tolu haatnulu resin lima vírgula hitu lima'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='mgm'),
            'menus rua vírgula tolu haat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='mgm'),
            'menus sia vírgula sia sia'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='mgm'),
            'menus hitu vírgula zero ida'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='mgm'),
            'menus atus rua ruanulu resin rua vírgula rua rua'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='mgm', ordinal=True), 'primeiru')
        self.assertEqual(num2words(2, lang='mgm', ordinal=True), 'segundu')
        self.assertEqual(num2words(3, lang='mgm', ordinal=True), 'terceiru')
        self.assertEqual(num2words(4, lang='mgm', ordinal=True), 'quartu')
        self.assertEqual(num2words(5, lang='mgm', ordinal=True), 'quintu')
        self.assertEqual(num2words(6, lang='mgm', ordinal=True), 'sextu')
        self.assertEqual(num2words(7, lang='mgm', ordinal=True), 'sétimu')
        self.assertEqual(num2words(8, lang='mgm', ordinal=True), 'oitavu')
        self.assertEqual(num2words(9, lang='mgm', ordinal=True), 'nonu')
        self.assertEqual(num2words(10, lang='mgm', ordinal=True), 'décimu')
        self.assertEqual(
            num2words(11, lang='mgm', ordinal=True), 'décimu primeiru'
        )
        self.assertEqual(
            num2words(12, lang='mgm', ordinal=True), 'décimu segundu'
        )
        self.assertEqual(
            num2words(13, lang='mgm', ordinal=True), 'décimu terceiru'
        )
        self.assertEqual(
            num2words(14, lang='mgm', ordinal=True), 'décimu quartu'
        )
        self.assertEqual(
            num2words(15, lang='mgm', ordinal=True), 'décimu quintu'
        )
        self.assertEqual(
            num2words(16, lang='mgm', ordinal=True), 'décimu sextu'
        )
        self.assertEqual(
            num2words(17, lang='mgm', ordinal=True), 'décimu sétimu'
        )
        self.assertEqual(
            num2words(18, lang='mgm', ordinal=True), 'décimu oitavu'
        )
        self.assertEqual(
            num2words(19, lang='mgm', ordinal=True), 'décimu nonu'
        )
        self.assertEqual(
            num2words(20, lang='mgm', ordinal=True), 'vigésimu'
        )

        self.assertEqual(
            num2words(21, lang='mgm', ordinal=True), 'vigésimu primeiru'
        )
        self.assertEqual(
            num2words(22, lang='mgm', ordinal=True), 'vigésimu segundu'
        )
        self.assertEqual(
            num2words(35, lang='mgm', ordinal=True), 'trigésimu quintu'
        )
        self.assertEqual(
            num2words(99, lang='mgm', ordinal=True), 'nonagésimu nonu'
        )

        self.assertEqual(
            num2words(100, lang='mgm', ordinal=True), 'centésimu'
        )
        self.assertEqual(
            num2words(101, lang='mgm', ordinal=True), 'centésimu primeiru'
        )
        self.assertEqual(
            num2words(128, lang='mgm', ordinal=True),
            'centésimu vigésimu oitavu'
        )
        self.assertEqual(
            num2words(713, lang='mgm', ordinal=True),
            'septigentésimu décimu terceiru'
        )

        self.assertEqual(
            num2words(1000, lang='mgm', ordinal=True), 'milésimu'
        )
        self.assertEqual(
            num2words(1001, lang='mgm', ordinal=True), 'milésimu primeiru'
        )
        self.assertEqual(
            num2words(1111, lang='mgm', ordinal=True),
            'milésimu centésimu décimu primeiru'
        )
        self.assertEqual(
            num2words(2114, lang='mgm', ordinal=True),
            'segundu milésimu centésimu décimu quartu'
        )
        self.assertEqual(
            num2words(73421, lang='mgm', ordinal=True),
            'septuagésimu terceiru milésimu quadrigentésimu vigésimu primeiru'
        )

        self.assertEqual(
            num2words(100000, lang='mgm', ordinal=True),
            'centésimu milésimu'
        )
        self.assertEqual(
            num2words(250050, lang='mgm', ordinal=True),
            'ducentésimu quinquagésimu milésimu quinquagésimu'
        )
        self.assertEqual(
            num2words(6000000, lang='mgm', ordinal=True), 'sextu milionésimu'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm', ordinal=True),
            'décimu nonu milésimu milionésimu'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm', ordinal=True),
            'centésimu quadragésimu quintu milésimu milionésimu segundu'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'ida euru')
        self.assertEqual(self.n2w.to_currency(2.00), 'rua eurus')
        self.assertEqual(self.n2w.to_currency(3.00), 'tolu eurus')
        self.assertEqual(self.n2w.to_currency(4.00), 'haat eurus')
        self.assertEqual(self.n2w.to_currency(5.00), 'lima eurus')
        self.assertEqual(self.n2w.to_currency(6.00), 'neen eurus')
        self.assertEqual(self.n2w.to_currency(7.00), 'hitu eurus')
        self.assertEqual(self.n2w.to_currency(8.00), 'walu eurus')
        self.assertEqual(self.n2w.to_currency(9.00), 'sia eurus')
        self.assertEqual(self.n2w.to_currency(10.00), 'sanulu eurus')
        self.assertEqual(self.n2w.to_currency(11.00), 'sanulu resin ida eurus')
        self.assertEqual(self.n2w.to_currency(12.00), 'sanulu resin rua eurus')
        self.assertEqual(self.n2w.to_currency(13.00), 'sanulu resin tolu eurus')
        self.assertEqual(self.n2w.to_currency(14.00), 'sanulu resin haat eurus')
        self.assertEqual(self.n2w.to_currency(15.00), 'sanulu resin lima eurus')
        self.assertEqual(self.n2w.to_currency(16.00), 'sanulu resin neen eurus')
        self.assertEqual(self.n2w.to_currency(17.00), 'sanulu resin hitu eurus')
        self.assertEqual(self.n2w.to_currency(18.00), 'sanulu resin walu eurus')
        self.assertEqual(self.n2w.to_currency(19.00), 'sanulu resin sia eurus')
        self.assertEqual(self.n2w.to_currency(20.00), 'ruanulu eurus')

        self.assertEqual(self.n2w.to_currency(21.00), 'ruanulu resin ida eurus')
        self.assertEqual(self.n2w.to_currency(22.00), 'ruanulu resin rua eurus')
        self.assertEqual(self.n2w.to_currency(35.00), 'tolunulu resin lima eurus')
        self.assertEqual(self.n2w.to_currency(99.00), 'sianulu resin sia eurus')

        self.assertEqual(self.n2w.to_currency(100.00), 'atus ida eurus')
        self.assertEqual(self.n2w.to_currency(101.00), 'atus ida resin ida eurus')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'atus ida ruanulu resin walu eurus'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'atus hitu sanulu resin tolu eurus')

        self.assertEqual(self.n2w.to_currency(1000.00), 'rihun ida eurus')
        self.assertEqual(self.n2w.to_currency(1001.00), 'rihun ida resin ida eurus')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'rihun ida atus ida sanulu resin ida eurus')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'rihun rua atus ida sanulu resin haat eurus'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'rihun hitunulu resin tolu atus haat ruanulu resin ida eurus'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'rihun atus ida eurus')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'rihun atus rua limanulu limanulu eurus'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'miliaun neen eurus'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'miliaun rihun sanulu resin sia eurus'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'miliaun rihun atus ida haatnulu resin lima resin rua eurus'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'ida dólar')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'ida dólar resin limanulu cêntimus')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus ida euru')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus atus rua limanulu resin neen eurus'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus rihun ida eurus')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus miliaun ida eurus'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus miliaun ida rihun atus rua tolunulu resin haat atus lima neenulu resin hitu eurus'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'ida euru')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'ida euru resin ida cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'ida euru resin tolu cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'ida euru resin tolunulu resin lima cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'tolu eurus resin sanulu resin haat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'atus ida resin ida eurus resin ruanulu resin rua cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'rihun rua atus tolu haatnulu resin lima eurus resin hitunulu resin lima cêntimus'

        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus rua eurus resin tolunulu resin haat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus sia eurus resin sianulu resin sia cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus hitu eurus resin ida cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus atus rua ruanulu resin rua eurus resin ruanulu resin rua cêntimus'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihun ida resin ida')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihun ida atus hitu walunulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihun ida atus sia haatnulu resin rua'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihun ida atus sia walunulu resin haat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihun rua')
        self.assertEqual(self.n2w.to_year(2001), 'rihun rua resin ida')
        self.assertEqual(self.n2w.to_year(2016), 'rihun rua sanulu resin neen')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'tolunulu antes Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atus hitu haatnulu resin haat antes Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'rihun sanulu antes Kristu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
