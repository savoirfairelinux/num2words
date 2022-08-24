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


class Num2WordsTGTest(TestCase):
    def test_cardinal(self):
        with self.assertRaises(OverflowError):
            num2words(1000000000000000000000000, lang="tg")
        self.assertEqual(num2words(100, lang="tg"), "сад")
        self.assertEqual(num2words(100000, lang="tg"), "сад ҳазор")
        self.assertEqual(num2words(101, lang="tg"), "яксаду як")
        self.assertEqual(num2words(110, lang="tg"), "яксаду даҳ")
        self.assertEqual(num2words(115, lang="tg"), "яксаду понздаҳ")
        self.assertEqual(num2words(123, lang="tg"), "яксаду бисту се")
        self.assertEqual(num2words(1000, lang="tg"), "як ҳазор")
        self.assertEqual(num2words(1001, lang="tg"), "як ҳазору як")
        self.assertEqual(num2words(2012, lang="tg"), "ду ҳазору дувоздаҳ")
        self.assertEqual(
            num2words(12519.85, lang="tg"),
            "дувоздаҳ ҳазору панҷсаду нуздаҳ нуқта ҳашт панҷ",
        )

        self.assertEqual(
            num2words(1234567890, lang="tg"),
            "як миллиарду дусаду сию чор миллиону панҷсаду шасту ҳафт ҳазору "
            "ҳаштсаду навад",
        )
        self.assertEqual(num2words(1000000, lang="tg"), "як миллион")
        self.assertEqual(num2words(1000000000, lang="tg"), "як миллиард")
        self.assertEqual(num2words(1000000000000, lang="tg"), "як триллион")
        self.assertEqual(num2words(5, lang="tg"), "панҷ")
        self.assertEqual(num2words(-1, lang="tg"), "минус як")
        self.assertEqual(num2words(-15, lang="tg"), "минус понздаҳ")
        self.assertEqual(num2words(-100, lang="tg"), "минус сад")

    def test_to_ordinal(self):
        self.assertEqual(num2words(1, lang="tg", to="ordinal"), "якум")
        self.assertEqual(num2words(2, lang="tg", to="ordinal"), "дуюм")
        self.assertEqual(num2words(3, lang="tg", to="ordinal"), "сеюм")
        self.assertEqual(num2words(30, lang="tg", to="ordinal"), "сиюм")

        self.assertEqual(num2words(13, lang="tg", to="ordinal"), "сенздаҳум")
        self.assertEqual(num2words(20, lang="tg", to="ordinal"), "бистум")
        self.assertEqual(num2words(23, lang="tg", to="ordinal"), "бисту сеюм")
        self.assertEqual(num2words(100, lang="tg", to="ordinal"), "садум")
        self.assertEqual(
            num2words(136, lang="tg", to="ordinal"), "яксаду сию шашум"
        )
        self.assertEqual(num2words(500, lang="tg", to="ordinal"), "панҷсадум")
        self.assertEqual(
            num2words(1000, lang="tg", to="ordinal"), "як ҳазорум"
        )
        self.assertEqual(
            num2words(1001, lang="tg", to="ordinal"), "як ҳазору якум"
        )
        self.assertEqual(
            num2words(2000, lang="tg", to="ordinal"), "ду ҳазорум"
        )
        self.assertEqual(
            num2words(1000000, lang="tg", to="ordinal"), "як миллионум"
        )
        self.assertEqual(
            num2words(1000000000, lang="tg", to="ordinal"), "як миллиардум"
        )

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang="tg", to="currency", currency="EUR"),
            "як евро, сифр сент",
        )
        self.assertEqual(
            num2words(1.0, lang="tg", to="currency", currency="TJS"),
            "як сомонӣ, сифр дирам",
        )
        self.assertEqual(
            num2words(1234.56, lang="tg", to="currency", currency="TJS"),
            "як ҳазору дусаду сию чор сомонӣ, панҷову шаш дирам",
        )
        self.assertEqual(
            num2words(1234.56, lang="tg", to="currency", currency="RUB"),
            "як ҳазору дусаду сию чор рубл, панҷову шаш копейк",
        )
        self.assertEqual(
            num2words(
                12519.85, lang="tg", to="currency", currency="TJS", cents=False
            ),
            "дувоздаҳ ҳазору панҷсаду нуздаҳ сомонӣ, 85 дирам",
        )
        self.assertEqual(
            num2words("1230.56", lang="tg", to="currency", currency="USD"),
            "як ҳазору дусаду си доллар, панҷову шаш сент",
        )

    def test_to_ordinal_num(self):
        self.assertEqual(
            num2words("100", lang="tg", to="ordinal_num"),
            "100ум",
        )
