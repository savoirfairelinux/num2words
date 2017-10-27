# encoding: UTF-8
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

TEST_CASES_CARDINAL = (
    (1, 'واحد'),
    (2, 'اثنين'),
    (11, 'أحد عشر'),
    (12, 'اثناعشر'),
    (20, 'عشرين'),
    (21, 'واحد وعشرين'),
    (26, 'ستة وعشرين'),
    (30, 'ثلاثين'),
    (67, 'سبعة وستين'),
    (70, 'سبعين'),
    (100, 'مئة'),
    (101, 'مئة و واحد'),
    (199, 'مئة و تسعة وتسعين'),
    (203, 'مئتين و ثلاثة'),
    (1000, 'ألف'),
    (1001, 'ألف و واحد'),
    (1097, 'ألف و سبعة وتسعين'),
    (1000000, 'مليون'),
    (1000001, 'مليون و واحد'),
)

TEST_CASES_ORDINAL = (
    (1, 'أول'),
    (8, 'ثامن'),
    (12, 'ثاني عشر'),
    (100, 'مئة'),
)


class Num2WordsARTest(TestCase):

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='ar'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='ar', ordinal=True),
                test[1]
            )
