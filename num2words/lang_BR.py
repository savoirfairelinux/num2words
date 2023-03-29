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


def _vigesimal(val):
    """Helper function for splitting breton numbers into two parts"""
    two_digits = val % 100
    hundreds = val - two_digits
    special_values = [0, 20, 30, 40, 50, 60, 80, 100]
    if two_digits in special_values:
        units_part = two_digits
    else:
        units_part = min(
            (two_digits - x for x in special_values[:-1] if two_digits - x > 0),
            default=0)
    return hundreds + units_part, val - hundreds - units_part


class Num2Word_BR(Num2Word_EU):
    """Breton spelling for numbers
    Some details taken from http://www.preder.net/r/bibli/jedoniezh_6ved.pdf and
    http://www.culture-bretagne.net/wp-content/uploads/2017/05/liste-montants-rediger-cheque-breton.pdf
    And from teachers and students from the Skol Diwan, Saint-Herblain
    """
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euro'), ('santim', 'santim')),
        'USD': (('dollar', 'dollar'), ('sent', 'sent')),
        'FRF': (('lur', 'lur'), ('santim', 'santim')),
        # https://br.wikipedia.org/wiki/Lur_sterling
        'GBP': (('lur sterling', 'lur sterling'), ('penny', 'penny')),
    }
    MEGA_SUFFIX = "ilion"
    GIGA_SUFFIX = "iliard"

    def setup(self):
        Num2Word_EU.setup(self)
        self.negword = "nemet "
        self.pointword = "skej"
        self.errmsg_nonnum = (
            "mar ha nemet mar an niver eo, e c'haller treiñ anezho e gerioù."
        )
        self.errmsg_toobig = "nemet an niver a c'haller treiñ e gerioù."
        self.exclude_title = ["ha", "skej", "nemet"]
        self.mid_numwords = [(1000, "mil"), (100, "kant"),
                             (80, "pevar-ugent"), (60, "tri-ugent"),
                             (50, "hanter-kant"), (40, "daou-ugent"),
                             (30, "tregont")]
        self.low_numwords = ['ugent', 'naontek', "triwec'h", 'seitek',
                             "c'hwezek", 'pemzek', 'pevarzek', 'trizek',
                             'daouzek', 'unnek', 'dek', 'nav', 'eizh',
                             'seizh', "c'hwec'h", 'pemp', 'pevar', 'tri',
                             'daou', 'unan', 'zero']


    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
        # Mutations:
        if ntext == "kant" and ctext in ["daou", "tri", "pevar", "nav"]:
            ntext = "c'hant"
        if ntext.startswith("mil") and ctext == "daou":
            ntext = "vil" + ntext[3:]
        if nnum < cnum < 100:
            if cnum < 30:
                and_ = "warn"
            elif cnum == 50:
                and_ = "hag"
            else:
                and_ = "ha"
            if nnum % 10 == 1 and cnum != 80:
                return ("%s %s %s" % (ntext, and_, ctext), cnum + nnum)
            return ("%s %s %s" % (ntext, and_, ctext), cnum + nnum)
        if nnum > cnum:
            return ("%s %s" % (ctext, ntext), cnum * nnum)
        return ("%s %s" % (ctext, ntext), cnum + nnum)

    # according to https://fr.wiktionary.org/wiki/Mod%C3%A8le:ordinaux_en_breton
    def to_ordinal(self, value):
        self.verify_ordinal(value)
        ordinals = {1: 'kentañ',
                    2: 'eil',
                    3: 'trede',
                    4: 'pevare',
                    }
        if value in ordinals:
            return ordinals[value]
        value, scores = _vigesimal(value)
        word = self.to_cardinal(value)
        word = word + "vet"
        if scores:
            and_ = " hag " if scores == 50 else " ha "
            word += and_ + self.to_cardinal(scores)
        word = word.replace("ha ugent", "warn ugent")
        return word

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        ordinal_nums = {1: '1añ',
                        2: '2l',
                        3: '3e',
                        4: '4e',
                        }
        if value in ordinal_nums:
            return ordinal_nums[value]
        out = str(value)
        out += "vet"
        return out

    def to_currency(self, val, currency='EUR', cents=True, separator=',',
                    adjective=False):
        """For all values with units in breton (currency, measurements, ...) the 'twenties'
        part (20, 30, ...) is placed after the units unless there is no digit after the
        twenties part (20 euros is simply ugent euro but 21 euros is un euro warn ugent)
        https://www.culture-bretagne.net/comment-ecrire-cheque-en-breton/
        """
        euros = int(val)
        centimes = round(100 * val) % 100
        _, euros_2 = _vigesimal(euros)
        _, cents_2 = _vigesimal(centimes)
        result = super(Num2Word_BR, self).to_currency(
            (val - euros_2 - cents_2 / 100), currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        result = result.replace("unan ", "un ")
        (currency_name, _), (cents_name, _) = self.CURRENCY_FORMS[currency]
        if euros_2:
            result = result.replace(currency_name,
                                    currency_name + " ha " + Num2Word_BR().to_cardinal(euros_2)
                                    )
        if cents_2:
            result = result.replace(cents_name,
                                    cents_name + " ha " + Num2Word_BR().to_cardinal(cents_2)
                                    )
        result = result.replace("ha ugent", "warn ugent").replace("ha hanter", "hag hanter")
        return result
