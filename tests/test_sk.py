
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


class Num2WordsSKTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='sk'), "sto")
        self.assertEqual(num2words(101, lang='sk'), "stojeden")
        self.assertEqual(num2words(110, lang='sk'), "stodesať")
        self.assertEqual(num2words(115, lang='sk'), "stopätnásť")
        self.assertEqual(num2words(123, lang='sk'), "stodvadsaťtri")
        self.assertEqual(num2words(1000, lang='sk'), "tisíc")
        self.assertEqual(num2words(1001, lang='sk'), "tisícjeden")
        self.assertEqual(num2words(2012, lang='sk'), "dvetisícdvanásť")
        self.assertEqual(
            num2words(10.02, lang='sk'),
            "desať celých nula dva"
        )
        self.assertEqual(
            num2words(15.007, lang='sk'),
            "pätnásť celých nula nula sedem"
        )
        self.assertEqual(
            num2words(12519.85, lang='sk'),
            "dvanásťtisícpäťstodevätnásť celých osemdesiatpäť"
        )
        self.assertEqual(
            num2words(123.50, lang='sk'),
            "stodvadsaťtri celých päť"
        )
        self.assertEqual(
            num2words(1234567890, lang='sk'),
            "miliarda dvestotridsaťštyri miliónov päťstošesťdesiat"
            "sedemtisícosemstodeväťdesiat"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='sk'),
            "dvestopätnásť kvintiliónov štyristošesťdesiatjeden kvadriliárd "
            "štyristosedem kvadriliónov osemstodeväťdesiatdva triliárd "
            "tridsaťdeväť triliónov dve biliardy stopäťdesiatsedem biliónov "
            "stoosemdesiatdeväť miliárd osemstoosemdesiattri miliónov "
            "deväťstojedentisícšesťstosedemdesiatšesť"
        )
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='sk'),
            "sedemstodevätnásť kvintiliónov deväťdesiatštyri kvadriliárd "
            "dvestotridsaťštyri kvadriliónov šesťstodeväťdesiattri triliárd "
            "šesťstošesťdesiattri triliónov tridsaťštyri biliárd "
            "osemstodvadsaťdva biliónov osemstodvadsaťštyri miliárd "
            "tristoosemdesiatštyri miliónov "
            "dvestodvadsaťtisícdvestodeväťdesiatjeden"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='sk', to='ordinal')

    def test_currency(self):
        self.assertEqual(
            num2words(10.0, lang='sk', to='currency', currency='EUR'),
            "desať eur, nula centov")
        self.assertEqual(
            num2words(1234.56, lang='sk', to='currency', currency='EUR'),
            "tisícdvestotridsaťštyri eur, päťdesiatšesť centov")
        self.assertEqual(
            num2words(101.11, lang='sk', to='currency', currency='EUR',
                      separator=' a'),
            "stojeden eur a jedenásť centov")
        self.assertEqual(
            num2words(-12519.85, lang='sk', to='currency', cents=False),
            "mínus dvanásťtisícpäťstodevätnásť eur, 85 centov"
        )
        self.assertEqual(
            num2words(19.50, lang='sk', to='currency', cents=False),
            "devätnásť eur, 50 centov"
        )
