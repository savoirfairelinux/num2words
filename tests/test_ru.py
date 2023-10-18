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


class Num2WordsRUTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='ru'), "сто")
        self.assertEqual(num2words(101, lang='ru'), "сто один")
        self.assertEqual(num2words(110, lang='ru'), "сто десять")
        self.assertEqual(num2words(115, lang='ru'), "сто пятнадцать")
        self.assertEqual(num2words(123, lang='ru'), "сто двадцать три")
        self.assertEqual(num2words(1000, lang='ru'), "одна тысяча")
        self.assertEqual(num2words(1001, lang='ru'), "одна тысяча один")
        self.assertEqual(num2words(2012, lang='ru'), "две тысячи двенадцать")
        self.assertEqual(
            num2words(12519.85, lang='ru'),
            "двенадцать тысяч пятьсот девятнадцать целых восемьдесят пять "
            "сотых"
        )
        self.assertEqual(
            num2words(1234567890, lang='ru'),
            "один миллиард двести тридцать четыре миллиона пятьсот "
            "шестьдесят семь тысяч восемьсот девяносто")
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='ru'),
            "двести пятнадцать нониллионов четыреста шестьдесят один "
            "октиллион четыреста семь септиллионов восемьсот девяносто "
            "два секстиллиона тридцать девять квинтиллионов два квадриллиона "
            "сто пятьдесят семь триллионов сто восемьдесят девять миллиардов "
            "восемьсот восемьдесят три миллиона девятьсот одна тысяча "
            "шестьсот семьдесят шесть")
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='ru'),
            "семьсот девятнадцать нониллионов девяносто четыре октиллиона "
            "двести тридцать четыре септиллиона шестьсот девяносто три "
            "секстиллиона шестьсот шестьдесят три квинтиллиона тридцать "
            "четыре квадриллиона восемьсот двадцать два триллиона восемьсот "
            "двадцать четыре миллиарда триста восемьдесят четыре миллиона "
            "двести двадцать тысяч двести девяносто один")
        self.assertEqual(num2words(5, lang='ru'), "пять")
        self.assertEqual(num2words(15, lang='ru'), "пятнадцать")
        self.assertEqual(num2words(154, lang='ru'), "сто пятьдесят четыре")
        self.assertEqual(
            num2words(1135, lang='ru'), "одна тысяча сто тридцать пять"
        )
        self.assertEqual(
            num2words(418531, lang='ru'),
            "четыреста восемнадцать тысяч пятьсот тридцать один"
        )
        self.assertEqual(
            num2words(1000139, lang='ru'), "один миллион сто тридцать девять"
        )
        self.assertEqual(num2words(-1, lang='ru'), "минус один")
        self.assertEqual(num2words(-15, lang='ru'), "минус пятнадцать")
        self.assertEqual(num2words(-100, lang='ru'), "минус сто")

    def test_cardinal_feminine(self):
        self.assertEqual(num2words(1, lang='ru', gender='f'), 'одна')
        self.assertEqual(num2words(2, lang='ru', gender='f'), 'две')
        self.assertEqual(num2words(3, lang='ru', gender='f'), 'три')
        self.assertEqual(num2words(100, lang='ru', gender='f'), "сто")
        self.assertEqual(num2words(101, lang='ru', gender='f'), "сто одна")
        self.assertEqual(num2words(110, lang='ru', gender='f'), "сто десять")
        self.assertEqual(
            num2words(115, lang='ru', gender='f'), "сто пятнадцать"
        )
        self.assertEqual(
            num2words(122, lang='ru', gender='f'), "сто двадцать две"
        )
        self.assertEqual(
            num2words(125.1, lang='ru', gender='f'),
            'сто двадцать пять целых одна десятая'
        )
        self.assertEqual(num2words(-1, lang='ru', gender='f'), "минус одна")
        self.assertEqual(num2words(-100, lang='ru', gender='f'), "минус сто")

    def test_cardinal_neuter(self):
        self.assertEqual(num2words(1, lang='ru', gender='n'), 'одно')
        self.assertEqual(num2words(2, lang='ru', gender='n'), 'два')
        self.assertEqual(num2words(3, lang='ru', gender='n'), 'три')
        self.assertEqual(num2words(100, lang='ru', gender='n'), "сто")
        self.assertEqual(num2words(101, lang='ru', gender='n'), "сто одно")
        self.assertEqual(num2words(110, lang='ru', gender='n'), "сто десять")
        self.assertEqual(
            num2words(115, lang='ru', gender='n'), "сто пятнадцать"
        )
        self.assertEqual(
            num2words(122, lang='ru', gender='n'), "сто двадцать два"
        )
        self.assertEqual(
            num2words(125.1, lang='ru', gender='n'),
            'сто двадцать пять целых одна десятая')
        self.assertEqual(num2words(-1, lang='ru', gender='n'), "минус одно")
        self.assertEqual(num2words(-100, lang='ru', gender='n'), "минус сто")

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang='ru'), "пять целых две десятых")
        self.assertEqual(num2words(5.0, lang='ru'), "пять целых ноль десятых")
        self.assertEqual(num2words(5.10, lang='ru'), "пять целых одна десятая")
        self.assertEqual(num2words("5.10", lang='ru'),
                         "пять целых десять сотых")
        self.assertEqual(num2words(1.001, lang='ru'),
                         "одна целая одна тысячная")
        self.assertEqual(num2words(1.011, lang='ru'),
                         "одна целая одиннадцать тысячных")
        self.assertEqual(num2words(10.02, lang='ru'),
                         "десять целых две сотых")
        self.assertEqual(num2words(15.007, lang='ru'),
                         "пятнадцать целых семь тысячных")
        self.assertEqual(num2words(561.42, lang='ru'),
                         "пятьсот шестьдесят одна целая сорок две сотых")
        self.assertEqual(num2words(561.00001, lang='ru'),
                         "пятьсот шестьдесят одна целая одна стотысячная")

    def test_to_ordinal(self):
        self.assertEqual(
            num2words(0, lang='ru', to='ordinal'),
            'нулевой'
        )
        self.assertEqual(
            num2words(1, lang='ru', to='ordinal'),
            'первый'
        )
        self.assertEqual(
            num2words(5, lang='ru', to='ordinal'),
            'пятый'
        )
        self.assertEqual(
            num2words(10, lang='ru', to='ordinal'),
            'десятый'
        )

        self.assertEqual(
            num2words(13, lang='ru', to='ordinal'),
            'тринадцатый'
        )
        self.assertEqual(
            num2words(20, lang='ru', to='ordinal'),
            'двадцатый'
        )
        self.assertEqual(
            num2words(23, lang='ru', to='ordinal'),
            'двадцать третий'
        )
        self.assertEqual(
            num2words(40, lang='ru', to='ordinal'),
            'сороковой'
        )
        self.assertEqual(
            num2words(70, lang='ru', to='ordinal'),
            'семидесятый'
        )
        self.assertEqual(
            num2words(100, lang='ru', to='ordinal'),
            'сотый'
        )
        self.assertEqual(
            num2words(136, lang='ru', to='ordinal'),
            'сто тридцать шестой'
        )
        self.assertEqual(
            num2words(500, lang='ru', to='ordinal'),
            'пятисотый'
        )
        self.assertEqual(
            num2words(1000, lang='ru', to='ordinal'),
            'тысячный'
        )
        self.assertEqual(
            num2words(1001, lang='ru', to='ordinal'),
            'тысяча первый'
        )
        self.assertEqual(
            num2words(1060, lang='ru', to='ordinal'),
            'тысяча шестидесятый'
        )
        self.assertEqual(
            num2words(2000, lang='ru', to='ordinal'),
            'двухтысячный'
        )
        self.assertEqual(
            num2words(10000, lang='ru', to='ordinal'),
            'десятитысячный'
        )
        self.assertEqual(
            num2words(90000, lang='ru', to='ordinal'),
            'девяностотысячный'
        )
        self.assertEqual(
            num2words(21000, lang='ru', to='ordinal'),
            'двадцатиоднотысячный'
        )
        self.assertEqual(
            num2words(130000, lang='ru', to='ordinal'),
            'стотридцатитысячный'
        )
        self.assertEqual(
            num2words(135000, lang='ru', to='ordinal'),
            'стотридцатипятитысячный'
        )
        self.assertEqual(
            num2words(135100, lang='ru', to='ordinal'),
            'сто тридцать пять тысяч сотый'
        )
        self.assertEqual(
            num2words(135120, lang='ru', to='ordinal'),
            'сто тридцать пять тысяч сто двадцатый'
        )
        self.assertEqual(
            num2words(135121, lang='ru', to='ordinal'),
            'сто тридцать пять тысяч сто двадцать первый'
        )
        self.assertEqual(
            num2words(190000, lang='ru', to='ordinal'),
            'стодевяностотысячный'
        )
        self.assertEqual(
            num2words(1000000, lang='ru', to='ordinal'),
            'миллионный'
        )
        self.assertEqual(
            num2words(2000000, lang='ru', to='ordinal'),
            'двухмиллионный'
        )
        self.assertEqual(
            num2words(5135000, lang='ru', to='ordinal'),
            'пять миллионов стотридцатипятитысячный'
        )
        self.assertEqual(
            num2words(21000000, lang='ru', to='ordinal'),
            'двадцатиодномиллионный'
        )
        self.assertEqual(
            num2words(1000000000, lang='ru', to='ordinal'),
            'миллиардный'
        )
        self.assertEqual(
            num2words(123456000000, lang='ru', to='ordinal'),
            'сто двадцать три миллиарда четырёхсотпятидесятишестимиллионный'
        )

    def test_to_ordinal_feminine(self):
        self.assertEqual(
            num2words(1, lang='ru', to='ordinal', gender='f'), 'первая'
        )
        self.assertEqual(
            num2words(3, lang='ru', to='ordinal', gender='f'), 'третья'
        )
        self.assertEqual(
            num2words(10, lang='ru', to='ordinal', gender='f'), 'десятая'
        )
        self.assertEqual(
            num2words(23, lang='ru', to='ordinal', gender='f'),
            'двадцать третья'
        )
        self.assertEqual(
            num2words(1000, lang='ru', to='ordinal', gender='f'), 'тысячная'
        )
        self.assertEqual(
            num2words(2000000, lang='ru', to='ordinal', gender='f'),
            'двухмиллионная'
        )

    def test_to_ordinal_neuter(self):
        self.assertEqual(
            num2words(1, lang='ru', to='ordinal', gender='n'), 'первое'
        )
        self.assertEqual(
            num2words(3, lang='ru', to='ordinal', gender='n'), 'третье'
        )
        self.assertEqual(
            num2words(10, lang='ru', to='ordinal', gender='n'), 'десятое'
        )
        self.assertEqual(
            num2words(23, lang='ru', to='ordinal', gender='n'),
            'двадцать третье'
        )
        self.assertEqual(
            num2words(1000, lang='ru', to='ordinal', gender='n'), 'тысячное'
        )
        self.assertEqual(
            num2words(2000000, lang='ru', to='ordinal', gender='n'),
            'двухмиллионное'
        )

    def test_cardinal_cases(self):
        self.assertEqual(
            num2words(1, lang='ru', case='nominative'), 'один')
        self.assertEqual(
            num2words(1, lang='ru', case='genitive'), 'одного')
        self.assertEqual(
            num2words(1, lang='ru', case='a', plural=True, animate=False),
            'одни')
        self.assertEqual(
            num2words(2, lang='ru', case='a', gender='f', animate=True),
            'двух')
        self.assertEqual(
            num2words(2, lang='ru', case='a', gender='f', animate=False),
            'две')
        self.assertEqual(
            num2words(100, lang='ru', case='g'),
            'ста')
        self.assertEqual(
            num2words(122, lang='ru', case='d'),
            'ста двадцати двум')
        self.assertEqual(
            num2words(1000, lang='ru', case='p'),
            'одной тысяче')
        self.assertEqual(
            num2words(1122, lang='ru', case='p'),
            'одной тысяче ста двадцати двух')
        self.assertEqual(
            num2words(1211, lang='ru', case='i', gender='f'),
            'одной тысячей двумястами одиннадцатью')
        self.assertEqual(
            num2words(5121000, lang='ru', case='i'),
            'пятью миллионами ста двадцатью одной тысячей')

    def test_ordinal_cases(self):
        self.assertEqual(
            num2words(1, lang='ru', to='ordinal', case='nominative'), 'первый')
        self.assertEqual(
            num2words(1, lang='ru', to='ordinal', case='genitive'), 'первого')
        self.assertEqual(
            num2words(1, lang='ru', to='ordinal', case='a', plural=True,
                      animate=False),
            'первые')
        self.assertEqual(
            num2words(2, lang='ru', to='ordinal', case='a', gender='f',
                      animate=True),
            'вторую')
        self.assertEqual(
            num2words(2, lang='ru', to='ordinal', case='a', gender='f',
                      animate=False),
            'вторую')
        self.assertEqual(
            num2words(100, lang='ru', to='ordinal', case='g'),
            'сотого')
        self.assertEqual(
            num2words(122, lang='ru', to='ordinal', case='d'),
            'сто двадцать второму')
        self.assertEqual(
            num2words(1000, lang='ru', to='ordinal', case='p'),
            'тысячном')
        self.assertEqual(
            num2words(1122, lang='ru', to='ordinal', case='p'),
            'тысяча сто двадцать втором')
        self.assertEqual(
            num2words(1211, lang='ru', to='ordinal', case='i', gender='f'),
            'тысяча двести одиннадцатой')
        self.assertEqual(
            num2words(5121000, lang='ru', to='ordinal', case='i'),
            'пять миллионов стодвадцатиоднотысячным')

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='ru', to='currency', currency='EUR'),
            'один евро, ноль центов'
        )
        self.assertEqual(
            num2words(1.0, lang='ru', to='currency', currency='RUB'),
            'один рубль, ноль копеек'
        )
        self.assertEqual(
            num2words(1.0, lang='ru', to='currency', currency='UAH'),
            'одна гривна, ноль копеек'
        )
        self.assertEqual(
            num2words(1234.56, lang='ru', to='currency', currency='EUR'),
            'одна тысяча двести тридцать четыре евро, пятьдесят шесть центов'
        )
        self.assertEqual(
            num2words(1234.56, lang='ru', to='currency', currency='RUB'),
            'одна тысяча двести тридцать четыре рубля, пятьдесят шесть копеек'
        )
        self.assertEqual(
            num2words(1234.56, lang='ru', to='currency', currency='UAH'),
            'одна тысяча двести тридцать четыре гривны, пятьдесят шесть копеек'
        )
        self.assertEqual(
            num2words(10111, lang='ru', to='currency', currency='EUR',
                      separator=' и'),
            'сто один евро и одиннадцать центов'
        )
        self.assertEqual(
            num2words(10111, lang='ru', to='currency', currency='RUB',
                      separator=' и'),
            'сто один рубль и одиннадцать копеек'
        )
        self.assertEqual(
            num2words(10111, lang='ru', to='currency', currency='UAH',
                      separator=' и'),
            'сто одна гривна и одиннадцать копеек'
        )
        self.assertEqual(
            num2words(10121, lang='ru', to='currency', currency='EUR',
                      separator=' и'),
            'сто один евро и двадцать один цент'
        )
        self.assertEqual(
            num2words(10121, lang='ru', to='currency', currency='RUB',
                      separator=' и'),
            'сто один рубль и двадцать одна копейка'
        )
        self.assertEqual(
            num2words(10121, lang='ru', to='currency', currency='UAH',
                      separator=' и'),
            'сто одна гривна и двадцать одна копейка'
        )
        self.assertEqual(
            num2words(10122, lang='ru', to='currency', currency='EUR',
                      separator=' и'),
            'сто один евро и двадцать два цента'
        )
        self.assertEqual(
            num2words(10122, lang='ru', to='currency', currency='RUB',
                      separator=' и'),
            'сто один рубль и двадцать две копейки'
        )
        self.assertEqual(
            num2words(10122, lang='ru', to='currency', currency='UAH',
                      separator=' и'),
            'сто одна гривна и двадцать две копейки'
        )
        self.assertEqual(
            num2words(-1251985, lang='ru', to='currency', currency='EUR',
                      cents=False),
            'минус двенадцать тысяч пятьсот девятнадцать евро, 85 центов'
        )
        self.assertEqual(
            num2words(-1251985, lang='ru', to='currency', currency='RUB',
                      cents=False),
            'минус двенадцать тысяч пятьсот девятнадцать рублей, 85 копеек'
        )
        self.assertEqual(
            num2words(-1251985, lang='ru', to='currency', currency='UAH',
                      cents=False),
            'минус двенадцать тысяч пятьсот девятнадцать гривен, 85 копеек'
        )
        self.assertEqual(
            num2words('38.4', lang='ru', to='currency', separator=' и',
                      cents=False, currency='EUR'),
            "тридцать восемь евро и 40 центов"
        )
        self.assertEqual(
            num2words('38.4', lang='ru', to='currency', separator=' и',
                      cents=False, currency='RUB'),
            "тридцать восемь рублей и 40 копеек"
        )
        self.assertEqual(
            num2words('38.4', lang='ru', to='currency', separator=' и',
                      cents=False, currency='UAH'),
            "тридцать восемь гривен и 40 копеек"
        )
        self.assertEqual(
            num2words('1230.56', lang='ru', to='currency', currency='USD'),
            'одна тысяча двести тридцать долларов, пятьдесят шесть центов'
        )
        self.assertEqual(
            num2words('1231.56', lang='ru', to='currency', currency='USD'),
            'одна тысяча двести тридцать один доллар, пятьдесят шесть центов'
        )
        self.assertEqual(
            num2words('1234.56', lang='ru', to='currency', currency='USD'),
            'одна тысяча двести тридцать четыре доллара, пятьдесят шесть '
            'центов'
        )
        self.assertEqual(
            num2words(10122, lang='ru', to='currency', currency='UZS',
                      separator=' и'),
            'сто один сум и двадцать два тийина'
        )
