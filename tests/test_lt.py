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


class Num2WordsLTTest(TestCase):
    def test_to_cardinal(self):
        self.assertEqual(num2words(100, lang='lt'), 'vienas šimtas')
        self.assertEqual(num2words(101, lang='lt'), 'vienas šimtas vienas')
        self.assertEqual(num2words(110, lang='lt'), 'vienas šimtas dešimt')
        self.assertEqual(num2words(115, lang='lt'),
                         'vienas šimtas penkiolika')
        self.assertEqual(num2words(123, lang='lt'),
                         'vienas šimtas dvidešimt trys')
        self.assertEqual(num2words(1000, lang='lt'), 'vienas tūkstantis')
        self.assertEqual(num2words(1001, lang='lt'),
                         'vienas tūkstantis vienas')
        self.assertEqual(num2words(2012, lang='lt'),
                         'du tūkstančiai dvylika')
        self.assertEqual(
            num2words(1234567890, lang='lt'),
            "vienas milijardas du šimtai trisdešimt keturi milijonai "
            "penki šimtai šešiasdešimt septyni tūkstančiai aštuoni šimtai "
            "devyniasdešimt")
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='lt'),
            "du šimtai penkiolika naintilijonų keturi šimtai šešiasdešimt "
            "vienas oktilijonas keturi šimtai septyni septilijonai aštuoni "
            "šimtai devyniasdešimt du sikstilijonai trisdešimt devyni "
            "kvintilijonai du kvadrilijonai vienas šimtas penkiasdešimt "
            "septyni trilijonai vienas šimtas aštuoniasdešimt devyni "
            "milijardai aštuoni šimtai aštuoniasdešimt trys milijonai "
            "devyni šimtai vienas tūkstantis šeši šimtai "
            "septyniasdešimt šeši")
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='lt'),
            "septyni šimtai devyniolika naintilijonų devyniasdešimt keturi "
            "oktilijonai du šimtai trisdešimt keturi septilijonai šeši "
            "šimtai devyniasdešimt trys sikstilijonai šeši šimtai "
            "šešiasdešimt trys kvintilijonai trisdešimt keturi kvadrilijonai "
            "aštuoni šimtai dvidešimt du trilijonai aštuoni šimtai dvidešimt "
            "keturi milijardai trys šimtai aštuoniasdešimt keturi milijonai "
            "du šimtai dvidešimt tūkstančių du šimtai devyniasdešimt vienas")
        self.assertEqual(
            num2words(-5000, lang='lt'),
            'minus penki tūkstančiai',
        )
        self.assertEqual(
            num2words(-5000.22, lang='lt'),
            'minus penki tūkstančiai kablelis dvidešimt du',
        )
        self.assertEqual(
            num2words(10.02, lang='lt'),
            "dešimt kablelis nulis du"
        )
        self.assertEqual(
            num2words(15.007, lang='lt'),
            "penkiolika kablelis nulis nulis septyni"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='lt', to='ordinal')

    def test_to_currency(self):
        # Test all available currency forms.
        # LTL
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='LTL'),
            'vienas litas, nulis centų'
        )
        self.assertEqual(
            num2words(10.01, lang='lt', to='currency', currency='LTL'),
            'dešimt litų, vienas centas'
        )
        self.assertEqual(
            num2words(1234.56, lang='lt', to='currency', currency='LTL'),
            'vienas tūkstantis du šimtai trisdešimt keturi litai, '
            'penkiasdešimt šeši centai'
        )
        # EUR
        self.assertEqual(
            num2words(-1251981, lang='lt', to='currency', currency='EUR',
                      cents=False),
            'minus dvylika tūkstančių penki šimtai devyniolika eurų, '
            '81 centas'
        )
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='EUR'),
            'vienas euras, nulis centų'
        )
        self.assertEqual(
            num2words(1234.56, lang='lt', to='currency', currency='EUR'),
            'vienas tūkstantis du šimtai trisdešimt keturi eurai, '
            'penkiasdešimt šeši centai'
        )
        self.assertEqual(
            num2words(1122.22, lang='lt', to='currency', currency='EUR'),
            'vienas tūkstantis vienas šimtas dvidešimt du eurai, '
            'dvidešimt du centai'
        )
        # USD
        self.assertEqual(
            num2words(-1281, lang='lt', to='currency', currency='USD',
                      cents=False),
            'minus dvylika dolerių, 81 centas'
        )
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='USD'),
            'vienas doleris, nulis centų'
        )
        self.assertEqual(
            num2words(5.06, lang='lt', to='currency', currency='USD'),
            'penki doleriai, šeši centai'
        )
        # GBP
        self.assertEqual(
            num2words(-1281, lang='lt', to='currency', currency='GBP',
                      cents=False),
            'minus dvylika svarų sterlingų, 81 pensas'
        )
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='GBP'),
            'vienas svaras sterlingų, nulis pensų'
        )
        self.assertEqual(
            num2words(5.06, lang='lt', to='currency', currency='GBP'),
            'penki svarai sterlingų, šeši pensai'
        )
        # PLN
        self.assertEqual(
            num2words(-1281, lang='lt', to='currency', currency='PLN',
                      cents=False),
            'minus dvylika zlotų, 81 grašis'
        )
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='PLN'),
            'vienas zlotas, nulis grašių'
        )
        self.assertEqual(
            num2words(5.06, lang='lt', to='currency', currency='PLN'),
            'penki zlotai, šeši grašiai'
        )
        # RUB
        self.assertEqual(
            num2words(-1281, lang='lt', to='currency', currency='RUB',
                      cents=False),
            'minus dvylika rublių, 81 kapeika'
        )
        self.assertEqual(
            num2words(1.0, lang='lt', to='currency', currency='RUB'),
            'vienas rublis, nulis kapeikų'
        )
        self.assertEqual(
            num2words(5.06, lang='lt', to='currency', currency='RUB'),
            'penki rubliai, šešios kapeikos'
        )
        self.assertEqual(
            num2words(-12.01, lang='lt', to='currency', currency='RUB'),
            'minus dvylika rublių, viena kapeika'
        )
        self.assertEqual(
            num2words(1122.22, lang='lt', to='currency', currency='RUB'),
            'vienas tūkstantis vienas šimtas dvidešimt du rubliai, '
            'dvidešimt dvi kapeikos'
        )
