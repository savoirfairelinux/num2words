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
from num2words.lang_TET import Num2Word_TET


class Num2WordsTETTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_TET()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='tet'), 'ida')
        self.assertEqual(num2words(2, lang='tet'), 'rua')
        self.assertEqual(num2words(3, lang='tet'), 'tolu')
        self.assertEqual(num2words(4, lang='tet'), 'haat')
        self.assertEqual(num2words(5, lang='tet'), 'lima')
        self.assertEqual(num2words(6, lang='tet'), 'neen')
        self.assertEqual(num2words(7, lang='tet'), 'hitu')
        self.assertEqual(num2words(8, lang='tet'), 'walu')
        self.assertEqual(num2words(9, lang='tet'), 'sia')
        self.assertEqual(num2words(10, lang='tet'), 'sanulu')
        self.assertEqual(num2words(11, lang='tet'), 'sanulu resin ida')
        self.assertEqual(num2words(12, lang='tet'), 'sanulu resin rua')
        self.assertEqual(num2words(13, lang='tet'), 'sanulu resin tolu')
        self.assertEqual(num2words(14, lang='tet'), 'sanulu resin haat')
        self.assertEqual(num2words(15, lang='tet'), 'sanulu resin lima')
        self.assertEqual(num2words(16, lang='tet'), 'sanulu resin neen')
        self.assertEqual(num2words(17, lang='tet'), 'sanulu resin hitu')
        self.assertEqual(num2words(18, lang='tet'), 'sanulu resin walu')
        self.assertEqual(num2words(19, lang='tet'), 'sanulu resin sia')
        self.assertEqual(num2words(20, lang='tet'), 'ruanulu')

        self.assertEqual(num2words(21, lang='tet'), 'ruanulu resin ida')
        self.assertEqual(num2words(22, lang='tet'), 'ruanulu resin rua')
        self.assertEqual(num2words(35, lang='tet'), 'tolunulu resin lima')
        self.assertEqual(num2words(99, lang='tet'), 'sianulu resin sia')

        self.assertEqual(num2words(100, lang='tet'), 'atus ida')
        self.assertEqual(num2words(101, lang='tet'), 'atus ida resin ida')
        self.assertEqual(num2words(107, lang='tet'), 'atus ida resin hitu')
        self.assertEqual(num2words(110, lang='tet'), 'atus ida sanulu')
        self.assertEqual(num2words(114, lang='tet'), 'atus ida sanulu resin haat')
        self.assertEqual(num2words(128, lang='tet'), 'atus ida ruanulu resin walu')
        self.assertEqual(num2words(151, lang='tet'), 'atus ida limanulu resin ida')
        self.assertEqual(num2words(713, lang='tet'), 'atus hitu sanulu resin tolu')
        self.assertEqual(num2words(999, lang='tet'), 'atus sia sianulu resin sia')

        self.assertEqual(num2words(1000, lang='tet'), 'rihun ida')
        self.assertEqual(num2words(1001, lang='tet'), 'rihun ida resin ida')
        self.assertEqual(num2words(1011, lang='tet'), 'rihun ida sanulu resin ida')
        self.assertEqual(num2words(1111, lang='tet'), 'rihun ida atus ida sanulu resin ida')
        self.assertEqual(num2words(2357, lang='tet'), 'rihun rua atus tolu limanulu resin hitu')
        self.assertEqual(
            num2words(2200, lang='tet'),
            'rihun rua atus rua'
        )
        self.assertEqual(num2words(2230, lang='tet'), 'rihun rua atus rua tolunulu')
        self.assertEqual(num2words(73400, lang='tet'), 'rihun hitunulu resin tolu atus haat')
        self.assertEqual(num2words(73421, lang='tet'), 'rihun hitunulu resin tolu atus haat ruanulu resin ida')
        self.assertEqual(num2words(100000, lang='tet'), 'rihun atus ida')
        self.assertEqual(num2words(250050, lang='tet'), 'rihun atus rua limanulu limanulu')
        self.assertEqual(
            num2words(6000000, lang='tet'), 'miliaun neen'
        )
        self.assertEqual(
            num2words(100000000, lang='tet'), 'miliaun atus ida'
        )
        self.assertEqual(
            num2words(19000000000, lang='tet'), 'miliaun rihun sanulu resin sia'
        )
        self.assertEqual(
            num2words(145000000002, lang='tet'),
            'miliaun rihun atus ida haatnulu resin lima resin rua'
        )
        self.assertEqual(
            num2words(4635102, lang='tet'),
            'miliaun haat rihun atus neen tolunulu resin lima atus ida resin rua'
        )
        self.assertEqual(
            num2words(145254635102, lang='tet'),
            'miliaun rihun atus ida haatnulu resin lima atus rua limanulu resin haat rihun atus neen tolunulu resin lima atus ida resin rua'
        )
        self.assertEqual(
            num2words(1000000000000, lang='tet'),
            'biliaun ida'
        )
        self.assertEqual(
            num2words(2000000000000, lang='tet'),
            'biliaun rua'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='tet'),
            'biliaun rihun ida'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='tet'),
            'biliaun rihun rua'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='tet'),
            'triliaun ida'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='tet'),
            'triliaun rua'
        )

    #@skip("not implemented yet")
    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='tet'), 'menus ida')
        self.assertEqual(
            num2words(-256, lang='tet'), 'menus atus rua limanulu resin neen'
        )
        self.assertEqual(num2words(-1000, lang='tet'), 'menus rihun ida')
        self.assertEqual(num2words(-1000000, lang='tet'), 'menus miliaun ida')
        self.assertEqual(
            num2words(-1234567, lang='tet'),
            'menus miliaun ida rihun atus rua tolunulu resin haat atus lima neenulu resin hitu'
        )

    #@skip("not implemented yet")
    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='tet'), 'ida')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='tet'), 'ida vírgula zero ida')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='tet'), 'ida vírgula zero tolu lima'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='tet'), 'ida vírgula tolu lima'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='tet'),
            'tolu vírgula ida haat ida lima sia'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='tet'),
            'atus ida resin ida vírgula rua rua'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='tet'),
            'rihun rua atus tolu haatnulu resin lima vírgula hitu lima'
        )


    #@skip("not implemented yet")
    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='tet'),
            'menus rua vírgula tolu haat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='tet'),
            'menus sia vírgula sia sia'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='tet'),
            'menus hitu vírgula zero ida'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='tet'),
            'menus atus rua ruanulu resin rua vírgula rua rua'
        )

    #@skip("not implemented yet")
    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='tet', ordinal=True), 'primeiru')
        self.assertEqual(num2words(2, lang='tet', ordinal=True), 'segundu')
        self.assertEqual(num2words(3, lang='tet', ordinal=True), 'terceiru')
        self.assertEqual(num2words(4, lang='tet', ordinal=True), 'quartu')
        self.assertEqual(num2words(5, lang='tet', ordinal=True), 'quintu')
        self.assertEqual(num2words(6, lang='tet', ordinal=True), 'sextu')
        self.assertEqual(num2words(7, lang='tet', ordinal=True), 'sétimu')
        self.assertEqual(num2words(8, lang='tet', ordinal=True), 'oitavu')
        self.assertEqual(num2words(9, lang='tet', ordinal=True), 'nonu')
        self.assertEqual(num2words(10, lang='tet', ordinal=True), 'décimu')
        self.assertEqual(
            num2words(11, lang='tet', ordinal=True), 'décimu primeiru'
        )
        self.assertEqual(
            num2words(12, lang='tet', ordinal=True), 'décimu segundu'
        )
        self.assertEqual(
            num2words(13, lang='tet', ordinal=True), 'décimu terceiru'
        )
        self.assertEqual(
            num2words(14, lang='tet', ordinal=True), 'décimu quartu'
        )
        self.assertEqual(
            num2words(15, lang='tet', ordinal=True), 'décimu quintu'
        )
        self.assertEqual(
            num2words(16, lang='tet', ordinal=True), 'décimu sextu'
        )
        self.assertEqual(
            num2words(17, lang='tet', ordinal=True), 'décimu sétimu'
        )
        self.assertEqual(
            num2words(18, lang='tet', ordinal=True), 'décimu oitavu'
        )
        self.assertEqual(
            num2words(19, lang='tet', ordinal=True), 'décimu nonu'
        )
        self.assertEqual(
            num2words(20, lang='tet', ordinal=True), 'vigésimu'
        )

        self.assertEqual(
            num2words(21, lang='tet', ordinal=True), 'vigésimu primeiru'
        )
        self.assertEqual(
            num2words(22, lang='tet', ordinal=True), 'vigésimu segundu'
        )
        self.assertEqual(
            num2words(35, lang='tet', ordinal=True), 'trigésimu quintu'
        )
        self.assertEqual(
            num2words(99, lang='tet', ordinal=True), 'nonagésimu nonu'
        )

        self.assertEqual(
            num2words(100, lang='tet', ordinal=True), 'centésimu'
        )
        self.assertEqual(
            num2words(101, lang='tet', ordinal=True), 'centésimu primeiru'
        )
        self.assertEqual(
            num2words(128, lang='tet', ordinal=True),
            'centésimu vigésimu oitavu'
        )
        self.assertEqual(
            num2words(713, lang='tet', ordinal=True),
            'septigentésimu décimu terceiru'
        )

        self.assertEqual(
            num2words(1000, lang='tet', ordinal=True), 'milésimu'
        )
        self.assertEqual(
            num2words(1001, lang='tet', ordinal=True), 'milésimu primeiru'
        )
        self.assertEqual(
            num2words(1111, lang='tet', ordinal=True),
            'milésimu centésimu décimu primeiru'
        )
        self.assertEqual(
            num2words(2114, lang='tet', ordinal=True),
            'segundu milésimu centésimu décimu quartu'
        )
        self.assertEqual(
            num2words(73421, lang='tet', ordinal=True),
            'septuagésimu terceiru milésimu quadrigentésimu vigésimu primeiru'
        )

        self.assertEqual(
            num2words(100000, lang='tet', ordinal=True),
            'centésimu milésimu'
        )
        self.assertEqual(
            num2words(250050, lang='tet', ordinal=True),
            'ducentésimu quinquagésimu milésimu quinquagésimu'
        )
        self.assertEqual(
            num2words(6000000, lang='tet', ordinal=True), 'sextu milionésimu'
        )
        self.assertEqual(
            num2words(19000000000, lang='tet', ordinal=True),
            'décimu nonu milésimu milionésimu'
        )
        self.assertEqual(
            num2words(145000000002, lang='tet', ordinal=True),
            'centésimu quadragésimu quintu milésimu milionésimu segundu'
        )

    #@skip("not implemented yet")
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

    @skip("not implemented yet")
    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menos um euro')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menos duzentos e cinquenta e seis euros'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menos mil euros')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menos um milhão de euros'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menos um milhão duzentos e trinta e quatro mil quinhentos e '
            'sessenta e sete euros'
        )

    @skip("not implemented yet")
    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'um euro')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'um euro e um cêntimo'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'um euro e três cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'um euro e trinta e cinco cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'três euros e catorze cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'cento e um euros e vinte e dois cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dois mil trezentos e quarenta e cinco euros e setenta e cinco '
            'cêntimos'
        )

    @skip("not implemented yet")
    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menos dois euros e trinta e quatro cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menos nove euros e noventa e nove cêntimos'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menos sete euros e um cêntimo'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menos duzentos e vinte e dois euros e vinte e dois cêntimos'
        )

    @skip("not implemented yet")
    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'mil e um')
        self.assertEqual(
            self.n2w.to_year(1789), 'mil setecentos e oitenta e nove'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'mil novecentos e quarenta e dois'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'mil novecentos e oitenta e quatro'
        )
        self.assertEqual(self.n2w.to_year(2000), 'dois mil')
        self.assertEqual(self.n2w.to_year(2001), 'dois mil e um')
        self.assertEqual(self.n2w.to_year(2016), 'dois mil e dezasseis')

    @skip("not implemented yet")
    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'trinta antes de Cristo')
        self.assertEqual(
            self.n2w.to_year(-744),
            'setecentos e quarenta e quatro antes de Cristo'
        )
        self.assertEqual(self.n2w.to_year(-10000), 'dez mil antes de Cristo')

    @skip("not implemented yet")
    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
