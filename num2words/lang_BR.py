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


class Num2Word_BR(Num2Word_EU):
    """Breton spelling for numbers
    Some details taken from http://www.preder.net/r/bibli/jedoniezh_6ved.pdf and
    http://www.culture-bretagne.net/wp-content/uploads/2017/05/liste-montants-rediger-cheque-breton.pdf
    And from teachers from the Skol Diwan, Saint-Herblain
    """
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euro'), ('santim', 'santim')),
        'USD': (('dollar', 'dollarioù'), ('sent', 'sent')),
        'FRF': (('lur', 'lur'), ('kantim', 'kantim')),
        'GBP': (('lur sterling', 'lur sterling'), ('sent sterling', 'sent sterling')),
    }
    MEGA_SUFFIX = "ilion"
    GIGA_SUFFIX = "iliard"

    def setup(self):
        Num2Word_EU.setup(self)

        self.negword = "nemet "
        self.pointword = "skej"
        self.errmsg_nonnum = (
            u"Seulement des nombres peuvent être convertis en mots."
        )
        self.errmsg_toobig = u"Nombre trop grand pour être converti en mots."
        self.exclude_title = ["ha", "skej", "nemet"]
        self.mid_numwords = [(1000, "mil"), (100, "kant"),
                             (80, "pevar-ugent"), (60, "tri-ugent"),
                             (50, "hanter-kant"), (40, "daou-ugent"),
                             (30, "tregont")]
        self.low_numwords = ['ugent', 'naontek', "triwec'h", 'seitek', "c'hwezek", 'pemzek', 'pevarzek', 'trizek',
                             'daouzek', 'unnek', 'dek', 'nav', 'eizh', 'seizh', "c'hwec'h", 'pemp', 'pevar', 'tri',
                             'daou', 'unan', 'zero']
        self.ords = {
            "cinq": "cinquième",
            "neuf": "neuvième",
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
        else:
            if (not (cnum - 80) % 100
                or (not cnum % 100 and cnum < 1000)) \
                    and nnum < 1000000 \
                    and ctext[-1] == "s":
                ctext = ctext[:-1]
            # if cnum < 1000 and nnum != 1000 and \
            #         ntext[-1] != "s" and not nnum % 100:
            #     ntext += "s"
        # Mutations:
        if ntext == "kant" and ctext in ["daou", "tri", "pevar", "nav"]:
            ntext = "c'hant"
        if ntext.startswith("mil") and ctext == "daou":
            ntext = "vil" + ntext[3:]
        if nnum < cnum < 100:
            if cnum < 30:
                and_ = "warn"
            else:
                and_ = "ha"
            if nnum % 10 == 1 and cnum != 80:
                return ("%s %s %s" % (ntext, and_,ctext), cnum + nnum)
            return ("%s %s %s" % (ntext, and_, ctext), cnum + nnum)
        if nnum > cnum:
            return ("%s %s" % (ctext, ntext), cnum * nnum)
        return ("%s %s" % (ctext, ntext), cnum + nnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 1:
            return "premier"
        word = self.to_cardinal(value)
        for src, repl in self.ords.items():
            if word.endswith(src):
                word = word[:-len(src)] + repl
                break
        else:
            if word[-1] == "e":
                word = word[:-1]
            word = word + "ième"
        return word

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        out = str(value)
        out += "er" if value == 1 else "me"
        return out

    def to_currency(self, val, currency='EUR', cents=True, separator=' et',
                    adjective=False):
        result = super(Num2Word_BR, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        return result
