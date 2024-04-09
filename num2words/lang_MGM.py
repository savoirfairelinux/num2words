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
            (1000, "rihun"), (100, "atus"), (90, "gulhohopat"),
            (80, "gulhohoteil"), (70, "gulhohoru"), (60, "gulhohonid"),
            (50, "gullim"), (40, "gulpat"), (30, "gulteil"),
            (20, "gulru")
        ]
        self.low_numwords = [
            "sagul",
            "hohopat", "hohoteil", "hohoru", "hohonid", "lim", "pat", "teil", "ru",
            "id", "mamu"
        ]
        self.ords = [
            {
                0: "",
                1: "daid",
                2: "daru",
                3: "dateil",
                4: "dapat",
                5: "dalim",
                6: "dahohonid",
                7: "dahohoru",
                8: "dahohoteil",
                9: "dahohopat",
            },
            {
                0: "",
                1: "dasagul",
                2: "dagulru",
                3: "dagulteil",
                4: "dagulpat",
                5: "dagullim",
                6: "dagulhohonid",
                7: "dagulhohoru",
                8: "dagulhohoteil",
                9: "dagulhohopat",
            },
            {
                0: "",
                1: "daatusid",
                2: "daatusru",
                3: "daatusteil",
                4: "daatuspat",
                5: "daatuslim",
                6: "daatushohonid",
                7: "daatushohoru",
                8: "daatushohoteil",
                9: "daatushohopat",
            },
        ]
        self.thousand_separators = {
            3: "darihun",
            6: "damiliaun",
            9: "darihun damiliaun",
            12: "dabiliaun",
            15: "darihun dabiliaun"
        }
        self.hundreds = {
            1: "atus id",
            2: "atus ru",
            3: "atus teil",
            4: "atus pat",
            5: "atus lim",
            6: "atus hohonid",
            7: "atus hohoru",
            8: "atus hohoteil",
            9: "atus hohopat",
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

        # Transforms "mil e cento e catorze" into "mil cento e catorze"
        # Transforms "cem milhões e duzentos mil e duzentos e dez" em "cem
        # milhões duzentos mil duzentos e dez" but "cem milhões e duzentos
        # mil e duzentos" in "cem milhões duzentos mil e duzentos" and not in
        # "cem milhões duzentos mil duzentos"
        for ext in (
                'rihun', 'miliaun','miliaun rihun',
                'biliaun', 'biliaun rihun'):
            if re.match('.*{} resi \\w*entus? (?=.*resi)'.format(ext), result):
                result = result.replace(
                    f'{ext} resi', f'{ext}'
                )

        return result

    # for the ordinal conversion the code is similar to pt_BR code,
    # although there are other rules that are probably more correct in
    # Portugal. Concerning numbers from 2000th on, saying "dois
    # milésimos" instead of "segundo milésimo" (the first number
    # would be used in the cardinal form instead of the ordinal) is better.
    # This was not implemented.
    # source:
    # https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/a-forma-por-extenso-de-2000-e-de-outros-ordinais/16428
    def to_ordinal(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)

        result = []
        value = str(value)
        thousand_separator = ''

        for idx, char in enumerate(value[::-1]):
            if idx and idx % 3 == 0:
                thousand_separator = self.thousand_separators[idx]

            if char != '0' and thousand_separator:
                # avoiding "segundo milionésimo milésimo" for 6000000,
                # for instance
                result.append(thousand_separator)
                thousand_separator = ''

            result.append(self.ords[idx % 3][int(char)])

        result = ' '.join(result[::-1])
        result = result.strip()
        result = re.sub('\\s+', ' ', result)

        if result.startswith('daid') and value != '1':
            # avoiding "primeiro milésimo", "primeiro milionésimo" and so on
            result = result[5:]

        return result

    def to_ordinal_num(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)
        return "%sº" % (value)

    def to_year(self, val, longval=True):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        if val < 0:
            return self.to_cardinal(abs(val)) + ' muna Kristu'
        return self.to_cardinal(val)

    def to_currency(self, val, currency='USD', cents=True,
                    adjective=False):
        cr1, _ = self.CURRENCY_FORMS[currency]
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

        return u'%s%s %s %s %s' % (
            minus_str,
            self.pluralize(left, cr1),
            money_str,
            self.pluralize(right, cr2),
            cents_str
        )
