# -*- encoding: utf-8 -*-
# Copyright (c) 2015, Savoir-faire Linux inc.  All Rights Reserved.

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

class Num2WordsITTest(TestCase):

    def test_number(self):

        test_cases = (
            (1,'uno'),
            (2,'due'),
            (3,'tre'),
            (11,'undici'),
            (12,'dodici'),
            (16,'sedici'),
            (19,'diciannove'),
            (20,'venti'),
            (21,'ventuno'),
            (26,'ventisei'),
            (30,'trenta'),
            (31,'trentuno'),
            (40,'quaranta'),
            (43,'quarantatre'),
            (50,'cinquanta'),
            (55,'cinquantacinque'),
            (60,'sessanta'),
            (67,'sessantasette'),
            (70,'settanta'),
            (79,'settantanove'),
            (100,'cento'),
            (101,'centouno'),
            (199,'centonovantanove'),
            (203,'duecentotre'),
            (287,'duecentoottantasette'),
            (300,'trecento'),
            (356,'trecentocinquantasei'),
            (410,'quattrocentodieci'),
            (434,'quattrocentotrentaquattro'),
            (578,'cinquecentosettantotto'),
            (689,'seicentoottantanove'),
            (729,'settecentoventinove'),
            (894,'ottocentonovantaquattro'),
            (999,'novecentonovantanove'),
            (1000,'mille'),
            (1001,'milleuno'),
            (1097,'millenovantasette'),
            (1104,'millecentoquattro'),
            (1243,'milleduecentoquarantatre'),
            (2385,'duemilatrecentoottantacinque'),
            (3766,'tremilasettecentosessantasei'),
            (4196,'quattromilacentonovantasei'),
            (5846,'cinquemilaottocentoquarantasei'),
            (6459,'seimilaquattrocentocinquantanove'),
            (7232,'settemiladuecentotrentadue'),
            (8569,'ottomilacinquecentosessantanove'),
            (9539,'novemilacinquecentotrentanove'),
            (1000000,'un milione'),
            (1000001,'un milioneuno'),
            # (1000000100,'un miliardocento'), # DOES NOT WORK TODO: FIX
        )

        for test in test_cases:
            self.assertEqual(num2words(test[0], lang='it'), test[1])

