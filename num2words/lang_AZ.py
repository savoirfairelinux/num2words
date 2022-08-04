# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2017, Tufan Kaynak, Framras.  All Rights Reserved.
# Copyright (c) 2021, Tarlan Ismayilsoy.  All Rights Reserved.

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

from .lang_TR import Num2Word_TR


class Num2Word_AZ(Num2Word_TR):

    def __init__(self):
        self.tr_instance = Num2Word_TR()

    def translate_to_aze(self, turkish_str):
        """Translates the given turkish string to azerbaijani"""
        aze_str = turkish_str

        aze_str = aze_str.replace('eksi', 'mənfi')
        aze_str = aze_str.replace('virgül', 'vergül')
        aze_str = aze_str.replace('lira', 'manat')
        aze_str = aze_str.replace('kuruş', 'qəpik')

        aze_str = aze_str.replace('dört', 'dörd')
        aze_str = aze_str.replace('yedi', 'yeddi')
        aze_str = aze_str.replace('sekiz', 'səkkiz')
        aze_str = aze_str.replace('dokuz', 'doqquz')
        aze_str = aze_str.replace('yirmi', 'iyirmi')
        aze_str = aze_str.replace('kırk', 'qırx')
        aze_str = aze_str.replace('elli', 'əlli')
        aze_str = aze_str.replace('seksen', 'səksən')
        aze_str = aze_str.replace('doksan', 'doxsan')
        aze_str = aze_str.replace('bin', 'min')
        aze_str = aze_str.replace('milyar', 'milyard')
        aze_str = aze_str.replace('katrilyon', 'kvadrilyon')
        aze_str = aze_str.replace('kentilyon', 'kvintilyon')

        aze_str = aze_str.replace('bedelsiz', 'pulsuz')

        return aze_str

    def to_cardinal(self, value):
        return self.translate_to_aze(self.tr_instance.to_cardinal(value))

    def to_cardinal_float(self, value):
        return self.translate_to_aze(self.tr_instance.to_cardinal_float(value))

    def verify_cardinal(self, value):
        return self.tr_instance.verify_cardinal(value)

    def verify_ordinal(self, value):
        return self.tr_instance.verify_ordinal(value)

    def to_ordinal(self, value):
        return self.translate_to_aze(self.tr_instance.to_ordinal(value))

    def to_splitnum(self, val):
        self.tr_instance.to_splitnum(val)

    def to_currency(self, value):
        return self.translate_to_aze(self.tr_instance.to_currency(value))
