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
        self.assertEqual('nulltais', num2words(0, lang='lv', to='ordinal'))
        self.assertEqual('pirmais', num2words(1, lang='lv', to='ordinal'))
        self.assertEqual('otrais', num2words(2, lang='lv', to='ordinal'))
        self.assertEqual('trešais', num2words(3, lang='lv', to='ordinal'))
        self.assertEqual('ceturtais', num2words(4, lang='lv', to='ordinal'))
        self.assertEqual('piektais', num2words(5, lang='lv', to='ordinal'))
        self.assertEqual('sestais', num2words(6, lang='lv', to='ordinal'))
        self.assertEqual('septītais', num2words(7, lang='lv', to='ordinal'))
        self.assertEqual('astotais', num2words(8, lang='lv', to='ordinal'))
        self.assertEqual('devītais', num2words(9, lang='lv', to='ordinal'))
        self.assertEqual('desmitais', num2words(10, lang='lv', to='ordinal'))
        self.assertEqual('vienpadsmitais', num2words(11, lang='lv', to='ordinal'))
        self.assertEqual('divpadsmitais', num2words(12, lang='lv', to='ordinal'))
        self.assertEqual('trīspadsmitais', num2words(13, lang='lv', to='ordinal'))
        self.assertEqual('četrpadsmitais', num2words(14, lang='lv', to='ordinal'))
        self.assertEqual('piecpadsmitais', num2words(15, lang='lv', to='ordinal'))
        self.assertEqual('sešpadsmitais', num2words(16, lang='lv', to='ordinal'))
        self.assertEqual('septiņpadsmitais', num2words(17, lang='lv', to='ordinal'))
        self.assertEqual('astoņpadsmitais', num2words(18, lang='lv', to='ordinal'))
        self.assertEqual('deviņpadsmitais', num2words(19, lang='lv', to='ordinal'))
        self.assertEqual('divdesmitais', num2words(20, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit pirmais', num2words(21, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit otrais', num2words(22, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit trešais', num2words(23, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit ceturtais', num2words(24, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit piektais', num2words(25, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit sestais', num2words(26, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit septītais', num2words(27, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit astotais', num2words(28, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit devītais', num2words(29, lang='lv', to='ordinal'))
        self.assertEqual('trīsdesmitais', num2words(30, lang='lv', to='ordinal'))
        self.assertEqual('trīsdesmit pirmais', num2words(31, lang='lv', to='ordinal'))
        self.assertEqual('trīsdesmit devītais', num2words(39, lang='lv', to='ordinal'))
        self.assertEqual('četrdesmitais', num2words(40, lang='lv', to='ordinal'))
        self.assertEqual('piecdesmitais', num2words(50, lang='lv', to='ordinal'))
        self.assertEqual('sešdesmitais', num2words(60, lang='lv', to='ordinal'))
        self.assertEqual('septiņdesmitais', num2words(70, lang='lv', to='ordinal'))
        self.assertEqual('astoņdesmitais', num2words(80, lang='lv', to='ordinal'))
        self.assertEqual('deviņdesmitais', num2words(90, lang='lv', to='ordinal'))
        self.assertEqual('deviņdesmit devītais', num2words(99, lang='lv', to='ordinal'))
        self.assertEqual('simtais', num2words(100, lang='lv', to='ordinal'))
        self.assertEqual('simts pirmais', num2words(101, lang='lv', to='ordinal'))
        self.assertEqual('divsimtais', num2words(200, lang='lv', to='ordinal'))
        self.assertEqual('trīssimtais', num2words(300, lang='lv', to='ordinal'))
        self.assertEqual('četrsimtais', num2words(400, lang='lv', to='ordinal'))
        self.assertEqual('piecsimtais', num2words(500, lang='lv', to='ordinal'))
        self.assertEqual('sešsimtais', num2words(600, lang='lv', to='ordinal'))
        self.assertEqual('septiņsimtais', num2words(700, lang='lv', to='ordinal'))
        self.assertEqual('astoņsimtais', num2words(800, lang='lv', to='ordinal'))
        self.assertEqual('deviņsimtais', num2words(900, lang='lv', to='ordinal'))
        self.assertEqual('simts pirmais', num2words(101, lang='lv', to='ordinal'))
        self.assertEqual('simts vienpadsmitais', num2words(111, lang='lv', to='ordinal'))
        self.assertEqual('simts divdesmitais', num2words(120, lang='lv', to='ordinal'))
        self.assertEqual('simts trīsdesmit ceturtais', num2words(134, lang='lv', to='ordinal'))
        self.assertEqual('divi simti četrdesmitais', num2words(240, lang='lv', to='ordinal'))
        self.assertEqual('septiņi simti piecdesmit septītais', num2words(757, lang='lv', to='ordinal'))
        self.assertEqual('tūkstošais', num2words(1000, lang='lv', to='ordinal'))
        self.assertEqual('miljonais', num2words(1000000, lang='lv', to='ordinal'))
        self.assertEqual('divi tūkstošais', num2words(2000, lang='lv', to='ordinal'))
        self.assertEqual('deviņi tūkstošais', num2words(9000, lang='lv', to='ordinal'))
        self.assertEqual('tūkstotis pirmais', num2words(1001, lang='lv', to='ordinal'))
        self.assertEqual('tūkstotis septītais', num2words(1007, lang='lv', to='ordinal'))
        self.assertEqual('tūkstotis desmitais', num2words(1010, lang='lv', to='ordinal'))
        self.assertEqual('tūkstotis vienpadsmitais', num2words(1011, lang='lv', to='ordinal'))
        self.assertEqual('tūkstotis septiņpadsmitais', num2words(1017, lang='lv', to='ordinal'))
        self.assertEqual('tūkstotis divdesmitais', num2words(1020, lang='lv', to='ordinal'))
        self.assertEqual('divi tūkstoši pieci simti četrdesmitais', num2words(2540, lang='lv', to='ordinal'))
        self.assertEqual('trīs tūkstoši septiņi simti piecdesmit trešais', num2words(3753, lang='lv', to='ordinal'))
        self.assertEqual('desmit tūkstošais', num2words(10000, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit tūkstošais', num2words(20000, lang='lv', to='ordinal'))
        self.assertEqual('divdesmit divi tūkstošais', num2words(22000, lang='lv', to='ordinal'))
        self.assertEqual('trīsdesmit četri tūkstoši piecsimtais', num2words(34500, lang='lv', to='ordinal'))
        self.assertEqual('četrdesmit septiņi tūkstoši trīs simti divdesmitais',
                         num2words(47320, lang='lv', to='ordinal'))
        self.assertEqual('deviņdesmit astoņi tūkstoši septiņi simti sešdesmit piektais',
                         num2words(98765, lang='lv', to='ordinal'))
        self.assertEqual('simts tūkstošais', num2words(100000, lang='lv', to='ordinal'))
        self.assertEqual('simts tūkstoši vienpadsmitais', num2words(100011, lang='lv', to='ordinal'))
        self.assertEqual('trīs simti četrdesmit pieci tūkstoši vienpadsmitais',
                         num2words(345011, lang='lv', to='ordinal'))
        self.assertEqual('četri simti piecdesmit seši tūkstoši divi simti trīsdesmit trešais',
                         num2words(456233, lang='lv', to='ordinal'))
        self.assertEqual('miljons pirmais', num2words(1000001, lang='lv', to='ordinal'))
        self.assertEqual('divi miljonais', num2words(2000000, lang='lv', to='ordinal'))
        self.assertEqual('deviņi miljonais', num2words(9000000, lang='lv', to='ordinal'))
        self.assertEqual('deviņi miljoni astoņi simti septiņdesmit seši tūkstoši pieci simti četrdesmit trešais',
                         num2words(9876543, lang='lv', to='ordinal'))


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
