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


class Num2WordsENNGTest(TestCase):

    # only the test for currency is writen as other
    # functions in the Class remains the
    # same and have been properly tested in the
    # test test_en which tests the parent class
    # upon which this class inherits

    def test_to_currency(self):

        language = 'en_NG'
        separator = ' and'

        self.assertEqual(
            num2words(
                '38.4',
                lang=language,
                to='currency',
                separator=separator,
                kobo=False
            ),
            "thirty-eight naira and 40 kobo"
        )
        self.assertEqual(
            num2words(
                '0',
                lang=language,
                to='currency',
                separator=separator,
                kobo=False
            ),
            "zero naira"
        )

        self.assertEqual(
            num2words(
                '1.01',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            "one naira and one kobo"
        )

        self.assertEqual(
            num2words(
                '4778.00',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True, adjective=True
            ),
            'four thousand, seven hundred and seventy-eight Nigerian naira'
            ' and zero kobo')

        self.assertEqual(
            num2words(
                '4778.00',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            'four thousand, seven hundred and seventy-eight naira and'
            ' zero kobo')

        self.assertEqual(
            num2words(
                '1.1',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            "one naira and ten kobo"
        )

        self.assertEqual(
            num2words(
                '158.3',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            "one hundred and fifty-eight naira and thirty kobo"
        )

        self.assertEqual(
            num2words(
                '2000.00',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            "two thousand naira and zero kobo"
        )

        self.assertEqual(
            num2words(
                '4.01',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            "four naira and one kobo"
        )

        self.assertEqual(
            num2words(
                '2000.00',
                lang=language,
                to='currency',
                separator=separator,
                kobo=True
            ),
            "two thousand naira and zero kobo"
        )
