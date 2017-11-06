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

    def test_cardinal_for_float_number(self):
        # issue 24
        self.assertEqual(num2words(12.50), "twelve point five zero")
        self.assertEqual(num2words(12.51), "twelve point five one")
        self.assertEqual(num2words(12.53), "twelve point five three")
        self.assertEqual(num2words(12.59), "twelve point five nine")

    def test_to_currency(self):
        self.assertEqual(
            num2words('38.4', lang='en', to='currency', seperator=' and',
                      cents=False, currency='USD'),
            "thirty-eight dollars and 40 cents"
        )
        self.assertEqual(
            num2words('0', lang='en', to='currency', seperator=' and',
                      cents=False, currency='USD'),
            "zero dollars and 00 cents"
        )

        self.assertEqual(
            num2words('1.01', lang='en', to='currency', seperator=' and',
                      cents=True, currency='USD'),
            "one dollar and one cent"
        )

        self.assertEqual(
            num2words('4778.00', lang='en', to='currency', seperator=' and',
                      cents=True, currency='USD', adjective=True),
            'four thousand, seven hundred and seventy-eight US dollars'
            ' and zero cents')

        self.assertEqual(
            num2words('4778.00', lang='en', to='currency', seperator=' and',
                      cents=True, currency='USD'),
            'four thousand, seven hundred and seventy-eight dollars and'
            ' zero cents')
