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
        self.assertEqual(num2words(1, lang='mgm'), 'iid')
        self.assertEqual(num2words(2, lang='mgm'), 'ruu')
        self.assertEqual(num2words(3, lang='mgm'), 'teil')
        self.assertEqual(num2words(4, lang='mgm'), 'paat')
        self.assertEqual(num2words(5, lang='mgm'), 'liim')
        self.assertEqual(num2words(6, lang='mgm'), 'hohon iid')
        self.assertEqual(num2words(7, lang='mgm'), 'hoho ruu')
        self.assertEqual(num2words(8, lang='mgm'), 'hoho teil')
        self.assertEqual(num2words(9, lang='mgm'), 'hoho paat')
        self.assertEqual(num2words(10, lang='mgm'), 'saguul')
        self.assertEqual(num2words(11, lang='mgm'), 'saguul resi iid')
        self.assertEqual(num2words(12, lang='mgm'), 'saguul resi ruu')
        self.assertEqual(num2words(13, lang='mgm'), 'saguul resi teil')
        self.assertEqual(num2words(14, lang='mgm'), 'saguul resi paat')
        self.assertEqual(num2words(15, lang='mgm'), 'saguul resi liim')
        self.assertEqual(num2words(16, lang='mgm'), 'saguul resi hohon iid')
        self.assertEqual(num2words(17, lang='mgm'), 'saguul resi hoho ruu')
        self.assertEqual(num2words(18, lang='mgm'), 'saguul resi hoho teil')
        self.assertEqual(num2words(19, lang='mgm'), 'saguul resi hoho paat')
        self.assertEqual(num2words(20, lang='mgm'), 'guul ruu')

        self.assertEqual(num2words(21, lang='mgm'), 'guul ruu resi iid')
        self.assertEqual(num2words(22, lang='mgm'), 'guul ruu resi ruu')
        self.assertEqual(num2words(35, lang='mgm'), 'guul teil resi liim')
        self.assertEqual(num2words(99, lang='mgm'), 'guul hoho paat resi hoho paat')

        self.assertEqual(num2words(100, lang='mgm'), 'atus iid')
        self.assertEqual(num2words(101, lang='mgm'), 'atus iid resi iid')
        self.assertEqual(num2words(107, lang='mgm'), 'atus iid resi hoho ruu')
        self.assertEqual(num2words(110, lang='mgm'), 'atus iid saguul')
        self.assertEqual(num2words(114, lang='mgm'), 'atus iid saguul resi paat')
        self.assertEqual(num2words(128, lang='mgm'), 'atus iid guul ruu resi hoho teil')
        self.assertEqual(num2words(151, lang='mgm'), 'atus iid guul liim resi iid')
        self.assertEqual(num2words(713, lang='mgm'), 'atus hoho ruu saguul resi teil')
        self.assertEqual(num2words(999, lang='mgm'), 'atus hoho paat guul hoho paat resi hoho paat')

        self.assertEqual(num2words(1000, lang='mgm'), 'rihun iid')
        self.assertEqual(num2words(1001, lang='mgm'), 'rihun iid resi iid')
        self.assertEqual(num2words(1011, lang='mgm'), 'rihun iid saguul resi iid')
        self.assertEqual(num2words(1111, lang='mgm'), 'rihun iid atus iid saguul resi iid')
        self.assertEqual(num2words(2357, lang='mgm'), 'rihun ruu atus teil guul liim resi hoho ruu')
        self.assertEqual(
            num2words(2200, lang='mgm'),
            'rihun ruu atus ruu'
        )
        self.assertEqual(num2words(2230, lang='mgm'), 'rihun ruu atus ruu guul teil')
        self.assertEqual(num2words(73400, lang='mgm'), 'rihun guul hoho ruu resi teil atus paat')
        self.assertEqual(num2words(73421, lang='mgm'), 'rihun guul hoho ruu resi teil atus paat guul ruu resi iid')
        self.assertEqual(num2words(100000, lang='mgm'), 'rihun atus iid')
        self.assertEqual(num2words(250050, lang='mgm'), 'rihun atus ruu guul liim guul liim')
        self.assertEqual(
            num2words(6000000, lang='mgm'), 'miliaun hohon iid'
        )
        self.assertEqual(
            num2words(100000000, lang='mgm'), 'miliaun atus iid'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm'), 'miliaun rihun saguul resi hoho paat'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm'),
            'miliaun rihun atus iid guul paat resi liim resi ruu'
        )
        self.assertEqual(
            num2words(4635102, lang='mgm'),
            'miliaun paat rihun atus hohon iid guul teil resi liim atus iid resi ruu'
        )
        self.assertEqual(
            num2words(145254635102, lang='mgm'),
            'miliaun rihun atus iid guul paat resi liim atus ruu guul liim resi paat rihun atus hohon iid guul teil resi liim atus iid resi ruu'
        )
        self.assertEqual(
            num2words(1000000000000, lang='mgm'),
            'biliaun iid'
        )
        self.assertEqual(
            num2words(2000000000000, lang='mgm'),
            'biliaun ruu'
        )
        self.assertEqual(
            num2words(1000000000000000, lang='mgm'),
            'biliaun rihun iid'
        )
        self.assertEqual(
            num2words(2000000000000000, lang='mgm'),
            'biliaun rihun ruu'
        )
        self.assertEqual(
            num2words(1000000000000000000, lang='mgm'),
            'triliaun iid'
        )
        self.assertEqual(
            num2words(2000000000000000000, lang='mgm'),
            'triliaun ruu'
        )

    def test_cardinal_integer_negative(self):
        self.assertEqual(num2words(-1, lang='mgm'), 'menus iid')
        self.assertEqual(
            num2words(-256, lang='mgm'), 'menus atus ruu guul liim resi hohon iid'
        )
        self.assertEqual(num2words(-1000, lang='mgm'), 'menus rihun iid')
        self.assertEqual(num2words(-1000000, lang='mgm'), 'menus miliaun iid')
        self.assertEqual(
            num2words(-1234567, lang='mgm'),
            'menus miliaun iid rihun atus ruu guul teil resi paat atus liim guul hohon iid resi hoho ruu'
        )

    def test_cardinal_float(self):
        self.assertEqual(num2words(Decimal('1.00'), lang='mgm'), 'iid')
        self.assertEqual(num2words(
            Decimal('1.01'), lang='mgm'), 'iid vírgula mamu iid')
        self.assertEqual(num2words(
            Decimal('1.035'), lang='mgm'), 'iid vírgula mamu teil liim'
        )
        self.assertEqual(num2words(
            Decimal('1.35'), lang='mgm'), 'iid vírgula teil liim'
        )
        self.assertEqual(
            num2words(Decimal('3.14159'), lang='mgm'),
            'teil vírgula iid paat iid liim hoho paat'
        )
        self.assertEqual(
            num2words(Decimal('101.22'), lang='mgm'),
            'atus iid resi iid vírgula ruu ruu'
        )
        self.assertEqual(
            num2words(Decimal('2345.75'), lang='mgm'),
            'rihun ruu atus teil guul paat resi liim vírgula hoho ruu liim'
        )


    def test_cardinal_float_negative(self):
        self.assertEqual(
            num2words(Decimal('-2.34'), lang='mgm'),
            'menus ruu vírgula teil paat'
        )
        self.assertEqual(
            num2words(Decimal('-9.99'), lang='mgm'),
            'menus hoho paat vírgula hoho paat hoho paat'
        )
        self.assertEqual(
            num2words(Decimal('-7.01'), lang='mgm'),
            'menus hoho ruu vírgula mamu iid'
        )
        self.assertEqual(
            num2words(Decimal('-222.22'), lang='mgm'),
            'menus atus ruu guul ruu resi ruu vírgula ruu ruu'
        )

    def test_ordinal(self):
        self.assertEqual(num2words(1, lang='mgm', ordinal=True), 'daiid')
        self.assertEqual(num2words(2, lang='mgm', ordinal=True), 'daruu')
        self.assertEqual(num2words(3, lang='mgm', ordinal=True), 'dateil')
        self.assertEqual(num2words(4, lang='mgm', ordinal=True), 'dapaat')
        self.assertEqual(num2words(5, lang='mgm', ordinal=True), 'daliim')
        self.assertEqual(num2words(6, lang='mgm', ordinal=True), 'dahohon iid')
        self.assertEqual(num2words(7, lang='mgm', ordinal=True), 'dahoho ruu')
        self.assertEqual(num2words(8, lang='mgm', ordinal=True), 'dahoho teil')
        self.assertEqual(num2words(9, lang='mgm', ordinal=True), 'dahoho paat')
        self.assertEqual(num2words(10, lang='mgm', ordinal=True), 'dasaguul')
        self.assertEqual(
            num2words(11, lang='mgm', ordinal=True), 'dasaguul resi iid'
        )
        self.assertEqual(
            num2words(12, lang='mgm', ordinal=True), 'dasaguul resi ruu'
        )
        self.assertEqual(
            num2words(13, lang='mgm', ordinal=True), 'dasaguul resi teil'
        )
        self.assertEqual(
            num2words(14, lang='mgm', ordinal=True), 'dasaguul resi paat'
        )
        self.assertEqual(
            num2words(15, lang='mgm', ordinal=True), 'dasaguul resi liim'
        )
        self.assertEqual(
            num2words(16, lang='mgm', ordinal=True), 'dasaguul resi hohon iid'
        )
        self.assertEqual(
            num2words(17, lang='mgm', ordinal=True), 'dasaguul resi hoho ruu'
        )
        self.assertEqual(
            num2words(18, lang='mgm', ordinal=True), 'dasaguul resi hoho teil'
        )
        self.assertEqual(
            num2words(19, lang='mgm', ordinal=True), 'dasaguul resi hoho paat'
        )
        self.assertEqual(
            num2words(20, lang='mgm', ordinal=True), 'daguul ruu'
        )

        self.assertEqual(
            num2words(21, lang='mgm', ordinal=True), 'daguul ruu resi iid'
        )
        self.assertEqual(
            num2words(22, lang='mgm', ordinal=True), 'daguul ruu resi ruu'
        )
        self.assertEqual(
            num2words(35, lang='mgm', ordinal=True), 'daguul teil resi liim'
        )
        self.assertEqual(
            num2words(99, lang='mgm', ordinal=True), 'daguul hoho paat resi hoho paat'
        )

        self.assertEqual(
            num2words(100, lang='mgm', ordinal=True), 'daatus iid'
        )
        self.assertEqual(
            num2words(101, lang='mgm', ordinal=True), 'daatus iid resi iid'
        )
        self.assertEqual(
            num2words(128, lang='mgm', ordinal=True),
            'daatus iid guul ruu resi hoho teil'
        )
        self.assertEqual(
            num2words(713, lang='mgm', ordinal=True),
            'daatus hoho ruu saguul resi teil'
        )

        self.assertEqual(
            num2words(1000, lang='mgm', ordinal=True), 'darihun iid'
        )
        self.assertEqual(
            num2words(1001, lang='mgm', ordinal=True), 'darihun iid resi iid'
        )
        self.assertEqual(
            num2words(1111, lang='mgm', ordinal=True),
            'darihun iid atus iid saguul resi iid'
        )
        self.assertEqual(
            num2words(2114, lang='mgm', ordinal=True),
            'darihun ruu atus iid saguul resi paat'
        )
        self.assertEqual(
            num2words(73421, lang='mgm', ordinal=True),
            'darihun guul hoho ruu resi teil atus paat guul ruu resi iid'
        )

        self.assertEqual(
            num2words(100000, lang='mgm', ordinal=True),
            'darihun atus iid'
        )
        self.assertEqual(
            num2words(250050, lang='mgm', ordinal=True),
            'darihun atus ruu guul liim guul liim'
        )
        self.assertEqual(
            num2words(6000000, lang='mgm', ordinal=True), 'damiliaun hohon iid'
        )
        self.assertEqual(
            num2words(19000000000, lang='mgm', ordinal=True),
            'damiliaun rihun saguul resi hoho paat'
        )
        self.assertEqual(
            num2words(145000000002, lang='mgm', ordinal=True),
            'damiliaun rihun atus iid guul paat resi liim resi ruu'
        )

    def test_currency_integer(self):
        self.assertEqual(self.n2w.to_currency(1.00), 'dolar iid')
        self.assertEqual(self.n2w.to_currency(2.00), 'dolar ruu')
        self.assertEqual(self.n2w.to_currency(3.00), 'dolar teil')
        self.assertEqual(self.n2w.to_currency(4.00), 'dolar paat')
        self.assertEqual(self.n2w.to_currency(5.00), 'dolar liim')
        self.assertEqual(self.n2w.to_currency(6.00), 'dolar hohon iid')
        self.assertEqual(self.n2w.to_currency(7.00), 'dolar hoho ruu')
        self.assertEqual(self.n2w.to_currency(8.00), 'dolar hoho teil')
        self.assertEqual(self.n2w.to_currency(9.00), 'dolar hoho paat')
        self.assertEqual(self.n2w.to_currency(10.00), 'dolar saguul')
        self.assertEqual(self.n2w.to_currency(11.00), 'dolar saguul resi iid')
        self.assertEqual(self.n2w.to_currency(12.00), 'dolar saguul resi ruu')
        self.assertEqual(self.n2w.to_currency(13.00), 'dolar saguul resi teil')
        self.assertEqual(self.n2w.to_currency(14.00), 'dolar saguul resi paat')
        self.assertEqual(self.n2w.to_currency(15.00), 'dolar saguul resi liim')
        self.assertEqual(self.n2w.to_currency(16.00), 'dolar saguul resi hohon iid')
        self.assertEqual(self.n2w.to_currency(17.00), 'dolar saguul resi hoho ruu')
        self.assertEqual(self.n2w.to_currency(18.00), 'dolar saguul resi hoho teil')
        self.assertEqual(self.n2w.to_currency(19.00), 'dolar saguul resi hoho paat')
        self.assertEqual(self.n2w.to_currency(20.00), 'dolar guul ruu')

        self.assertEqual(self.n2w.to_currency(21.00), 'dolar guul ruu resi iid')
        self.assertEqual(self.n2w.to_currency(22.00), 'dolar guul ruu resi ruu')
        self.assertEqual(self.n2w.to_currency(35.00), 'dolar guul teil resi liim')
        self.assertEqual(self.n2w.to_currency(99.00), 'dolar guul hoho paat resi hoho paat')

        self.assertEqual(self.n2w.to_currency(100.00), 'dolar atus iid')
        self.assertEqual(self.n2w.to_currency(101.00), 'dolar atus iid resi iid')
        self.assertEqual(
            self.n2w.to_currency(128.00), 'dolar atus iid guul ruu resi hoho teil'
        )
        self.assertEqual(
            self.n2w.to_currency(713.00), 'dolar atus hoho ruu saguul resi teil')

        self.assertEqual(self.n2w.to_currency(1000.00), 'dolar rihun iid')
        self.assertEqual(self.n2w.to_currency(1001.00), 'dolar rihun iid resi iid')
        self.assertEqual(
            self.n2w.to_currency(1111.00), 'dolar rihun iid atus iid saguul resi iid')
        self.assertEqual(
            self.n2w.to_currency(2114.00), 'dolar rihun ruu atus iid saguul resi paat'
        )
        self.assertEqual(
            self.n2w.to_currency(73421.00),
            'dolar rihun guul hoho ruu resi teil atus paat guul ruu resi iid'
        )

        self.assertEqual(self.n2w.to_currency(100000.00), 'dolar rihun atus iid')
        self.assertEqual(
            self.n2w.to_currency(250050.00),
            'dolar rihun atus ruu guul liim guul liim'
        )
        self.assertEqual(
            self.n2w.to_currency(6000000.00),
            'dolar miliaun hohon iid'
        )
        self.assertEqual(
            self.n2w.to_currency(19000000000.00),
            'dolar miliaun rihun saguul resi hoho paat'
        )
        self.assertEqual(
            self.n2w.to_currency(145000000002.00),
            'dolar miliaun rihun atus iid guul paat resi liim resi ruu'
        )
        self.assertEqual(self.n2w.to_currency(1.00, currency='USD'),
                         'dolar iid')
        self.assertEqual(self.n2w.to_currency(1.50, currency='USD'),
                         'dolar iid sentavu guul liim')
        with self.assertRaises(NotImplementedError):
            self.n2w.to_currency(1.00, currency='CHF')

    def test_currency_integer_negative(self):
        self.assertEqual(self.n2w.to_currency(-1.00), 'menus dolar iid')
        self.assertEqual(
            self.n2w.to_currency(-256.00),
            'menus dolar atus ruu guul liim resi hohon iid'
        )
        self.assertEqual(self.n2w.to_currency(-1000.00), 'menus dolar rihun iid')
        self.assertEqual(
            self.n2w.to_currency(-1000000.00), 'menus dolar miliaun iid'
        )
        self.assertEqual(
            self.n2w.to_currency(-1234567.00),
            'menus dolar miliaun iid rihun atus ruu guul teil resi paat atus liim guul hohon iid resi hoho ruu'
        )

    def test_currency_float(self):
        self.assertEqual(self.n2w.to_currency(Decimal('1.00')), 'dolar iid')
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.01')), 'dolar iid sentavu iid'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.03')), 'dolar iid sentavu teil'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('1.35')),
            'dolar iid sentavu guul teil resi liim'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('3.14')),
            'dolar teil sentavu saguul resi paat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('101.22')),
            'dolar atus iid resi iid sentavu guul ruu resi ruu'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('2345.75')),
            'dolar rihun ruu atus teil guul paat resi liim sentavu guul hoho ruu resi liim'

        )

    def test_currency_float_negative(self):
        self.assertEqual(
            self.n2w.to_currency(Decimal('-2.34')),
            'menus dolar ruu sentavu guul teil resi paat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-9.99')),
            'menus dolar hoho paat sentavu guul hoho paat resi hoho paat'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-7.01')),
            'menus dolar hoho ruu sentavu iid'
        )
        self.assertEqual(
            self.n2w.to_currency(Decimal('-222.22')),
            'menus dolar atus ruu guul ruu resi ruu sentavu guul ruu resi ruu'
        )

    def test_year(self):
        self.assertEqual(self.n2w.to_year(1001), 'rihun iid resi iid')
        self.assertEqual(
            self.n2w.to_year(1789), 'rihun iid atus hoho ruu guul hoho teil resi hoho paat'
        )
        self.assertEqual(
            self.n2w.to_year(1942), 'rihun iid atus hoho paat guul paat resi ruu'
        )
        self.assertEqual(
            self.n2w.to_year(1984), 'rihun iid atus hoho paat guul hoho teil resi paat'
        )
        self.assertEqual(self.n2w.to_year(2000), 'rihun ruu')
        self.assertEqual(self.n2w.to_year(2001), 'rihun ruu resi iid')
        self.assertEqual(self.n2w.to_year(2016), 'rihun ruu saguul resi hohon iid')

    def test_year_negative(self):
        self.assertEqual(self.n2w.to_year(-30), 'guul teil muna Kristu')
        self.assertEqual(
            self.n2w.to_year(-744),
            'atus hoho ruu guul paat resi paat muna Kristu'
        )
        self.assertEqual(
            self.n2w.to_year(-10000),
            'rihun saguul muna Kristu'
        )

    def test_to_ordinal_num(self):
        self.assertEqual(self.n2w.to_ordinal_num(1), '1º')
        self.assertEqual(self.n2w.to_ordinal_num(100), '100º')
