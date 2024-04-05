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
from num2words.lang_KMK import Num2Word_KMK


class Num2WordsKMKTest(TestCase):
    def setUp(self):
        super().setUp()
        self.n2w = Num2Word_KMK()

    def test_cardinal_integer(self):
        self.assertEqual(num2words(1, lang='kmk'), 'sia')
        self.assertEqual(num2words(2, lang='kmk'), 'rua')
        self.assertEqual(num2words(3, lang='kmk'), 'telu')
        self.assertEqual(num2words(4, lang='kmk'), 'paat')
        self.assertEqual(num2words(5, lang='kmk'), 'lima')
        self.assertEqual(num2words(6, lang='kmk'), 'neem')
        self.assertEqual(num2words(7, lang='kmk'), 'itsu')
        self.assertEqual(num2words(8, lang='kmk'), 'balu')
        self.assertEqual(num2words(9, lang='kmk'), 'sibe')
        self.assertEqual(num2words(10, lang='kmk'), 'sapulu')
        self.assertEqual(num2words(11, lang='kmk'), 'sapulu resin sia')
        self.assertEqual(num2words(12, lang='kmk'), 'sapulu resin rua')
        self.assertEqual(num2words(13, lang='kmk'), 'sapulu resin telu')
        self.assertEqual(num2words(14, lang='kmk'), 'sapulu resin paat')
        self.assertEqual(num2words(15, lang='kmk'), 'sapulu resin lima')
        self.assertEqual(num2words(16, lang='kmk'), 'sapulu resin neem')
        self.assertEqual(num2words(17, lang='kmk'), 'sapulu resin itsu')
        self.assertEqual(num2words(18, lang='kmk'), 'sapulu resin balu')
        self.assertEqual(num2words(19, lang='kmk'), 'sapulu resin sibe')
        self.assertEqual(num2words(20, lang='kmk'), 'gulurua')

        self.assertEqual(num2words(21, lang='kmk'), 'gulurua resin sia')
        self.assertEqual(num2words(22, lang='kmk'), 'gulurua resin rua')
        self.assertEqual(num2words(35, lang='kmk'), 'gulutelu resin lima')
        self.assertEqual(num2words(99, lang='kmk'), 'gulusibe resin sibe')

        self.assertEqual(num2words(100, lang='kmk'), 'atsus sia')
        self.assertEqual(num2words(101, lang='kmk'), 'atsus sia resin sia')
        self.assertEqual(num2words(107, lang='kmk'), 'atsus sia resin itsu')
        self.assertEqual(num2words(110, lang='kmk'), 'atsus sia sapulu')
        self.assertEqual(num2words(114, lang='kmk'), 'atsus sia sapulu resin paat')
        self.assertEqual(num2words(128, lang='kmk'), 'atsus sia gulurua resin balu')
        self.assertEqual(num2words(151, lang='kmk'), 'atsus sia gululima resin sia')
        self.assertEqual(num2words(713, lang='kmk'), 'atsus itsu sapulu resin telu')
        self.assertEqual(num2words(999, lang='kmk'), 'atsus sibe gulusibe resin sibe')

        self.assertEqual(num2words(1000, lang='kmk'), 'ribun sia')
        self.assertEqual(num2words(1001, lang='kmk'), 'ribun sia resin sia')
        self.assertEqual(num2words(1011, lang='kmk'), 'ribun sia sapulu resin sia')
        self.assertEqual(num2words(1111, lang='kmk'), 'ribun sia atsus sia sapulu resin sia')
        self.assertEqual(num2words(2357, lang='kmk'), 'ribun rua atsus telu gululima resin itsu')
        self.assertEqual(
            num2words(2200, lang='kmk'),
            'ribun rua atsus rua'
        )
        self.assertEqual(num2words(2230, lang='kmk'), 'ribun rua atsus rua gulutelu')
        self.assertEqual(num2words(73400, lang='kmk'), 'ribun guluitsu resin telu atsus paat')
        self.assertEqual(num2words(73421, lang='kmk'), 'ribun guluitsu resin telu atsus paat gulurua resin sia')
        self.assertEqual(num2words(100000, lang='kmk'), 'ribun atsus sia')
        self.assertEqual(num2words(250050, lang='kmk'), 'ribun atsus rua gululima gululima')
        self.assertEqual(
            num2words(6000000, lang='kmk'), 'miliaun neem'
        )
        self.assertEqual(
            num2words(100000000, lang='kmk'), 'miliaun atsus sia'
        )
        self.assertEqual(
            num2words(19000000000, lang='kmk'), 'miliaun ribun sapulu resin sibe'
        )
        self.assertEqual(
            num2words(145000000002, lang='kmk'),
            'miliaun ribun atsus sia gulupaat resin lima resin rua'
        )
        self.assertEqual(
            num2words(4635102, lang='kmk'),
            'miliaun paat ribun atsus neem gulutelu resin lima atsus sia resin rua'
        )
        self.assertEqual(
            num2words(145254635102, lang='kmk'),
            'miliaun ribun atsus sia gulupaat resin lima atsus rua gululima resin paat ribun atsus neem gulutelu resin lima atsus sia resin rua'
        )
        self.assertEqual(
            num2words(1000000000000, lang='kmk'),
            'biliaun sia'
        )
        self.assertEqual(
            num2words(2000000000000, lang='kmk'),
            'biliaun rua'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='kmk'),
            'biliaun ribun sia'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='kmk'),
            'biliaun ribun rua'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='kmk'),
            'triliaun sia'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='kmk'),
            'triliaun rua'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='kmk'), 'menus sia')
        self.assertEqual(
            num2words(-256, lang='kmk'), 'menus atsus rua gululima resin neem'
        )
        self.assertEqual(num2words(-1000, lang='kmk'), 'menus ribun sia')
        self.assertEqual(num2words(-1000000, lang='kmk'), 'menus miliaun sia')
        self.assertEqual(
            num2words(-1234567, lang='kmk'),
            'menus miliaun sia ribun atsus rua gulutelu resin paat atsus lima guluneem resin itsu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='kmk'), 'sia')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='kmk'), 'sia vírgula bai sia')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='kmk'), 'sia vírgula bai telu lima'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='kmk'), 'sia vírgula telu lima'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='kmk'),
            'telu vírgula sia paat sia lima sibe'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='kmk'),
            'atsus sia resin sia vírgula rua rua'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='kmk'),
            'ribun rua atsus telu gulupaat resin lima vírgula itsu lima'
        )

    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='kmk'),
            'menus rua vírgula telu paat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='kmk'),
            'menus sibe vírgula sibe sibe'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='kmk'),
            'menus itsu vírgula bai sia'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='kmk'),
            'menus atsus rua gulurua resin rua vírgula rua rua'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='kmk', ordinal=True), 'saba')
        self.assertEqual(num2words(2, lang='kmk', ordinal=True), 'abarua')
        self.assertEqual(num2words(3, lang='kmk', ordinal=True), 'abatelu')
        self.assertEqual(num2words(4, lang='kmk', ordinal=True), 'abapaat')
        self.assertEqual(num2words(5, lang='kmk', ordinal=True), 'abalima')
        self.assertEqual(num2words(6, lang='kmk', ordinal=True), 'abaneem')
        self.assertEqual(num2words(7, lang='kmk', ordinal=True), 'abaitsu')
        self.assertEqual(num2words(8, lang='kmk', ordinal=True), 'ababalu')
        self.assertEqual(num2words(9, lang='kmk', ordinal=True), 'abasibe')
        self.assertEqual(num2words(10, lang='kmk', ordinal=True), 'abasapulu')
        self.assertEqual(
            num2words(11, lang='kmk', ordinal=True), 'décimu primeiru'
        )
        self.assertEqual(
            num2words(12, lang='kmk', ordinal=True), 'décimu segundu'
        )
        self.assertEqual(
            num2words(13, lang='kmk', ordinal=True), 'décimu terceiru'
        )
        self.assertEqual(
            num2words(14, lang='kmk', ordinal=True), 'décimu quartu'
        )
        self.assertEqual(
            num2words(15, lang='kmk', ordinal=True), 'décimu quintu'
        )
        self.assertEqual(
            num2words(16, lang='kmk', ordinal=True), 'décimu sextu'
        )
        self.assertEqual(
            num2words(17, lang='kmk', ordinal=True), 'décimu sétimu'
        )
        self.assertEqual(
            num2words(18, lang='kmk', ordinal=True), 'décimu oitavu'
        )
        self.assertEqual(
            num2words(19, lang='kmk', ordinal=True), 'décimu nonu'
        )
        self.assertEqual(
            num2words(20, lang='kmk', ordinal=True), 'vigésimu'
        )

        self.assertEqual(
            num2words(21, lang='kmk', ordinal=True), 'vigésimu primeiru'
        )
        self.assertEqual(
            num2words(22, lang='kmk', ordinal=True), 'vigésimu segundu'
        )
        self.assertEqual(
            num2words(35, lang='kmk', ordinal=True), 'trigésimu quintu'
        )
        self.assertEqual(
            num2words(99, lang='kmk', ordinal=True), 'nonagésimu nonu'
        )

        self.assertEqual(
            num2words(100, lang='kmk', ordinal=True), 'centésimu'
        )
        self.assertEqual(
            num2words(101, lang='kmk', ordinal=True), 'centésimu primeiru'
        )
        self.assertEqual(
            num2words(128, lang='kmk', ordinal=True),
            'centésimu vigésimu oitavu'
        )
        self.assertEqual(
            num2words(713, lang='kmk', ordinal=True),
            'septigentésimu décimu terceiru'
        )

        self.assertEqual(
            num2words(1000, lang='kmk', ordinal=True), 'milésimu'
        )
        self.assertEqual(
            num2words(1001, lang='kmk', ordinal=True), 'milésimu primeiru'
        )
        self.assertEqual(
            num2words(1111, lang='kmk', ordinal=True),
            'milésimu centésimu décimu primeiru'
        )
        self.assertEqual(
            num2words(2114, lang='kmk', ordinal=True),
            'segundu milésimu centésimu décimu quartu'
        )
        self.assertEqual(
            num2words(73421, lang='kmk', ordinal=True),
            'septuagésimu terceiru milésimu quadrigentésimu vigésimu primeiru'
        )

        self.assertEqual(
            num2words(100000, lang='kmk', ordinal=True),
            'centésimu milésimu'
        )
        self.assertEqual(
            num2words(250050, lang='kmk', ordinal=True),
            'ducentésimu quinquagésimu milésimu quinquagésimu'
        )
        self.assertEqual(
            num2words(6000000, lang='kmk', ordinal=True), 'sextu milionésimu'
        )
        self.assertEqual(
            num2words(19000000000, lang='kmk', ordinal=True),
            'décimu nonu milésimu milionésimu'
        )
        self.assertEqual(
            num2words(145000000002, lang='kmk', ordinal=True),
            'centésimu quadragésimu quintu milésimu milionésimu segundu'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'sia dólar')
        self.assertEqual(self.n2w.to_currency(2.00), 'rua dólares')
        self.assertEqual(self.n2w.to_currency(3.00), 'telu dólares')
        self.assertEqual(self.n2w.to_currency(4.00), 'paat dólares')
        self.assertEqual(self.n2w.to_currency(5.00), 'lima dólares')
        self.assertEqual(self.n2w.to_currency(6.00), 'neem dólares')
        self.assertEqual(self.n2w.to_currency(7.00), 'itsu dólares')
        self.assertEqual(self.n2w.to_currency(8.00), 'balu dólares')
        self.assertEqual(self.n2w.to_currency(9.00), 'sibe dólares')
        self.assertEqual(self.n2w.to_currency(10.00), 'sapulu dólares')
        self.assertEqual(self.n2w.to_currency(11.00), 'sapulu resin sia dólares')
        self.assertEqual(self.n2w.to_currency(12.00), 'sapulu resin rua dólares')
        self.assertEqual(self.n2w.to_currency(13.00), 'sapulu resin telu dólares')
        self.assertEqual(self.n2w.to_currency(14.00), 'sapulu resin paat dólares')
        self.assertEqual(self.n2w.to_currency(15.00), 'sapulu resin lima dólares')
        self.assertEqual(self.n2w.to_currency(16.00), 'sapulu resin neem dólares')
        self.assertEqual(self.n2w.to_currency(17.00), 'sapulu resin itsu dólares')
        self.assertEqual(self.n2w.to_currency(18.00), 'sapulu resin balu dólares')
        self.assertEqual(self.n2w.to_currency(19.00), 'sapulu resin sibe dólares')
        self.assertEqual(self.n2w.to_currency(20.00), 'gulurua dólares')

        self.assertEqual(self.n2w.to_currency(21.00), 'gulurua resin sia dólares')
        self.assertEqual(self.n2w.to_currency(22.00), 'gulurua resin rua dólares')
        self.assertEqual(self.n2w.to_currency(35.00), 'gulutelu resin lima dólares')
        self.assertEqual(self.n2w.to_currency(99.00), 'gulusibe resin sibe dólares')

        self.assertEqual(self.n2w.to_currency(100.00), 'atsus sia dólares')
        self.assertEqual(self.n2w.to_currency(101.00), 'atsus sia resin sia dólares')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'atsus sia gulurua resin balu dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'atsus itsu sapulu resin telu dólares')

        self.assertEqual(self.n2w.to_currency(1000.00), 'ribun sia dólares')
        self.assertEqual(self.n2w.to_currency(1001.00), 'ribun sia resin sia dólares')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'ribun sia atsus sia sapulu resin sia dólares')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'ribun rua atsus sia sapulu resin paat dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'ribun guluitsu resin telu atsus paat gulurua resin sia dólares'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'ribun atsus sia dólares')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'ribun atsus rua gululima gululima dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'miliaun neem dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'miliaun ribun sapulu resin sibe dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'miliaun ribun atsus sia gulupaat resin lima resin rua dólares'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'sia dólar')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'sia dólar resin gululima cêntimus')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus sia dólar')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus atsus rua gululima resin neem dólares'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus ribun sia dólares')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus miliaun sia dólares'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus miliaun sia ribun atsus rua gulutelu resin paat atsus lima guluneem resin itsu dólares'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'sia dólar')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'sia dólar resin sia cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'sia dólar resin telu cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'sia dólar resin gulutelu resin lima cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'telu dólares resin sapulu resin paat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'atsus sia resin sia dólares resin gulurua resin rua cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'ribun rua atsus telu gulupaat resin lima dólares resin guluitsu resin lima cêntimus'

        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus rua dólares resin gulutelu resin paat cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus sibe dólares resin gulusibe resin sibe cêntimus'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus itsu dólares resin sia cêntimu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus atsus rua gulurua resin rua dólares resin gulurua resin rua cêntimus'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'ribun sia resin sia')
        self.assertEqual(
            self.n2w.to_year(1789), 'ribun sia atsus itsu gulubalu resin sibe'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'ribun sia atsus sibe gulupaat resin rua'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'ribun sia atsus sibe gulubalu resin paat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'ribun rua')
        self.assertEqual(self.n2w.to_year(2001), 'ribun rua resin sia')
        self.assertEqual(self.n2w.to_year(2016), 'ribun rua sapulu resin neem')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'gulutelu baipila eh Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atsus itsu gulupaat resin paat baipila eh Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'ribun sapulu baipila eh Kristu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
