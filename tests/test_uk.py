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
        self.assertEqual(num2words(100, lang='uk'), "сто")
        self.assertEqual(num2words(101, lang='uk'), "сто один")
        self.assertEqual(num2words(110, lang='uk'), "сто десять")
        self.assertEqual(num2words(115, lang='uk'), "сто п'ятнадцять")
        self.assertEqual(num2words(123, lang='uk'), "сто двадцять три")
        self.assertEqual(num2words(1000, lang='uk'), "одна тисяча")
        self.assertEqual(num2words(1001, lang='uk'), "одна тисяча один")
        self.assertEqual(num2words(2012, lang='uk'), "дві тисячі дванадцять")
        self.assertEqual(
            num2words(12519.85, lang='uk'),
            "дванадцять тисяч п'ятсот дев'ятнадцять кома вісімдесят п'ять")
        self.assertEqual(
           num2words(1234567890, lang='uk'),
           "один мільярд двісті тридцять чотири мільйони п'ятсот шістдесят сім "
           "тисяч вісімсот дев'яносто")
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='uk'),
            "двісті п'ятнадцять нонільйонів чотириста шістдесят один "
            "октильйон чотириста сім септильйонів вісімсот дев'яносто "
            "два секстильйони тридцять дев'ять квінтильйонів два "
            "квадрильйони сто п'ятдесят сім трильйонів сто вісімдесят "
            "дев'ять мільярдів вісімсот вісімдесят три мільйони "
            "дев'ятсот одна тисяча шістсот "
            "сімдесят шість")
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='uk'),
            "сімсот дев'ятнадцять нонільйонів дев'яносто чотири октильйони "
            "двісті тридцять чотири септильйони шістсот дев'яносто три "
            "секстильйони шістсот шістдесят три квінтильйони тридцять "
            "чотири квадрильйони вісімсот двадцять два трильйони вісімсот "
            "двадцять чотири мільярди триста вісімдесят чотири мільйони "
            "двісті двадцять тисяч двісті дев'яносто один")

    def test_and_join_199(self):
        self.assertEqual(num2words(199, lang='uk'), "сто дев'яносто дев'ять")

    def test_cardinal_for_float_number(self):
        self.assertEqual(
            num2words(12.40, lang='uk'), "дванадцять кома чотири"
        )
        self.assertEqual(
            num2words(17.31, lang='uk'), "сімнадцять кома тридцять один"
        )
        self.assertEqual(
            num2words(14.13, lang='uk'), "чотирнадцять кома тринадцять"
        )
        self.assertEqual(
            num2words(12.31, lang='uk'), "дванадцять кома тридцять один"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='uk', to='ordinal')

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='uk', to='currency', currency='EUR'),
            "один євро, нуль центів"
        )
        self.assertEqual(
            num2words(1.0, lang='uk', to='currency', currency='UAH'),
            "одна гривня, нуль копійок"
        )
        self.assertEqual(
            num2words(1234.56, lang='uk', to='currency', currency='EUR'),
            "одна тисяча двісті тридцять чотири євро, п'ятдесят шість центів"
        )
        self.assertEqual(
            num2words(1234.56, lang='uk', to='currency', currency='UAH'),
            "одна тисяча двісті тридцять чотири гривні, п'ятдесят шість "
            "копійок"
        )
        self.assertEqual(
            num2words(101.11, lang='uk', to='currency', currency='EUR',
                      separator=u' та'),
            "сто один євро та одинадцять центів"
        )
        self.assertEqual(
            num2words(101.11, lang='uk', to='currency', currency='UAH',
                      separator=u' та'),
            "сто одна гривня та одинадцять копійок"
        )
        self.assertEqual(
            num2words(10121, lang='uk', to='currency', currency='EUR',
                      separator=u' та'),
            "сто один євро та двадцять один цент"
        )
        self.assertEqual(
            num2words(10121, lang='uk', to='currency', currency='UAH',
                      separator=u' та'),
            "сто одна гривня та двадцять одна копійка"
        )
        self.assertEqual(
            num2words(10222, lang='uk', to='currency', currency='EUR',
                      separator=u' та'),
            "сто два євро та двадцять два центи"
        )
        self.assertEqual(
            num2words(10222, lang='uk', to='currency', currency='UAH',
                      separator=u' та'),
            "сто дві гривні та двадцять дві копійки"
        )
        self.assertEqual(
            num2words(-1251985, lang='uk', to='currency', currency='EUR',
                      cents=False),
            "мінус дванадцять тисяч п'ятсот дев'ятнадцять євро, 85 центів"
        )
        self.assertEqual(
            num2words(-1251985, lang='uk', to='currency', currency='UAH',
                      cents=False),
            "мінус дванадцять тисяч п'ятсот дев'ятнадцять гривень, 85 копійок"
        )
        self.assertEqual(
            num2words('38.4', lang='uk', to='currency', separator=' і',
                      cents=False, currency='EUR'),
            "тридцять вісім євро і 40 центів"
        )
        self.assertEqual(
            num2words('38.4', lang='uk', to='currency', separator=' і',
                      cents=False, currency='UAH'),
            "тридцять вісім гривень і 40 копійок"
        )
