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

CARDINAL_TEST_CASES = (
    ('0', 'нула'),
    ('1', 'едно'),
    ('10', 'десет'),
    ('100', 'сто'),
    ('101', 'сто и едно'),
    ('110', 'сто и десет'),
    ('120', 'сто и двадесет'),
    ('121', 'сто двадесет и едно'),
    ('1000', 'хиляда'),
    ('1001', 'хиляда и едно'),
    ('1021', 'хиляда двадесет и едно'),
    ('1020', 'хиляда и двадесет'),
    ('1200', 'хиляда и двеста'),
    ('1201', 'хиляда двеста и едно'),
    ('2201', 'две хиляди двеста и едно'),
    ('3200', 'три хиляди и двеста'),
    ('10000', 'десет хиляди'),
    ('10001', 'десет хиляди и едно'),
    ('50001', 'петдесет хиляди и едно'),
    ('51000', 'петдесет и една хиляди'),
    ('100000', 'сто хиляди'),
    ('155000', 'сто петдесет и пет хиляди'),
    ('155201', 'сто петдесет и пет хиляди двеста и едно'),
    ('251000', 'двеста петдесет и една хиляди'),
    ('1000000', 'един милион'),
    ('1200000', 'един милион и двеста хиляди'),
    ('1250000', 'един милион двеста и петдесет хиляди'),
    ('1250001', 'един милион двеста и петдесет хиляди и едно'),
    ('1251000', 'един милион двеста петдесет и една хиляди'),
    ('1251001', 'един милион двеста петдесет и една хиляди и едно'),
)


class Num2WordsBGTest(TestCase):
    def test_cardinal(self):
        for test in CARDINAL_TEST_CASES:
            self.assertEqual(
                num2words(test[0], lang='bg', to='cardinal'), test[1]
            )
