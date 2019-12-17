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


class Num2WordsUATest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='ua'), "сто")
        self.assertEqual(num2words(101, lang='ua'), "сто один")
        self.assertEqual(num2words(110, lang='ua'), "сто десять")
        self.assertEqual(num2words(115, lang='ua'), "сто п’ятнадцять")
        self.assertEqual(num2words(123, lang='ua'), "сто двадцять три")
        self.assertEqual(num2words(1000, lang='ua'), "одна тисяча")
        self.assertEqual(num2words(1001, lang='ua'), "одна тисяча один")
        self.assertEqual(num2words(2012, lang='ua'), "дві тисячі дванадцять")
        self.assertEqual(
            num2words(12519.85, lang='ua'),
            "дванадцять тисяч п’ятсот дев’ятнадцять кома вісімдесят п’ять")
        self.assertEqual(
            num2words(1234567890, lang='ua'),
            "один мільярд двісті тридцять чотири мільйони п’ятсот "
            "шістдесят сім тисяч вісімсот дев’яносто")
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='ua'),
            "двісті п’ятнадцять нонілліонов чотириста шістдесят один "
            "октілліон чотириста сім септілліонов вісімсот дев’яносто "
            "два секстильйонів тридцять дев’ять квінтильйонів два "
            "квадрильйона сто п’ятдесят сім трильйонів сто вісімдесят дев’ять "
            "мільярдів вісімсот вісімдесят три мільйони дев’ятсот одна тисяча "
            "шістсот сімдесят шість")
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='ua'),
            "сімсот дев’ятнадцять нонілліонов дев’яносто чотири октілліона "
            "двісті тридцять чотири септілліона шістсот дев’яносто три "
            "секстильйонів шістсот шістдесят три квінтильйони тридцять "
            "чотири квадрильйона вісімсот двадцять два трильйона вісімсот "
            "двадцять чотири мільярди триста вісімдесят чотири мільйони "
            "двісті двадцять тисяч двісті дев’яносто один")
        self.assertEqual(num2words(5, lang='ua'), "п’ять")
        self.assertEqual(num2words(15, lang='ua'), "п’ятнадцять")
        self.assertEqual(num2words(154, lang='ua'), "сто п’ятдесят чотири")

        self.assertEqual(
            num2words(1135, lang='ua'), "одна тисяча сто тридцять п’ять"
        )
        self.assertEqual(
            num2words(418531, lang='ua'),
            "чотириста вісімнадцять тисяч п’ятсот тридцять один"
        )
        self.assertEqual(
            num2words(1000139, lang='ua'), "один мільйон сто тридцять дев’ять"
        )
        self.assertEqual(num2words(-1, lang='ua'), "мінус один")
        self.assertEqual(num2words(-15, lang='ua'), "мінус п’ятнадцять")
        self.assertEqual(num2words(-100, lang='ua'), "мінус сто")

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang='ua'), "п’ять кома два")
        self.assertEqual(
            num2words(561.42, lang='ua'),
            "п’ятсот шістдесят один кома сорок два"
        )

    def test_to_ordinal(self):
        self.assertEqual(
            num2words(1, lang='ua', to='ordinal'),
            "перший"
        )
        self.assertEqual(
            num2words(5, lang='ua', to='ordinal'),
            "п’ятий"
        )
        self.assertEqual(
            num2words(10, lang='ua', to='ordinal'),
            "десятий"
        )

        self.assertEqual(
            num2words(13, lang='ua', to='ordinal'),
            "тринадцятий"
        )
        self.assertEqual(
            num2words(20, lang='ua', to='ordinal'),
            "двадцятий"
        )
        self.assertEqual(
            num2words(23, lang='ua', to='ordinal'),
            "двадцять третій"
        )
        self.assertEqual(
            num2words(40, lang='ua', to='ordinal'),
            "сороковий"
        )
        self.assertEqual(
            num2words(70, lang='ua', to='ordinal'),
            "сімдесятий"
        )
        self.assertEqual(
            num2words(100, lang='ua', to='ordinal'),
            "сотий"
        )
        self.assertEqual(
            num2words(136, lang='ua', to='ordinal'),
            "сто тридцять шостий"
        )
        self.assertEqual(
            num2words(500, lang='ua', to='ordinal'),
            "п’ятсот"
        )
        self.assertEqual(
            num2words(1000, lang='ua', to='ordinal'),
            "тисячний"
        )
        self.assertEqual(
            num2words(1001, lang='ua', to='ordinal'),
            "тисяча перший"
        )
        self.assertEqual(
            num2words(2000, lang='ua', to='ordinal'),
            "двох тисячний"
        )
        self.assertEqual(
            num2words(10000, lang='ua', to='ordinal'),
            "десяти тисячний"
        )
        self.assertEqual(
            num2words(1000000, lang='ua', to='ordinal'),
            "мільйонний"
        )
        self.assertEqual(
            num2words(1000000000, lang='ua', to='ordinal'),
            "мільярдний"
        )

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='ua', to='currency', currency='EUR'),
            "один євро, нуль центів"
        )
        self.assertEqual(
            num2words(1.0, lang='ua', to='currency', currency='UAH'),
            "одна гривня, нуль копійок"
        )
        self.assertEqual(
            num2words(1.0, lang='ua', to='currency', currency='RUB'),
            "один рубль, нуль копійок"
        )
        self.assertEqual(
            num2words(1234.56, lang='ua', to='currency', currency='EUR'),
            "одна тисяча двісті тридцять чотири євро, п’ятдесят шість центів"
        )
        self.assertEqual(
            num2words(1234.56, lang='ua', to='currency', currency='UAH'),
            "одна тисяча двісті тридцять чотири гривні, п’ятдесят шість копійок"
        )
        self.assertEqual(
            num2words(10111, lang='ua', to='currency', currency='EUR',
                      separator=' і'),
            "сто один євро і одинадцять центів"
        )
        self.assertEqual(
            num2words(10121, lang='ua', to='currency', currency='UAH',
                      separator=' і'),
            "сто одна гривня і двадцять одна копійка"
        )
        self.assertEqual(
            num2words(10121, lang='ua', to='currency', currency='RUB',
                      separator=' і'),
            "сто один рубль і двадцять одна копійка"
        )
        self.assertEqual(
            num2words(10122, lang='ua', to='currency', currency='UAH',
                      separator=' і'),
            "сто одна гривня і двадцять дві копійки"
        )
        self.assertEqual(
            num2words(10122, lang='ua', to='currency', currency='RUB',
                      separator=' і'),
            "сто один рубль і двадцять дві копійки"
        )
        self.assertEqual(
            num2words(10121, lang='ua', to='currency', currency='EUR',
                      separator=' і'),
            "сто один євро і двадцять один цент"
        )
        self.assertEqual(
            num2words(-1251985, lang='ua', to="currency", currency='EUR',
                      cents=False),
            "мінус дванадцять тисяч п’ятсот дев’ятнадцять євро, 85 центів"
        )
        self.assertEqual(
            num2words('38.4', lang='ua', to='currency', separator=' і',
                      cents=False, currency='EUR'),
            "тридцять вісім євро і 40 центів"
        )
        self.assertEqual(
            num2words('1230.56', lang='ua', to='currency', currency='USD'),
            "одна тисяча двісті тридцять доларів, п’ятдесят шість центів"
        )
        self.assertEqual(
            num2words('1231.56', lang='ua', to='currency', currency='USD'),
            "одна тисяча двісті тридцять один долар, п’ятдесят шість центів"
        )
        self.assertEqual(
            num2words('1234.56', lang='ua', to='currency', currency='USD'),
            "одна тисяча двісті тридцять чотири долара, п’ятдесят шість "
            "центів"
        )
