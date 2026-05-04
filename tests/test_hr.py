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


class Num2WordsHRTest(TestCase):

    def test_cardinal(self):
        self.assertEqual("sto", num2words(100, lang='hr'))
        self.assertEqual("sto jedan", num2words(101, lang='hr'))
        self.assertEqual("sto deset", num2words(110, lang='hr'))
        self.assertEqual("sto petnaest", num2words(115, lang='hr'))
        self.assertEqual(
            "sto dvadeset tri", num2words(123, lang='hr')
        )
        self.assertEqual(
            "jedna tisuća", num2words(1000, lang='hr')
        )
        self.assertEqual(
            "jedna tisuća jedan", num2words(1001, lang='hr')
        )
        self.assertEqual(
            "dvije tisuće dvanaest", num2words(2012, lang='hr')
        )
        self.assertEqual(
            "dvanaest tisuća petsto devetnaest zarez osamdeset pet",
            num2words(12519.85, lang='hr')
        )
        self.assertEqual(
            "jedna milijarda dvjesto trideset četiri milijuna petsto "
            "šezdeset sedam tisuća osamsto devedeset",
            num2words(1234567890, lang='hr')
        )
        self.assertEqual(
            "dvjesto petnaest kvintilijuna četiristo šezdeset jedna "
            "kvadrilijarda četiristo sedam kvadrilijuna osamsto devedeset "
            "dvije trilijarde trideset devet trilijuna dvije bilijarde "
            "sto pedeset sedam bilijuna sto osamdeset devet milijardi "
            "osamsto osamdeset tri milijuna devetsto jedna tisuća "
            "šesto sedamdeset šest",
            num2words(215461407892039002157189883901676, lang='hr')
        )
        self.assertEqual("pet", num2words(5, lang='hr'))
        self.assertEqual("petnaest", num2words(15, lang='hr'))
        self.assertEqual("sto pedeset četiri", num2words(154, lang='hr'))
        self.assertEqual(
            "jedna tisuća sto trideset pet",
            num2words(1135, lang='hr')
        )
        self.assertEqual(
            "četiristo osamnaest tisuća petsto trideset jedan",
            num2words(418531, lang='hr'),
        )
        self.assertEqual(
            "jedan milijun sto trideset devet",
            num2words(1000139, lang='hr')
        )

    def test_floating_point(self):
        self.assertEqual("pet zarez dva", num2words(5.2, lang='hr'))
        self.assertEqual(
            num2words(10.02, lang='hr'),
            "deset zarez nula dva"
        )
        self.assertEqual(
            num2words(15.007, lang='hr'),
            "petnaest zarez nula nula sedam"
        )
        self.assertEqual(
            "petsto šezdeset jedan zarez četrdeset dva",
            num2words(561.42, lang='hr')
        )

    def test_to_ordinal(self):
        # ones — irregular forms
        self.assertEqual("prvi", num2words(1, lang='hr', to='ordinal'))
        self.assertEqual("drugi", num2words(2, lang='hr', to='ordinal'))
        self.assertEqual("treći", num2words(3, lang='hr', to='ordinal'))
        self.assertEqual("četvrti", num2words(4, lang='hr', to='ordinal'))
        # ones — regular
        self.assertEqual("peti", num2words(5, lang='hr', to='ordinal'))
        self.assertEqual("šesti", num2words(6, lang='hr', to='ordinal'))
        self.assertEqual("sedmi", num2words(7, lang='hr', to='ordinal'))
        self.assertEqual("osmi", num2words(8, lang='hr', to='ordinal'))
        self.assertEqual("deveti", num2words(9, lang='hr', to='ordinal'))
        # tens
        self.assertEqual("deseti", num2words(10, lang='hr', to='ordinal'))
        self.assertEqual(
            "sedamnaesti", num2words(17, lang='hr', to='ordinal')
        )
        self.assertEqual(
            "dvadeseti", num2words(20, lang='hr', to='ordinal')
        )
        # compound — only last word becomes ordinal
        self.assertEqual(
            "dvadeset prvi", num2words(21, lang='hr', to='ordinal')
        )
        self.assertEqual(
            "trideset peti", num2words(35, lang='hr', to='ordinal')
        )
        # hundreds
        self.assertEqual("stoti", num2words(100, lang='hr', to='ordinal'))
        self.assertEqual(
            "sto prvi", num2words(101, lang='hr', to='ordinal')
        )
        self.assertEqual(
            "sto dvadeset peti", num2words(125, lang='hr', to='ordinal')
        )
        # thousand — exact 10^k uses dedicated form
        self.assertEqual(
            "tisućiti", num2words(1000, lang='hr', to='ordinal')
        )
        self.assertEqual(
            "milijunti", num2words(1_000_000, lang='hr', to='ordinal')
        )
        # year-shaped numbers as masculine ordinals
        self.assertEqual(
            "jedna tisuća devetsto osamdeset šesti",
            num2words(1986, lang='hr', to='ordinal')
        )
        self.assertEqual(
            "dvije tisuće dvadeset četvrti",
            num2words(2024, lang='hr', to='ordinal')
        )

    def test_to_year(self):
        # 1000-1999 collapse "jedna tisuća" → "tisuću" and apply fem-gen ending
        self.assertEqual(
            "tisuću devetsto osamdeset šeste",
            num2words(1986, lang='hr', to='year')
        )
        self.assertEqual(
            "tisuću devetsto četrdeset osme",
            num2words(1948, lang='hr', to='year')
        )
        # 2000+ keeps "dvije tisuće ..." prefix; last word still feminine genitive
        self.assertEqual(
            "dvije tisuće dvadeset četvrte",
            num2words(2024, lang='hr', to='year')
        )
        self.assertEqual(
            "dvije tisuće trinaeste",
            num2words(2013, lang='hr', to='year')
        )
        # Round years
        self.assertEqual(
            "dvije tisuće",
            num2words(2000, lang='hr', to='year')
        )

    def test_to_currency(self):
        self.assertEqual(
            'jedan euro, nula centi',
            num2words(1.0, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, nula centi',
            num2words(2.0, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'pet eura, nula centi',
            num2words(5.0, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, jedan cent',
            num2words(2.01, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, dva centa',
            num2words(2.02, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'dva eura, pet centi',
            num2words(2.05, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'jedna kuna, nula lipa',
            num2words(1.0, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvije kune, jedna lipa',
            num2words(2.01, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvije kune, dvije lipe',
            num2words(2.02, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'pet kuna, pet lipa',
            num2words(5.05, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'jedanaest kuna, jedanaest lipa',
            num2words(11.11, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvadeset jedna kuna, dvadeset jedna lipa',
            num2words(21.21, lang='hr', to='currency', currency='HRK')
        )
        self.assertEqual(
            'dvadeset jedan euro, dvadeset jedan cent',
            num2words(21.21, lang='hr', to='currency', currency='EUR')
        )
        self.assertEqual(
            'jedna tisuća dvjesto trideset četiri eura, '
            'pedeset šest centi',
            num2words(
                1234.56, lang='hr', to='currency', currency='EUR'
            )
        )
        self.assertEqual(
            'sto jedan euro i jedanaest centi',
            num2words(
                10111,
                lang='hr',
                to='currency',
                currency='EUR',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna kuna i dvadeset jedna lipa',
            num2words(
                10121,
                lang='hr',
                to='currency',
                currency='HRK',
                separator=' i'
            )
        )
        self.assertEqual(
            'sto jedna kuna i dvadeset dvije lipe',
            num2words(10122, lang='hr', to='currency', currency='HRK',
                      separator=' i')
        )
        self.assertEqual(
            'sto jedan euro i dvadeset jedan cent',
            num2words(10121, lang='hr', to='currency', currency='EUR',
                      separator=' i'),
        )
        self.assertEqual(
            'minus dvanaest tisuća petsto devetnaest eura, 85 centi',
            num2words(
                -1251985,
                lang='hr',
                to='currency',
                currency='EUR',
                cents=False
            )
        )
        self.assertEqual(
            "trideset osam eura i 40 centi",
            num2words('38.4', lang='hr', to='currency', separator=' i',
                      cents=False, currency='EUR'),
        )