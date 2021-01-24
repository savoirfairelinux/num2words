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

from decimal import Decimal
from unittest import TestCase

from num2words.base import Num2Word_Base


class Num2WordBaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(Num2WordBaseTest, cls).setUpClass()
        cls.base = Num2Word_Base()

    def test_to_currency_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.base.to_currency(Decimal('1.00'), currency='EUR')

    def test_error_to_cardinal_float(self):
        from num2words.base import Num2Word_Base
        with self.assertRaises(TypeError):
            Num2Word_Base.to_cardinal_float(9)
        with self.assertRaises(TypeError):
            Num2Word_Base.to_cardinal_float("a")

    def test_error_merge(self):
        from num2words.base import Num2Word_Base
        self.base = Num2Word_Base()
        with self.assertRaises(NotImplementedError):
            self.base.merge(2, 3)

    def test_is_title(self):
        from num2words.base import Num2Word_Base
        self.base = Num2Word_Base()
        self.assertEqual(
            self.base.title("one"),
            "one"
            )
        self.base.is_title = True
        self.assertEqual(
            self.base.title("one"),
            "One"
            )
