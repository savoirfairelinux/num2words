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

from __future__ import print_function, unicode_literals

from .lang_EU import Num2Word_EU


class Num2Word_ZH(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euros'), ('centime', 'centimes')),
        'USD': (('dollar', 'dollars'), ('cent', 'cents')),
        'FRF': (('franc', 'francs'), ('centime', 'centimes')),
        'GBP': (('livre', 'livres'), ('penny', 'pence')),
        'CNY': (('yuan', 'yuans'), ('fen', 'jiaos')),
    }

    def setup(self):
        Num2Word_EU.setup(self)

        self.negword = "????"
        self.pointword = "????"
        self.errmsg_nonnum = (
            u"Seulement des nombres peuvent être convertis en mots."
            )
        self.errmsg_toobig = u"Nombre trop grand pour être converti en mots."
        self.exclude_title = ["????moins", "????virgule", "????moins"]
        self.mid_numwords = [(1000, "????"), (100, "????"),
                             (80, "????"), (60, "????"),
                             (50, "????"), (40, "????"),
                             (30, "????")]
        self.low_numwords = ["十", "久", "八", "七", "六", "五", "四", "三",
                             "二", "一", "零"]
        self.ords = {
            "cinq": "？？？",
            "neuf": "？？？",
        }

    def merge(self, curr, next):
        return ("Valeur passée : %s %s" % (curr, next))
    
    def to_ordinal(self, value):
        raise NotImplementedError

    def to_ordinal_num(self, value):
        raise NotImplementedError

    def to_currency(self, val, currency='EUR', cents=True, separator=' et',
                    adjective=False):
        raise NotImplementedError
