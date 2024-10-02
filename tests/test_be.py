# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2023, Sergei Ruzki/Ivan Shakh  All Rights Reserved.

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


class Num2WordsBYTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang="be"), "сто")
        self.assertEqual(num2words(101, lang="be"), "сто адзін")
        self.assertEqual(num2words(110, lang="be"), "сто дзесяць")
        self.assertEqual(num2words(115, lang="be"), "сто пятнаццаць")
        self.assertEqual(num2words(123, lang="be"), "сто дваццаць тры")
        self.assertEqual(num2words(1000, lang="be"), "адна тысяча")
        self.assertEqual(num2words(1001, lang="be"), "адна тысяча адзін")
        self.assertEqual(num2words(2012, lang="be"), "дзве тысячы дванаццаць")
        self.assertEqual(
            num2words(12519.85, lang="be"),
            "дванаццаць тысяч пяцьсот дзевятнаццаць коска восемдзесят пяць",
        )
        self.assertEqual(
            num2words(1234567890, lang="be"),
            "адзін мільярд дзвесце трыццаць чатыры мільёны пяцьсот "
            "шэсцьдзясят сем тысяч восемсот дзевяноста",
        )
        self.assertEqual(
            num2words(461407892039002157189883901676, lang="be"),
            "чатырыста шэсцьдзясят адзін "
            "актыльён чатырыста сем сэптыльёнаў восемсот дзевяноста "
            "два секстыльёны трыццаць дзевяць квінтыльёнаў два квадрыльёны "
            "сто пяцьдзясят сем трыльёнаў сто восемдзесят дзевяць мільярдаў "
            "восемсот восемдзесят тры мільёны дзевяцьсот адна тысяча "
            "шэсцьсот семдзесят шэсць",
        )
        self.assertEqual(
            num2words(94234693663034822824384220291, lang="be"),
            "дзевяноста чатыры актыльёны "
            "дзвесце трыццаць чатыры сэптыльёны шэсцьсот дзевяноста тры "
            "секстыльёны шэсцьсот шэсцьдзясят тры квінтыльёны трыццаць "
            "чатыры квадрыльёны восемсот дваццаць два трыльёны восемсот "
            "дваццаць чатыры мільярды трыста восемдзесят чатыры мільёны "
            "дзвесце дваццаць тысяч дзвесце дзевяноста адзін",
        )
        self.assertEqual(num2words(5, lang="be"), "пяць")
        self.assertEqual(num2words(15, lang="be"), "пятнаццаць")
        self.assertEqual(num2words(154, lang="be"), "сто пяцьдзясят чатыры")
        self.assertEqual(
            num2words(1135, lang="be"), "адна тысяча сто трыццаць пяць"
        )
        self.assertEqual(
            num2words(418531, lang="be"),
            "чатырыста васямнаццаць тысяч пяцьсот трыццаць адзін",
        )
        self.assertEqual(
            num2words(1000139, lang="be"), "адзін мільён сто трыццаць дзевяць"
        )
        self.assertEqual(num2words(-1, lang="be"), "мінус адзін")
        self.assertEqual(num2words(-15, lang="be"), "мінус пятнаццаць")
        self.assertEqual(num2words(-100, lang="be"), "мінус сто")

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang="be"), "пяць коска два")
        self.assertEqual(num2words(10.02, lang="be"), "дзесяць коска нуль два")
        self.assertEqual(
            num2words(15.007, lang="be"), "пятнаццаць коска нуль нуль сем"
        )
        self.assertEqual(
            num2words(561.42, lang="be"),
            "пяцьсот шэсцьдзясят адзін коска сорак два",
        )

        self.assertEqual(
            num2words(561.0, lang="be"), "пяцьсот шэсцьдзясят адзін коска нуль"
        )

    def test_to_ordinal(self):
        self.assertEqual(num2words(1, lang="be", to="ordinal"), "першы")
        self.assertEqual(num2words(5, lang="be", to="ordinal"), "пяты")
        self.assertEqual(num2words(6, lang="be", to="ordinal"), "шосты")
        self.assertEqual(num2words(10, lang="be", to="ordinal"), "дзясяты")

        self.assertEqual(num2words(13, lang="be", to="ordinal"), "трынаццаты")
        self.assertEqual(num2words(20, lang="be", to="ordinal"), "дваццаты")
        self.assertEqual(
            num2words(23, lang="be", to="ordinal"), "дваццаць трэці"
        )
        self.assertEqual(
            num2words(23, lang="be", to="ordinal", gender="f"),
            "дваццаць трэцяя",
        )
        self.assertEqual(
            num2words(23, lang="be", to="ordinal", gender=True),
            "дваццаць трэцяя",
        )
        self.assertEqual(
            num2words(23, lang="be", to="ordinal", gender="n"),
            "дваццаць трэцяе",
        )
        self.assertEqual(
            num2words(46, lang="be", to="ordinal", gender="m"),
            "сорак шосты",
        )
        self.assertEqual(num2words(40, lang="be", to="ordinal"), "саракавы")
        self.assertEqual(
            num2words(61, lang="be", to="ordinal"), "шэсцьдзясят першы"
        )
        self.assertEqual(num2words(70, lang="be", to="ordinal"), "сямідзясяты")
        self.assertEqual(num2words(100, lang="be", to="ordinal"), "соты")
        self.assertEqual(
            num2words(136, lang="be", to="ordinal"), "сто трыццаць шосты"
        )
        self.assertEqual(num2words(500, lang="be", to="ordinal"), "пяцісоты")

        self.assertEqual(
            num2words(500, lang="be", to="ordinal", gender="f"), "пяцісотая"
        )

        self.assertEqual(
            num2words(500, lang="be", to="ordinal", gender="n"), "пяцісотае"
        )

        self.assertEqual(num2words(1000, lang="be", to="ordinal"), "тысячны")

        self.assertEqual(
            num2words(1000, lang="be", to="ordinal", gender="f"), "тысячная"
        )

        self.assertEqual(
            num2words(1000, lang="be", to="ordinal", gender="n"), "тысячнае"
        )

        self.assertEqual(
            num2words(1001, lang="be", to="ordinal"), "тысяча першы"
        )
        self.assertEqual(
            num2words(3000, lang="be", to="ordinal"), "трохтысячны"
        )
        self.assertEqual(
            num2words(10000, lang="be", to="ordinal"), "дзесяцітысячны"
        )
        self.assertEqual(
            num2words(30000, lang="be", to="ordinal"), "трыццацітысячны"
        )
        self.assertEqual(
            num2words(42000, lang="be", to="ordinal"), "саракадвухтысячны"
        )

        self.assertEqual(
            num2words(75000, lang="be", to="ordinal"), "сямідзесяціпяцітысячны"
        )

        self.assertEqual(
            num2words(1000000, lang="be", to="ordinal"), "мільённы"
        )
        self.assertEqual(
            num2words(30000000, lang="be", to="ordinal"), "трыццацімільённы"
        )
        self.assertEqual(
            num2words(1000000000, lang="be", to="ordinal"), "мільярдны"
        )
        self.assertEqual(
            num2words(3000000000, lang="be", to="ordinal"), "трохмільярдны"
        )
        self.assertEqual(
            num2words(43000000000, lang="be", to="ordinal"),
            "саракатрохмільярдны",
        )
        self.assertEqual(
            num2words(333000000000, lang="be", to="ordinal"),
            "трыстатрыццацітрохмільярдны",
        )

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang="be", to="currency", currency="EUR"),
            "адзін еўра, нуль цэнтаў",
        )
        self.assertEqual(
            num2words(1.0, lang="be", to="currency", currency="RUB"),
            "адзін расійскі рубель, нуль капеек",
        )
        self.assertEqual(
            num2words(1.0, lang="be", to="currency", currency="BYN"),
            "адзін беларускі рубель, нуль капеек",
        )
        self.assertEqual(
            num2words(1.0, lang="be", to="currency", currency="UAH"),
            "адна грыўна, нуль капеек",
        )
        self.assertEqual(
            num2words(1234.56, lang="be", to="currency", currency="EUR"),
            "адна тысяча дзвесце трыццаць чатыры еўра, "
            "пяцьдзясят шэсць цэнтаў",
        )
        self.assertEqual(
            num2words(1234.56, lang="be", to="currency", currency="RUB"),
            "адна тысяча дзвесце трыццаць чатыры расійскія рублі, "
            "пяцьдзясят шэсць капеек",
        )
        self.assertEqual(
            num2words(1234.56, lang="be", to="currency", currency="BYN"),
            "адна тысяча дзвесце трыццаць чатыры беларускія рублі, "
            "пяцьдзясят шэсць капеек",
        )
        self.assertEqual(
            num2words(1234.56, lang="be", to="currency", currency="UAH"),
            "адна тысяча дзвесце трыццаць чатыры грыўны, "
            "пяцьдзясят шэсць капеек",
        )
        self.assertEqual(
            num2words(
                10111, lang="be", to="currency", currency="EUR", separator=" і"
            ),
            "сто адзін еўра і адзінаццаць цэнтаў",
        )
        self.assertEqual(
            num2words(
                10111, lang="be", to="currency", currency="RUB", separator=" і"
            ),
            "сто адзін расійскі рубель і адзінаццаць капеек",
        )
        self.assertEqual(
            num2words(
                10111, lang="be", to="currency", currency="BYN", separator=" і"
            ),
            "сто адзін беларускі рубель і адзінаццаць капеек",
        )
        self.assertEqual(
            num2words(
                10111, lang="be", to="currency", currency="UAH", separator=" і"
            ),
            "сто адна грыўна і адзінаццаць капеек",
        )
        self.assertEqual(
            num2words(
                10121, lang="be", to="currency", currency="EUR", separator=" і"
            ),
            "сто адзін еўра і дваццаць адзін цэнт",
        )
        self.assertEqual(
            num2words(
                10121, lang="be", to="currency", currency="RUB", separator=" і"
            ),
            "сто адзін расійскі рубель і дваццаць адна капейка",
        )
        self.assertEqual(
            num2words(
                10121, lang="be", to="currency", currency="BYN", separator=" і"
            ),
            "сто адзін беларускі рубель і дваццаць адна капейка",
        )
        self.assertEqual(
            num2words(
                10121, lang="be", to="currency", currency="UAH", separator=" і"
            ),
            "сто адна грыўна і дваццаць адна капейка",
        )
        self.assertEqual(
            num2words(
                10122, lang="be", to="currency", currency="EUR", separator=" і"
            ),
            "сто адзін еўра і дваццаць два цэнты",
        )
        self.assertEqual(
            num2words(
                10122, lang="be", to="currency", currency="RUB", separator=" і"
            ),
            "сто адзін расійскі рубель і дваццаць дзве капейкі",
        )
        self.assertEqual(
            num2words(
                10122, lang="be", to="currency", currency="BYN", separator=" і"
            ),
            "сто адзін беларускі рубель і дваццаць дзве капейкі",
        )
        self.assertEqual(
            num2words(
                10122, lang="be", to="currency", currency="UAH", separator=" і"
            ),
            "сто адна грыўна і дваццаць дзве капейкі",
        )
        self.assertEqual(
            num2words(
                10122, lang="be", to="currency", currency="KZT", separator=" і"
            ),
            "сто адзін тэнге і дваццаць два тыйіны",
        )
        self.assertEqual(
            num2words(
                -1251985, lang="be", to="currency", currency="EUR", cents=False
            ),
            "мінус дванаццаць тысяч пяцьсот дзевятнаццаць еўра, 85 цэнтаў",
        )
        self.assertEqual(
            num2words(
                -1251985, lang="be", to="currency", currency="RUB", cents=False
            ),
            "мінус дванаццаць тысяч пяцьсот дзевятнаццаць "
            "расійскіх рублёў, 85 капеек",
        )
        self.assertEqual(
            num2words(
                -1251985, lang="be", to="currency", currency="BYN", cents=False
            ),
            "мінус дванаццаць тысяч пяцьсот дзевятнаццаць "
            "беларускіх рублёў, 85 капеек",
        )
        self.assertEqual(
            num2words(
                -1251985, lang="be", to="currency", currency="UAH", cents=False
            ),
            "мінус дванаццаць тысяч пяцьсот дзевятнаццаць грыўнаў, 85 капеек",
        )
        self.assertEqual(
            num2words(
                "38.4",
                lang="be",
                to="currency",
                separator=" і",
                cents=False,
                currency="EUR",
            ),
            "трыццаць восем еўра і 40 цэнтаў",
        )
        self.assertEqual(
            num2words(
                "38.4",
                lang="be",
                to="currency",
                separator=" і",
                cents=False,
                currency="RUB",
            ),
            "трыццаць восем расійскіх рублёў і 40 капеек",
        )
        self.assertEqual(
            num2words(
                "38.4",
                lang="be",
                to="currency",
                separator=" і",
                cents=False,
                currency="UAH",
            ),
            "трыццаць восем грыўнаў і 40 капеек",
        )
        self.assertEqual(
            num2words("1230.56", lang="be", to="currency", currency="USD"),
            "адна тысяча дзвесце трыццаць долараў, пяцьдзясят шэсць цэнтаў",
        )
        self.assertEqual(
            num2words("1231.56", lang="be", to="currency", currency="USD"),
            "адна тысяча дзвесце трыццаць адзін долар, "
            "пяцьдзясят шэсць цэнтаў",
        )
        self.assertEqual(
            num2words("1234.56", lang="be", to="currency", currency="USD"),
            "адна тысяча дзвесце трыццаць чатыры долары, пяцьдзясят шэсць "
            "цэнтаў",
        )
        self.assertEqual(
            num2words(
                10122, lang="be", to="currency", currency="UZS", separator=" і"
            ),
            "сто адзін сум і дваццаць два тыйіны",
        )

        self.assertEqual(
            num2words(1.0, lang="be", to="currency", currency="PLN"),
            "адзін злоты, нуль грошаў",
        )

        self.assertEqual(
            num2words(23.40, lang="be", to="currency", currency="PLN"),
            "дваццаць тры злотых, сорак грошаў",
        )

        self.assertEqual(
            num2words(9999.39, lang="be", to="currency", currency="PLN"),
            "дзевяць тысяч дзевяцьсот дзевяноста дзевяць злотых, "
            "трыццаць дзевяць грошаў",
        )
