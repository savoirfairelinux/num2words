# -*- coding: utf-8 -*-Num2Word_TET
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

from __future__ import division, unicode_literals
from num2words.currency import parse_currency_parts, prefix_currency

import re

from .lang_EU import Num2Word_EU

DOLLAR = ('dolar', 'dolar')
CENTS = ('sentavu', 'sentavu')


class Num2Word_MGM(Num2Word_EU):

    CURRENCY_FORMS = {
        'AUD': (DOLLAR, CENTS),
        'CAD': (DOLLAR, CENTS),
        'EUR': (('euro', 'euros'), CENTS),
        'GBP': (('pound sterling', 'pound sterling'), ('pence', 'pence')),
        'USD': (DOLLAR, CENTS),
    }

    GIGA_SUFFIX = None
    MEGA_SUFFIX = "iliaun"

    def setup(self):
        super().setup()
        lows = ["kuatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menus "
        self.pointword = "vírgula"
        self.exclude_title = ["resi", "vírgula", "menus"]

        self.mid_numwords = [
            (1000, "rihun"), (100, "atus"), (90, "guul hoho paat"),
            (80, "guul hoho teil"), (70, "guul hoho ruu"), (60, "guul hohon iid"),
            (50, "guul liim"), (40, "guul paat"), (30, "guul teil"),
            (20, "guul ruu")
        ]
        self.low_numwords = [
            "saguul",
            "hoho paat", "hoho teil", "hoho ruu", "hohon iid", "liim", "paat", "teil", "ruu",
            "iid", "mamu"
        ]
        self.hundreds = {
            1: "atus iid",
            2: "atus ruu",
            3: "atus teil",
            4: "atus paat",
            5: "atus liim",
            6: "atus hohon iid",
            7: "atus hohon ruu",
            8: "atus hoho teil",
            9: "atus hoho paat",
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1 and nnum < 100:
            return next

        if nnum < cnum:
            if nnum < 10:
                return ("%s resi %s" % (ctext, ntext), cnum + nnum)
            else:
                return ("%s %s" % (ctext, ntext), cnum + nnum)

        return (ntext + " " + ctext, cnum * nnum)

    def to_cardinal(self, value):
        result = super().to_cardinal(value)

        for ext in (
                'rihun', 'miliaun','miliaun rihun',
                'biliaun', 'biliaun rihun'):
            if re.match('.*{} resi \\w*entus? (?=.*resi)'.format(ext), result):
                result = result.replace(
                    f'{ext} resi', f'{ext}'
                )

        return result

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        result = super().to_cardinal(value)
        result = 'da'+result
        return result

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%sº" % (value)

    def to_year(self, val, longval=True):
        if val < 0:
            return self.to_cardinal(abs(val)) + ' muna Kristu'
        return self.to_cardinal(val)

    def to_currency(self, val, currency='USD', cents=True,
                    adjective=False):
        """
        Args:
            val: Numeric value
            currency (str): Currency code
            cents (bool): Verbose cents
            adjective (bool): Prefix currency name with adjective
        Returns:
            str: Formatted string
        """
        left, right, is_negative = parse_currency_parts(val)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]
        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            cr1 = prefix_currency(self.CURRENCY_ADJECTIVES[currency], cr1)

        minus_str = "%s " % self.negword.strip() if is_negative else ""
        money_str = self._money_verbose(left, currency)
        cents_str = self._cents_verbose(right, currency) \
            if cents else self._cents_terse(right, currency)

        if right == 0:
            return u'%s%s %s' % (
                minus_str,
                self.pluralize(left, cr1),
                money_str
            )
        else:

            return u'%s%s %s %s %s' % (
                minus_str,
                self.pluralize(left, cr1),
                money_str,
                self.pluralize(right, cr2),
                cents_str
            )
