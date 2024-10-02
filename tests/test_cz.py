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


class Num2WordsCZTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='cz'), "sto")
        self.assertEqual(num2words(101, lang='cz'), "sto jedna")
        self.assertEqual(num2words(110, lang='cz'), "sto deset")
        self.assertEqual(num2words(115, lang='cz'), "sto patnáct")
        self.assertEqual(num2words(123, lang='cz'), "sto dvacet tři")
        self.assertEqual(num2words(1000, lang='cz'), "tisíc")
        self.assertEqual(num2words(1001, lang='cz'), "tisíc jedna")
        self.assertEqual(num2words(2012, lang='cz'), "dva tisíce dvanáct")
        self.assertEqual(
            num2words(10.02, lang='cz'),
            "deset celá nula dva"
        )
        self.assertEqual(
            num2words(15.007, lang='cz'),
            "patnáct celá nula nula sedm"
        )
        self.assertEqual(
            num2words(12519.85, lang='cz'),
            "dvanáct tisíc pětset devatenáct celá osmdesát pět"
        )
        self.assertEqual(
            num2words(123.50, lang='cz'),
            "sto dvacet tři celá pět"
        )
        self.assertEqual(
            num2words(1234567890, lang='cz'),
            "miliarda dvěstě třicet čtyři miliony pětset šedesát "
            "sedm tisíc osmset devadesát"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='cz'),
            "dvěstě patnáct quintillionů čtyřista šedesát jedna kvadriliard "
            "čtyřista sedm kvadrilionů osmset devadesát dva triliardy třicet "
            "devět trilionů dva biliardy sto padesát sedm bilionů sto "
            "osmdesát devět miliard osmset osmdesát tři miliony "
            "devětset jedna tisíc šestset sedmdesát šest"
        )
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='cz'),
            "sedmset devatenáct quintillionů devadesát "
            "čtyři kvadriliardy dvěstě třicet čtyři "
            "kvadriliony šestset devadesát tři triliardy "
            "šestset šedesát tři triliony třicet čtyři biliardy osmset "
            "dvacet dva biliony osmset dvacet čtyři "
            "miliardy třista osmdesát čtyři miliony dvěstě dvacet "
            "tisíc dvěstě devadesát jedna"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='cz', to='ordinal')

    def test_currency(self):
        self.assertEqual(
            num2words(10.0, lang='cz', to='currency', currency='EUR'),
            "deset euro, nula centů")
        self.assertEqual(
            num2words(1.0, lang='cz', to='currency', currency='CZK'),
            "jedna koruna, nula haléřů")
        self.assertEqual(
            num2words(1234.56, lang='cz', to='currency', currency='EUR'),
            "tisíc dvěstě třicet čtyři euro, padesát šest centů")
        self.assertEqual(
            num2words(1234.56, lang='cz', to='currency', currency='CZK'),
            "tisíc dvěstě třicet čtyři koruny, padesát šest haléřů")
        self.assertEqual(
            num2words(101.11, lang='cz', to='currency', currency='EUR',
                      separator=' a'),
            "sto jedna euro a jedenáct centů")
        self.assertEqual(
            num2words(101.21, lang='cz', to='currency', currency='CZK',
                      separator=' a'),
            "sto jedna korun a dvacet jedna haléřů"
        )
        self.assertEqual(
            num2words(-12519.85, lang='cz', to='currency', cents=False),
            "mínus dvanáct tisíc pětset devatenáct euro, 85 centů"
        )
        self.assertEqual(
            num2words(123.50, lang='cz', to='currency', currency='CZK',
                      separator=' a'),
            "sto dvacet tři koruny a padesát haléřů"
        )
        self.assertEqual(
            num2words(19.50, lang='cz', to='currency', cents=False),
            "devatenáct euro, 50 centů"
        )
