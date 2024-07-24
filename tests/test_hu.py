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


class Num2WordsHUTest(TestCase):
    def test_and_join_199(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/8
        self.assertEqual(num2words(199), "one hundred and ninety-nine")

    def test_cardinal(self):
        self.assertEqual(
            num2words(-1, lang='hu'),
            'mínusz egy'
        )
        self.assertEqual(
            num2words(0, lang='hu'),
            'nulla'
        )
        self.assertEqual(
            num2words(1, lang='hu'),
            'egy'
        )
        self.assertEqual(
            num2words(13, lang='hu'),
            'tizenhárom'
        )
        self.assertEqual(
            num2words(22, lang='hu'),
            'huszonkettő'
        )
        self.assertEqual(
            num2words(75, lang='hu'),
            'hetvenöt'
        )
        self.assertEqual(
            num2words(124, lang='hu'),
            'százhuszonnégy'
        )
        self.assertEqual(
            num2words(651, lang='hu'),
            'hatszázötvenegy'
        )
        self.assertEqual(
            num2words(2232, lang='hu'),
            'kétezer-kétszázharminckettő'
        )
        self.assertEqual(
            num2words(16501, lang='hu'),
            'tizenhatezer-ötszázegy'
        )
        self.assertEqual(
            num2words(1900000000000, lang='hu'),
            'egybillió-kilencszázmilliárd'
        )
        self.assertEqual(
            num2words(24656451324564987566, lang='hu'),
            'huszonnégytrillió-hatszázötvenhatbilliárd-négyszázötvenegybillió'
            '-háromszázhuszonnégymilliárd-ötszázhatvannégymillió-'
            'kilencszáznyolcvanhétezer-ötszázhatvanhat'
        )

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='hu', to='ordinal'),
            'nulladik'
        )
        self.assertEqual(
            num2words(1, lang='hu', to='ordinal'),
            'első'
        )
        self.assertEqual(
            num2words(2, lang='hu', to='ordinal'),
            'második'
        )
        self.assertEqual(
            num2words(-3, lang='hu', to='ordinal'),
            'mínusz harmadik'
        )
        self.assertEqual(
            num2words(13, lang='hu', to='ordinal'),
            'tizenharmadik'
        )
        self.assertEqual(
            num2words(22, lang='hu', to='ordinal'),
            'huszonkettedik'
        )
        self.assertEqual(
            num2words(75, lang='hu', to='ordinal'),
            'hetvenötödik'
        )
        self.assertEqual(
            num2words(124, lang='hu', to='ordinal'),
            'százhuszonnegyedik'
        )
        self.assertEqual(
            num2words(1532, lang='hu', to='ordinal'),
            'ezerötszázharminckettedik'
        )
        self.assertEqual(
            num2words(16501, lang='hu', to='ordinal'),
            'tizenhatezer-ötszázegyedik'
        )
        self.assertEqual(
            num2words(458755640120000, lang='hu', to='ordinal'),
            'négyszázötvennyolcbillió-hétszázötvenötmilliárd-'
            'hatszáznegyvenmillió-százhúszezredik'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='hu', to='ordinal_num'), '10.')
        self.assertEqual(num2words(21, lang='hu', to='ordinal_num'), '21.')
        self.assertEqual(num2words(102, lang='hu', to='ordinal_num'), '102.')
        self.assertEqual(num2words(73, lang='hu', to='ordinal_num'), '73.')

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(num2words(12, lang='hu'),
                         "tizenkettő")
        self.assertEqual(num2words(12.0, lang='hu'),
                         "tizenkettő")
        self.assertEqual(num2words(12.5, lang='hu'),
                         "tizenkettő egész öt tized")
        self.assertEqual(num2words(-12.5, lang='hu'),
                         "mínusz tizenkettő egész öt tized")
        self.assertEqual(num2words(12.51, lang='hu'),
                         "tizenkettő egész ötvenegy század")
        self.assertEqual(num2words(12.53, lang='hu'),
                         "tizenkettő egész ötvenhárom század")
        self.assertEqual(num2words(12.590, lang='hu'),
                         "tizenkettő egész ötvenkilenc század")
        self.assertEqual(num2words(12.005, lang='hu'),
                         "tizenkettő egész öt ezred")

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            num2words("1000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "0000000000000000000000000000000000000000000000000000000"
                      "00000000000000000000000000000000")

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='hu', to='currency', separator=' és',
                      cents=False, currency='HUF'),
            "harmincnyolc forint és 40 fillér"
        )
        self.assertEqual(
            num2words('0', lang='hu', to='currency', separator=' és',
                      cents=False, currency='HUF'),
            "nulla forint és 00 fillér"
        )

        self.assertEqual(
            num2words('1.01', lang='hu', to='currency', separator=' és',
                      cents=True, currency='HUF'),
            "egy forint és egy fillér"
        )

        self.assertEqual(
            num2words('4778.00', lang='hu', to='currency', separator=' és',
                      cents=True, currency='HUF', adjective=True),
            'négyezer-hétszázhetvennyolc Hungarian forint'
            ' és nulla fillér')

        self.assertEqual(
            num2words('4778.00', lang='hu', to='currency', separator=' és',
                      cents=True, currency='HUF'),
            'négyezer-hétszázhetvennyolc forint és nulla fillér')

    def test_to_year(self):
        # issue 141
        # "e2 e2"
        self.assertEqual(num2words(1990, lang='hu', to='year'),
                         'ezerkilencszázkilencven')
        self.assertEqual(num2words(5555, lang='hu', to='year'),
                         'ötezer-ötszázötvenöt')
        self.assertEqual(num2words(2020, lang='hu', to='year'),
                         'kétezer-húsz')
        self.assertEqual(num2words(905, lang='hu', to='year'),
                         'kilencszázöt')
        self.assertEqual(num2words(0, lang='hu', to='year'),
                         'nulla')
        # suffixes
        self.assertEqual(num2words(-44, lang='hu', to='year'),
                         'i. e. negyvennégy')
        self.assertEqual(num2words(-44, lang='hu', to='year', suffix='Kr. e.'),
                         'Kr. e. negyvennégy')
        self.assertEqual(num2words(1, lang='hu', to='year', suffix='Kr. u.'),
                         'Kr. u. egy')
        self.assertEqual(num2words(-66000000, lang='hu', to='year'),
                         'i. e. hatvanhatmillió')
