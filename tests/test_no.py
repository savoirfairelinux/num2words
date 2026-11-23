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


class Num2WordsNOTest(TestCase):
    def test_neuter_one_before_hundred_and_thousand(self):
        for value, expected in [
            (100, 'ett hundre'),
            (1000, 'ett tusen'),
            (101, 'ett hundre og en'),
            (1001, 'ett tusen og en'),
            (1100, 'ett tusen ett hundre'),
            (1100000, 'en million ett hundre tusen'),
            (1000000, 'en million'),
            (1, 'en'),
        ]:
            self.assertEqual(num2words(value, lang='no'), expected)

    def test_cardinal(self):
        self.assertEqual(num2words(0, to="cardinal", lang="no"), "null")
        self.assertEqual(num2words(1, to="cardinal", lang="no"), "en")
        self.assertEqual(num2words(3, to="cardinal", lang="no"), "tre")
        self.assertEqual(num2words(5, to="cardinal", lang="no"), "fem")
        self.assertEqual(num2words(18, to="cardinal", lang="no"), "atten")
        self.assertEqual(num2words(45, to="cardinal", lang="no"), "førtifem")
        self.assertEqual(num2words(92, to="cardinal", lang="no"), "nittito")
        self.assertEqual(num2words(1345, to="cardinal", lang="no"),
                         "ett tusen tre hundre og førtifem")
        self.assertEqual(num2words(4435, to="cardinal", lang="no"),
                         "fire tusen fire hundre og trettifem")
        self.assertEqual(num2words(1004435, to="cardinal", lang="no"),
                         "en million fire tusen fire hundre og trettifem")
        self.assertEqual(num2words(4335000, to="cardinal", lang="no"),
                         "fire million tre hundre og trettifem tusen")
        self.assertEqual(num2words(14004535, to="cardinal", lang="no"),
                         "fjorten million fire tusen fem hundre og trettifem")
        self.assertEqual(num2words(1.5, to="cardinal", lang="no"),
                         "en komma fem")

    def test_ordinal(self):
        self.assertEqual(num2words(1, to="ordinal", lang="no"), "første")
        self.assertEqual(num2words(5, to="ordinal", lang="no"), "femte")
        self.assertEqual(num2words(10, to="ordinal", lang="no"), "tiende")
        self.assertEqual(num2words(14, to="ordinal", lang="no"), "fjortende")
        self.assertEqual(num2words(30, to="ordinal", lang="no"), "trettiende")
        self.assertEqual(num2words(32, to="ordinal", lang="no"), "trettiandre")
        self.assertEqual(num2words(100, to="ordinal", lang="no"),
                         "ett hundrede")
        self.assertEqual(num2words(1000, to="ordinal", lang="no"),
                         "ett tusende")
        self.assertEqual(num2words(1435, to="ordinal", lang="no"),
                         "ett tusen fire hundre og trettifemte")
        self.assertEqual(num2words(1000000, to="ordinal", lang="no"),
                         "en millionte")

    def test_ordinal_num(self):
        self.assertEqual(num2words(1, to="ordinal_num", lang="no"), "1.")
        self.assertEqual(num2words(5, to="ordinal_num", lang="no"), "5.")
        self.assertEqual(num2words(10, to="ordinal_num", lang="no"), "10.")
        self.assertEqual(num2words(14, to="ordinal_num", lang="no"), "14.")
        self.assertEqual(num2words(32, to="ordinal_num", lang="no"), "32.")

    def test_year(self):
        self.assertEqual(num2words(1835, to="year", lang="no"),
                         "atten hundre og trettifem")
        self.assertEqual(num2words(2015, to="year", lang="no"),
                         "to tusen og femten")

    def test_currency(self):
        self.assertEqual(num2words(1.00, to="currency", lang="no"), "en krone")
        self.assertEqual(num2words(2.00, to="currency", lang="no"),
                         "to kroner")
        self.assertEqual(num2words(2.50, to="currency", lang="no"),
                         "to kroner og femti øre")
        self.assertEqual(num2words(135.00, to="currency", lang="no"),
                         "ett hundre og trettifem kroner")
        self.assertEqual(num2words(135.59, to="currency", lang="no"),
                         "ett hundre og trettifem kroner og femtini øre")
