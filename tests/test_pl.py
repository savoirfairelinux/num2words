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


class Num2WordsPLTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(90, lang='pl'), "dziewięćdziesiąt")
        self.assertEqual(num2words(100, lang='pl'), "sto")
        self.assertEqual(num2words(101, lang='pl'), "sto jeden")
        self.assertEqual(num2words(110, lang='pl'), "sto dziesięć")
        self.assertEqual(num2words(115, lang='pl'), "sto piętnaście")
        self.assertEqual(num2words(123, lang='pl'), "sto dwadzieścia trzy")
        self.assertEqual(num2words(400, lang='pl'), "czterysta")
        self.assertEqual(num2words(1000, lang='pl'), "tysiąc")
        self.assertEqual(num2words(1001, lang='pl'), "tysiąc jeden")
        self.assertEqual(num2words(2012, lang='pl'), "dwa tysiące dwanaście")
        self.assertEqual(
            num2words(10.02, lang='pl'),
            "dziesięć przecinek zero dwa"
        )
        self.assertEqual(
            num2words(15.007, lang='pl'),
            "piętnaście przecinek zero zero siedem"
        )
        self.assertEqual(
            num2words(12519.85, lang='pl'),
            "dwanaście tysięcy pięćset dziewiętnaście przecinek "
            "osiemdziesiąt pięć"
        )
        self.assertEqual(
            num2words(123.50, lang='pl'),
            "sto dwadzieścia trzy przecinek pięć"
        )
        self.assertEqual(
            num2words(1234567890, lang='pl'),
            "miliard dwieście trzydzieści cztery miliony pięćset "
            "sześćdziesiąt siedem tysięcy osiemset dziewięćdziesiąt"
        )
        self.assertEqual(
            num2words(10000000001000000100000, lang='pl'),
            "dziesięć tryliardów bilion sto tysięcy"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='pl'),
            "dwieście piętnaście kwintylionów czterysta sześćdziesiąt jeden "
            "kwadryliardów czterysta siedem kwadrylionów osiemset "
            "dziewięćdziesiąt dwa tryliardy trzydzieści dziewięć trylionów "
            "dwa biliardy sto pięćdziesiąt siedem bilionów sto osiemdziesiąt "
            "dziewięć miliardów osiemset osiemdziesiąt trzy miliony "
            "dziewięćset jeden tysięcy sześćset siedemdziesiąt sześć"
        )
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='pl'),
            "siedemset dziewiętnaście kwintylionów dziewięćdziesiąt cztery "
            "kwadryliardy dwieście trzydzieści cztery kwadryliony sześćset "
            "dziewięćdziesiąt trzy tryliardy sześćset sześćdziesiąt trzy "
            "tryliony trzydzieści cztery biliardy osiemset dwadzieścia dwa "
            "biliony osiemset dwadzieścia cztery miliardy trzysta "
            "osiemdziesiąt cztery miliony dwieście dwadzieścia "
            "tysięcy dwieście dziewięćdziesiąt jeden"
        )
        self.assertEqual(
            num2words(
                963301000001918264129471001047146102 * 10**30 + 1007,
                lang='pl'
            ),
            "dziewięćset sześćdziesiąt trzy decyliardy trzysta jeden "
            "decylionów nonylion dziewięćset osiemnaście oktyliardów dwieście "
            "sześćdziesiąt cztery oktyliony sto dwadzieścia dziewięć "
            "septyliardów czterysta siedemdziesiąt jeden septylionów "
            "sekstyliard czterdzieści siedem sekstylionów sto czterdzieści "
            "sześć kwintyliardów sto dwa kwintyliony tysiąc siedem"
        )

    def test_to_ordinal(self):
        self.assertEqual(num2words(100, lang='pl', to='ordinal'), "setny")
        self.assertEqual(
            num2words(101, lang='pl', to='ordinal'), "sto pierwszy")
        self.assertEqual(num2words(120, lang='pl', to='ordinal'),
                         "sto dwudziesty")
        self.assertEqual(num2words(20, lang='pl', to='ordinal'), "dwudziesty")
        self.assertEqual(num2words(121, lang='pl', to='ordinal'),
                         "sto dwudziesty pierwszy")
        self.assertEqual(
            num2words(115, lang='pl', to='ordinal'), "sto piętnasty")
        self.assertEqual(
            num2words(25, lang='pl', to='ordinal'), "dwudziesty piąty")
        self.assertEqual(num2words(1021, lang='pl', to='ordinal'),
                         "tysiąc dwudziesty pierwszy")
        self.assertEqual(
            num2words(120, lang='pl', to='ordinal'), "sto dwudziesty")
        self.assertEqual(num2words(1000021, lang='pl',
                                   to='ordinal'), "milion dwudziesty pierwszy")
        self.assertEqual(num2words(1000, lang='pl', to='ordinal'), "tysięczny")
        self.assertEqual(num2words(10000, lang='pl',
                                   to='ordinal'), "dziesięciotysięczny")
        self.assertEqual(num2words(100000000, lang='pl',
                                   to='ordinal'), "stumilionowy")
        self.assertEqual(num2words(1002000, lang='pl',
                                   to='ordinal'), "milion dwutysięczny")
        self.assertEqual(num2words(1001000, lang='pl',
                                   to='ordinal'), "milion tysięczny")
        self.assertEqual(num2words(1000000, lang='pl',
                                   to='ordinal'), "milionowy")

    def test_to_ordinal_error(self):
        with self.assertRaises(NotImplementedError):
            num2words(1.5, lang='pl', to='ordinal')

    def test_currency(self):
        self.assertEqual(
            num2words(1.0, lang='pl', to='currency', currency='EUR'),
            "jeden euro, zero centów")
        self.assertEqual(
            num2words(1.0, lang='pl', to='currency', currency='PLN'),
            "jeden złoty, zero groszy")
        self.assertEqual(
            num2words(1234.56, lang='pl', to='currency', currency='EUR'),
            "tysiąc dwieście trzydzieści cztery euro, pięćdziesiąt sześć "
            "centów"
        )
        self.assertEqual(
            num2words(1234.56, lang='pl', to='currency', currency='PLN'),
            "tysiąc dwieście trzydzieści cztery złote, pięćdziesiąt sześć "
            "groszy"
        )
        self.assertEqual(
            num2words(10111, lang='pl', to='currency', currency='EUR',
                      separator=' i'),
            "sto jeden euro i jedenaście centów"
        )
        self.assertEqual(
            num2words(10121, lang='pl', to='currency', currency='PLN',
                      separator=' i'),
            "sto jeden złotych i dwadzieścia jeden groszy"
        )
        self.assertEqual(
            num2words(-1251985, lang='pl', to='currency', cents=False),
            "minus dwanaście tysięcy pięćset dziewiętnaście euro, 85 centów"
        )
        self.assertEqual(
            num2words(123.50, lang='pl', to='currency', currency='PLN',
                      separator=' i'),
            "sto dwadzieścia trzy złote i pięćdziesiąt groszy"
        )
        self.assertEqual(
            num2words(1950, lang='pl', to='currency', cents=False),
            "dziewiętnaście euro, 50 centów"
        )
