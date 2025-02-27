# coding: utf-8
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


class Num2WordsSVTest(TestCase):
    def test_ordinal(self):
        self.assertEqual(num2words(14, to="ordinal", lang="sv"), "fjortonde")
        self.assertEqual(num2words(1435, to="ordinal", lang="sv"),
                         "etttusen fyrahundratrettiofemte")
        self.assertEqual(num2words(32, to="ordinal", lang="sv"),
                         "trettioandra")
        self.assertEqual(num2words(1, to="ordinal", lang="sv"), "första")
        self.assertEqual(num2words(5, to="ordinal", lang="sv"), "femte")
        self.assertEqual(num2words(10, to="ordinal", lang="sv"), "tionde")

    def test_cardinal(self):
        self.assertEqual(num2words(0, to="cardinal", lang="sv"), "noll")
        self.assertEqual(num2words(1, to="cardinal", lang="sv"), "ett")
        self.assertEqual(num2words(3, to="cardinal", lang="sv"), "tre")
        self.assertEqual(num2words(5, to="cardinal", lang="sv"), "fem")
        self.assertEqual(num2words(18, to="cardinal", lang="sv"), "arton")
        self.assertEqual(num2words(45, to="cardinal", lang="sv"), "förtiofem")
        self.assertEqual(num2words(1345, to="cardinal", lang="sv"),
                         "etttusen trehundraförtiofem")
        self.assertEqual(num2words(4435, to="cardinal", lang="sv"),
                         "fyratusen fyrahundratrettiofem")
        self.assertEqual(num2words(1004135, to="cardinal", lang="sv"),
                         "en miljon fyratusen etthundratrettiofem")
        self.assertEqual(num2words(4335000, to="cardinal", lang="sv"),
                         "fyra miljoner trehundratrettiofemtusen")
        self.assertEqual(num2words(14004535, to="cardinal", lang="sv"),
                         "fjorton miljoner fyratusen femhundratrettiofem")
        self.assertEqual(num2words(1.5, to="cardinal", lang="sv"),
                         "ett komma fem")

    def test_not_implemented_options(self):
        with self.assertRaises(NotImplementedError) as context:
            num2words(1235, to="year", lang="sv")
        self.assertTrue("'year' is not implemented for swedish language"
                        in str(context.exception))

        with self.assertRaises(NotImplementedError) as context:
            num2words(1235, to="currency", lang="sv")
        self.assertTrue("'currency' is not implemented for swedish language"
                        in str(context.exception))

        with self.assertRaises(NotImplementedError) as context:
            num2words(1235, to="ordinal_num", lang="sv")
        self.assertTrue("'ordinal_num' is not implemented for swedish language"
                        in str(context.exception))
