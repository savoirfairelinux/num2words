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

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, "un euro e zero citti"),
    (2.01, "doî euro e un citto"),
    (8.10, "eutto euro e dexe citti"),
    (12.26, "dozze euro e vintisëi citti"),
    (21.29, "vintun euro e vintineuve citti"),
    (81.25, "ottantun euro e vintiçinque citti"),
    (100.00, "çento euro e zero citti"),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, "un dòllao e zero citti"),
    (2.01, "doî dòllai e un citto"),
    (8.10, "eutto dòllai e dexe citti"),
    (12.26, "dozze dòllai e vintisëi citti"),
    (21.29, "vintun dòllai e vintineuve citti"),
    (81.25, "ottantun dòllai e vintiçinque citti"),
    (100.00, "çento dòllai e zero citti"),
)

TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, "uña sterliña e zero pence"),
    (2.01, "doe sterliñe e un penny"),
    (8.10, "eutto sterliñe e dexe pence"),
    (12.26, "dozze sterliñe e vintisëi pence"),
    (21.29, "vintun sterliñe e vintineuve pence"),
    (81.25, "ottantun sterliñe e vintiçinque pence"),
    (100.00, "çento sterliñe e zero pence"),
)


class Num2WordsITTest(TestCase):
    maxDiff = None

    def test_negative(self):
        number = 648972145
        pos_crd = num2words(+number, lang="lij")
        neg_crd = num2words(-number, lang="lij")
        pos_ord = num2words(+number, lang="lij", ordinal=True)
        neg_ord = num2words(-number, lang="lij", ordinal=True)
        self.assertEqual("meno " + pos_crd, neg_crd)
        self.assertEqual("meno " + pos_ord, neg_ord)

    def test_float_to_cardinal(self):
        self.assertEqual(
            num2words("3.1415", lang="lij"),
            "trei virgola un quattro un çinque",
        )
        self.assertEqual(
            num2words(3.1415, lang="lij"), "trei virgola un quattro un çinque"
        )
        self.assertEqual(
            num2words(-5.15, lang="lij"), "meno çinque virgola un çinque"
        )
        self.assertEqual(
            num2words(-0.15, lang="lij"), "meno zero virgola un çinque"
        )

    def test_float_to_ordinal(self):
        self.assertEqual(
            num2words(3.1415, lang="lij", ordinal=True),
            "terso virgola un quattro un çinque",
        )
        self.assertEqual(
            num2words(-5.15, lang="lij", ordinal=True),
            "meno quinto virgola un çinque",
        )
        self.assertEqual(
            num2words(-0.15, lang="lij", ordinal=True),
            "meno zero virgola un çinque",
        )

    def test_0(self):
        self.assertEqual(num2words(0, lang="lij"), "zero")
        self.assertEqual(num2words(0, lang="lij", ordinal=True), "zero")

    def test_1_to_10(self):
        self.assertEqual(num2words(1, lang="lij"), "un")
        self.assertEqual(num2words(1, lang="lij", gender="f"), "uña")
        self.assertEqual(num2words(2, lang="lij"), "doî")
        self.assertEqual(num2words(2, lang="lij", gender="f"), "doe")
        self.assertEqual(num2words(3, lang="lij"), "trei")
        self.assertEqual(num2words(3, lang="lij", gender="f"), "træ")
        self.assertEqual(num2words(7, lang="lij"), "sette")
        self.assertEqual(num2words(7, lang="lij", gender="f"), "sette")
        self.assertEqual(num2words(10, lang="lij"), "dexe")

    def test_11_to_19(self):
        self.assertEqual(num2words(11, lang="lij"), "unze")
        self.assertEqual(num2words(13, lang="lij"), "trezze")
        self.assertEqual(num2words(15, lang="lij"), "chinze")
        self.assertEqual(num2words(16, lang="lij"), "sezze")
        self.assertEqual(num2words(19, lang="lij"), "dixineuve")

    def test_20_to_99(self):
        self.assertEqual(num2words(20, lang="lij"), "vinti")
        self.assertEqual(num2words(21, lang="lij"), "vintun")
        self.assertEqual(num2words(21, lang="lij", gender="f"), "vintun")
        self.assertEqual(num2words(23, lang="lij"), "vintitrei")
        self.assertEqual(num2words(23, lang="lij", gender="f"), "vintitræ")
        self.assertEqual(num2words(28, lang="lij"), "vinteutto")
        self.assertEqual(num2words(31, lang="lij"), "trentun")
        self.assertEqual(num2words(40, lang="lij"), "quaranta")
        self.assertEqual(num2words(66, lang="lij"), "sciusciantesëi")
        self.assertEqual(num2words(92, lang="lij"), "novantedoî")
        self.assertEqual(num2words(92, lang="lij", gender="f"), "novantedoe")

    def test_100_to_999(self):
        self.assertEqual(num2words(100, lang="lij"), "çento")
        self.assertEqual(num2words(111, lang="lij"), "çentounze")
        self.assertEqual(num2words(150, lang="lij"), "çentoçinquanta")
        self.assertEqual(num2words(196, lang="lij"), "çentonovantesëi")
        self.assertEqual(num2words(200, lang="lij"), "duxento")
        self.assertEqual(num2words(210, lang="lij"), "duxentodexe")
        self.assertEqual(num2words(701, lang="lij"), "setteçentoun")
        self.assertEqual(
            num2words(701, lang="lij", gender="f"), "setteçentoun"
        )
        self.assertEqual(num2words(882, lang="lij"), "euttoçentottantedoî")
        self.assertEqual(
            num2words(882, lang="lij", gender="f"), "euttoçentottantedoe"
        )

    def test_1000_to_9999(self):
        self.assertEqual(num2words(1000, lang="lij"), "mille")
        self.assertEqual(num2words(1001, lang="lij"), "milleun")
        self.assertEqual(num2words(1001, lang="lij", gender="f"), "milleun")
        self.assertEqual(num2words(1500, lang="lij"), "milleçinqueçento")
        self.assertEqual(
            num2words(7378, lang="lij"), "settemiatrexentosettanteutto"
        )
        self.assertEqual(num2words(2000, lang="lij"), "doamia")
        self.assertEqual(num2words(2100, lang="lij"), "doamiaçento")
        self.assertEqual(
            num2words(6870, lang="lij"), "seimiaeuttoçentosettanta"
        )
        self.assertEqual(num2words(10000, lang="lij"), "dexemia")
        self.assertEqual(
            num2words(98765, lang="lij"),
            "novanteuttomiasetteçentosciuscianteçinque",
        )
        self.assertEqual(num2words(100000, lang="lij"), "çentomia")
        self.assertEqual(
            num2words(523456, lang="lij"),
            "çinqueçentovintitræmiaquattroçentoçinquantesëi",
        )

    def test_big(self):
        self.assertEqual(num2words(1000000, lang="lij"), "un mion")
        self.assertEqual(num2words(1000007, lang="lij"), "un mion e sette")
        self.assertEqual(num2words(1000001, lang="lij"), "un mion e un")
        self.assertEqual(
            num2words(1000001, lang="lij", gender="f"), "un mion e un"
        )
        self.assertEqual(
            num2words(1200000, lang="lij"), "un mion e duxentomia"
        )
        self.assertEqual(num2words(3000000, lang="lij"), "trei mioin")
        self.assertEqual(num2words(3000005, lang="lij"), "trei mioin e çinque")
        self.assertEqual(
            num2words(3800000, lang="lij"), "trei mioin e euttoçentomia"
        )
        self.assertEqual(num2words(1000000000, lang="lij"), "un miliardo")
        self.assertEqual(
            num2words(1000000017, lang="lij"), "un miliardo e dïsette"
        )
        self.assertEqual(num2words(2000000000, lang="lij"), "doî miliardi")
        self.assertEqual(
            num2words(2000001000, lang="lij"), "doî miliardi e mille"
        )
        self.assertEqual(
            num2words(1234567890, lang="lij"),
            "un miliardo, duxentotrentequattro mioin e "
            "çinqueçentosciusciantesettemiaeuttoçentonovanta",
        )
        self.assertEqual(num2words(1000000000000, lang="lij"), "un bilion")
        self.assertEqual(
            num2words(123456789012345678901234567890, lang="lij"),
            "çentovintitrei quadriliardi, quattroçentoçinquantesëi "
            "quadrilioin, setteçentottanteneuve triliardi, dozze trilioin, "
            "trexentoquaranteçinque biliardi, seiçentosettanteutto bilioin, "
            "neuveçentoun miliardi, duxentotrentequattro mioin e "
            "çinqueçentosciusciantesettemiaeuttoçentonovanta",
        )

    def test_nth_1_to_99(self):
        self.assertEqual(num2words(1, lang="lij", ordinal=True), "primmo")
        self.assertEqual(
            num2words(1, lang="lij", ordinal=True, gender="f"), "primma"
        )
        self.assertEqual(num2words(8, lang="lij", ordinal=True), "otten")
        self.assertEqual(
            num2words(8, lang="lij", ordinal=True, plural=True), "otten"
        )
        self.assertEqual(
            num2words(8, lang="lij", ordinal=True, gender="f"), "otteña"
        )
        self.assertEqual(
            num2words(
                8,
                lang="lij",
                ordinal=True,
                gender="f",
                plural=True,
            ),
            "otteñe",
        )
        self.assertEqual(
            num2words(21, lang="lij", ordinal=True), "vintuneximo"
        )
        self.assertEqual(
            num2words(23, lang="lij", ordinal=True), "vintitreieximo"
        )
        self.assertEqual(
            num2words(47, lang="lij", ordinal=True), "quarantesetteximo"
        )
        self.assertEqual(
            num2words(99, lang="lij", ordinal=True), "novantenoveximo"
        )

    def test_nth_100_to_999(self):
        self.assertEqual(num2words(100, lang="lij", ordinal=True), "çenteximo")
        self.assertEqual(
            num2words(100, lang="lij", ordinal=True, gender="f"), "çentexima"
        )
        self.assertEqual(
            num2words(100, lang="lij", ordinal=True, plural=True), "çenteximi"
        )
        self.assertEqual(
            num2words(100, lang="lij", ordinal=True, gender="f", plural=True),
            "çentexime",
        )
        self.assertEqual(
            num2words(101, lang="lij", ordinal=True), "çentouneximo"
        )
        self.assertEqual(
            num2words(188, lang="lij", ordinal=True), "çentottantotteximo"
        )
        self.assertEqual(
            num2words(112, lang="lij", ordinal=True), "çentodozzeximo"
        )
        self.assertEqual(
            num2words(120, lang="lij", ordinal=True), "çentovinteximo"
        )
        self.assertEqual(
            num2words(121, lang="lij", ordinal=True), "çentovintuneximo"
        )
        self.assertEqual(
            num2words(316, lang="lij", ordinal=True), "trexentosezzeximo"
        )
        self.assertEqual(
            num2words(700, lang="lij", ordinal=True), "setteçenteximo"
        )
        self.assertEqual(
            num2words(803, lang="lij", ordinal=True), "euttoçentotreieximo"
        )
        self.assertEqual(
            num2words(923, lang="lij", ordinal=True),
            "neuveçentovintitreieximo",
        )

    def test_nth_1000_to_999999(self):
        self.assertEqual(
            num2words(1000, lang="lij", ordinal=True), "milleximo"
        )
        self.assertEqual(
            num2words(1001, lang="lij", ordinal=True), "milleuneximo"
        )
        self.assertEqual(
            num2words(1003, lang="lij", ordinal=True), "milletreieximo"
        )
        self.assertEqual(
            num2words(1200, lang="lij", ordinal=True), "milleduxenteximo"
        )
        self.assertEqual(
            num2words(1800, lang="lij", ordinal=True, gender="f", plural=True),
            "milleeuttoçentexime",
        )
        self.assertEqual(
            num2words(8640, lang="lij", ordinal=True),
            "euttomiaseiçentoquaranteximo",
        )
        self.assertEqual(
            num2words(14000, lang="lij", ordinal=True), "quattorzemilleximo"
        )
        self.assertEqual(
            num2words(123456, lang="lij", ordinal=True),
            "çentovintitræmiaquattroçentoçinquanteseieximo",
        )
        self.assertEqual(
            num2words(987654, lang="lij", ordinal=True),
            "neuveçentottantesettemiaseiçentoçinquantequattreximo",
        )

    def test_nth_big(self):
        self.assertEqual(
            num2words(1000000001, lang="lij", ordinal=True),
            "un miliardo e uneximo",
        )
        self.assertEqual(
            num2words(1000000001, lang="lij", ordinal=True, gender="f"),
            "un miliardo e unexima",
        )
        self.assertEqual(
            num2words(
                123456789012345678901234567890, lang="lij", ordinal=True
            ),
            "çentovintitrei quadriliardi, quattroçentoçinquantesëi "
            "quadrilioin, setteçentottanteneuve triliardi, dozze trilioin, "
            "trexentoquaranteçinque biliardi, seiçentosettanteutto bilioin, "
            "neuveçentoun miliardi, duxentotrentequattro mioin e "
            "çinqueçentosciusciantesettemiaeuttoçentonovanteximo",
        )

    def test_with_floats(self):
        self.assertEqual(num2words(1.0, lang="lij"), "un")
        self.assertEqual(num2words(1.1, lang="lij"), "un virgola un")

    def test_with_strings(self):
        for i in range(2002):
            # Just make sure it doesn't raise an exception
            num2words(str(i), lang="lij", to="cardinal")
            num2words(str(i), lang="lij", to="ordinal")
        self.assertEqual(num2words("1", lang="lij", to="ordinal"), "primmo")
        self.assertEqual(
            num2words("100", lang="lij", to="ordinal"), "çenteximo"
        )
        self.assertEqual(
            num2words("1000", lang="lij", to="ordinal"), "milleximo"
        )
        self.assertEqual(
            num2words(
                "1234567890123456789012345678", lang="lij", to="ordinal"
            ),
            "un quadriliardo, duxentotrentequattro quadrilioin, "
            "çinqueçentosciusciantesette triliardi, euttoçentonovanta "
            "trilioin, çentovintitrei biliardi, quattroçentoçinquantesëi "
            "bilioin, setteçentottanteneuve miliardi, dozze mioin e "
            "trexentoquaranteçinquemiaseiçentosettantotteximo",
        )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang="lij", to="currency", currency="EUR"),
                test[1],
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang="lij", to="currency", currency="USD"),
                test[1],
            )

    def test_currency_gbp(self):
        for test in TEST_CASES_TO_CURRENCY_GBP:
            self.assertEqual(
                num2words(test[0], lang="lij", to="currency", currency="GBP"),
                test[1],
            )

    def test_currency_adjs(self):
        currencies = "USD HKD CHF FRF".split()
        names = [
            "doî dòllai americhen",
            "doî dòllai de Hong Kong",
            "doî franchi svisseri",
            "doî franchi franseixi",
        ]
        for currency, name in zip(currencies, names):
            self.assertEqual(
                num2words(
                    2.01,
                    lang="lij",
                    to="currency",
                    currency=currency,
                    adjective=True,
                ),
                name + " e un citto",
            )
