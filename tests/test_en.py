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

from unittest import TestCase

from num2words import num2words


class Num2WordsENTest(TestCase):
    def test_and_join_199(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/8
        self.assertEqual(num2words(199), "one hundred and ninety-nine")

    def test_ordinal(self):
        self.assertEqual(
            num2words(0, lang='en', to='ordinal'),
            'zeroth'
        )
        self.assertEqual(
            num2words(1, lang='en', to='ordinal'),
            'first'
        )
        self.assertEqual(
            num2words(13, lang='en', to='ordinal'),
            'thirteenth'
        )
        self.assertEqual(
            num2words(22, lang='en', to='ordinal'),
            'twenty-second'
        )
        self.assertEqual(
            num2words(12, lang='en', to='ordinal'),
            'twelfth'
        )
        self.assertEqual(
            num2words(130, lang='en', to='ordinal'),
            'one hundred and thirtieth'
        )
        self.assertEqual(
            num2words(1003, lang='en', to='ordinal'),
            'one thousand and third'
        )

    def test_ordinal_num(self):
        self.assertEqual(num2words(10, lang='en', to='ordinal_num'), '10th')
        self.assertEqual(num2words(21, lang='en', to='ordinal_num'), '21st')
        self.assertEqual(num2words(102, lang='en', to='ordinal_num'), '102nd')
        self.assertEqual(num2words(73, lang='en', to='ordinal_num'), '73rd')

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(num2words(12.5), "twelve point five")
        self.assertEqual(num2words(12.51), "twelve point five one")
        self.assertEqual(num2words(12.53), "twelve point five three")
        self.assertEqual(num2words(12.59), "twelve point five nine")

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
            num2words('38.4', lang='en', to='currency', separator=' and',
                      cents=False, currency='USD'),
            "thirty-eight dollars and 40 cents"
        )
        self.assertEqual(
            num2words('0', lang='en', to='currency', separator=' and',
                      cents=False, currency='USD'),
            "zero dollars and 00 cents"
        )

        self.assertEqual(
            num2words('1.01', lang='en', to='currency', separator=' and',
                      cents=True, currency='USD'),
            "one dollar and one cent"
        )

        self.assertEqual(
            num2words('4778.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='USD', adjective=True),
            'four thousand, seven hundred and seventy-eight US dollars'
            ' and zero cents')

        self.assertEqual(
            num2words('4778.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='USD'),
            'four thousand, seven hundred and seventy-eight dollars and'
            ' zero cents')

        self.assertEqual(
            num2words('1.1', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "one peso and ten cents"
        )

        self.assertEqual(
            num2words('158.3', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "one hundred and fifty-eight pesos and thirty cents"
        )

        self.assertEqual(
            num2words('2000.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "two thousand pesos and zero cents"
        )

        self.assertEqual(
            num2words('4.01', lang='en', to='currency', separator=' and',
                      cents=True, currency='MXN'),
            "four pesos and one cent"
        )

        self.assertEqual(
            num2words('2000.00', lang='en', to='currency', separator=' and',
                      cents=True, currency='UZS'),
            "two thousand sums and zero tiyins"
        )

    def test_to_year(self):
        # issue 141
        # "e2 e2"
        self.assertEqual(num2words(1990, lang='en', to='year'),
                         'nineteen ninety')
        self.assertEqual(num2words(5555, lang='en', to='year'),
                         'fifty-five fifty-five')
        self.assertEqual(num2words(2017, lang='en', to='year'),
                         'twenty seventeen')
        self.assertEqual(num2words(1066, lang='en', to='year'),
                         'ten sixty-six')
        self.assertEqual(num2words(1865, lang='en', to='year'),
                         'eighteen sixty-five')
        # "e3 and e1"; "e2 oh-e1"; "e3"
        self.assertEqual(num2words(3000, lang='en', to='year'),
                         'three thousand')
        self.assertEqual(num2words(2001, lang='en', to='year'),
                         'two thousand and one')
        self.assertEqual(num2words(1901, lang='en', to='year'),
                         'nineteen oh-one')
        self.assertEqual(num2words(2000, lang='en', to='year'),
                         'two thousand')
        self.assertEqual(num2words(905, lang='en', to='year'),
                         'nine oh-five')
        # "e2 hundred"; "e3"
        self.assertEqual(num2words(6600, lang='en', to='year'),
                         'sixty-six hundred')
        self.assertEqual(num2words(1900, lang='en', to='year'),
                         'nineteen hundred')
        self.assertEqual(num2words(600, lang='en', to='year'),
                         'six hundred')
        self.assertEqual(num2words(50, lang='en', to='year'),
                         'fifty')
        self.assertEqual(num2words(0, lang='en', to='year'),
                         'zero')
        # suffixes
        self.assertEqual(num2words(-44, lang='en', to='year'),
                         'forty-four BC')
        self.assertEqual(num2words(-44, lang='en', to='year', suffix='BCE'),
                         'forty-four BCE')
        self.assertEqual(num2words(1, lang='en', to='year', suffix='AD'),
                         'one AD')
        self.assertEqual(num2words(66, lang='en', to='year',
                                   suffix='m.y.a.'),
                         'sixty-six m.y.a.')
        self.assertEqual(num2words(-66000000, lang='en', to='year'),
                         'sixty-six million BC')

    def test_large_names(self):
        self.assertEqual(num2words(10 * 10**3, lang='en'), 'ten thousand')
        self.assertEqual(num2words(10 * 10**6, lang='en'), 'ten million')
        self.assertEqual(num2words(10 * 10**9, lang='en'), 'ten billion')
        self.assertEqual(num2words(10 * 10**12, lang='en'), 'ten trillion')
        self.assertEqual(num2words(10 * 10**15, lang='en'), 'ten quadrillion')
        self.assertEqual(num2words(10 * 10**18, lang='en'), 'ten quintillion')
        self.assertEqual(num2words(10 * 10**21, lang='en'), 'ten sextillion')
        self.assertEqual(num2words(10 * 10**24, lang='en'), 'ten septillion')
        self.assertEqual(num2words(10 * 10**27, lang='en'), 'ten octillion')
        self.assertEqual(num2words(10 * 10**30, lang='en'), 'ten nonillion')
        self.assertEqual(num2words(10 * 10**33, lang='en'), 'ten decillion')
        self.assertEqual(num2words(10 * 10**36, lang='en'), 'ten undecillion')
        self.assertEqual(num2words(10 * 10**39, lang='en'), 'ten duodecillion')
        self.assertEqual(num2words(10 * 10**42, lang='en'), 'ten tredecillion')
        self.assertEqual(num2words(10 * 10**45, lang='en'), 'ten quattuordecillion')
        self.assertEqual(num2words(10 * 10**48, lang='en'), 'ten quindecillion')
        self.assertEqual(num2words(10 * 10**51, lang='en'), 'ten sexdecillion')
        self.assertEqual(num2words(10 * 10**54, lang='en'), 'ten septdecillion')
        self.assertEqual(num2words(10 * 10**57, lang='en'), 'ten octodecillion')
        self.assertEqual(num2words(10 * 10**60, lang='en'), 'ten novemdecillion')
        self.assertEqual(num2words(10 * 10**63, lang='en'), 'ten vigintillion')
        self.assertEqual(num2words(10 * 10**66, lang='en'), 'ten unvigintillion')
        self.assertEqual(num2words(10 * 10**69, lang='en'), 'ten duovigintillion')
        self.assertEqual(num2words(10 * 10**72, lang='en'), 'ten trevigintillion')
        self.assertEqual(num2words(10 * 10**75, lang='en'), 'ten quattuorvigintillion')
        self.assertEqual(num2words(10 * 10**78, lang='en'), 'ten quinvigintillion')
        self.assertEqual(num2words(10 * 10**81, lang='en'), 'ten sexvigintillion')
        self.assertEqual(num2words(10 * 10**84, lang='en'), 'ten septvigintillion')
        self.assertEqual(num2words(10 * 10**87, lang='en'), 'ten octovigintillion')
        self.assertEqual(num2words(10 * 10**90, lang='en'), 'ten novemvigintillion')
        self.assertEqual(num2words(10 * 10**93, lang='en'), 'ten trigintillion')
        self.assertEqual(num2words(10 * 10**96, lang='en'), 'ten untrigintillion')
        self.assertEqual(num2words(10 * 10**99, lang='en'), 'ten duotrigintillion')
        self.assertEqual(num2words(10 * 10**102, lang='en'), 'ten tretrigintillion')
        self.assertEqual(num2words(10 * 10**105, lang='en'), 'ten quattuortrigintillion')
        self.assertEqual(num2words(10 * 10**108, lang='en'), 'ten quintrigintillion')
        self.assertEqual(num2words(10 * 10**111, lang='en'), 'ten sextrigintillion')
        self.assertEqual(num2words(10 * 10**114, lang='en'), 'ten septtrigintillion')
        self.assertEqual(num2words(10 * 10**117, lang='en'), 'ten octotrigintillion')
        self.assertEqual(num2words(10 * 10**120, lang='en'), 'ten novemtrigintillion')
        self.assertEqual(num2words(10 * 10**123, lang='en'), 'ten quadragintillion')
        self.assertEqual(num2words(10 * 10**126, lang='en'), 'ten unquadragintillion')
        self.assertEqual(num2words(10 * 10**129, lang='en'), 'ten duoquadragintillion')
        self.assertEqual(num2words(10 * 10**132, lang='en'), 'ten trequadragintillion')
        self.assertEqual(num2words(10 * 10**135, lang='en'), 'ten quattuorquadragintillion')
        self.assertEqual(num2words(10 * 10**138, lang='en'), 'ten quinquadragintillion')
        self.assertEqual(num2words(10 * 10**141, lang='en'), 'ten sexquadragintillion')
        self.assertEqual(num2words(10 * 10**144, lang='en'), 'ten septquadragintillion')
        self.assertEqual(num2words(10 * 10**147, lang='en'), 'ten octoquadragintillion')
        self.assertEqual(num2words(10 * 10**150, lang='en'), 'ten novemquadragintillion')
        self.assertEqual(num2words(10 * 10**153, lang='en'), 'ten quinquagintillion')
        self.assertEqual(num2words(10 * 10**156, lang='en'), 'ten unquinquagintillion')
        self.assertEqual(num2words(10 * 10**159, lang='en'), 'ten duoquinquagintillion')
        self.assertEqual(num2words(10 * 10**162, lang='en'), 'ten trequinquagintillion')
        self.assertEqual(num2words(10 * 10**165, lang='en'), 'ten quattuorquinquagintillion')
        self.assertEqual(num2words(10 * 10**168, lang='en'), 'ten quinquinquagintillion')
        self.assertEqual(num2words(10 * 10**171, lang='en'), 'ten sexquinquagintillion')
        self.assertEqual(num2words(10 * 10**174, lang='en'), 'ten septquinquagintillion')
        self.assertEqual(num2words(10 * 10**177, lang='en'), 'ten octoquinquagintillion')
        self.assertEqual(num2words(10 * 10**180, lang='en'), 'ten novemquinquagintillion')
        self.assertEqual(num2words(10 * 10**183, lang='en'), 'ten sexagintillion')
        self.assertEqual(num2words(10 * 10**186, lang='en'), 'ten unsexagintillion')
        self.assertEqual(num2words(10 * 10**189, lang='en'), 'ten duosexagintillion')
        self.assertEqual(num2words(10 * 10**192, lang='en'), 'ten tresexagintillion')
        self.assertEqual(num2words(10 * 10**195, lang='en'), 'ten quattuorsexagintillion')
        self.assertEqual(num2words(10 * 10**198, lang='en'), 'ten quinsexagintillion')
        self.assertEqual(num2words(10 * 10**201, lang='en'), 'ten sexsexagintillion')
        self.assertEqual(num2words(10 * 10**204, lang='en'), 'ten septsexagintillion')
        self.assertEqual(num2words(10 * 10**207, lang='en'), 'ten octosexagintillion')
        self.assertEqual(num2words(10 * 10**210, lang='en'), 'ten novemsexagintillion')
        self.assertEqual(num2words(10 * 10**213, lang='en'), 'ten septuagintillion')
        self.assertEqual(num2words(10 * 10**216, lang='en'), 'ten unseptuagintillion')
        self.assertEqual(num2words(10 * 10**219, lang='en'), 'ten duoseptuagintillion')
        self.assertEqual(num2words(10 * 10**222, lang='en'), 'ten treseptuagintillion')
        self.assertEqual(num2words(10 * 10**225, lang='en'), 'ten quattuorseptuagintillion')
        self.assertEqual(num2words(10 * 10**228, lang='en'), 'ten quinseptuagintillion')
        self.assertEqual(num2words(10 * 10**231, lang='en'), 'ten sexseptuagintillion')
        self.assertEqual(num2words(10 * 10**234, lang='en'), 'ten septseptuagintillion')
        self.assertEqual(num2words(10 * 10**237, lang='en'), 'ten octoseptuagintillion')
        self.assertEqual(num2words(10 * 10**240, lang='en'), 'ten novemseptuagintillion')
        self.assertEqual(num2words(10 * 10**243, lang='en'), 'ten octogintillion')
        self.assertEqual(num2words(10 * 10**246, lang='en'), 'ten unoctogintillion')
        self.assertEqual(num2words(10 * 10**249, lang='en'), 'ten duooctogintillion')
        self.assertEqual(num2words(10 * 10**252, lang='en'), 'ten treoctogintillion')
        self.assertEqual(num2words(10 * 10**255, lang='en'), 'ten quattuoroctogintillion')
        self.assertEqual(num2words(10 * 10**258, lang='en'), 'ten quinoctogintillion')
        self.assertEqual(num2words(10 * 10**261, lang='en'), 'ten sexoctogintillion')
        self.assertEqual(num2words(10 * 10**264, lang='en'), 'ten septoctogintillion')
        self.assertEqual(num2words(10 * 10**267, lang='en'), 'ten octooctogintillion')
        self.assertEqual(num2words(10 * 10**270, lang='en'), 'ten novemoctogintillion')
        self.assertEqual(num2words(10 * 10**273, lang='en'), 'ten nonagintillion')
        self.assertEqual(num2words(10 * 10**276, lang='en'), 'ten unnonagintillion')
        self.assertEqual(num2words(10 * 10**279, lang='en'), 'ten duononagintillion')
        self.assertEqual(num2words(10 * 10**282, lang='en'), 'ten trenonagintillion')
        self.assertEqual(num2words(10 * 10**285, lang='en'), 'ten quattuornonagintillion')
        self.assertEqual(num2words(10 * 10**288, lang='en'), 'ten quinnonagintillion')
        self.assertEqual(num2words(10 * 10**291, lang='en'), 'ten sexnonagintillion')
        self.assertEqual(num2words(10 * 10**294, lang='en'), 'ten septnonagintillion')
        self.assertEqual(num2words(10 * 10**297, lang='en'), 'ten octononagintillion')
        self.assertEqual(num2words(10 * 10**300, lang='en'), 'ten novemnonagintillion')
        self.assertEqual(num2words(10 * 10**303, lang='en'), 'ten centillion')
