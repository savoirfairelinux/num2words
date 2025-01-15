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


class Num2WordsLVTest(TestCase):
    def test_to_cardinal(self):
        self.assertEqual(num2words(100, lang='lv'), 'simts')
        self.assertEqual(num2words(101, lang='lv'), 'simtu viens')
        self.assertEqual(num2words(110, lang='lv'), 'simts desmit')
        self.assertEqual(num2words(115, lang='lv'), 'simts piecpadsmit')
        self.assertEqual(num2words(123, lang='lv'), 'simts divdesmit trīs')
        self.assertEqual(num2words(1000, lang='lv'), 'tūkstotis')
        self.assertEqual(num2words(1001, lang='lv'), 'tūkstotis viens')
        self.assertEqual(num2words(2012, lang='lv'),
                         'divi tūkstoši divpadsmit')
        self.assertEqual(
            num2words(1234567890, lang='lv'),
            'miljards divi simti trīsdesmit četri miljoni pieci simti '
            'sešdesmit septiņi tūkstoši astoņi simti deviņdesmit')
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='lv'),
            'divi simti piecpadsmit nontiljoni četri simti sešdesmit '
            'viens oktiljons četri simti septiņi septiljoni astoņi '
            'simti deviņdesmit divi sikstiljoni trīsdesmit deviņi '
            'kvintiljoni divi kvadriljoni simts piecdesmit septiņi '
            'triljoni simts astoņdesmit deviņi miljardi astoņi simti '
            'astoņdesmit trīs miljoni deviņi simti viens tūkstotis '
            'seši simti septiņdesmit seši')
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='lv'),
            'septiņi simti deviņpadsmit nontiljoni deviņdesmit četri '
            'oktiljoni divi simti trīsdesmit četri septiljoni seši simti '
            'deviņdesmit trīs sikstiljoni seši simti sešdesmit trīs '
            'kvintiljoni trīsdesmit četri kvadriljoni astoņi simti '
            'divdesmit divi triljoni astoņi simti divdesmit četri '
            'miljardi trīs simti astoņdesmit četri miljoni divi simti '
            'divdesmit tūkstoši divi simti deviņdesmit viens')
        self.assertEqual(
            num2words(-5000, lang='lv'),
            'mīnus pieci tūkstoši',
        )
        self.assertEqual(
            num2words(-5000.22, lang='lv'),
            'mīnus pieci tūkstoši komats divdesmit divi',
        )
        self.assertEqual(
            num2words(10.02, lang='lv'),
            "desmit komats nulle divi"
        )
        self.assertEqual(
            num2words(15.007, lang='lv'),
            "piecpadsmit komats nulle nulle septiņi"
        )

        self.assertEqual(num2words(0, lang='lv'), 'nulle')
        self.assertEqual(num2words(5, lang='lv'), "pieci")
        self.assertEqual(num2words(15, lang='lv'), "piecpadsmit")
        self.assertEqual(num2words(154, lang='lv'), "simts piecdesmit četri")
        self.assertEqual(num2words(101, lang='lv'), "simtu viens")
        self.assertEqual(
            num2words(1135, lang='lv'), "tūkstotis simts trīsdesmit pieci"
        )
        self.assertEqual(
            num2words(418531, lang='lv'),
            "četri simti astoņpadsmit tūkstoši pieci simti trīsdesmit viens"
        )
        self.assertEqual(
            num2words(1000139, lang='lv'),
            "miljons simts trīsdesmit deviņi"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='lv', to='ordinal')

    def test_to_currency(self):
        self.assertEqual(
            num2words(1.0, lang='lv', to='currency', currency='EUR'),
            "viens eiro, nulle centu"
        )
        self.assertEqual(
            num2words(1.0, lang='lv', to='currency', currency='LVL'),
            "viens lats, nulle santīmu"
        )
        self.assertEqual(
            num2words(1234.56, lang='lv', to='currency', currency='EUR'),
            "tūkstotis divi simti trīsdesmit četri eiro, piecdesmit seši centi"
        )
        self.assertEqual(
            num2words(1234.56, lang='lv', to='currency', currency='LVL'),
            "tūkstotis divi simti trīsdesmit četri lati, "
            "piecdesmit seši santīmi"
        )

        self.assertEqual(
            num2words(10111, lang='lv', to='currency', separator=' un',
                      currency='EUR'),
            "simtu viens eiro un vienpadsmit centi"
        )
        self.assertEqual(
            num2words(10121, lang='lv', to='currency', separator=' un',
                      currency='LVL'),
            "simtu viens lats un divdesmit viens santīms"
        )
        self.assertEqual(
            num2words(-1251985, lang='lv', to='currency', cents=False,
                      currency='EUR'),
            "mīnus divpadsmit tūkstoši pieci simti deviņpadsmit eiro,"
            " 85 centi"
        )
        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', separator=' un',
                      cents=False, currency='EUR'),
            "trīsdesmit astoņi eiro un 40 centi"
        )

        # EUR legal form
        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', separator=' un',
                      cents=False, currency='EUR_LEGAL'),
            "trīsdesmit astoņi euro un 40 centi"
        )

        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', separator=' un',
                      cents=False, currency='USD', adjective=False),
            "trīsdesmit astoņi dolāri un 40 centi"
        )

        self.assertEqual(
            num2words('38.4', lang='lv', to='currency', separator=' un',
                      cents=False, currency='USD', adjective=True),
            "trīsdesmit astoņi ASV dolāri un 40 centi"
        )

    def test_fractions(self):
        self.assertEqual(num2words(5.2, lang='lv'), "pieci komats divi")
        self.assertEqual(
            num2words(561.42, lang='lv'),
            "pieci simti sešdesmit viens komats četrdesmit divi"
        )
