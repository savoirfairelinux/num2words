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
from __future__ import division, unicode_literals

import re

from . import lang_PT


class Num2Word_PT_BR(lang_PT.Num2Word_PT):
    def set_high_numwords(self, high):
        max = 3 + 3*len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10**n] = word + "ilhão"

    def setup(self):
        super(Num2Word_PT_BR, self).setup()

        self.low_numwords[1] = 'dezenove'
        self.low_numwords[3] = 'dezessete'
        self.low_numwords[4] = 'dezesseis'

        self.thousand_separators = {
            3: "milésimo",
            6: "milionésimo",
            9: "bilionésimo",
            12: "trilionésimo",
            15: "quadrilionésimo"
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "um"
        elif cnum == 100 and not nnum == 1000:
            ctext = "cento"

        if nnum < cnum:
            if cnum < 100:
                return ("%s e %s" % (ctext, ntext), cnum + nnum)
            return ("%s e %s" % (ctext, ntext), cnum + nnum)

        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-4] + "lhões"

        if nnum == 100:
            ctext = self.hundreds[cnum]
            ntext = ""

        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)

    def to_cardinal(self, value):
        result = lang_PT.Num2Word_EU.to_cardinal(self, value)

        # Transforms "mil E cento e catorze reais" into "mil, cento e catorze
        # reais"
        for ext in (
                'mil', 'milhão', 'milhões', 'bilhão', 'bilhões',
                'trilhão', 'trilhões', 'quatrilhão', 'quatrilhões'):
            if re.match('.*{} e \\w*ento'.format(ext), result):
                result = result.replace(
                    '{} e'.format(ext), '{},'.format(ext), 1
                )

        return result

    def to_currency(self, val, longval=True):
        integer_part, decimal_part = ('%.2f' % val).split('.')

        result = self.to_cardinal(int(integer_part))

        appended_currency = False
        for ext in (
                'milhão', 'milhões', 'bilhão', 'bilhões',
                'trilhão', 'trilhões', 'quatrilhão', 'quatrilhões'):
            if result.endswith(ext):
                result += ' de reais'
                appended_currency = True

        if result in ['um', 'menos um']:
            result += ' real'
            appended_currency = True
        if not appended_currency:
            result += ' reais'

        if int(decimal_part):
            cents = self.to_cardinal(int(decimal_part))
            result += ' e ' + cents

            if cents == 'um':
                result += ' centavo'
            else:
                result += ' centavos'

        return result

    def to_date(self, val):
        map_month = {
            u'01':'janeiro',     u'1':'janeiro'
            u'02':'fevereiro',   u'2':'fevereiro',
            u'03':'março',       u'3':'março',
            u'04':'abril',       u'4':'abril',
            u'05':'maio',        u'5':'maio',
            u'06':'junho',       u'6':'junho',
            u'07':'julho',       u'7':'julho',
            u'08':'agosto',      u'8':'agosto',
            u'09':'setembro',    u'9':'setembro',
            u'10':'outubro',
            u'11':'novembro',
            u'12':'dezembro',
        }

        # NOTE supports only dd/mm/[yy|yyyy]
        day          = '(3[0-1]|[12][0-9]|0?[1-9])'
        month        = '(1[0-2]|[0]?[1-9])'
        year         = '(1[4-9]|2[0-1])([0-9][0-9])'
        short_year   = '([09][0-9]|1[0-9])'
        pattern_date = re.compile(r'^%s/%s/(%s|%s)$' % \
                    (day, month, year, short_year))

        if re.search(pattern_date, val) is None:
            print('deu ruim')
            return None

        vals  = val.split('/')

        year = vals[-1]
        if int(year) < 20:
            year = '20' + year
        year = self.str_to_number(year)
        year = self.to_cardinal(year)

        month = vals[-2]
        month = map_month[month]

        day = vals[-3]
        day = self.str_to_number(day)
        if day == 1:
            day = self.to_ordinal(day)
        else:
            day = self.to_cardinal(day)
        return '%s de %s de %s' % (day, month, year)
