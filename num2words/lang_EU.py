# -*- encoding: utf-8 -*-
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

from .base import Num2Word_Base
from .currency import parse_currency_parts, prefix_currency

GENERIC_DOLLARS = ('dollar', 'dollars')
GENERIC_CENTS = ('cent', 'cents')

"""
Source: http://publications.europa.eu/code/en/en-5000500.htm
"""
CURRENCIES = {
    'AUD': (GENERIC_DOLLARS, GENERIC_CENTS),
    'CAD': (GENERIC_DOLLARS, GENERIC_CENTS),
    # repalced by EUR
    'EEK': (('kroon', 'kroons'), ('sent', 'senti')),
    'EUR': (('euro', 'euro'), GENERIC_CENTS),
    'GBP': (('pound sterling', 'pounds sterling'), ('penny', 'pence')),
    # replaced by EUR
    'LTL': ('litas', 'litas', GENERIC_CENTS),
    # replaced by EUR
    'LVL': (('lat', 'lats'), ('santim', 'santims')),
    'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
    'RUB': (('rouble', 'roubles'), ('kopek', 'kopeks')),
    'SEK': (('krona', 'kronor'), ('öre', 'öre')),
    'NOK': (('krone', 'kroner'), ('øre', 'øre')),
    'PLN': (('zloty', 'zlotys', 'zlotu'), ('grosz', 'groszy')),
}

PREFIXES = {
    'AUD': 'Australian',
    'CAD': 'Canadian',
    'EEK': 'Estonian',
    'USD': 'US',
    'RUB': 'Russian',
    'NOK': 'Norwegian',
}


def pluralize(n, forms):
    form = 0 if n == 1 else 1
    return forms[form]


class Num2Word_EU(Num2Word_Base):
    def set_high_numwords(self, high):
        max = 3 + 6 * len(high)

        for word, n in zip(high, range(max, 3, -6)):
            self.cards[10 ** n] = word + "illiard"
            self.cards[10 ** (n - 3)] = word + "illion"

    def base_setup(self):
        lows = ["non", "oct", "sept", "sext", "quint", "quadr", "tr", "b", "m"]
        units = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "sept",
                 "octo", "novem"]
        tens = ["dec", "vigint", "trigint", "quadragint", "quinquagint",
                "sexagint", "septuagint", "octogint", "nonagint"]
        self.high_numwords = ["cent"] + self.gen_high_numwords(units, tens,
                                                               lows)

    def to_currency(self, val, longval=True, jointxt="", **kwargs):
        if 'currency' in kwargs:
            return self._to_currency(val, **kwargs)

        return self.to_splitnum(val, hightxt="Euro/s", lowtxt="Euro cent/s",
                                jointxt=jointxt, longval=longval)

    def _to_currency(self, val, currency='EUR', cents=True, seperator=',',
                     prefix=False):
        left, right, is_negative = parse_currency_parts(val)
        cr1, cr2 = CURRENCIES[currency]

        if prefix and currency in PREFIXES:
            cr1 = prefix_currency(PREFIXES[currency], cr1)

        minus_str = "minus " if is_negative else ""
        cents_str = self.to_cardinal(right) if cents else "%02d" % right

        return u'%s%s %s%s %s %s' % (
            minus_str,
            self.to_cardinal(left),
            pluralize(left, cr1),
            seperator,
            cents_str,
            pluralize(right, cr2)
        )
