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

# for Nepalese Number System
# Added support for Nepali Numbering System by Ajira Group, Nepal support@ajiragroup.com


from __future__ import unicode_literals

from .lang_EN import Num2Word_EN


class Num2Word_EN_NP(Num2Word_EN):
    def set_high_numwords(self, high):
        self.cards[10 ** 17] = "shankha"
        self.cards[10 ** 15] = "padam"
        self.cards[10 ** 13] = "neel"
        self.cards[10 ** 11] = "kharba"
        self.cards[10 ** 9] = "arba"
        self.cards[10 ** 7] = "crore"
        self.cards[10 ** 5] = "lakh"
