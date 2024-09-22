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

import decimal
from decimal import Decimal
from unittest import TestCase

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
        self.assertEqual(num2words(8, lang='tet'), 'ualu')
        self.assertEqual(num2words(9, lang='tet'), 'sia')
        self.assertEqual(num2words(10, lang='tet'), 'sanulu')
        self.assertEqual(num2words(11, lang='tet'), 'sanulu resin ida')
        self.assertEqual(num2words(12, lang='tet'), 'sanulu resin rua')
        self.assertEqual(num2words(13, lang='tet'), 'sanulu resin tolu')
        self.assertEqual(num2words(14, lang='tet'), 'sanulu resin haat')
        self.assertEqual(num2words(15, lang='tet'), 'sanulu resin lima')
        self.assertEqual(num2words(16, lang='tet'), 'sanulu resin neen')
        self.assertEqual(num2words(17, lang='tet'), 'sanulu resin hitu')
        self.assertEqual(num2words(18, lang='tet'), 'sanulu resin ualu')
        self.assertEqual(num2words(19, lang='tet'), 'sanulu resin sia')
        self.assertEqual(num2words(20, lang='tet'), 'ruanulu')

        self.assertEqual(num2words(21, lang='tet'), 'ruanulu resin ida')
        self.assertEqual(num2words(22, lang='tet'), 'ruanulu resin rua')
        self.assertEqual(num2words(35, lang='tet'), 'tolunulu resin lima')
        self.assertEqual(num2words(99, lang='tet'), 'sianulu resin sia')

        self.assertEqual(num2words(100, lang='tet'), 'atus ida')
        self.assertEqual(num2words(101, lang='tet'), 'atus ida ida')
        self.assertEqual(num2words(107, lang='tet'), 'atus ida hitu')
        self.assertEqual(num2words(110, lang='tet'), 'atus ida sanulu')
        self.assertEqual(
            num2words(114, lang='tet'),
            'atus ida sanulu resin haat'
        )
        self.assertEqual(
            num2words(128, lang='tet'),
            'atus ida ruanulu resin ualu'
        )
        self.assertEqual(
            num2words(151, lang='tet'),
            'atus ida limanulu resin ida'
        )
        self.assertEqual(
            num2words(713, lang='tet'),
            'atus hitu sanulu resin tolu'
        )
        self.assertEqual(
            num2words(999, lang='tet'),
            'atus sia sianulu resin sia'
        )

        self.assertEqual(num2words(1000, lang='tet'), 'rihun ida')
        self.assertEqual(num2words(1001, lang='tet'), 'rihun ida ida')
        self.assertEqual(
            num2words(1011, lang='tet'),
            'rihun ida sanulu resin ida'
        )
        self.assertEqual(
            num2words(1111, lang='tet'),
            'rihun ida atus ida sanulu resin ida'
        )
        self.assertEqual(
            num2words(2357, lang='tet'),
            'rihun rua atus tolu limanulu resin hitu'
        )
        self.assertEqual(
            num2words(2200, lang='tet'),
            'rihun rua atus rua'
        )
        self.assertEqual(
            num2words(2230, lang='tet'),
            'rihun rua atus rua tolunulu'
        )
        self.assertEqual(
            num2words(73400, lang='tet'),
            'rihun hitunulu resin tolu atus haat'
        )
        self.assertEqual(
            num2words(73421, lang='tet'),
            'rihun hitunulu resin tolu atus haat ruanulu resin ida'
        )
        self.assertEqual(num2words(100000, lang='tet'), 'rihun atus ida')
        self.assertEqual(
            num2words(250050, lang='tet'),
            'rihun atus rua limanulu limanulu'
        )
        self.assertEqual(
            num2words(6000000, lang='tet'), 'miliaun neen'
        )
        self.assertEqual(
            num2words(100000000, lang='tet'), 'miliaun atus ida'
        )
        self.assertEqual(
            num2words(19000000000, lang='tet'),
            'miliaun rihun sanulu resin sia'
        )
        self.assertEqual(
            num2words(145000000002, lang='tet'),
            'miliaun rihun atus ida haatnulu resin lima resin rua'
        )
        self.assertEqual(
            num2words(4635102, lang='tet'),
            'miliaun haat rihun atus neen tolunulu resin lima atus ida rua'
        )
        self.assertEqual(
            num2words(145254635102, lang='tet'),
            "miliaun rihun atus ida haatnulu resin lima atus rua limanulu \
resin haat rihun atus neen tolunulu resin lima atus ida rua"
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

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='tet'), 'menus ida')
        self.assertEqual(
            num2words(-256, lang='tet'), 'menus atus rua limanulu resin neen'
        )
        self.assertEqual(num2words(-1000, lang='tet'), 'menus rihun ida')
        self.assertEqual(num2words(-1000000, lang='tet'), 'menus miliaun ida')
        self.assertEqual(
            num2words(-1234567, lang='tet'),
            'menus miliaun ida rihun atus rua tolunulu resin \
haat atus lima neenulu resin hitu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='tet'), 'ida')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='tet'), 'ida vírgula mamuk ida')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='tet'), 'ida vírgula mamuk tolu lima'
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
            'atus ida ida vírgula rua rua'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='tet'),
            'rihun rua atus tolu haatnulu resin lima vírgula hitu lima'
        )

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
            'menus hitu vírgula mamuk ida'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='tet'),
            'menus atus rua ruanulu resin rua vírgula rua rua'
        )

    def test_ordinal(self):
        with self.assertRaises(decimal.InvalidOperation):
            num2words("hello", lang='tet', ordinal=True)
        with self.assertRaises(TypeError):
            num2words(5.1, lang='tet', ordinal=True)
        self.assertEqual(num2words(1, lang='tet', ordinal=True), 'dahuluk')
        self.assertEqual(num2words(2, lang='tet', ordinal=True), 'daruak')
        self.assertEqual(num2words(3, lang='tet', ordinal=True), 'datoluk')
        self.assertEqual(num2words(4, lang='tet', ordinal=True), 'dahaat')
        self.assertEqual(num2words(5, lang='tet', ordinal=True), 'dalimak')
        self.assertEqual(num2words(6, lang='tet', ordinal=True), 'daneen')
        self.assertEqual(num2words(7, lang='tet', ordinal=True), 'dahituk')
        self.assertEqual(num2words(8, lang='tet', ordinal=True), 'daualuk')
        self.assertEqual(num2words(9, lang='tet', ordinal=True), 'dasiak')
        self.assertEqual(num2words(10, lang='tet', ordinal=True), 'dasanuluk')
        self.assertEqual(
            num2words(11, lang='tet', ordinal=True), 'dasanulu resin idak'
        )
        self.assertEqual(
            num2words(12, lang='tet', ordinal=True), 'dasanulu resin ruak'
        )
        self.assertEqual(
            num2words(13, lang='tet', ordinal=True), 'dasanulu resin toluk'
        )
        self.assertEqual(
            num2words(14, lang='tet', ordinal=True), 'dasanulu resin haat'
        )
        self.assertEqual(
            num2words(15, lang='tet', ordinal=True), 'dasanulu resin limak'
        )
        self.assertEqual(
            num2words(16, lang='tet', ordinal=True), 'dasanulu resin neen'
        )
        self.assertEqual(
            num2words(17, lang='tet', ordinal=True), 'dasanulu resin hituk'
        )
        self.assertEqual(
            num2words(18, lang='tet', ordinal=True), 'dasanulu resin ualuk'
        )
        self.assertEqual(
            num2words(19, lang='tet', ordinal=True), 'dasanulu resin siak'
        )
        self.assertEqual(
            num2words(20, lang='tet', ordinal=True), 'daruanuluk'
        )

        self.assertEqual(
            num2words(21, lang='tet', ordinal=True), 'daruanulu resin idak'
        )
        self.assertEqual(
            num2words(22, lang='tet', ordinal=True), 'daruanulu resin ruak'
        )
        self.assertEqual(
            num2words(35, lang='tet', ordinal=True), 'datolunulu resin limak'
        )
        self.assertEqual(
            num2words(99, lang='tet', ordinal=True), 'dasianulu resin siak'
        )

        self.assertEqual(
            num2words(100, lang='tet', ordinal=True), 'dahatus idak'
        )
        self.assertEqual(
            num2words(101, lang='tet', ordinal=True), 'dahatus ida idak'
        )
        self.assertEqual(
            num2words(106, lang='tet', ordinal=True), 'dahatus ida neen'
        )
        self.assertEqual(
            num2words(128, lang='tet', ordinal=True),
            'dahatus ida ruanulu resin ualuk'
        )
        self.assertEqual(
            num2words(600, lang='tet', ordinal=True),
            'dahatus neen'
        )
        self.assertEqual(
            num2words(713, lang='tet', ordinal=True),
            'dahatus hitu sanulu resin toluk'
        )

        self.assertEqual(
            num2words(1000, lang='tet', ordinal=True), 'darihun idak'
        )
        self.assertEqual(
            num2words(1001, lang='tet', ordinal=True), 'darihun ida idak'
        )
        self.assertEqual(
            num2words(1111, lang='tet', ordinal=True),
            'darihun ida atus ida sanulu resin idak'
        )
        self.assertEqual(
            num2words(2114, lang='tet', ordinal=True),
            'darihun rua atus ida sanulu resin haat'
        )
        self.assertEqual(
            num2words(73421, lang='tet', ordinal=True),
            'darihun hitunulu resin tolu atus haat ruanulu resin idak'
        )

        self.assertEqual(
            num2words(100000, lang='tet', ordinal=True),
            'darihun atus idak'
        )
        self.assertEqual(
            num2words(250050, lang='tet', ordinal=True),
            'darihun atus rua limanulu limanuluk'
        )
        self.assertEqual(
            num2words(6000000, lang='tet', ordinal=True), 'damiliaun neen'
        )
        self.assertEqual(
            num2words(19000000000, lang='tet', ordinal=True),
            'damiliaun rihun sanulu resin siak'
        )
        self.assertEqual(
            num2words(145000000002, lang='tet', ordinal=True),
            'damiliaun rihun atus ida haatnulu resin lima resin ruak'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'dolar ida')
        self.assertEqual(self.n2w.to_currency(2.00), 'dolar rua')
        self.assertEqual(self.n2w.to_currency(3.00), 'dolar tolu')
        self.assertEqual(self.n2w.to_currency(4.00), 'dolar haat')
        self.assertEqual(self.n2w.to_currency(5.00), 'dolar lima')
        self.assertEqual(self.n2w.to_currency(6.00), 'dolar neen')
        self.assertEqual(self.n2w.to_currency(7.00), 'dolar hitu')
        self.assertEqual(self.n2w.to_currency(8.00), 'dolar ualu')
        self.assertEqual(self.n2w.to_currency(9.00), 'dolar sia')
        self.assertEqual(self.n2w.to_currency(10.00), 'dolar sanulu')
        self.assertEqual(self.n2w.to_currency(11.00), 'dolar sanulu resin ida')
        self.assertEqual(self.n2w.to_currency(12.00), 'dolar sanulu resin rua')
        self.assertEqual(
            self.n2w.to_currency(13.00),
            'dolar sanulu resin tolu'
        )
        self.assertEqual(
            self.n2w.to_currency(14.00),
            'dolar sanulu resin haat'
        )
        self.assertEqual(
            self.n2w.to_currency(15.00),
            'dolar sanulu resin lima'
        )
        self.assertEqual(
            self.n2w.to_currency(16.00),
            'dolar sanulu resin neen'
        )
        self.assertEqual(
            self.n2w.to_currency(17.00),
            'dolar sanulu resin hitu'
        )
        self.assertEqual(
            self.n2w.to_currency(18.00),
            'dolar sanulu resin ualu'
        )
        self.assertEqual(
            self.n2w.to_currency(19.00),
            'dolar sanulu resin sia'
        )
        self.assertEqual(self.n2w.to_currency(20.00), 'dolar ruanulu')

        self.assertEqual(
            self.n2w.to_currency(21.00),
            'dolar ruanulu resin ida'
        )
        self.assertEqual(
            self.n2w.to_currency(22.00),
            'dolar ruanulu resin rua'
        )
        self.assertEqual(
            self.n2w.to_currency(35.00),
            'dolar tolunulu resin lima'
        )
        self.assertEqual(
            self.n2w.to_currency(99.00),
            'dolar sianulu resin sia'
        )

        self.assertEqual(self.n2w.to_currency(100.00), 'dolar atus ida')
        self.assertEqual(self.n2w.to_currency(101.00), 'dolar atus ida ida')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'dolar atus ida ruanulu resin ualu'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'dolar atus hitu sanulu resin tolu')

        self.assertEqual(self.n2w.to_currency(1000.00), 'dolar rihun ida')
        self.assertEqual(self.n2w.to_currency(1001.00), 'dolar rihun ida ida')
        self.assertEqual(
            self.n2w.to_currency(1111.00),
            'dolar rihun ida atus ida sanulu resin ida'
        )
        self.assertEqual(
            self.n2w.to_currency(2114.00),
            'dolar rihun rua atus ida sanulu resin haat'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'dolar rihun hitunulu resin tolu atus haat ruanulu resin ida'
        )

        self.assertEqual(
            self.n2w.to_currency(100000.00),
            'dolar rihun atus ida'
        )
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'dolar rihun atus rua limanulu limanulu'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'dolar miliaun neen'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dolar miliaun rihun sanulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'dolar miliaun rihun atus ida haatnulu resin lima resin rua'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'dolar ida')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'dolar ida sentavu limanulu')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus dolar ida')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus dolar atus rua limanulu resin neen'
        )
        self.assertEqual(
            self.n2w.to_currency(-1000.00),
            'menus dolar rihun ida'
        )
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus dolar miliaun ida'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus dolar miliaun ida rihun atus rua tolunulu \
resin haat atus lima neenulu resin hitu'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'dolar ida')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'dolar ida sentavu ida'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'dolar ida sentavu tolu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'dolar ida sentavu tolunulu resin lima'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'dolar tolu sentavu sanulu resin haat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'dolar atus ida ida sentavu ruanulu resin rua'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dolar rihun rua atus tolu haatnulu resin \
lima sentavu hitunulu resin lima'
        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus dolar rua sentavu tolunulu resin haat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus dolar sia sentavu sianulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus dolar hitu sentavu ida'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus dolar atus rua ruanulu resin rua sentavu ruanulu resin rua'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihun ida ida')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihun ida atus hitu ualunulu resin sia'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihun ida atus sia haatnulu resin rua'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihun ida atus sia ualunulu resin haat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihun rua')
        self.assertEqual(self.n2w.to_year(2001), 'rihun rua ida')
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
