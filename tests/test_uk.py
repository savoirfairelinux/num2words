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


class Num2WordsUKTest(TestCase):
    def test_to_cardinal(self):
        self.maxDiff = None
        self.assertEqual(num2words(100, lang='uk'), 'сто')
        # self.assertEqual(num2words(101, lang='uk'), 'сто один')
        self.assertEqual(num2words(110, lang='uk'), 'сто десять')
        self.assertEqual(num2words(115, lang='uk'), "сто п'ятнадцять")
        self.assertEqual(num2words(123, lang='uk'), 'сто двадцять три')
        self.assertEqual(num2words(1000, lang='uk'), 'одна тисяча')
        # self.assertEqual(num2words(1001, lang='uk'), 'одна тисяча один')
        self.assertEqual(num2words(2012, lang='uk'), 'двi тисячi дванадцять')
        self.assertEqual(
            num2words(12519.85, lang='uk'),
            "дванадцять тисяч п'ятсот дев'ятнадцять кома вiсiмдесят п'ять")
        # self.assertEqual(
        #    num2words(1234567890, lang='uk'),
        #    "мiльярд двiстi тридцать чотири мiльйона п'ятсот шiстдесят сiмь "
        #    "тисяч вiсiмсот дев'яносто")
        # self.assertEqual(
        #     num2words(215461407892039002157189883901676, lang='uk'),
        #     "двiстi п'ятнадцять нонiльйонiв чотириста шiстдесят один "
        #     "октильйон чотириста сiм септильйонiв вiсiмсот дев'яносто "
        #     "два секстильйони тридцять дев'ять квiнтильйонiв два "
        #     "квадрильйони сто п'ятдесят сiм трильйонiв сто вiсiмдесят "
        #     "дев'ять мiльярдiв вiсiмсот вiсiмдесят три мiльйона "
        #     "дев'ятсот одна тисяча шiстсот "
        #     "сiмдесят шiсть")
        # self.assertEqual(
        #     num2words(719094234693663034822824384220291, lang='uk'),
        #     "сiмсот дев'ятнадцять нонiльйонiв дев'яносто чотири октильйони "
        #     "двiстi тридцять чотири септильйони шiстсот дев'яносто три "
        #     "секстильйони шiстсот шiстдесят три квiнтильйони тридцять "
        #     "чотири квадрильйони вiсiмсот двадцять два трильйони вiсiмсот "
        #     "двадцять чотири мiльярди триста вiсiмдесят чотири мiльйона "
        #     "двiстi двадцять тисяч двiстi дев'яносто один")

    def test_and_join_199(self):
        self.assertEqual(num2words(187, lang='uk'), "сто вiсiмдесят сiм")

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            num2words(12.40, lang='uk'), "дванадцять кома чотири"
        )
        self.assertEqual(
            num2words(17.31, lang='uk'), "сiмнадцять кома тридцять одна"
        )
        self.assertEqual(
            num2words(14.13, lang='uk'), "чотирнадцять кома тринадцять"
        )
        self.assertEqual(
            num2words(12.31, lang='uk'), "дванадцять кома тридцять одна"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='uk', to='ordinal')

    def test_to_currency(self):
        # self.assertEqual(
        #     num2words(1.0, lang='uk', to='currency', currency='EUR'),
        #     "один євро, нуль центiв"
        # )
        self.assertEqual(
            num2words(1.0, lang='uk', to='currency', currency='UAH'),
            "одна гривня, нуль копiйок"
        )
        self.assertEqual(
            num2words(1234.56, lang='uk', to='currency', currency='EUR'),
            "одна тисяча двiстi тридцять чотири євро, п'ятдесят шiсть центiв"
        )
        self.assertEqual(
            num2words(1234.56, lang='uk', to='currency', currency='UAH'),
            "одна тисяча двiстi тридцять чотири гривнi, п'ятдесят шiсть "
            "копiйок"
        )
        # self.assertEqual(
        #     num2words(10111, lang='uk', to='currency', currency='EUR',
        #               separator=u' та'),
        #     "сто один євро та одинадцять центiв"
        # )
        self.assertEqual(
            num2words(10121, lang='uk', to='currency', currency='UAH',
                      separator=u' та'),
            "сто одна гривня та двадцять одна копiйка"
        )
        self.assertEqual(
            num2words(10121, lang='uk', to='currency', currency='UAH',
                      separator=u' та'),
            "сто одна гривня та двадцять одна копiйка"
        )
        self.assertEqual(
            num2words(10122, lang='uk', to='currency', currency='UAH',
                      separator=u' та'),
            "сто одна гривня та двадцять двi копiйки"
        )
        # self.assertEqual(
        #     num2words(10121, lang='uk', to='currency', currency='EUR',
        #               separator=u' та'),
        #     "сто один євро та двадцять один цент"
        # )
        self.assertEqual(
            num2words(-1251985, lang='uk', to='currency', currency='EUR',
                      cents=False),
            "мiнус дванадцять тисяч п'ятсот дев'ятнадцять євро, 85 центiв"
        )
        self.assertEqual(
            num2words('38.4', lang='uk', to='currency', separator=' и',
                      cents=False, currency='EUR'),
            "тридцять вiсiм євро и 40 центiв"
        )
