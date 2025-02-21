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

from __future__ import division, print_function, unicode_literals

from unittest import TestCase

from num2words import num2words


def n2zh_tw(*args, **kwargs):
    return num2words(*args, lang='zh_TW', **kwargs)


class Num2WordsZhTWTest(TestCase):




    def test_year(self):
        self.assertEqual(n2zh_tw(1912, to="year", era=True), "民國元年")
        self.assertEqual(n2zh_tw(1912, to="year", era=True, reading="arabic"), "民國1年")
        self.assertEqual(n2zh_tw(1913, to="year", era=True), "民國二年")
        self.assertEqual(n2zh_tw(1932, to="year", era=True), "民國二十一年")
        self.assertEqual(n2zh_tw(2011, to="year", era=True), "民國一百年")
        self.assertEqual(n2zh_tw(2012, to="year", era=True), "民國一零一年")
        self.assertEqual(n2zh_tw(2025, to="year", era=True), "民國一一四年")
        self.assertEqual(n2zh_tw(2025, to="year", era=True, reading="arabic"), "民國114年")
        with self.assertRaises(ValueError):
            n2zh_tw(1911, to="year", era=True)
