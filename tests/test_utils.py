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

from num2words.utils import splitbyx


class TestUtils(TestCase):
    def test_splitbyx(self):
        self.assertEqual(list(splitbyx(str(12), 3)), [12])
        self.assertEqual(list(splitbyx(str(1234), 3)), [1, 234])
        self.assertEqual(list(splitbyx(str(12345678900), 3)),
                         [12, 345, 678, 900]
                         )
        self.assertEqual(list(splitbyx(str(1000000), 6)), [1, 0])

        self.assertEqual(list(splitbyx(str(12), 3, format_int=False)), ['12'])
        self.assertEqual(list(splitbyx(str(1234), 3, format_int=False)),
                         ['1', '234']
                         )
        self.assertEqual(list(splitbyx(str(12345678900), 3, format_int=False)),
                         ['12', '345', '678', '900']
                         )
        self.assertEqual(list(splitbyx(str(1000000), 6, format_int=False)),
                         ['1', '000000']
                         )
