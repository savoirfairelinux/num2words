# -*- coding: utf-8 -*-
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

from __future__ import division, print_function, unicode_literals

import sys
from unittest import TestCase

from num2words import num2words


CASES = ["nominative", "genitive", "partitive",    # grammatical
         "inessive", "elative", "illative",        # internal locative
         "adessive", "ablative", "allative",       # external locative
         "essive", "translative",                  # essive
         "instructive", "abessive", "comitative"]  # rare


def n2f(*args, **kwargs):
    return num2words(lang='fi', *args, **kwargs)


def create_test(number, to):
    return (
        "# %s\n" % num2words(number, lang='en') +
        "self.assertEqual(\n" +
        '    tuple(n2f(%s, to="%s", case=c) for c in CASES),\n' %
        (number, to) +
        # grammatical
        '    ("%s", "%s", "%s",\n' %
        tuple(n2f(number, to=to, case=c) for c in CASES[0:3]) +
        # internal locative
        '     "%s", "%s", "%s",\n' %
        tuple(n2f(number, to=to, case=c) for c in CASES[3:6]) +
        # external locative
        '     "%s", "%s", "%s",\n' %
        tuple(n2f(number, to=to, case=c) for c in CASES[6:9]) +
        # essive
        '     "%s", "%s",\n'       %
        tuple(n2f(number, to=to, case=c) for c in CASES[9:11]) +
        # rare
        '     "%s", "%s", "%s")\n' %
        tuple(n2f(number, to=to, case=c) for c in CASES[11:14]) +
        ")\n" +
        "self.assertEqual(\n" +
        '    tuple(n2f(%s, to="%s", case=c, plural=True) for c in CASES),\n' %
        (number, to) +
        # grammatical
        '    ("%s", "%s", "%s",\n' %
        tuple(n2f(number, to=to, case=c, plural=True) for c in CASES[0:3]) +
        # internal locative
        '     "%s", "%s", "%s",\n' %
        tuple(n2f(number, to=to, case=c, plural=True) for c in CASES[3:6]) +
        # external locative
        '     "%s", "%s", "%s",\n' %
        tuple(n2f(number, to=to, case=c, plural=True) for c in CASES[6:9]) +
        # essive
        '     "%s", "%s",\n'       %
        tuple(n2f(number, to=to, case=c, plural=True) for c in CASES[9:11]) +
        # rare
        '     "%s", "%s", "%s")\n' %
        tuple(n2f(number, to=to, case=c, plural=True) for c in CASES[11:14]) +
        ")\n"
    )


class Num2WordsFITest(TestCase):

    def test_low(self):

        # zero
        self.assertEqual(
            tuple(n2f(0, to="cardinal", case=c) for c in CASES),
            ("nolla", "nollan", "nollaa",
             "nollassa", "nollasta", "nollaan",
             "nollalla", "nollalta", "nollalle",
             "nollana", "nollaksi",
             "nollin", "nollatta", "nolline")
        )
        self.assertEqual(
            tuple(n2f(0, to="cardinal", case=c, plural=True) for c in CASES),
            ("nollat", "nollien", "nollia",
             "nollissa", "nollista", "nolliin",
             "nollilla", "nollilta", "nollille",
             "nollina", "nolliksi",
             "nollin", "nollitta", "nolline")
        )

        # one
        self.assertEqual(
            tuple(n2f(1, to="cardinal", case=c) for c in CASES),
            ("yksi", "yhden", "yhtä",
             "yhdessä", "yhdestä", "yhteen",
             "yhdellä", "yhdeltä", "yhdelle",
             "yhtenä", "yhdeksi",
             "yksin", "yhdettä", "yksine")
        )
        self.assertEqual(
            tuple(n2f(1, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdet", "yksien", "yksiä",
             "yksissä", "yksistä", "yksiin",
             "yksillä", "yksiltä", "yksille",
             "yksinä", "yksiksi",
             "yksin", "yksittä", "yksine")
        )

        # two
        self.assertEqual(
            tuple(n2f(2, to="cardinal", case=c) for c in CASES),
            ("kaksi", "kahden", "kahta",
             "kahdessa", "kahdesta", "kahteen",
             "kahdella", "kahdelta", "kahdelle",
             "kahtena", "kahdeksi",
             "kaksin", "kahdetta", "kaksine")
        )
        self.assertEqual(
            tuple(n2f(2, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdet", "kaksien", "kaksia",
             "kaksissa", "kaksista", "kaksiin",
             "kaksilla", "kaksilta", "kaksille",
             "kaksina", "kaksiksi",
             "kaksin", "kaksitta", "kaksine")
        )

        # three
        self.assertEqual(
            tuple(n2f(3, to="cardinal", case=c) for c in CASES),
            ("kolme", "kolmen", "kolmea",
             "kolmessa", "kolmesta", "kolmeen",
             "kolmella", "kolmelta", "kolmelle",
             "kolmena", "kolmeksi",
             "kolmen", "kolmetta", "kolmine")
        )
        self.assertEqual(
            tuple(n2f(3, to="cardinal", case=c, plural=True) for c in CASES),
            ("kolmet", "kolmien", "kolmia",
             "kolmissa", "kolmista", "kolmiin",
             "kolmilla", "kolmilta", "kolmille",
             "kolmina", "kolmiksi",
             "kolmin", "kolmitta", "kolmine")
        )

        # four
        self.assertEqual(
            tuple(n2f(4, to="cardinal", case=c) for c in CASES),
            ("neljä", "neljän", "neljää",
             "neljässä", "neljästä", "neljään",
             "neljällä", "neljältä", "neljälle",
             "neljänä", "neljäksi",
             "neljin", "neljättä", "neljine")
        )
        self.assertEqual(
            tuple(n2f(4, to="cardinal", case=c, plural=True) for c in CASES),
            ("neljät", "neljien", "neljiä",
             "neljissä", "neljistä", "neljiin",
             "neljillä", "neljiltä", "neljille",
             "neljinä", "neljiksi",
             "neljin", "neljittä", "neljine")
        )

        # five
        self.assertEqual(
            tuple(n2f(5, to="cardinal", case=c) for c in CASES),
            ("viisi", "viiden", "viittä",
             "viidessä", "viidestä", "viiteen",
             "viidellä", "viideltä", "viidelle",
             "viitenä", "viideksi",
             "viisin", "viidettä", "viisine")
        )
        self.assertEqual(
            tuple(n2f(5, to="cardinal", case=c, plural=True) for c in CASES),
            ("viidet", "viisien", "viisiä",
             "viisissä", "viisistä", "viisiin",
             "viisillä", "viisiltä", "viisille",
             "viisinä", "viisiksi",
             "viisin", "viisittä", "viisine")
        )

        # six
        self.assertEqual(
            tuple(n2f(6, to="cardinal", case=c) for c in CASES),
            ("kuusi", "kuuden", "kuutta",
             "kuudessa", "kuudesta", "kuuteen",
             "kuudella", "kuudelta", "kuudelle",
             "kuutena", "kuudeksi",
             "kuusin", "kuudetta", "kuusine")
        )
        self.assertEqual(
            tuple(n2f(6, to="cardinal", case=c, plural=True) for c in CASES),
            ("kuudet", "kuusien", "kuusia",
             "kuusissa", "kuusista", "kuusiin",
             "kuusilla", "kuusilta", "kuusille",
             "kuusina", "kuusiksi",
             "kuusin", "kuusitta", "kuusine")
        )

        # seven
        self.assertEqual(
            tuple(n2f(7, to="cardinal", case=c) for c in CASES),
            ("seitsemän", "seitsemän", "seitsemää",
             "seitsemässä", "seitsemästä", "seitsemään",
             "seitsemällä", "seitsemältä", "seitsemälle",
             "seitsemänä", "seitsemäksi",
             "seitsemin", "seitsemättä", "seitsemine")
        )
        self.assertEqual(
            tuple(n2f(7, to="cardinal", case=c, plural=True) for c in CASES),
            ("seitsemät", "seitsemien", "seitsemiä",
             "seitsemissä", "seitsemistä", "seitsemiin",
             "seitsemillä", "seitsemiltä", "seitsemille",
             "seitseminä", "seitsemiksi",
             "seitsemin", "seitsemittä", "seitsemine")
        )

        # eight
        self.assertEqual(
            tuple(n2f(8, to="cardinal", case=c) for c in CASES),
            ("kahdeksan", "kahdeksan", "kahdeksaa",
             "kahdeksassa", "kahdeksasta", "kahdeksaan",
             "kahdeksalla", "kahdeksalta", "kahdeksalle",
             "kahdeksana", "kahdeksaksi",
             "kahdeksin", "kahdeksatta", "kahdeksine")
        )
        self.assertEqual(
            tuple(n2f(8, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdeksat", "kahdeksien", "kahdeksia",
             "kahdeksissa", "kahdeksista", "kahdeksiin",
             "kahdeksilla", "kahdeksilta", "kahdeksille",
             "kahdeksina", "kahdeksiksi",
             "kahdeksin", "kahdeksitta", "kahdeksine")
        )

        # nine
        self.assertEqual(
            tuple(n2f(9, to="cardinal", case=c) for c in CASES),
            ("yhdeksän", "yhdeksän", "yhdeksää",
             "yhdeksässä", "yhdeksästä", "yhdeksään",
             "yhdeksällä", "yhdeksältä", "yhdeksälle",
             "yhdeksänä", "yhdeksäksi",
             "yhdeksin", "yhdeksättä", "yhdeksine")
        )
        self.assertEqual(
            tuple(n2f(9, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdeksät", "yhdeksien", "yhdeksiä",
             "yhdeksissä", "yhdeksistä", "yhdeksiin",
             "yhdeksillä", "yhdeksiltä", "yhdeksille",
             "yhdeksinä", "yhdeksiksi",
             "yhdeksin", "yhdeksittä", "yhdeksine")
        )

        # ten
        self.assertEqual(
            tuple(n2f(10, to="cardinal", case=c) for c in CASES),
            ("kymmenen", "kymmenen", "kymmentä",
             "kymmenessä", "kymmenestä", "kymmeneen",
             "kymmenellä", "kymmeneltä", "kymmenelle",
             "kymmenenä", "kymmeneksi",
             "kymmenin", "kymmenettä", "kymmenine")
        )
        self.assertEqual(
            tuple(n2f(10, to="cardinal", case=c, plural=True) for c in CASES),
            ("kymmenet", "kymmenien", "kymmeniä",
             "kymmenissä", "kymmenistä", "kymmeniin",
             "kymmenillä", "kymmeniltä", "kymmenille",
             "kymmeninä", "kymmeniksi",
             "kymmenin", "kymmenittä", "kymmenine")
        )

        # eleven
        self.assertEqual(
            tuple(n2f(11, to="cardinal", case=c) for c in CASES),
            ("yksitoista", "yhdentoista", "yhtätoista",
             "yhdessätoista", "yhdestätoista", "yhteentoista",
             "yhdellätoista", "yhdeltätoista", "yhdelletoista",
             "yhtenätoista", "yhdeksitoista",
             "yksintoista", "yhdettätoista", "yksinetoista")
        )
        self.assertEqual(
            tuple(n2f(11, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdettoista", "yksientoista", "yksiätoista",
             "yksissätoista", "yksistätoista", "yksiintoista",
             "yksillätoista", "yksiltätoista", "yksilletoista",
             "yksinätoista", "yksiksitoista",
             "yksintoista", "yksittätoista", "yksinetoista")
        )

        # twelve
        self.assertEqual(
            tuple(n2f(12, to="cardinal", case=c) for c in CASES),
            ("kaksitoista", "kahdentoista", "kahtatoista",
             "kahdessatoista", "kahdestatoista", "kahteentoista",
             "kahdellatoista", "kahdeltatoista", "kahdelletoista",
             "kahtenatoista", "kahdeksitoista",
             "kaksintoista", "kahdettatoista", "kaksinetoista")
        )
        self.assertEqual(
            tuple(n2f(12, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdettoista", "kaksientoista", "kaksiatoista",
             "kaksissatoista", "kaksistatoista", "kaksiintoista",
             "kaksillatoista", "kaksiltatoista", "kaksilletoista",
             "kaksinatoista", "kaksiksitoista",
             "kaksintoista", "kaksittatoista", "kaksinetoista")
        )

        # thirteen
        self.assertEqual(
            tuple(n2f(13, to="cardinal", case=c) for c in CASES),
            ("kolmetoista", "kolmentoista", "kolmeatoista",
             "kolmessatoista", "kolmestatoista", "kolmeentoista",
             "kolmellatoista", "kolmeltatoista", "kolmelletoista",
             "kolmenatoista", "kolmeksitoista",
             "kolmentoista", "kolmettatoista", "kolminetoista")
        )
        self.assertEqual(
            tuple(n2f(13, to="cardinal", case=c, plural=True) for c in CASES),
            ("kolmettoista", "kolmientoista", "kolmiatoista",
             "kolmissatoista", "kolmistatoista", "kolmiintoista",
             "kolmillatoista", "kolmiltatoista", "kolmilletoista",
             "kolminatoista", "kolmiksitoista",
             "kolmintoista", "kolmittatoista", "kolminetoista")
        )

        # fourteen
        self.assertEqual(
            tuple(n2f(14, to="cardinal", case=c) for c in CASES),
            ("neljätoista", "neljäntoista", "neljäätoista",
             "neljässätoista", "neljästätoista", "neljääntoista",
             "neljällätoista", "neljältätoista", "neljälletoista",
             "neljänätoista", "neljäksitoista",
             "neljintoista", "neljättätoista", "neljinetoista")
        )
        self.assertEqual(
            tuple(n2f(14, to="cardinal", case=c, plural=True) for c in CASES),
            ("neljättoista", "neljientoista", "neljiätoista",
             "neljissätoista", "neljistätoista", "neljiintoista",
             "neljillätoista", "neljiltätoista", "neljilletoista",
             "neljinätoista", "neljiksitoista",
             "neljintoista", "neljittätoista", "neljinetoista")
        )

        # fifteen
        self.assertEqual(
            tuple(n2f(15, to="cardinal", case=c) for c in CASES),
            ("viisitoista", "viidentoista", "viittätoista",
             "viidessätoista", "viidestätoista", "viiteentoista",
             "viidellätoista", "viideltätoista", "viidelletoista",
             "viitenätoista", "viideksitoista",
             "viisintoista", "viidettätoista", "viisinetoista")
        )
        self.assertEqual(
            tuple(n2f(15, to="cardinal", case=c, plural=True) for c in CASES),
            ("viidettoista", "viisientoista", "viisiätoista",
             "viisissätoista", "viisistätoista", "viisiintoista",
             "viisillätoista", "viisiltätoista", "viisilletoista",
             "viisinätoista", "viisiksitoista",
             "viisintoista", "viisittätoista", "viisinetoista")
        )

        # sixteen
        self.assertEqual(
            tuple(n2f(16, to="cardinal", case=c) for c in CASES),
            ("kuusitoista", "kuudentoista", "kuuttatoista",
             "kuudessatoista", "kuudestatoista", "kuuteentoista",
             "kuudellatoista", "kuudeltatoista", "kuudelletoista",
             "kuutenatoista", "kuudeksitoista",
             "kuusintoista", "kuudettatoista", "kuusinetoista")
        )
        self.assertEqual(
            tuple(n2f(16, to="cardinal", case=c, plural=True) for c in CASES),
            ("kuudettoista", "kuusientoista", "kuusiatoista",
             "kuusissatoista", "kuusistatoista", "kuusiintoista",
             "kuusillatoista", "kuusiltatoista", "kuusilletoista",
             "kuusinatoista", "kuusiksitoista",
             "kuusintoista", "kuusittatoista", "kuusinetoista")
        )

        # seventeen
        self.assertEqual(
            tuple(n2f(17, to="cardinal", case=c) for c in CASES),
            ("seitsemäntoista", "seitsemäntoista", "seitsemäätoista",
             "seitsemässätoista", "seitsemästätoista", "seitsemääntoista",
             "seitsemällätoista", "seitsemältätoista", "seitsemälletoista",
             "seitsemänätoista", "seitsemäksitoista",
             "seitsemintoista", "seitsemättätoista", "seitseminetoista")
        )
        self.assertEqual(
            tuple(n2f(17, to="cardinal", case=c, plural=True) for c in CASES),
            ("seitsemättoista", "seitsemientoista", "seitsemiätoista",
             "seitsemissätoista", "seitsemistätoista", "seitsemiintoista",
             "seitsemillätoista", "seitsemiltätoista", "seitsemilletoista",
             "seitseminätoista", "seitsemiksitoista",
             "seitsemintoista", "seitsemittätoista", "seitseminetoista")
        )

        # eighteen
        self.assertEqual(
            tuple(n2f(18, to="cardinal", case=c) for c in CASES),
            ("kahdeksantoista", "kahdeksantoista", "kahdeksaatoista",
             "kahdeksassatoista", "kahdeksastatoista", "kahdeksaantoista",
             "kahdeksallatoista", "kahdeksaltatoista", "kahdeksalletoista",
             "kahdeksanatoista", "kahdeksaksitoista",
             "kahdeksintoista", "kahdeksattatoista", "kahdeksinetoista")
        )
        self.assertEqual(
            tuple(n2f(18, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdeksattoista", "kahdeksientoista", "kahdeksiatoista",
             "kahdeksissatoista", "kahdeksistatoista", "kahdeksiintoista",
             "kahdeksillatoista", "kahdeksiltatoista", "kahdeksilletoista",
             "kahdeksinatoista", "kahdeksiksitoista",
             "kahdeksintoista", "kahdeksittatoista", "kahdeksinetoista")
        )

        # nineteen
        self.assertEqual(
            tuple(n2f(19, to="cardinal", case=c) for c in CASES),
            ("yhdeksäntoista", "yhdeksäntoista", "yhdeksäätoista",
             "yhdeksässätoista", "yhdeksästätoista", "yhdeksääntoista",
             "yhdeksällätoista", "yhdeksältätoista", "yhdeksälletoista",
             "yhdeksänätoista", "yhdeksäksitoista",
             "yhdeksintoista", "yhdeksättätoista", "yhdeksinetoista")
        )
        self.assertEqual(
            tuple(n2f(19, to="cardinal", case=c, plural=True) for c in CASES),
            ("yhdeksättoista", "yhdeksientoista", "yhdeksiätoista",
             "yhdeksissätoista", "yhdeksistätoista", "yhdeksiintoista",
             "yhdeksillätoista", "yhdeksiltätoista", "yhdeksilletoista",
             "yhdeksinätoista", "yhdeksiksitoista",
             "yhdeksintoista", "yhdeksittätoista", "yhdeksinetoista")
        )

        # twenty
        self.assertEqual(
            tuple(n2f(20, to="cardinal", case=c) for c in CASES),
            ("kaksikymmentä", "kahdenkymmenen", "kahtakymmentä",
             "kahdessakymmenessä", "kahdestakymmenestä", "kahteenkymmeneen",
             "kahdellakymmenellä", "kahdeltakymmeneltä", "kahdellekymmenelle",
             "kahtenakymmenenä", "kahdeksikymmeneksi",
             "kaksinkymmenin", "kahdettakymmenettä", "kaksinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(20, to="cardinal", case=c, plural=True) for c in CASES),
            ("kahdetkymmenet", "kaksienkymmenien", "kaksiakymmeniä",
             "kaksissakymmenissä", "kaksistakymmenistä", "kaksiinkymmeniin",
             "kaksillakymmenillä", "kaksiltakymmeniltä", "kaksillekymmenille",
             "kaksinakymmeninä", "kaksiksikymmeniksi",
             "kaksinkymmenin", "kaksittakymmenittä", "kaksinekymmenine")
        )

    def test_low_ord(self):

        # zero
        self.assertEqual(
            tuple(n2f(0, to="ordinal", case=c) for c in CASES),
            ("nollas", "nollannen", "nollatta",
             "nollannessa", "nollannesta", "nollanteen",
             "nollannella", "nollannelta", "nollannelle",
             "nollantena", "nollanneksi",
             "nollansin", "nollannetta", "nollansine")
        )
        self.assertEqual(
            tuple(n2f(0, to="ordinal", case=c, plural=True) for c in CASES),
            ("nollannet", "nollansien", "nollansia",
             "nollansissa", "nollansista", "nollansiin",
             "nollansilla", "nollansilta", "nollansille",
             "nollansina", "nollansiksi",
             "nollansin", "nollansitta", "nollansine")
        )

        # one
        self.assertEqual(
            tuple(n2f(1, to="ordinal", case=c) for c in CASES),
            ("ensimmäinen", "ensimmäisen", "ensimmäistä",
             "ensimmäisessä", "ensimmäisestä", "ensimmäiseen",
             "ensimmäisellä", "ensimmäiseltä", "ensimmäiselle",
             "ensimmäisenä", "ensimmäiseksi",
             "ensimmäisin", "ensimmäisettä", "ensimmäisine")
        )
        self.assertEqual(
            tuple(n2f(1, to="ordinal", case=c, plural=True) for c in CASES),
            ("ensimmäiset", "ensimmäisten", "ensimmäisiä",
             "ensimmäisissä", "ensimmäisistä", "ensimmäisiin",
             "ensimmäisillä", "ensimmäisiltä", "ensimmäisille",
             "ensimmäisinä", "ensimmäisiksi",
             "ensimmäisin", "ensimmäisittä", "ensimmäisine")
        )

        # two
        self.assertEqual(
            tuple(n2f(2, to="ordinal", case=c) for c in CASES),
            ("toinen", "toisen", "toista",
             "toisessa", "toisesta", "toiseen",
             "toisella", "toiselta", "toiselle",
             "toisena", "toiseksi",
             "toisin", "toisetta", "toisine")
        )
        self.assertEqual(
            tuple(n2f(2, to="ordinal", case=c, plural=True) for c in CASES),
            ("toiset", "toisten", "toisia",
             "toisissa", "toisista", "toisiin",
             "toisilla", "toisilta", "toisille",
             "toisina", "toisiksi",
             "toisin", "toisitta", "toisine")
        )

        # three
        self.assertEqual(
            tuple(n2f(3, to="ordinal", case=c) for c in CASES),
            ("kolmas", "kolmannen", "kolmatta",
             "kolmannessa", "kolmannesta", "kolmanteen",
             "kolmannella", "kolmannelta", "kolmannelle",
             "kolmantena", "kolmanneksi",
             "kolmansin", "kolmannetta", "kolmansine")
        )
        self.assertEqual(
            tuple(n2f(3, to="ordinal", case=c, plural=True) for c in CASES),
            ("kolmannet", "kolmansien", "kolmansia",
             "kolmansissa", "kolmansista", "kolmansiin",
             "kolmansilla", "kolmansilta", "kolmansille",
             "kolmansina", "kolmansiksi",
             "kolmansin", "kolmansitta", "kolmansine")
        )

        # four
        self.assertEqual(
            tuple(n2f(4, to="ordinal", case=c) for c in CASES),
            ("neljäs", "neljännen", "neljättä",
             "neljännessä", "neljännestä", "neljänteen",
             "neljännellä", "neljänneltä", "neljännelle",
             "neljäntenä", "neljänneksi",
             "neljänsin", "neljännettä", "neljänsine")
        )
        self.assertEqual(
            tuple(n2f(4, to="ordinal", case=c, plural=True) for c in CASES),
            ("neljännet", "neljänsien", "neljänsiä",
             "neljänsissä", "neljänsistä", "neljänsiin",
             "neljänsillä", "neljänsiltä", "neljänsille",
             "neljänsinä", "neljänsiksi",
             "neljänsin", "neljänsittä", "neljänsine")
        )

        # five
        self.assertEqual(
            tuple(n2f(5, to="ordinal", case=c) for c in CASES),
            ("viides", "viidennen", "viidettä",
             "viidennessä", "viidennestä", "viidenteen",
             "viidennellä", "viidenneltä", "viidennelle",
             "viidentenä", "viidenneksi",
             "viidensin", "viidennettä", "viidensine")
        )
        self.assertEqual(
            tuple(n2f(5, to="ordinal", case=c, plural=True) for c in CASES),
            ("viidennet", "viidensien", "viidensiä",
             "viidensissä", "viidensistä", "viidensiin",
             "viidensillä", "viidensiltä", "viidensille",
             "viidensinä", "viidensiksi",
             "viidensin", "viidensittä", "viidensine")
        )

        # six
        self.assertEqual(
            tuple(n2f(6, to="ordinal", case=c) for c in CASES),
            ("kuudes", "kuudennen", "kuudetta",
             "kuudennessa", "kuudennesta", "kuudenteen",
             "kuudennella", "kuudennelta", "kuudennelle",
             "kuudentena", "kuudenneksi",
             "kuudensin", "kuudennetta", "kuudensine")
        )
        self.assertEqual(
            tuple(n2f(6, to="ordinal", case=c, plural=True) for c in CASES),
            ("kuudennet", "kuudensien", "kuudensia",
             "kuudensissa", "kuudensista", "kuudensiin",
             "kuudensilla", "kuudensilta", "kuudensille",
             "kuudensina", "kuudensiksi",
             "kuudensin", "kuudensitta", "kuudensine")
        )

        # seven
        self.assertEqual(
            tuple(n2f(7, to="ordinal", case=c) for c in CASES),
            ("seitsemäs", "seitsemännen", "seitsemättä",
             "seitsemännessä", "seitsemännestä", "seitsemänteen",
             "seitsemännellä", "seitsemänneltä", "seitsemännelle",
             "seitsemäntenä", "seitsemänneksi",
             "seitsemänsin", "seitsemännettä", "seitsemänsine")
        )
        self.assertEqual(
            tuple(n2f(7, to="ordinal", case=c, plural=True) for c in CASES),
            ("seitsemännet", "seitsemänsien", "seitsemänsiä",
             "seitsemänsissä", "seitsemänsistä", "seitsemänsiin",
             "seitsemänsillä", "seitsemänsiltä", "seitsemänsille",
             "seitsemänsinä", "seitsemänsiksi",
             "seitsemänsin", "seitsemänsittä", "seitsemänsine")
        )

        # eight
        self.assertEqual(
            tuple(n2f(8, to="ordinal", case=c) for c in CASES),
            ("kahdeksas", "kahdeksannen", "kahdeksatta",
             "kahdeksannessa", "kahdeksannesta", "kahdeksanteen",
             "kahdeksannella", "kahdeksannelta", "kahdeksannelle",
             "kahdeksantena", "kahdeksanneksi",
             "kahdeksansin", "kahdeksannetta", "kahdeksansine")
        )
        self.assertEqual(
            tuple(n2f(8, to="ordinal", case=c, plural=True) for c in CASES),
            ("kahdeksannet", "kahdeksansien", "kahdeksansia",
             "kahdeksansissa", "kahdeksansista", "kahdeksansiin",
             "kahdeksansilla", "kahdeksansilta", "kahdeksansille",
             "kahdeksansina", "kahdeksansiksi",
             "kahdeksansin", "kahdeksansitta", "kahdeksansine")
        )

        # nine
        self.assertEqual(
            tuple(n2f(9, to="ordinal", case=c) for c in CASES),
            ("yhdeksäs", "yhdeksännen", "yhdeksättä",
             "yhdeksännessä", "yhdeksännestä", "yhdeksänteen",
             "yhdeksännellä", "yhdeksänneltä", "yhdeksännelle",
             "yhdeksäntenä", "yhdeksänneksi",
             "yhdeksänsin", "yhdeksännettä", "yhdeksänsine")
        )
        self.assertEqual(
            tuple(n2f(9, to="ordinal", case=c, plural=True) for c in CASES),
            ("yhdeksännet", "yhdeksänsien", "yhdeksänsiä",
             "yhdeksänsissä", "yhdeksänsistä", "yhdeksänsiin",
             "yhdeksänsillä", "yhdeksänsiltä", "yhdeksänsille",
             "yhdeksänsinä", "yhdeksänsiksi",
             "yhdeksänsin", "yhdeksänsittä", "yhdeksänsine")
        )

        # ten
        self.assertEqual(
            tuple(n2f(10, to="ordinal", case=c) for c in CASES),
            ("kymmenes", "kymmenennen", "kymmenettä",
             "kymmenennessä", "kymmenennestä", "kymmenenteen",
             "kymmenennellä", "kymmenenneltä", "kymmenennelle",
             "kymmenentenä", "kymmenenneksi",
             "kymmenensin", "kymmenennettä", "kymmenensine")
        )
        self.assertEqual(
            tuple(n2f(10, to="ordinal", case=c, plural=True) for c in CASES),
            ("kymmenennet", "kymmenensien", "kymmenensiä",
             "kymmenensissä", "kymmenensistä", "kymmenensiin",
             "kymmenensillä", "kymmenensiltä", "kymmenensille",
             "kymmenensinä", "kymmenensiksi",
             "kymmenensin", "kymmenensittä", "kymmenensine")
        )

        # eleven
        self.assertEqual(
            tuple(n2f(11, to="ordinal", case=c) for c in CASES),
            ("yhdestoista", "yhdennentoista", "yhdettätoista",
             "yhdennessätoista", "yhdennestätoista", "yhdenteentoista",
             "yhdennellätoista", "yhdenneltätoista", "yhdennelletoista",
             "yhdentenätoista", "yhdenneksitoista",
             "yhdensintoista", "yhdennettätoista", "yhdensinetoista")
        )
        self.assertEqual(
            tuple(n2f(11, to="ordinal", case=c, plural=True) for c in CASES),
            ("yhdennettoista", "yhdensientoista", "yhdensiätoista",
             "yhdensissätoista", "yhdensistätoista", "yhdensiintoista",
             "yhdensillätoista", "yhdensiltätoista", "yhdensilletoista",
             "yhdensinätoista", "yhdensiksitoista",
             "yhdensintoista", "yhdensittätoista", "yhdensinetoista")
        )

        # twelve
        self.assertEqual(
            tuple(n2f(12, to="ordinal", case=c) for c in CASES),
            ("kahdestoista", "kahdennentoista", "kahdettatoista",
             "kahdennessatoista", "kahdennestatoista", "kahdenteentoista",
             "kahdennellatoista", "kahdenneltatoista", "kahdennelletoista",
             "kahdentenatoista", "kahdenneksitoista",
             "kahdensintoista", "kahdennettatoista", "kahdensinetoista")
        )
        self.assertEqual(
            tuple(n2f(12, to="ordinal", case=c, plural=True) for c in CASES),
            ("kahdennettoista", "kahdensientoista", "kahdensiatoista",
             "kahdensissatoista", "kahdensistatoista", "kahdensiintoista",
             "kahdensillatoista", "kahdensiltatoista", "kahdensilletoista",
             "kahdensinatoista", "kahdensiksitoista",
             "kahdensintoista", "kahdensittatoista", "kahdensinetoista")
        )

        # thirteen
        self.assertEqual(
            tuple(n2f(13, to="ordinal", case=c) for c in CASES),
            ("kolmastoista", "kolmannentoista", "kolmattatoista",
             "kolmannessatoista", "kolmannestatoista", "kolmanteentoista",
             "kolmannellatoista", "kolmanneltatoista", "kolmannelletoista",
             "kolmantenatoista", "kolmanneksitoista",
             "kolmansintoista", "kolmannettatoista", "kolmansinetoista")
        )
        self.assertEqual(
            tuple(n2f(13, to="ordinal", case=c, plural=True) for c in CASES),
            ("kolmannettoista", "kolmansientoista", "kolmansiatoista",
             "kolmansissatoista", "kolmansistatoista", "kolmansiintoista",
             "kolmansillatoista", "kolmansiltatoista", "kolmansilletoista",
             "kolmansinatoista", "kolmansiksitoista",
             "kolmansintoista", "kolmansittatoista", "kolmansinetoista")
        )

        # fourteen
        self.assertEqual(
            tuple(n2f(14, to="ordinal", case=c) for c in CASES),
            ("neljästoista", "neljännentoista", "neljättätoista",
             "neljännessätoista", "neljännestätoista", "neljänteentoista",
             "neljännellätoista", "neljänneltätoista", "neljännelletoista",
             "neljäntenätoista", "neljänneksitoista",
             "neljänsintoista", "neljännettätoista", "neljänsinetoista")
        )
        self.assertEqual(
            tuple(n2f(14, to="ordinal", case=c, plural=True) for c in CASES),
            ("neljännettoista", "neljänsientoista", "neljänsiätoista",
             "neljänsissätoista", "neljänsistätoista", "neljänsiintoista",
             "neljänsillätoista", "neljänsiltätoista", "neljänsilletoista",
             "neljänsinätoista", "neljänsiksitoista",
             "neljänsintoista", "neljänsittätoista", "neljänsinetoista")
        )

        # fifteen
        self.assertEqual(
            tuple(n2f(15, to="ordinal", case=c) for c in CASES),
            ("viidestoista", "viidennentoista", "viidettätoista",
             "viidennessätoista", "viidennestätoista", "viidenteentoista",
             "viidennellätoista", "viidenneltätoista", "viidennelletoista",
             "viidentenätoista", "viidenneksitoista",
             "viidensintoista", "viidennettätoista", "viidensinetoista")
        )
        self.assertEqual(
            tuple(n2f(15, to="ordinal", case=c, plural=True) for c in CASES),
            ("viidennettoista", "viidensientoista", "viidensiätoista",
             "viidensissätoista", "viidensistätoista", "viidensiintoista",
             "viidensillätoista", "viidensiltätoista", "viidensilletoista",
             "viidensinätoista", "viidensiksitoista",
             "viidensintoista", "viidensittätoista", "viidensinetoista")
        )

        # sixteen
        self.assertEqual(
            tuple(n2f(16, to="ordinal", case=c) for c in CASES),
            ("kuudestoista", "kuudennentoista", "kuudettatoista",
             "kuudennessatoista", "kuudennestatoista", "kuudenteentoista",
             "kuudennellatoista", "kuudenneltatoista", "kuudennelletoista",
             "kuudentenatoista", "kuudenneksitoista",
             "kuudensintoista", "kuudennettatoista", "kuudensinetoista")
        )
        self.assertEqual(
            tuple(n2f(16, to="ordinal", case=c, plural=True) for c in CASES),
            ("kuudennettoista", "kuudensientoista", "kuudensiatoista",
             "kuudensissatoista", "kuudensistatoista", "kuudensiintoista",
             "kuudensillatoista", "kuudensiltatoista", "kuudensilletoista",
             "kuudensinatoista", "kuudensiksitoista",
             "kuudensintoista", "kuudensittatoista", "kuudensinetoista")
        )

        # seventeen
        self.assertEqual(
            tuple(n2f(17, to="ordinal", case=c) for c in CASES),
            (
                "seitsemästoista",
                "seitsemännentoista",
                "seitsemättätoista",
                "seitsemännessätoista",
                "seitsemännestätoista",
                "seitsemänteentoista",
                "seitsemännellätoista",
                "seitsemänneltätoista",
                "seitsemännelletoista",
                "seitsemäntenätoista",
                "seitsemänneksitoista",
                "seitsemänsintoista",
                "seitsemännettätoista",
                "seitsemänsinetoista"
            )
        )
        self.assertEqual(
            tuple(n2f(17, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "seitsemännettoista",
                "seitsemänsientoista",
                "seitsemänsiätoista",
                "seitsemänsissätoista",
                "seitsemänsistätoista",
                "seitsemänsiintoista",
                "seitsemänsillätoista",
                "seitsemänsiltätoista",
                "seitsemänsilletoista",
                "seitsemänsinätoista",
                "seitsemänsiksitoista",
                "seitsemänsintoista",
                "seitsemänsittätoista",
                "seitsemänsinetoista"
            )
        )

        # eighteen
        self.assertEqual(
            tuple(n2f(18, to="ordinal", case=c) for c in CASES),
            (
                "kahdeksastoista",
                "kahdeksannentoista",
                "kahdeksattatoista",
                "kahdeksannessatoista",
                "kahdeksannestatoista",
                "kahdeksanteentoista",
                "kahdeksannellatoista",
                "kahdeksanneltatoista",
                "kahdeksannelletoista",
                "kahdeksantenatoista",
                "kahdeksanneksitoista",
                "kahdeksansintoista",
                "kahdeksannettatoista",
                "kahdeksansinetoista"
            )
        )
        self.assertEqual(
            tuple(n2f(18, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdeksannettoista",
                "kahdeksansientoista",
                "kahdeksansiatoista",
                "kahdeksansissatoista",
                "kahdeksansistatoista",
                "kahdeksansiintoista",
                "kahdeksansillatoista",
                "kahdeksansiltatoista",
                "kahdeksansilletoista",
                "kahdeksansinatoista",
                "kahdeksansiksitoista",
                "kahdeksansintoista",
                "kahdeksansittatoista",
                "kahdeksansinetoista"
            )
        )

        # nineteen
        self.assertEqual(
            tuple(n2f(19, to="ordinal", case=c) for c in CASES),
            (
                "yhdeksästoista",
                "yhdeksännentoista",
                "yhdeksättätoista",
                "yhdeksännessätoista",
                "yhdeksännestätoista",
                "yhdeksänteentoista",
                "yhdeksännellätoista",
                "yhdeksänneltätoista",
                "yhdeksännelletoista",
                "yhdeksäntenätoista",
                "yhdeksänneksitoista",
                "yhdeksänsintoista",
                "yhdeksännettätoista",
                "yhdeksänsinetoista"
            )
        )
        self.assertEqual(
            tuple(n2f(19, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "yhdeksännettoista",
                "yhdeksänsientoista",
                "yhdeksänsiätoista",
                "yhdeksänsissätoista",
                "yhdeksänsistätoista",
                "yhdeksänsiintoista",
                "yhdeksänsillätoista",
                "yhdeksänsiltätoista",
                "yhdeksänsilletoista",
                "yhdeksänsinätoista",
                "yhdeksänsiksitoista",
                "yhdeksänsintoista",
                "yhdeksänsittätoista",
                "yhdeksänsinetoista"
            )
        )

        # twenty
        self.assertEqual(
            tuple(n2f(20, to="ordinal", case=c) for c in CASES),
            (
                "kahdeskymmenes",
                "kahdennenkymmenennen",
                "kahdettakymmenettä",
                "kahdennessakymmenennessä",
                "kahdennestakymmenennestä",
                "kahdenteenkymmenenteen",
                "kahdennellakymmenennellä",
                "kahdenneltakymmenenneltä",
                "kahdennellekymmenennelle",
                "kahdentenakymmenentenä",
                "kahdenneksikymmenenneksi",
                "kahdensinkymmenensin",
                "kahdennettakymmenennettä",
                "kahdensinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(20, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdennetkymmenennet",
                "kahdensienkymmenensien",
                "kahdensiakymmenensiä",
                "kahdensissakymmenensissä",
                "kahdensistakymmenensistä",
                "kahdensiinkymmenensiin",
                "kahdensillakymmenensillä",
                "kahdensiltakymmenensiltä",
                "kahdensillekymmenensille",
                "kahdensinakymmenensinä",
                "kahdensiksikymmenensiksi",
                "kahdensinkymmenensin",
                "kahdensittakymmenensittä",
                "kahdensinekymmenensine"
            )
        )

    def test_mid(self):

        # thirty
        self.assertEqual(
            tuple(n2f(30, to="cardinal", case=c) for c in CASES),
            ("kolmekymmentä", "kolmenkymmenen", "kolmeakymmentä",
             "kolmessakymmenessä", "kolmestakymmenestä", "kolmeenkymmeneen",
             "kolmellakymmenellä", "kolmeltakymmeneltä", "kolmellekymmenelle",
             "kolmenakymmenenä", "kolmeksikymmeneksi",
             "kolmenkymmenin", "kolmettakymmenettä", "kolminekymmenine")
        )
        self.assertEqual(
            tuple(n2f(30, to="cardinal", case=c, plural=True) for c in CASES),
            ("kolmetkymmenet", "kolmienkymmenien", "kolmiakymmeniä",
             "kolmissakymmenissä", "kolmistakymmenistä", "kolmiinkymmeniin",
             "kolmillakymmenillä", "kolmiltakymmeniltä", "kolmillekymmenille",
             "kolminakymmeninä", "kolmiksikymmeniksi",
             "kolminkymmenin", "kolmittakymmenittä", "kolminekymmenine")
        )

        # forty
        self.assertEqual(
            tuple(n2f(40, to="cardinal", case=c) for c in CASES),
            ("neljäkymmentä", "neljänkymmenen", "neljääkymmentä",
             "neljässäkymmenessä", "neljästäkymmenestä", "neljäänkymmeneen",
             "neljälläkymmenellä", "neljältäkymmeneltä", "neljällekymmenelle",
             "neljänäkymmenenä", "neljäksikymmeneksi",
             "neljinkymmenin", "neljättäkymmenettä", "neljinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(40, to="cardinal", case=c, plural=True) for c in CASES),
            ("neljätkymmenet", "neljienkymmenien", "neljiäkymmeniä",
             "neljissäkymmenissä", "neljistäkymmenistä", "neljiinkymmeniin",
             "neljilläkymmenillä", "neljiltäkymmeniltä", "neljillekymmenille",
             "neljinäkymmeninä", "neljiksikymmeniksi",
             "neljinkymmenin", "neljittäkymmenittä", "neljinekymmenine")
        )

        # fifty
        self.assertEqual(
            tuple(n2f(50, to="cardinal", case=c) for c in CASES),
            ("viisikymmentä", "viidenkymmenen", "viittäkymmentä",
             "viidessäkymmenessä", "viidestäkymmenestä", "viiteenkymmeneen",
             "viidelläkymmenellä", "viideltäkymmeneltä", "viidellekymmenelle",
             "viitenäkymmenenä", "viideksikymmeneksi",
             "viisinkymmenin", "viidettäkymmenettä", "viisinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(50, to="cardinal", case=c, plural=True) for c in CASES),
            ("viidetkymmenet", "viisienkymmenien", "viisiäkymmeniä",
             "viisissäkymmenissä", "viisistäkymmenistä", "viisiinkymmeniin",
             "viisilläkymmenillä", "viisiltäkymmeniltä", "viisillekymmenille",
             "viisinäkymmeninä", "viisiksikymmeniksi",
             "viisinkymmenin", "viisittäkymmenittä", "viisinekymmenine")
        )

        # sixty
        self.assertEqual(
            tuple(n2f(60, to="cardinal", case=c) for c in CASES),
            ("kuusikymmentä", "kuudenkymmenen", "kuuttakymmentä",
             "kuudessakymmenessä", "kuudestakymmenestä", "kuuteenkymmeneen",
             "kuudellakymmenellä", "kuudeltakymmeneltä", "kuudellekymmenelle",
             "kuutenakymmenenä", "kuudeksikymmeneksi",
             "kuusinkymmenin", "kuudettakymmenettä", "kuusinekymmenine")
        )
        self.assertEqual(
            tuple(n2f(60, to="cardinal", case=c, plural=True) for c in CASES),
            ("kuudetkymmenet", "kuusienkymmenien", "kuusiakymmeniä",
             "kuusissakymmenissä", "kuusistakymmenistä", "kuusiinkymmeniin",
             "kuusillakymmenillä", "kuusiltakymmeniltä", "kuusillekymmenille",
             "kuusinakymmeninä", "kuusiksikymmeniksi",
             "kuusinkymmenin", "kuusittakymmenittä", "kuusinekymmenine")
        )

        # seventy
        self.assertEqual(
            tuple(n2f(70, to="cardinal", case=c) for c in CASES),
            (
                "seitsemänkymmentä",
                "seitsemänkymmenen",
                "seitsemääkymmentä",
                "seitsemässäkymmenessä",
                "seitsemästäkymmenestä",
                "seitsemäänkymmeneen",
                "seitsemälläkymmenellä",
                "seitsemältäkymmeneltä",
                "seitsemällekymmenelle",
                "seitsemänäkymmenenä",
                "seitsemäksikymmeneksi",
                "seitseminkymmenin",
                "seitsemättäkymmenettä",
                "seitseminekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(70, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "seitsemätkymmenet",
                "seitsemienkymmenien",
                "seitsemiäkymmeniä",
                "seitsemissäkymmenissä",
                "seitsemistäkymmenistä",
                "seitsemiinkymmeniin",
                "seitsemilläkymmenillä",
                "seitsemiltäkymmeniltä",
                "seitsemillekymmenille",
                "seitseminäkymmeninä",
                "seitsemiksikymmeniksi",
                "seitseminkymmenin",
                "seitsemittäkymmenittä",
                "seitseminekymmenine"
            )
        )

        # eighty
        self.assertEqual(
            tuple(n2f(80, to="cardinal", case=c) for c in CASES),
            (
                "kahdeksankymmentä",
                "kahdeksankymmenen",
                "kahdeksaakymmentä",
                "kahdeksassakymmenessä",
                "kahdeksastakymmenestä",
                "kahdeksaankymmeneen",
                "kahdeksallakymmenellä",
                "kahdeksaltakymmeneltä",
                "kahdeksallekymmenelle",
                "kahdeksanakymmenenä",
                "kahdeksaksikymmeneksi",
                "kahdeksinkymmenin",
                "kahdeksattakymmenettä",
                "kahdeksinekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(80, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "kahdeksatkymmenet",
                "kahdeksienkymmenien",
                "kahdeksiakymmeniä",
                "kahdeksissakymmenissä",
                "kahdeksistakymmenistä",
                "kahdeksiinkymmeniin",
                "kahdeksillakymmenillä",
                "kahdeksiltakymmeniltä",
                "kahdeksillekymmenille",
                "kahdeksinakymmeninä",
                "kahdeksiksikymmeniksi",
                "kahdeksinkymmenin",
                "kahdeksittakymmenittä",
                "kahdeksinekymmenine"
            )
        )

        # ninety
        self.assertEqual(
            tuple(n2f(90, to="cardinal", case=c) for c in CASES),
            (
                "yhdeksänkymmentä",
                "yhdeksänkymmenen",
                "yhdeksääkymmentä",
                "yhdeksässäkymmenessä",
                "yhdeksästäkymmenestä",
                "yhdeksäänkymmeneen",
                "yhdeksälläkymmenellä",
                "yhdeksältäkymmeneltä",
                "yhdeksällekymmenelle",
                "yhdeksänäkymmenenä",
                "yhdeksäksikymmeneksi",
                "yhdeksinkymmenin",
                "yhdeksättäkymmenettä",
                "yhdeksinekymmenine"
            )
        )
        self.assertEqual(
            tuple(n2f(90, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "yhdeksätkymmenet",
                "yhdeksienkymmenien",
                "yhdeksiäkymmeniä",
                "yhdeksissäkymmenissä",
                "yhdeksistäkymmenistä",
                "yhdeksiinkymmeniin",
                "yhdeksilläkymmenillä",
                "yhdeksiltäkymmeniltä",
                "yhdeksillekymmenille",
                "yhdeksinäkymmeninä",
                "yhdeksiksikymmeniksi",
                "yhdeksinkymmenin",
                "yhdeksittäkymmenittä",
                "yhdeksinekymmenine"
            )
        )

        # one hundred
        self.assertEqual(
            tuple(n2f(100, to="cardinal", case=c) for c in CASES),
            ("sata", "sadan", "sataa",
             "sadassa", "sadasta", "sataan",
             "sadalla", "sadalta", "sadalle",
             "satana", "sadaksi",
             "sadoin", "sadatta", "satoine")
        )
        self.assertEqual(
            tuple(n2f(100, to="cardinal", case=c, plural=True) for c in CASES),
            ("sadat", "satojen", "satoja",
             "sadoissa", "sadoista", "satoihin",
             "sadoilla", "sadoilta", "sadoille",
             "satoina", "sadoiksi",
             "sadoin", "sadoitta", "satoine")
        )

        # one hundred and twenty-three
        self.assertEqual(
            tuple(n2f(123, to="cardinal", case=c) for c in CASES),
            (
                "satakaksikymmentäkolme",
                "sadankahdenkymmenenkolmen",
                "sataakahtakymmentäkolmea",
                "sadassakahdessakymmenessäkolmessa",
                "sadastakahdestakymmenestäkolmesta",
                "sataankahteenkymmeneenkolmeen",
                "sadallakahdellakymmenelläkolmella",
                "sadaltakahdeltakymmeneltäkolmelta",
                "sadallekahdellekymmenellekolmelle",
                "satanakahtenakymmenenäkolmena",
                "sadaksikahdeksikymmeneksikolmeksi",
                "sadoinkaksinkymmeninkolmen",
                "sadattakahdettakymmenettäkolmetta",
                "satoinekaksinekymmeninekolmine"
            )
        )
        self.assertEqual(
            tuple(n2f(123, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "sadatkahdetkymmenetkolmet",
                "satojenkaksienkymmenienkolmien",
                "satojakaksiakymmeniäkolmia",
                "sadoissakaksissakymmenissäkolmissa",
                "sadoistakaksistakymmenistäkolmista",
                "satoihinkaksiinkymmeniinkolmiin",
                "sadoillakaksillakymmenilläkolmilla",
                "sadoiltakaksiltakymmeniltäkolmilta",
                "sadoillekaksillekymmenillekolmille",
                "satoinakaksinakymmeninäkolmina",
                "sadoiksikaksiksikymmeniksikolmiksi",
                "sadoinkaksinkymmeninkolmin",
                "sadoittakaksittakymmenittäkolmitta",
                "satoinekaksinekymmeninekolmine"
            )
        )

        # one thousand
        self.assertEqual(
            tuple(n2f(1000, to="cardinal", case=c) for c in CASES),
            ("tuhat", "tuhannen", "tuhatta",
             "tuhannessa", "tuhannesta", "tuhanteen",
             "tuhannella", "tuhannelta", "tuhannelle",
             "tuhantena", "tuhanneksi",
             "tuhansin", "tuhannetta", "tuhansine")
        )
        self.assertEqual(
            tuple(n2f(1000, to="cardinal", case=c, plural=True) for c in CASES),
            ("tuhannet", "tuhansien", "tuhansia",
             "tuhansissa", "tuhansista", "tuhansiin",
             "tuhansilla", "tuhansilta", "tuhansille",
             "tuhansina", "tuhansiksi",
             "tuhansin", "tuhansitta", "tuhansine")
        )

        # one thousand, two hundred and thirty-four
        self.assertEqual(
            tuple(n2f(1234, to="cardinal", case=c) for c in CASES),
            (
                "tuhat kaksisataakolmekymmentäneljä",
                "tuhannen kahdensadankolmenkymmenenneljän",
                "tuhatta kahtasataakolmeakymmentäneljää",
                "tuhannessa kahdessasadassakolmessakymmenessäneljässä",
                "tuhannesta kahdestasadastakolmestakymmenestäneljästä",
                "tuhanteen kahteensataankolmeenkymmeneenneljään",
                "tuhannella kahdellasadallakolmellakymmenelläneljällä",
                "tuhannelta kahdeltasadaltakolmeltakymmeneltäneljältä",
                "tuhannelle kahdellesadallekolmellekymmenelleneljälle",
                "tuhantena kahtenasatanakolmenakymmenenäneljänä",
                "tuhanneksi kahdeksisadaksikolmeksikymmeneksineljäksi",
                "tuhansin kaksinsadoinkolmenkymmeninneljin",
                "tuhannetta kahdettasadattakolmettakymmenettäneljättä",
                "tuhansine kaksinesatoinekolminekymmenineneljine"
            )
        )
        self.assertEqual(
            tuple(n2f(1234, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "tuhannet kahdetsadatkolmetkymmenetneljät",
                "tuhansien kaksiensatojenkolmienkymmenienneljien",
                "tuhansia kaksiasatojakolmiakymmeniäneljiä",
                "tuhansissa kaksissasadoissakolmissakymmenissäneljissä",
                "tuhansista kaksistasadoistakolmistakymmenistäneljistä",
                "tuhansiin kaksiinsatoihinkolmiinkymmeniinneljiin",
                "tuhansilla kaksillasadoillakolmillakymmenilläneljillä",
                "tuhansilta kaksiltasadoiltakolmiltakymmeniltäneljiltä",
                "tuhansille kaksillesadoillekolmillekymmenilleneljille",
                "tuhansina kaksinasatoinakolminakymmeninäneljinä",
                "tuhansiksi kaksiksisadoiksikolmiksikymmeniksineljiksi",
                "tuhansin kaksinsadoinkolminkymmeninneljin",
                "tuhansitta kaksittasadoittakolmittakymmenittäneljittä",
                "tuhansine kaksinesatoinekolminekymmenineneljine"
            )
        )

    def test_mid_ord(self):

        # thirty
        self.assertEqual(
            tuple(n2f(30, to="ordinal", case=c) for c in CASES),
            (
                "kolmaskymmenes",
                "kolmannenkymmenennen",
                "kolmattakymmenettä",
                "kolmannessakymmenennessä",
                "kolmannestakymmenennestä",
                "kolmanteenkymmenenteen",
                "kolmannellakymmenennellä",
                "kolmanneltakymmenenneltä",
                "kolmannellekymmenennelle",
                "kolmantenakymmenentenä",
                "kolmanneksikymmenenneksi",
                "kolmansinkymmenensin",
                "kolmannettakymmenennettä",
                "kolmansinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(30, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kolmannetkymmenennet",
                "kolmansienkymmenensien",
                "kolmansiakymmenensiä",
                "kolmansissakymmenensissä",
                "kolmansistakymmenensistä",
                "kolmansiinkymmenensiin",
                "kolmansillakymmenensillä",
                "kolmansiltakymmenensiltä",
                "kolmansillekymmenensille",
                "kolmansinakymmenensinä",
                "kolmansiksikymmenensiksi",
                "kolmansinkymmenensin",
                "kolmansittakymmenensittä",
                "kolmansinekymmenensine"
            )
        )

        # forty
        self.assertEqual(
            tuple(n2f(40, to="ordinal", case=c) for c in CASES),
            (
                "neljäskymmenes",
                "neljännenkymmenennen",
                "neljättäkymmenettä",
                "neljännessäkymmenennessä",
                "neljännestäkymmenennestä",
                "neljänteenkymmenenteen",
                "neljännelläkymmenennellä",
                "neljänneltäkymmenenneltä",
                "neljännellekymmenennelle",
                "neljäntenäkymmenentenä",
                "neljänneksikymmenenneksi",
                "neljänsinkymmenensin",
                "neljännettäkymmenennettä",
                "neljänsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(40, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "neljännetkymmenennet",
                "neljänsienkymmenensien",
                "neljänsiäkymmenensiä",
                "neljänsissäkymmenensissä",
                "neljänsistäkymmenensistä",
                "neljänsiinkymmenensiin",
                "neljänsilläkymmenensillä",
                "neljänsiltäkymmenensiltä",
                "neljänsillekymmenensille",
                "neljänsinäkymmenensinä",
                "neljänsiksikymmenensiksi",
                "neljänsinkymmenensin",
                "neljänsittäkymmenensittä",
                "neljänsinekymmenensine"
            )
        )

        # fifty
        self.assertEqual(
            tuple(n2f(50, to="ordinal", case=c) for c in CASES),
            (
                "viideskymmenes",
                "viidennenkymmenennen",
                "viidettäkymmenettä",
                "viidennessäkymmenennessä",
                "viidennestäkymmenennestä",
                "viidenteenkymmenenteen",
                "viidennelläkymmenennellä",
                "viidenneltäkymmenenneltä",
                "viidennellekymmenennelle",
                "viidentenäkymmenentenä",
                "viidenneksikymmenenneksi",
                "viidensinkymmenensin",
                "viidennettäkymmenennettä",
                "viidensinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(50, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "viidennetkymmenennet",
                "viidensienkymmenensien",
                "viidensiäkymmenensiä",
                "viidensissäkymmenensissä",
                "viidensistäkymmenensistä",
                "viidensiinkymmenensiin",
                "viidensilläkymmenensillä",
                "viidensiltäkymmenensiltä",
                "viidensillekymmenensille",
                "viidensinäkymmenensinä",
                "viidensiksikymmenensiksi",
                "viidensinkymmenensin",
                "viidensittäkymmenensittä",
                "viidensinekymmenensine"
            )
        )

        # sixty
        self.assertEqual(
            tuple(n2f(60, to="ordinal", case=c) for c in CASES),
            (
                "kuudeskymmenes",
                "kuudennenkymmenennen",
                "kuudettakymmenettä",
                "kuudennessakymmenennessä",
                "kuudennestakymmenennestä",
                "kuudenteenkymmenenteen",
                "kuudennellakymmenennellä",
                "kuudenneltakymmenenneltä",
                "kuudennellekymmenennelle",
                "kuudentenakymmenentenä",
                "kuudenneksikymmenenneksi",
                "kuudensinkymmenensin",
                "kuudennettakymmenennettä",
                "kuudensinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(60, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kuudennetkymmenennet",
                "kuudensienkymmenensien",
                "kuudensiakymmenensiä",
                "kuudensissakymmenensissä",
                "kuudensistakymmenensistä",
                "kuudensiinkymmenensiin",
                "kuudensillakymmenensillä",
                "kuudensiltakymmenensiltä",
                "kuudensillekymmenensille",
                "kuudensinakymmenensinä",
                "kuudensiksikymmenensiksi",
                "kuudensinkymmenensin",
                "kuudensittakymmenensittä",
                "kuudensinekymmenensine"
            )
        )

        # seventy
        self.assertEqual(
            tuple(n2f(70, to="ordinal", case=c) for c in CASES),
            (
                "seitsemäskymmenes",
                "seitsemännenkymmenennen",
                "seitsemättäkymmenettä",
                "seitsemännessäkymmenennessä",
                "seitsemännestäkymmenennestä",
                "seitsemänteenkymmenenteen",
                "seitsemännelläkymmenennellä",
                "seitsemänneltäkymmenenneltä",
                "seitsemännellekymmenennelle",
                "seitsemäntenäkymmenentenä",
                "seitsemänneksikymmenenneksi",
                "seitsemänsinkymmenensin",
                "seitsemännettäkymmenennettä",
                "seitsemänsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(70, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "seitsemännetkymmenennet",
                "seitsemänsienkymmenensien",
                "seitsemänsiäkymmenensiä",
                "seitsemänsissäkymmenensissä",
                "seitsemänsistäkymmenensistä",
                "seitsemänsiinkymmenensiin",
                "seitsemänsilläkymmenensillä",
                "seitsemänsiltäkymmenensiltä",
                "seitsemänsillekymmenensille",
                "seitsemänsinäkymmenensinä",
                "seitsemänsiksikymmenensiksi",
                "seitsemänsinkymmenensin",
                "seitsemänsittäkymmenensittä",
                "seitsemänsinekymmenensine"
            )
        )

        # eighty
        self.assertEqual(
            tuple(n2f(80, to="ordinal", case=c) for c in CASES),
            (
                "kahdeksaskymmenes",
                "kahdeksannenkymmenennen",
                "kahdeksattakymmenettä",
                "kahdeksannessakymmenennessä",
                "kahdeksannestakymmenennestä",
                "kahdeksanteenkymmenenteen",
                "kahdeksannellakymmenennellä",
                "kahdeksanneltakymmenenneltä",
                "kahdeksannellekymmenennelle",
                "kahdeksantenakymmenentenä",
                "kahdeksanneksikymmenenneksi",
                "kahdeksansinkymmenensin",
                "kahdeksannettakymmenennettä",
                "kahdeksansinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(80, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdeksannetkymmenennet",
                "kahdeksansienkymmenensien",
                "kahdeksansiakymmenensiä",
                "kahdeksansissakymmenensissä",
                "kahdeksansistakymmenensistä",
                "kahdeksansiinkymmenensiin",
                "kahdeksansillakymmenensillä",
                "kahdeksansiltakymmenensiltä",
                "kahdeksansillekymmenensille",
                "kahdeksansinakymmenensinä",
                "kahdeksansiksikymmenensiksi",
                "kahdeksansinkymmenensin",
                "kahdeksansittakymmenensittä",
                "kahdeksansinekymmenensine"
            )
        )

        # ninety
        self.assertEqual(
            tuple(n2f(90, to="ordinal", case=c) for c in CASES),
            (
                "yhdeksäskymmenes",
                "yhdeksännenkymmenennen",
                "yhdeksättäkymmenettä",
                "yhdeksännessäkymmenennessä",
                "yhdeksännestäkymmenennestä",
                "yhdeksänteenkymmenenteen",
                "yhdeksännelläkymmenennellä",
                "yhdeksänneltäkymmenenneltä",
                "yhdeksännellekymmenennelle",
                "yhdeksäntenäkymmenentenä",
                "yhdeksänneksikymmenenneksi",
                "yhdeksänsinkymmenensin",
                "yhdeksännettäkymmenennettä",
                "yhdeksänsinekymmenensine"
            )
        )
        self.assertEqual(
            tuple(n2f(90, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "yhdeksännetkymmenennet",
                "yhdeksänsienkymmenensien",
                "yhdeksänsiäkymmenensiä",
                "yhdeksänsissäkymmenensissä",
                "yhdeksänsistäkymmenensistä",
                "yhdeksänsiinkymmenensiin",
                "yhdeksänsilläkymmenensillä",
                "yhdeksänsiltäkymmenensiltä",
                "yhdeksänsillekymmenensille",
                "yhdeksänsinäkymmenensinä",
                "yhdeksänsiksikymmenensiksi",
                "yhdeksänsinkymmenensin",
                "yhdeksänsittäkymmenensittä",
                "yhdeksänsinekymmenensine"
            )
        )

        # one hundred
        self.assertEqual(
            tuple(n2f(100, to="ordinal", case=c) for c in CASES),
            ("sadas", "sadannen", "sadatta",
             "sadannessa", "sadannesta", "sadanteen",
             "sadannella", "sadannelta", "sadannelle",
             "sadantena", "sadanneksi",
             "sadansin", "sadannetta", "sadansine")
        )
        self.assertEqual(
            tuple(n2f(100, to="ordinal", case=c, plural=True) for c in CASES),
            ("sadannet", "sadansien", "sadansia",
             "sadansissa", "sadansista", "sadansiin",
             "sadansilla", "sadansilta", "sadansille",
             "sadansina", "sadansiksi",
             "sadansin", "sadansitta", "sadansine")
        )

        # one hundred and twenty-three
        self.assertEqual(
            tuple(n2f(123, to="ordinal", case=c) for c in CASES),
            (
                "sadaskahdeskymmeneskolmas",
                "sadannenkahdennenkymmenennenkolmannen",
                "sadattakahdettakymmenettäkolmatta",
                "sadannessakahdennessakymmenennessäkolmannessa",
                "sadannestakahdennestakymmenennestäkolmannesta",
                "sadanteenkahdenteenkymmenenteenkolmanteen",
                "sadannellakahdennellakymmenennelläkolmannella",
                "sadanneltakahdenneltakymmenenneltäkolmannelta",
                "sadannellekahdennellekymmenennellekolmannelle",
                "sadantenakahdentenakymmenentenäkolmantena",
                "sadanneksikahdenneksikymmenenneksikolmanneksi",
                "sadansinkahdensinkymmenensinkolmansin",
                "sadannettakahdennettakymmenennettäkolmannetta",
                "sadansinekahdensinekymmenensinekolmansine"
            )
        )
        self.assertEqual(
            tuple(n2f(123, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "sadannetkahdennetkymmenennetkolmannet",
                "sadansienkahdensienkymmenensienkolmansien",
                "sadansiakahdensiakymmenensiäkolmansia",
                "sadansissakahdensissakymmenensissäkolmansissa",
                "sadansistakahdensistakymmenensistäkolmansista",
                "sadansiinkahdensiinkymmenensiinkolmansiin",
                "sadansillakahdensillakymmenensilläkolmansilla",
                "sadansiltakahdensiltakymmenensiltäkolmansilta",
                "sadansillekahdensillekymmenensillekolmansille",
                "sadansinakahdensinakymmenensinäkolmansina",
                "sadansiksikahdensiksikymmenensiksikolmansiksi",
                "sadansinkahdensinkymmenensinkolmansin",
                "sadansittakahdensittakymmenensittäkolmansitta",
                "sadansinekahdensinekymmenensinekolmansine"
            )
        )

        # one thousand
        self.assertEqual(
            tuple(n2f(1000, to="ordinal", case=c) for c in CASES),
            ("tuhannes", "tuhannennen", "tuhannetta",
             "tuhannennessa", "tuhannennesta", "tuhannenteen",
             "tuhannennella", "tuhannennelta", "tuhannennelle",
             "tuhannentena", "tuhannenneksi",
             "tuhannensin", "tuhannennetta", "tuhannensine")
        )
        self.assertEqual(
            tuple(n2f(1000, to="ordinal", case=c, plural=True) for c in CASES),
            ("tuhannennet", "tuhannensien", "tuhannensia",
             "tuhannensissa", "tuhannensista", "tuhannensiin",
             "tuhannensilla", "tuhannensilta", "tuhannensille",
             "tuhannensina", "tuhannensiksi",
             "tuhannensin", "tuhannensitta", "tuhannensine")
        )

        # one thousand, two hundred and thirty-four
        self.assertEqual(
            tuple(n2f(1234, to="ordinal", case=c) for c in CASES),
            (
                "tuhannes kahdessadaskolmaskymmenesneljäs",
                "tuhannennen kahdennensadannenkolmannenkymmenennenneljännen",
                "tuhannetta kahdettasadattakolmattakymmenettäneljättä",
                "tuhannennessa kahdennessasadannessakolmannessakymmenennessäneljännessä",  # NOQA
                "tuhannennesta kahdennestasadannestakolmannestakymmenennestäneljännestä",  # NOQA
                "tuhannenteen kahdenteensadanteenkolmanteenkymmenenteenneljänteen",  # NOQA
                "tuhannennella kahdennellasadannellakolmannellakymmenennelläneljännellä",  # NOQA
                "tuhannennelta kahdenneltasadanneltakolmanneltakymmenenneltäneljänneltä",  # NOQA
                "tuhannennelle kahdennellesadannellekolmannellekymmenennelleneljännelle",  # NOQA
                "tuhannentena kahdentenasadantenakolmantenakymmenentenäneljäntenä",  # NOQA
                "tuhannenneksi kahdenneksisadanneksikolmanneksikymmenenneksineljänneksi",  # NOQA
                "tuhannensin kahdensinsadansinkolmansinkymmenensinneljänsin",  # NOQA
                "tuhannennetta kahdennettasadannettakolmannettakymmenennettäneljännettä",  # NOQA
                "tuhannensine kahdensinesadansinekolmansinekymmenensineneljänsine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(1234, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "tuhannennet kahdennetsadannetkolmannetkymmenennetneljännet",
                "tuhannensien kahdensiensadansienkolmansienkymmenensienneljänsien",  # NOQA
                "tuhannensia kahdensiasadansiakolmansiakymmenensiäneljänsiä",
                "tuhannensissa kahdensissasadansissakolmansissakymmenensissäneljänsissä",  # NOQA
                "tuhannensista kahdensistasadansistakolmansistakymmenensistäneljänsistä",  # NOQA
                "tuhannensiin kahdensiinsadansiinkolmansiinkymmenensiinneljänsiin",  # NOQA
                "tuhannensilla kahdensillasadansillakolmansillakymmenensilläneljänsillä",  # NOQA
                "tuhannensilta kahdensiltasadansiltakolmansiltakymmenensiltäneljänsiltä",  # NOQA
                "tuhannensille kahdensillesadansillekolmansillekymmenensilleneljänsille",  # NOQA
                "tuhannensina kahdensinasadansinakolmansinakymmenensinäneljänsinä",  # NOQA
                "tuhannensiksi kahdensiksisadansiksikolmansiksikymmenensiksineljänsiksi",  # NOQA
                "tuhannensin kahdensinsadansinkolmansinkymmenensinneljänsin",
                "tuhannensitta kahdensittasadansittakolmansittakymmenensittäneljänsittä",  # NOQA
                "tuhannensine kahdensinesadansinekolmansinekymmenensineneljänsine"  # NOQA
            )
        )

    def test_high(self):

        # ten thousand
        self.assertEqual(
            tuple(n2f(10000, to="cardinal", case=c) for c in CASES),
            (
                "kymmenentuhatta",
                "kymmenentuhannen",
                "kymmentätuhatta",
                "kymmenessätuhannessa",
                "kymmenestätuhannesta",
                "kymmeneentuhanteen",
                "kymmenellätuhannella",
                "kymmeneltätuhannelta",
                "kymmenelletuhannelle",
                "kymmenenätuhantena",
                "kymmeneksituhanneksi",
                "kymmenintuhansin",
                "kymmenettätuhannetta",
                "kymmeninetuhansine"
            )
        )
        self.assertEqual(
            tuple(n2f(10000, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "kymmenettuhannet",
                "kymmenientuhansien",
                "kymmeniätuhansia",
                "kymmenissätuhansissa",
                "kymmenistätuhansista",
                "kymmeniintuhansiin",
                "kymmenillätuhansilla",
                "kymmeniltätuhansilta",
                "kymmenilletuhansille",
                "kymmeninätuhansina",
                "kymmeniksituhansiksi",
                "kymmenintuhansin",
                "kymmenittätuhansitta",
                "kymmeninetuhansine"
            )
        )

        # twelve thousand, three hundred and forty-five
        self.assertEqual(
            tuple(n2f(12345, to="cardinal", case=c) for c in CASES),
            (
                "kaksitoistatuhatta kolmesataaneljäkymmentäviisi",
                "kahdentoistatuhannen kolmensadanneljänkymmenenviiden",
                "kahtatoistatuhatta kolmeasataaneljääkymmentäviittä",
                "kahdessatoistatuhannessa kolmessasadassaneljässäkymmenessäviidessä",  # NOQA
                "kahdestatoistatuhannesta kolmestasadastaneljästäkymmenestäviidestä",  # NOQA
                "kahteentoistatuhanteen kolmeensataanneljäänkymmeneenviiteen",
                "kahdellatoistatuhannella kolmellasadallaneljälläkymmenelläviidellä",  # NOQA
                "kahdeltatoistatuhannelta kolmeltasadaltaneljältäkymmeneltäviideltä",  # NOQA
                "kahdelletoistatuhannelle kolmellesadalleneljällekymmenelleviidelle",  # NOQA
                "kahtenatoistatuhantena kolmenasatananeljänäkymmenenäviitenä",
                "kahdeksitoistatuhanneksi kolmeksisadaksineljäksikymmeneksiviideksi",  # NOQA
                "kaksintoistatuhansin kolmensadoinneljinkymmeninviisin",
                "kahdettatoistatuhannetta kolmettasadattaneljättäkymmenettäviidettä",  # NOQA
                "kaksinetoistatuhansine kolminesatoineneljinekymmenineviisine"
            )
        )
        self.assertEqual(
            tuple(n2f(
                12345, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "kahdettoistatuhannet kolmetsadatneljätkymmenetviidet",
                "kaksientoistatuhansien kolmiensatojenneljienkymmenienviisien",
                "kaksiatoistatuhansia kolmiasatojaneljiäkymmeniäviisiä",
                "kaksissatoistatuhansissa kolmissasadoissaneljissäkymmenissäviisissä",  # NOQA
                "kaksistatoistatuhansista kolmistasadoistaneljistäkymmenistäviisistä",  # NOQA
                "kaksiintoistatuhansiin kolmiinsatoihinneljiinkymmeniinviisiin",  # NOQA
                "kaksillatoistatuhansilla kolmillasadoillaneljilläkymmenilläviisillä",  # NOQA
                "kaksiltatoistatuhansilta kolmiltasadoiltaneljiltäkymmeniltäviisiltä",  # NOQA
                "kaksilletoistatuhansille kolmillesadoilleneljillekymmenilleviisille",  # NOQA
                "kaksinatoistatuhansina kolminasatoinaneljinäkymmeninäviisinä",
                "kaksiksitoistatuhansiksi kolmiksisadoiksineljiksikymmeniksiviisiksi",  # NOQA
                "kaksintoistatuhansin kolminsadoinneljinkymmeninviisin",
                "kaksittatoistatuhansitta kolmittasadoittaneljittäkymmenittäviisittä",  # NOQA
                "kaksinetoistatuhansine kolminesatoineneljinekymmenineviisine"
            )
        )

        # one hundred thousand
        self.assertEqual(
            tuple(n2f(100000, to="cardinal", case=c) for c in CASES),
            ("satatuhatta", "sadantuhannen", "sataatuhatta",
             "sadassatuhannessa", "sadastatuhannesta", "sataantuhanteen",
             "sadallatuhannella", "sadaltatuhannelta", "sadalletuhannelle",
             "satanatuhantena", "sadaksituhanneksi",
             "sadointuhansin", "sadattatuhannetta", "satoinetuhansine")
        )
        self.assertEqual(
            tuple(n2f(100000, to="cardinal", case=c, plural=True) for c in CASES),
            ("sadattuhannet", "satojentuhansien", "satojatuhansia",
             "sadoissatuhansissa", "sadoistatuhansista", "satoihintuhansiin",
             "sadoillatuhansilla", "sadoiltatuhansilta", "sadoilletuhansille",
             "satoinatuhansina", "sadoiksituhansiksi",
             "sadointuhansin", "sadoittatuhansitta", "satoinetuhansine")
        )

        # one hundred and twenty-three thousand, four hundred and fifty-six
        self.assertEqual(
            tuple(n2f(123456, to="cardinal", case=c) for c in CASES),
            (
                "satakaksikymmentäkolmetuhatta neljäsataaviisikymmentäkuusi",
                "sadankahdenkymmenenkolmentuhannen neljänsadanviidenkymmenenkuuden",  # NOQA
                "sataakahtakymmentäkolmeatuhatta neljääsataaviittäkymmentäkuutta",  # NOQA
                "sadassakahdessakymmenessäkolmessatuhannessa neljässäsadassaviidessäkymmenessäkuudessa",  # NOQA
                "sadastakahdestakymmenestäkolmestatuhannesta neljästäsadastaviidestäkymmenestäkuudesta",  # NOQA
                "sataankahteenkymmeneenkolmeentuhanteen neljäänsataanviiteenkymmeneenkuuteen",  # NOQA
                "sadallakahdellakymmenelläkolmellatuhannella neljälläsadallaviidelläkymmenelläkuudella",  # NOQA
                "sadaltakahdeltakymmeneltäkolmeltatuhannelta neljältäsadaltaviideltäkymmeneltäkuudelta",  # NOQA
                "sadallekahdellekymmenellekolmelletuhannelle neljällesadalleviidellekymmenellekuudelle",  # NOQA
                "satanakahtenakymmenenäkolmenatuhantena neljänäsatanaviitenäkymmenenäkuutena",  # NOQA
                "sadaksikahdeksikymmeneksikolmeksituhanneksi neljäksisadaksiviideksikymmeneksikuudeksi",  # NOQA
                "sadoinkaksinkymmeninkolmentuhansin neljinsadoinviisinkymmeninkuusin",  # NOQA
                "sadattakahdettakymmenettäkolmettatuhannetta neljättäsadattaviidettäkymmenettäkuudetta",  # NOQA
                "satoinekaksinekymmeninekolminetuhansine neljinesatoineviisinekymmeninekuusine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(123456, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "sadatkahdetkymmenetkolmettuhannet neljätsadatviidetkymmenetkuudet",  # NOQA
                "satojenkaksienkymmenienkolmientuhansien neljiensatojenviisienkymmenienkuusien",  # NOQA
                "satojakaksiakymmeniäkolmiatuhansia neljiäsatojaviisiäkymmeniäkuusia",  # NOQA
                "sadoissakaksissakymmenissäkolmissatuhansissa neljissäsadoissaviisissäkymmenissäkuusissa",  # NOQA
                "sadoistakaksistakymmenistäkolmistatuhansista neljistäsadoistaviisistäkymmenistäkuusista",  # NOQA
                "satoihinkaksiinkymmeniinkolmiintuhansiin neljiinsatoihinviisiinkymmeniinkuusiin",  # NOQA
                "sadoillakaksillakymmenilläkolmillatuhansilla neljilläsadoillaviisilläkymmenilläkuusilla",  # NOQA
                "sadoiltakaksiltakymmeniltäkolmiltatuhansilta neljiltäsadoiltaviisiltäkymmeniltäkuusilta",  # NOQA
                "sadoillekaksillekymmenillekolmilletuhansille neljillesadoilleviisillekymmenillekuusille",  # NOQA
                "satoinakaksinakymmeninäkolminatuhansina neljinäsatoinaviisinäkymmeninäkuusina",  # NOQA
                "sadoiksikaksiksikymmeniksikolmiksituhansiksi neljiksisadoiksiviisiksikymmeniksikuusiksi",  # NOQA
                "sadoinkaksinkymmeninkolmintuhansin neljinsadoinviisinkymmeninkuusin",  # NOQA
                "sadoittakaksittakymmenittäkolmittatuhansitta neljittäsadoittaviisittäkymmenittäkuusitta",  # NOQA
                "satoinekaksinekymmeninekolminetuhansine neljinesatoineviisinekymmeninekuusine"  # NOQA
            )
        )

        # one million
        self.assertEqual(
            tuple(n2f(10**6, to="cardinal", case=c) for c in CASES),
            ("miljoona", "miljoonan", "miljoonaa",
             "miljoonassa", "miljoonasta", "miljoonaan",
             "miljoonalla", "miljoonalta", "miljoonalle",
             "miljoonana", "miljoonaksi",
             "miljoonin", "miljoonatta", "miljoonine")
        )
        self.assertEqual(
            tuple(n2f(10**6, to="cardinal", case=c, plural=True) for c in CASES),
            ("miljoonat", "miljoonien", "miljoonia",
             "miljoonissa", "miljoonista", "miljooniin",
             "miljoonilla", "miljoonilta", "miljoonille",
             "miljoonina", "miljooniksi",
             "miljoonin", "miljoonitta", "miljoonine")
        )

        # one million, two hundred and thirty-four thousand, five hundred and sixty-seven
        self.assertEqual(
            tuple(n2f(1234567, to="cardinal", case=c) for c in CASES),
            (
                "miljoona kaksisataakolmekymmentäneljätuhatta viisisataakuusikymmentäseitsemän",  # NOQA
                "miljoonan kahdensadankolmenkymmenenneljäntuhannen viidensadankuudenkymmenenseitsemän",  # NOQA
                "miljoonaa kahtasataakolmeakymmentäneljäätuhatta viittäsataakuuttakymmentäseitsemää",  # NOQA
                "miljoonassa kahdessasadassakolmessakymmenessäneljässätuhannessa viidessäsadassakuudessakymmenessäseitsemässä",  # NOQA
                "miljoonasta kahdestasadastakolmestakymmenestäneljästätuhannesta viidestäsadastakuudestakymmenestäseitsemästä",  # NOQA
                "miljoonaan kahteensataankolmeenkymmeneenneljääntuhanteen viiteensataankuuteenkymmeneenseitsemään",  # NOQA
                "miljoonalla kahdellasadallakolmellakymmenelläneljällätuhannella viidelläsadallakuudellakymmenelläseitsemällä",  # NOQA
                "miljoonalta kahdeltasadaltakolmeltakymmeneltäneljältätuhannelta viideltäsadaltakuudeltakymmeneltäseitsemältä",  # NOQA
                "miljoonalle kahdellesadallekolmellekymmenelleneljälletuhannelle viidellesadallekuudellekymmenelleseitsemälle",  # NOQA
                "miljoonana kahtenasatanakolmenakymmenenäneljänätuhantena viitenäsatanakuutenakymmenenäseitsemänä",  # NOQA
                "miljoonaksi kahdeksisadaksikolmeksikymmeneksineljäksituhanneksi viideksisadaksikuudeksikymmeneksiseitsemäksi",  # NOQA
                "miljoonin kaksinsadoinkolmenkymmeninneljintuhansin viisinsadoinkuusinkymmeninseitsemin",  # NOQA
                "miljoonatta kahdettasadattakolmettakymmenettäneljättätuhannetta viidettäsadattakuudettakymmenettäseitsemättä",  # NOQA
                "miljoonine kaksinesatoinekolminekymmenineneljinetuhansine viisinesatoinekuusinekymmenineseitsemine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(1234567, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "miljoonat kahdetsadatkolmetkymmenetneljättuhannet viidetsadatkuudetkymmenetseitsemät",  # NOQA
                "miljoonien kaksiensatojenkolmienkymmenienneljientuhansien viisiensatojenkuusienkymmenienseitsemien",  # NOQA
                "miljoonia kaksiasatojakolmiakymmeniäneljiätuhansia viisiäsatojakuusiakymmeniäseitsemiä",  # NOQA
                "miljoonissa kaksissasadoissakolmissakymmenissäneljissätuhansissa viisissäsadoissakuusissakymmenissäseitsemissä",  # NOQA
                "miljoonista kaksistasadoistakolmistakymmenistäneljistätuhansista viisistäsadoistakuusistakymmenistäseitsemistä",  # NOQA
                "miljooniin kaksiinsatoihinkolmiinkymmeniinneljiintuhansiin viisiinsatoihinkuusiinkymmeniinseitsemiin",  # NOQA
                "miljoonilla kaksillasadoillakolmillakymmenilläneljillätuhansilla viisilläsadoillakuusillakymmenilläseitsemillä",  # NOQA
                "miljoonilta kaksiltasadoiltakolmiltakymmeniltäneljiltätuhansilta viisiltäsadoiltakuusiltakymmeniltäseitsemiltä",  # NOQA
                "miljoonille kaksillesadoillekolmillekymmenilleneljilletuhansille viisillesadoillekuusillekymmenilleseitsemille",  # NOQA
                "miljoonina kaksinasatoinakolminakymmeninäneljinätuhansina viisinäsatoinakuusinakymmeninäseitseminä",  # NOQA
                "miljooniksi kaksiksisadoiksikolmiksikymmeniksineljiksituhansiksi viisiksisadoiksikuusiksikymmeniksiseitsemiksi",  # NOQA
                "miljoonin kaksinsadoinkolminkymmeninneljintuhansin viisinsadoinkuusinkymmeninseitsemin",  # NOQA
                "miljoonitta kaksittasadoittakolmittakymmenittäneljittätuhansitta viisittäsadoittakuusittakymmenittäseitsemittä",  # NOQA
                "miljoonine kaksinesatoinekolminekymmenineneljinetuhansine viisinesatoinekuusinekymmenineseitsemine"  # NOQA
            )
        )

        # one billion (short scale)
        self.assertEqual(
            tuple(n2f(10**9, to="cardinal", case=c) for c in CASES),
            ("miljardi", "miljardin", "miljardia",
             "miljardissa", "miljardista", "miljardiin",
             "miljardilla", "miljardilta", "miljardille",
             "miljardina", "miljardiksi",
             "miljardein", "miljarditta", "miljardeine")
        )
        self.assertEqual(
            tuple(n2f(10**9, to="cardinal", case=c, plural=True) for c in CASES),
            ("miljardit", "miljardien", "miljardeja",
             "miljardeissa", "miljardeista", "miljardeihin",
             "miljardeilla", "miljardeilta", "miljardeille",
             "miljardeina", "miljardeiksi",
             "miljardein", "miljardeitta", "miljardeine")
        )

        # one billion, two hundred and thirty-four million,
        # five hundred and sixty-seven thousand, eight hundred and ninety
        # (short scale)
        self.assertEqual(
            tuple(n2f(1234567890, to="cardinal", case=c) for c in CASES),
            (
                "miljardi kaksisataakolmekymmentäneljämiljoonaa viisisataakuusikymmentäseitsemäntuhatta kahdeksansataayhdeksänkymmentä",  # NOQA
                "miljardin kahdensadankolmenkymmenenneljänmiljoonan viidensadankuudenkymmenenseitsemäntuhannen kahdeksansadanyhdeksänkymmenen",  # NOQA
                "miljardia kahtasataakolmeakymmentäneljäämiljoonaa viittäsataakuuttakymmentäseitsemäätuhatta kahdeksaasataayhdeksääkymmentä",  # NOQA
                "miljardissa kahdessasadassakolmessakymmenessäneljässämiljoonassa viidessäsadassakuudessakymmenessäseitsemässätuhannessa kahdeksassasadassayhdeksässäkymmenessä",  # NOQA
                "miljardista kahdestasadastakolmestakymmenestäneljästämiljoonasta viidestäsadastakuudestakymmenestäseitsemästätuhannesta kahdeksastasadastayhdeksästäkymmenestä",  # NOQA
                "miljardiin kahteensataankolmeenkymmeneenneljäänmiljoonaan viiteensataankuuteenkymmeneenseitsemääntuhanteen kahdeksaansataanyhdeksäänkymmeneen",  # NOQA
                "miljardilla kahdellasadallakolmellakymmenelläneljällämiljoonalla viidelläsadallakuudellakymmenelläseitsemällätuhannella kahdeksallasadallayhdeksälläkymmenellä",  # NOQA
                "miljardilta kahdeltasadaltakolmeltakymmeneltäneljältämiljoonalta viideltäsadaltakuudeltakymmeneltäseitsemältätuhannelta kahdeksaltasadaltayhdeksältäkymmeneltä",  # NOQA
                "miljardille kahdellesadallekolmellekymmenelleneljällemiljoonalle viidellesadallekuudellekymmenelleseitsemälletuhannelle kahdeksallesadalleyhdeksällekymmenelle",  # NOQA
                "miljardina kahtenasatanakolmenakymmenenäneljänämiljoonana viitenäsatanakuutenakymmenenäseitsemänätuhantena kahdeksanasatanayhdeksänäkymmenenä",  # NOQA
                "miljardiksi kahdeksisadaksikolmeksikymmeneksineljäksimiljoonaksi viideksisadaksikuudeksikymmeneksiseitsemäksituhanneksi kahdeksaksisadaksiyhdeksäksikymmeneksi",  # NOQA
                "miljardein kaksinsadoinkolmenkymmeninneljinmiljoonin viisinsadoinkuusinkymmeninseitsemintuhansin kahdeksinsadoinyhdeksinkymmenin",  # NOQA
                "miljarditta kahdettasadattakolmettakymmenettäneljättämiljoonatta viidettäsadattakuudettakymmenettäseitsemättätuhannetta kahdeksattasadattayhdeksättäkymmenettä",  # NOQA
                "miljardeine kaksinesatoinekolminekymmenineneljinemiljoonine viisinesatoinekuusinekymmenineseitseminetuhansine kahdeksinesatoineyhdeksinekymmenine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(1234567890, to="cardinal", case=c, plural=True) for c in CASES),
            (
                "miljardit kahdetsadatkolmetkymmenetneljätmiljoonat viidetsadatkuudetkymmenetseitsemättuhannet kahdeksatsadatyhdeksätkymmenet",  # NOQA
                "miljardien kaksiensatojenkolmienkymmenienneljienmiljoonien viisiensatojenkuusienkymmenienseitsemientuhansien kahdeksiensatojenyhdeksienkymmenien",  # NOQA
                "miljardeja kaksiasatojakolmiakymmeniäneljiämiljoonia viisiäsatojakuusiakymmeniäseitsemiätuhansia kahdeksiasatojayhdeksiäkymmeniä",  # NOQA
                "miljardeissa kaksissasadoissakolmissakymmenissäneljissämiljoonissa viisissäsadoissakuusissakymmenissäseitsemissätuhansissa kahdeksissasadoissayhdeksissäkymmenissä",  # NOQA
                "miljardeista kaksistasadoistakolmistakymmenistäneljistämiljoonista viisistäsadoistakuusistakymmenistäseitsemistätuhansista kahdeksistasadoistayhdeksistäkymmenistä",  # NOQA
                "miljardeihin kaksiinsatoihinkolmiinkymmeniinneljiinmiljooniin viisiinsatoihinkuusiinkymmeniinseitsemiintuhansiin kahdeksiinsatoihinyhdeksiinkymmeniin",  # NOQA
                "miljardeilla kaksillasadoillakolmillakymmenilläneljillämiljoonilla viisilläsadoillakuusillakymmenilläseitsemillätuhansilla kahdeksillasadoillayhdeksilläkymmenillä",  # NOQA
                "miljardeilta kaksiltasadoiltakolmiltakymmeniltäneljiltämiljoonilta viisiltäsadoiltakuusiltakymmeniltäseitsemiltätuhansilta kahdeksiltasadoiltayhdeksiltäkymmeniltä",  # NOQA
                "miljardeille kaksillesadoillekolmillekymmenilleneljillemiljoonille viisillesadoillekuusillekymmenilleseitsemilletuhansille kahdeksillesadoilleyhdeksillekymmenille",  # NOQA
                "miljardeina kaksinasatoinakolminakymmeninäneljinämiljoonina viisinäsatoinakuusinakymmeninäseitseminätuhansina kahdeksinasatoinayhdeksinäkymmeninä",  # NOQA
                "miljardeiksi kaksiksisadoiksikolmiksikymmeniksineljiksimiljooniksi viisiksisadoiksikuusiksikymmeniksiseitsemiksituhansiksi kahdeksiksisadoiksiyhdeksiksikymmeniksi",  # NOQA
                "miljardein kaksinsadoinkolminkymmeninneljinmiljoonin viisinsadoinkuusinkymmeninseitsemintuhansin kahdeksinsadoinyhdeksinkymmenin",  # NOQA
                "miljardeitta kaksittasadoittakolmittakymmenittäneljittämiljoonitta viisittäsadoittakuusittakymmenittäseitsemittätuhansitta kahdeksittasadoittayhdeksittäkymmenittä",  # NOQA
                "miljardeine kaksinesatoinekolminekymmenineneljinemiljoonine viisinesatoinekuusinekymmenineseitseminetuhansine kahdeksinesatoineyhdeksinekymmenine"  # NOQA
            )
        )

        # one trillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**2, to="cardinal", case=c) for c in CASES),
            ("biljoona", "biljoonan", "biljoonaa",
             "biljoonassa", "biljoonasta", "biljoonaan",
             "biljoonalla", "biljoonalta", "biljoonalle",
             "biljoonana", "biljoonaksi",
             "biljoonin", "biljoonatta", "biljoonine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**2, to="cardinal", case=c, plural=True) for c in CASES),
            ("biljoonat", "biljoonien", "biljoonia",
             "biljoonissa", "biljoonista", "biljooniin",
             "biljoonilla", "biljoonilta", "biljoonille",
             "biljoonina", "biljooniksi",
             "biljoonin", "biljoonitta", "biljoonine")
        )

        # one quintillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**3, to="cardinal", case=c) for c in CASES),
            ("triljoona", "triljoonan", "triljoonaa",
             "triljoonassa", "triljoonasta", "triljoonaan",
             "triljoonalla", "triljoonalta", "triljoonalle",
             "triljoonana", "triljoonaksi",
             "triljoonin", "triljoonatta", "triljoonine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**3, to="cardinal", case=c, plural=True) for c in CASES),
            ("triljoonat", "triljoonien", "triljoonia",
             "triljoonissa", "triljoonista", "triljooniin",
             "triljoonilla", "triljoonilta", "triljoonille",
             "triljoonina", "triljooniksi",
             "triljoonin", "triljoonitta", "triljoonine")
        )

    def test_high_ord(self):

        # ten thousand
        self.assertEqual(
            tuple(n2f(10000, to="ordinal", case=c) for c in CASES),
            (
                "kymmenestuhannes",
                "kymmenennentuhannennen",
                "kymmenettätuhannetta",
                "kymmenennessätuhannennessa",
                "kymmenennestätuhannennesta",
                "kymmenenteentuhannenteen",
                "kymmenennellätuhannennella",
                "kymmenenneltätuhannennelta",
                "kymmenennelletuhannennelle",
                "kymmenentenätuhannentena",
                "kymmenenneksituhannenneksi",
                "kymmenensintuhannensin",
                "kymmenennettätuhannennetta",
                "kymmenensinetuhannensine"
            )
        )
        self.assertEqual(
            tuple(n2f(10000, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kymmenennettuhannennet",
                "kymmenensientuhannensien",
                "kymmenensiätuhannensia",
                "kymmenensissätuhannensissa",
                "kymmenensistätuhannensista",
                "kymmenensiintuhannensiin",
                "kymmenensillätuhannensilla",
                "kymmenensiltätuhannensilta",
                "kymmenensilletuhannensille",
                "kymmenensinätuhannensina",
                "kymmenensiksituhannensiksi",
                "kymmenensintuhannensin",
                "kymmenensittätuhannensitta",
                "kymmenensinetuhannensine"
            )
        )

        # twelve thousand, three hundred and forty-five
        self.assertEqual(
            tuple(n2f(12345, to="ordinal", case=c) for c in CASES),
            (
                "kahdestoistatuhannes kolmassadasneljäskymmenesviides",
                "kahdennentoistatuhannennen kolmannensadannenneljännenkymmenennenviidennen",  # NOQA
                "kahdettatoistatuhannetta kolmattasadattaneljättäkymmenettäviidettä",  # NOQA
                "kahdennessatoistatuhannennessa kolmannessasadannessaneljännessäkymmenennessäviidennessä",  # NOQA
                "kahdennestatoistatuhannennesta kolmannestasadannestaneljännestäkymmenennestäviidennestä",  # NOQA
                "kahdenteentoistatuhannenteen kolmanteensadanteenneljänteenkymmenenteenviidenteen",  # NOQA
                "kahdennellatoistatuhannennella kolmannellasadannellaneljännelläkymmenennelläviidennellä",  # NOQA
                "kahdenneltatoistatuhannennelta kolmanneltasadanneltaneljänneltäkymmenenneltäviidenneltä",  # NOQA
                "kahdennelletoistatuhannennelle kolmannellesadannelleneljännellekymmenennelleviidennelle",  # NOQA
                "kahdentenatoistatuhannentena kolmantenasadantenaneljäntenäkymmenentenäviidentenä",  # NOQA
                "kahdenneksitoistatuhannenneksi kolmanneksisadanneksineljänneksikymmenenneksiviidenneksi",  # NOQA
                "kahdensintoistatuhannensin kolmansinsadansinneljänsinkymmenensinviidensin",  # NOQA
                "kahdennettatoistatuhannennetta kolmannettasadannettaneljännettäkymmenennettäviidennettä",  # NOQA
                "kahdensinetoistatuhannensine kolmansinesadansineneljänsinekymmenensineviidensine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(12345, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "kahdennettoistatuhannennet kolmannetsadannetneljännetkymmenennetviidennet",  # NOQA
                "kahdensientoistatuhannensien kolmansiensadansienneljänsienkymmenensienviidensien",  # NOQA
                "kahdensiatoistatuhannensia kolmansiasadansianeljänsiäkymmenensiäviidensiä",  # NOQA
                "kahdensissatoistatuhannensissa kolmansissasadansissaneljänsissäkymmenensissäviidensissä",  # NOQA
                "kahdensistatoistatuhannensista kolmansistasadansistaneljänsistäkymmenensistäviidensistä",  # NOQA
                "kahdensiintoistatuhannensiin kolmansiinsadansiinneljänsiinkymmenensiinviidensiin",  # NOQA
                "kahdensillatoistatuhannensilla kolmansillasadansillaneljänsilläkymmenensilläviidensillä",  # NOQA
                "kahdensiltatoistatuhannensilta kolmansiltasadansiltaneljänsiltäkymmenensiltäviidensiltä",  # NOQA
                "kahdensilletoistatuhannensille kolmansillesadansilleneljänsillekymmenensilleviidensille",  # NOQA
                "kahdensinatoistatuhannensina kolmansinasadansinaneljänsinäkymmenensinäviidensinä",  # NOQA
                "kahdensiksitoistatuhannensiksi kolmansiksisadansiksineljänsiksikymmenensiksiviidensiksi",  # NOQA
                "kahdensintoistatuhannensin kolmansinsadansinneljänsinkymmenensinviidensin",  # NOQA
                "kahdensittatoistatuhannensitta kolmansittasadansittaneljänsittäkymmenensittäviidensittä",  # NOQA
                "kahdensinetoistatuhannensine kolmansinesadansineneljänsinekymmenensineviidensine"  # NOQA
            )
        )

        # one hundred thousand
        self.assertEqual(
            tuple(n2f(100000, to="ordinal", case=c) for c in CASES),
            (
                "sadastuhannes",
                "sadannentuhannennen",
                "sadattatuhannetta",
                "sadannessatuhannennessa",
                "sadannestatuhannennesta",
                "sadanteentuhannenteen",
                "sadannellatuhannennella",
                "sadanneltatuhannennelta",
                "sadannelletuhannennelle",
                "sadantenatuhannentena",
                "sadanneksituhannenneksi",
                "sadansintuhannensin",
                "sadannettatuhannennetta",
                "sadansinetuhannensine"
            )
        )
        self.assertEqual(
            tuple(n2f(100000, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "sadannettuhannennet",
                "sadansientuhannensien",
                "sadansiatuhannensia",
                "sadansissatuhannensissa",
                "sadansistatuhannensista",
                "sadansiintuhannensiin",
                "sadansillatuhannensilla",
                "sadansiltatuhannensilta",
                "sadansilletuhannensille",
                "sadansinatuhannensina",
                "sadansiksituhannensiksi",
                "sadansintuhannensin",
                "sadansittatuhannensitta",
                "sadansinetuhannensine"
            )
        )

        # one hundred and twenty-three thousand, four hundred and fifty-six
        self.assertEqual(
            tuple(n2f(123456, to="ordinal", case=c) for c in CASES),
            (
                "sadaskahdeskymmeneskolmastuhannes neljässadasviideskymmeneskuudes",  # NOQA
                "sadannenkahdennenkymmenennenkolmannentuhannennen neljännensadannenviidennenkymmenennenkuudennen",  # NOQA
                "sadattakahdettakymmenettäkolmattatuhannetta neljättäsadattaviidettäkymmenettäkuudetta",  # NOQA
                "sadannessakahdennessakymmenennessäkolmannessatuhannennessa neljännessäsadannessaviidennessäkymmenennessäkuudennessa",  # NOQA
                "sadannestakahdennestakymmenennestäkolmannestatuhannennesta neljännestäsadannestaviidennestäkymmenennestäkuudennesta",  # NOQA
                "sadanteenkahdenteenkymmenenteenkolmanteentuhannenteen neljänteensadanteenviidenteenkymmenenteenkuudenteen",  # NOQA
                "sadannellakahdennellakymmenennelläkolmannellatuhannennella neljännelläsadannellaviidennelläkymmenennelläkuudennella",  # NOQA
                "sadanneltakahdenneltakymmenenneltäkolmanneltatuhannennelta neljänneltäsadanneltaviidenneltäkymmenenneltäkuudennelta",  # NOQA
                "sadannellekahdennellekymmenennellekolmannelletuhannennelle neljännellesadannelleviidennellekymmenennellekuudennelle",  # NOQA
                "sadantenakahdentenakymmenentenäkolmantenatuhannentena neljäntenäsadantenaviidentenäkymmenentenäkuudentena",  # NOQA
                "sadanneksikahdenneksikymmenenneksikolmanneksituhannenneksi neljänneksisadanneksiviidenneksikymmenenneksikuudenneksi",  # NOQA
                "sadansinkahdensinkymmenensinkolmansintuhannensin neljänsinsadansinviidensinkymmenensinkuudensin",  # NOQA
                "sadannettakahdennettakymmenennettäkolmannettatuhannennetta neljännettäsadannettaviidennettäkymmenennettäkuudennetta",  # NOQA
                "sadansinekahdensinekymmenensinekolmansinetuhannensine neljänsinesadansineviidensinekymmenensinekuudensine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(123456, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "sadannetkahdennetkymmenennetkolmannettuhannennet neljännetsadannetviidennetkymmenennetkuudennet",  # NOQA
                "sadansienkahdensienkymmenensienkolmansientuhannensien neljänsiensadansienviidensienkymmenensienkuudensien",  # NOQA
                "sadansiakahdensiakymmenensiäkolmansiatuhannensia neljänsiäsadansiaviidensiäkymmenensiäkuudensia",  # NOQA
                "sadansissakahdensissakymmenensissäkolmansissatuhannensissa neljänsissäsadansissaviidensissäkymmenensissäkuudensissa",  # NOQA
                "sadansistakahdensistakymmenensistäkolmansistatuhannensista neljänsistäsadansistaviidensistäkymmenensistäkuudensista",  # NOQA
                "sadansiinkahdensiinkymmenensiinkolmansiintuhannensiin neljänsiinsadansiinviidensiinkymmenensiinkuudensiin",  # NOQA
                "sadansillakahdensillakymmenensilläkolmansillatuhannensilla neljänsilläsadansillaviidensilläkymmenensilläkuudensilla",  # NOQA
                "sadansiltakahdensiltakymmenensiltäkolmansiltatuhannensilta neljänsiltäsadansiltaviidensiltäkymmenensiltäkuudensilta",  # NOQA
                "sadansillekahdensillekymmenensillekolmansilletuhannensille neljänsillesadansilleviidensillekymmenensillekuudensille",  # NOQA
                "sadansinakahdensinakymmenensinäkolmansinatuhannensina neljänsinäsadansinaviidensinäkymmenensinäkuudensina",  # NOQA
                "sadansiksikahdensiksikymmenensiksikolmansiksituhannensiksi neljänsiksisadansiksiviidensiksikymmenensiksikuudensiksi",  # NOQA
                "sadansinkahdensinkymmenensinkolmansintuhannensin neljänsinsadansinviidensinkymmenensinkuudensin",  # NOQA
                "sadansittakahdensittakymmenensittäkolmansittatuhannensitta neljänsittäsadansittaviidensittäkymmenensittäkuudensitta",  # NOQA
                "sadansinekahdensinekymmenensinekolmansinetuhannensine neljänsinesadansineviidensinekymmenensinekuudensine"  # NOQA
            )
        )

        # one million
        self.assertEqual(
            tuple(n2f(10**6, to="ordinal", case=c) for c in CASES),
            ("miljoonas", "miljoonannen", "miljoonatta",
             "miljoonannessa", "miljoonannesta", "miljoonanteen",
             "miljoonannella", "miljoonannelta", "miljoonannelle",
             "miljoonantena", "miljoonanneksi",
             "miljoonansin", "miljoonannetta", "miljoonansine")
        )
        self.assertEqual(
            tuple(n2f(10**6, to="ordinal", case=c, plural=True) for c in CASES),
            ("miljoonannet", "miljoonansien", "miljoonansia",
             "miljoonansissa", "miljoonansista", "miljoonansiin",
             "miljoonansilla", "miljoonansilta", "miljoonansille",
             "miljoonansina", "miljoonansiksi",
             "miljoonansin", "miljoonansitta", "miljoonansine")
        )

        # one million, two hundred and thirty-four thousand, five hundred and sixty-seven
        self.assertEqual(
            tuple(n2f(1234567, to="ordinal", case=c) for c in CASES),
            (
                "miljoonas kahdessadaskolmaskymmenesneljästuhannes viidessadaskuudeskymmenesseitsemäs",  # NOQA
                "miljoonannen kahdennensadannenkolmannenkymmenennenneljännentuhannennen viidennensadannenkuudennenkymmenennenseitsemännen",  # NOQA
                "miljoonatta kahdettasadattakolmattakymmenettäneljättätuhannetta viidettäsadattakuudettakymmenettäseitsemättä",  # NOQA
                "miljoonannessa kahdennessasadannessakolmannessakymmenennessäneljännessätuhannennessa viidennessäsadannessakuudennessakymmenennessäseitsemännessä",  # NOQA
                "miljoonannesta kahdennestasadannestakolmannestakymmenennestäneljännestätuhannennesta viidennestäsadannestakuudennestakymmenennestäseitsemännestä",  # NOQA
                "miljoonanteen kahdenteensadanteenkolmanteenkymmenenteenneljänteentuhannenteen viidenteensadanteenkuudenteenkymmenenteenseitsemänteen",  # NOQA
                "miljoonannella kahdennellasadannellakolmannellakymmenennelläneljännellätuhannennella viidennelläsadannellakuudennellakymmenennelläseitsemännellä",  # NOQA
                "miljoonannelta kahdenneltasadanneltakolmanneltakymmenenneltäneljänneltätuhannennelta viidenneltäsadanneltakuudenneltakymmenenneltäseitsemänneltä",  # NOQA
                "miljoonannelle kahdennellesadannellekolmannellekymmenennelleneljännelletuhannennelle viidennellesadannellekuudennellekymmenennelleseitsemännelle",  # NOQA
                "miljoonantena kahdentenasadantenakolmantenakymmenentenäneljäntenätuhannentena viidentenäsadantenakuudentenakymmenentenäseitsemäntenä",  # NOQA
                "miljoonanneksi kahdenneksisadanneksikolmanneksikymmenenneksineljänneksituhannenneksi viidenneksisadanneksikuudenneksikymmenenneksiseitsemänneksi",  # NOQA
                "miljoonansin kahdensinsadansinkolmansinkymmenensinneljänsintuhannensin viidensinsadansinkuudensinkymmenensinseitsemänsin",  # NOQA
                "miljoonannetta kahdennettasadannettakolmannettakymmenennettäneljännettätuhannennetta viidennettäsadannettakuudennettakymmenennettäseitsemännettä",  # NOQA
                "miljoonansine kahdensinesadansinekolmansinekymmenensineneljänsinetuhannensine viidensinesadansinekuudensinekymmenensineseitsemänsine"  # NOQA
            )
        )
        self.assertEqual(
            tuple(n2f(1234567, to="ordinal", case=c, plural=True) for c in CASES),
            (
                "miljoonannet kahdennetsadannetkolmannetkymmenennetneljännettuhannennet viidennetsadannetkuudennetkymmenennetseitsemännet",  # NOQA
                "miljoonansien kahdensiensadansienkolmansienkymmenensienneljänsientuhannensien viidensiensadansienkuudensienkymmenensienseitsemänsien",  # NOQA
                "miljoonansia kahdensiasadansiakolmansiakymmenensiäneljänsiätuhannensia viidensiäsadansiakuudensiakymmenensiäseitsemänsiä",  # NOQA
                "miljoonansissa kahdensissasadansissakolmansissakymmenensissäneljänsissätuhannensissa viidensissäsadansissakuudensissakymmenensissäseitsemänsissä",  # NOQA
                "miljoonansista kahdensistasadansistakolmansistakymmenensistäneljänsistätuhannensista viidensistäsadansistakuudensistakymmenensistäseitsemänsistä",  # NOQA
                "miljoonansiin kahdensiinsadansiinkolmansiinkymmenensiinneljänsiintuhannensiin viidensiinsadansiinkuudensiinkymmenensiinseitsemänsiin",  # NOQA
                "miljoonansilla kahdensillasadansillakolmansillakymmenensilläneljänsillätuhannensilla viidensilläsadansillakuudensillakymmenensilläseitsemänsillä",  # NOQA
                "miljoonansilta kahdensiltasadansiltakolmansiltakymmenensiltäneljänsiltätuhannensilta viidensiltäsadansiltakuudensiltakymmenensiltäseitsemänsiltä",  # NOQA
                "miljoonansille kahdensillesadansillekolmansillekymmenensilleneljänsilletuhannensille viidensillesadansillekuudensillekymmenensilleseitsemänsille",  # NOQA
                "miljoonansina kahdensinasadansinakolmansinakymmenensinäneljänsinätuhannensina viidensinäsadansinakuudensinakymmenensinäseitsemänsinä",  # NOQA
                "miljoonansiksi kahdensiksisadansiksikolmansiksikymmenensiksineljänsiksituhannensiksi viidensiksisadansiksikuudensiksikymmenensiksiseitsemänsiksi",  # NOQA
                "miljoonansin kahdensinsadansinkolmansinkymmenensinneljänsintuhannensin viidensinsadansinkuudensinkymmenensinseitsemänsin",  # NOQA
                "miljoonansitta kahdensittasadansittakolmansittakymmenensittäneljänsittätuhannensitta viidensittäsadansittakuudensittakymmenensittäseitsemänsittä",  # NOQA
                "miljoonansine kahdensinesadansinekolmansinekymmenensineneljänsinetuhannensine viidensinesadansinekuudensinekymmenensineseitsemänsine"  # NOQA
            )
        )

        # one billion (short scale)
        self.assertEqual(
            tuple(n2f(10**9, to="ordinal", case=c) for c in CASES),
            ("miljardis", "miljardinnen", "miljarditta",
             "miljardinnessa", "miljardinnesta", "miljardinteen",
             "miljardinnella", "miljardinnelta", "miljardinnelle",
             "miljardintena", "miljardinneksi",
             "miljardinsin", "miljardinnetta", "miljardinsine")
        )
        self.assertEqual(
            tuple(n2f(10**9, to="ordinal", case=c, plural=True) for c in CASES),
            ("miljardinnet", "miljardinsien", "miljardinsia",
             "miljardinsissa", "miljardinsista", "miljardinsiin",
             "miljardinsilla", "miljardinsilta", "miljardinsille",
             "miljardinsina", "miljardinsiksi",
             "miljardinsin", "miljardinsitta", "miljardinsine")
        )

        # one billion, two hundred and thirty-four million,
        # five hundred and sixty-seven thousand, eight hundred and ninety
        # (short scale)
        self.assertEqual(
            tuple(n2f(1234567890, to="ordinal", case=c) for c in CASES),
            ("miljardis kahdessadaskolmaskymmenesneljäsmiljoonas viidessadaskuudeskymmenesseitsemästuhannes kahdeksassadasyhdeksäskymmenes", "miljardinnen kahdennensadannenkolmannenkymmenennenneljännenmiljoonannen viidennensadannenkuudennenkymmenennenseitsemännentuhannennen kahdeksannensadannenyhdeksännenkymmenennen", "miljarditta kahdettasadattakolmattakymmenettäneljättämiljoonatta viidettäsadattakuudettakymmenettäseitsemättätuhannetta kahdeksattasadattayhdeksättäkymmenettä",
             "miljardinnessa kahdennessasadannessakolmannessakymmenennessäneljännessämiljoonannessa viidennessäsadannessakuudennessakymmenennessäseitsemännessätuhannennessa kahdeksannessasadannessayhdeksännessäkymmenennessä", "miljardinnesta kahdennestasadannestakolmannestakymmenennestäneljännestämiljoonannesta viidennestäsadannestakuudennestakymmenennestäseitsemännestätuhannennesta kahdeksannestasadannestayhdeksännestäkymmenennestä", "miljardinteen kahdenteensadanteenkolmanteenkymmenenteenneljänteenmiljoonanteen viidenteensadanteenkuudenteenkymmenenteenseitsemänteentuhannenteen kahdeksanteensadanteenyhdeksänteenkymmenenteen",
             "miljardinnella kahdennellasadannellakolmannellakymmenennelläneljännellämiljoonannella viidennelläsadannellakuudennellakymmenennelläseitsemännellätuhannennella kahdeksannellasadannellayhdeksännelläkymmenennellä", "miljardinnelta kahdenneltasadanneltakolmanneltakymmenenneltäneljänneltämiljoonannelta viidenneltäsadanneltakuudenneltakymmenenneltäseitsemänneltätuhannennelta kahdeksanneltasadanneltayhdeksänneltäkymmenenneltä", "miljardinnelle kahdennellesadannellekolmannellekymmenennelleneljännellemiljoonannelle viidennellesadannellekuudennellekymmenennelleseitsemännelletuhannennelle kahdeksannellesadannelleyhdeksännellekymmenennelle",
             "miljardintena kahdentenasadantenakolmantenakymmenentenäneljäntenämiljoonantena viidentenäsadantenakuudentenakymmenentenäseitsemäntenätuhannentena kahdeksantenasadantenayhdeksäntenäkymmenentenä", "miljardinneksi kahdenneksisadanneksikolmanneksikymmenenneksineljänneksimiljoonanneksi viidenneksisadanneksikuudenneksikymmenenneksiseitsemänneksituhannenneksi kahdeksanneksisadanneksiyhdeksänneksikymmenenneksi",
             "miljardinsin kahdensinsadansinkolmansinkymmenensinneljänsinmiljoonansin viidensinsadansinkuudensinkymmenensinseitsemänsintuhannensin kahdeksansinsadansinyhdeksänsinkymmenensin", "miljardinnetta kahdennettasadannettakolmannettakymmenennettäneljännettämiljoonannetta viidennettäsadannettakuudennettakymmenennettäseitsemännettätuhannennetta kahdeksannettasadannettayhdeksännettäkymmenennettä", "miljardinsine kahdensinesadansinekolmansinekymmenensineneljänsinemiljoonansine viidensinesadansinekuudensinekymmenensineseitsemänsinetuhannensine kahdeksansinesadansineyhdeksänsinekymmenensine")
        )
        self.assertEqual(
            tuple(n2f(1234567890, to="ordinal", case=c, plural=True) for c in CASES),
            ("miljardinnet kahdennetsadannetkolmannetkymmenennetneljännetmiljoonannet viidennetsadannetkuudennetkymmenennetseitsemännettuhannennet kahdeksannetsadannetyhdeksännetkymmenennet", "miljardinsien kahdensiensadansienkolmansienkymmenensienneljänsienmiljoonansien viidensiensadansienkuudensienkymmenensienseitsemänsientuhannensien kahdeksansiensadansienyhdeksänsienkymmenensien", "miljardinsia kahdensiasadansiakolmansiakymmenensiäneljänsiämiljoonansia viidensiäsadansiakuudensiakymmenensiäseitsemänsiätuhannensia kahdeksansiasadansiayhdeksänsiäkymmenensiä",
             "miljardinsissa kahdensissasadansissakolmansissakymmenensissäneljänsissämiljoonansissa viidensissäsadansissakuudensissakymmenensissäseitsemänsissätuhannensissa kahdeksansissasadansissayhdeksänsissäkymmenensissä", "miljardinsista kahdensistasadansistakolmansistakymmenensistäneljänsistämiljoonansista viidensistäsadansistakuudensistakymmenensistäseitsemänsistätuhannensista kahdeksansistasadansistayhdeksänsistäkymmenensistä", "miljardinsiin kahdensiinsadansiinkolmansiinkymmenensiinneljänsiinmiljoonansiin viidensiinsadansiinkuudensiinkymmenensiinseitsemänsiintuhannensiin kahdeksansiinsadansiinyhdeksänsiinkymmenensiin",
             "miljardinsilla kahdensillasadansillakolmansillakymmenensilläneljänsillämiljoonansilla viidensilläsadansillakuudensillakymmenensilläseitsemänsillätuhannensilla kahdeksansillasadansillayhdeksänsilläkymmenensillä", "miljardinsilta kahdensiltasadansiltakolmansiltakymmenensiltäneljänsiltämiljoonansilta viidensiltäsadansiltakuudensiltakymmenensiltäseitsemänsiltätuhannensilta kahdeksansiltasadansiltayhdeksänsiltäkymmenensiltä", "miljardinsille kahdensillesadansillekolmansillekymmenensilleneljänsillemiljoonansille viidensillesadansillekuudensillekymmenensilleseitsemänsilletuhannensille kahdeksansillesadansilleyhdeksänsillekymmenensille",
             "miljardinsina kahdensinasadansinakolmansinakymmenensinäneljänsinämiljoonansina viidensinäsadansinakuudensinakymmenensinäseitsemänsinätuhannensina kahdeksansinasadansinayhdeksänsinäkymmenensinä", "miljardinsiksi kahdensiksisadansiksikolmansiksikymmenensiksineljänsiksimiljoonansiksi viidensiksisadansiksikuudensiksikymmenensiksiseitsemänsiksituhannensiksi kahdeksansiksisadansiksiyhdeksänsiksikymmenensiksi",
             "miljardinsin kahdensinsadansinkolmansinkymmenensinneljänsinmiljoonansin viidensinsadansinkuudensinkymmenensinseitsemänsintuhannensin kahdeksansinsadansinyhdeksänsinkymmenensin", "miljardinsitta kahdensittasadansittakolmansittakymmenensittäneljänsittämiljoonansitta viidensittäsadansittakuudensittakymmenensittäseitsemänsittätuhannensitta kahdeksansittasadansittayhdeksänsittäkymmenensittä", "miljardinsine kahdensinesadansinekolmansinekymmenensineneljänsinemiljoonansine viidensinesadansinekuudensinekymmenensineseitsemänsinetuhannensine kahdeksansinesadansineyhdeksänsinekymmenensine")
        )

        # one trillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**2, to="ordinal", case=c) for c in CASES),
            ("biljoonas", "biljoonannen", "biljoonatta",
             "biljoonannessa", "biljoonannesta", "biljoonanteen",
             "biljoonannella", "biljoonannelta", "biljoonannelle",
             "biljoonantena", "biljoonanneksi",
             "biljoonansin", "biljoonannetta", "biljoonansine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**2, to="ordinal", case=c, plural=True) for c in CASES),
            ("biljoonannet", "biljoonansien", "biljoonansia",
             "biljoonansissa", "biljoonansista", "biljoonansiin",
             "biljoonansilla", "biljoonansilta", "biljoonansille",
             "biljoonansina", "biljoonansiksi",
             "biljoonansin", "biljoonansitta", "biljoonansine")
        )

        # one quintillion (short scale)
        self.assertEqual(
            tuple(n2f((10**6)**3, to="ordinal", case=c) for c in CASES),
            ("triljoonas", "triljoonannen", "triljoonatta",
             "triljoonannessa", "triljoonannesta", "triljoonanteen",
             "triljoonannella", "triljoonannelta", "triljoonannelle",
             "triljoonantena", "triljoonanneksi",
             "triljoonansin", "triljoonannetta", "triljoonansine")
        )
        self.assertEqual(
            tuple(n2f((10**6)**3, to="ordinal", case=c, plural=True) for c in CASES),
            ("triljoonannet", "triljoonansien", "triljoonansia",
             "triljoonansissa", "triljoonansista", "triljoonansiin",
             "triljoonansilla", "triljoonansilta", "triljoonansille",
             "triljoonansina", "triljoonansiksi",
             "triljoonansin", "triljoonansitta", "triljoonansine")
        )

    def test_year(self):
        self.assertEqual(n2f(2018, to="year"), "kaksituhattakahdeksantoista")
        self.assertEqual(
            n2f(-99, to="year"),
            "yhdeksänkymmentäyhdeksän ennen ajanlaskun alkua")

    def test_currency(self):
        self.assertEqual(
            n2f(150, to="currency"), "yksi euro ja viisikymmentä senttiä")
        self.assertEqual(
            n2f(150, to="currency", currency="FIM", adjective=True),
            "yksi Suomen markka ja viisikymmentä penniä")


if __name__ == '__main__':
    print(create_test(int(sys.argv[1]), sys.argv[2]))
