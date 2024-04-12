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

import re

from num2words.currency import parse_currency_parts, prefix_currency

from .lang_EU import Num2Word_EU

DOLLAR = ('dolar', 'dolar')
CENTS = ('sentavu', 'sentavu')


class Num2Word_TET(Num2Word_EU):

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
        lows = ["quatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menus "
        self.pointword = "vírgula"
        self.exclude_title = ["resin", "vírgula", "menus"]

        self.mid_numwords = [
            (1000, "rihun"), (100, "atus"), (90, "sianulu"),
            (80, "ualunulu"), (70, "hitunulu"), (60, "neenulu"),
            (50, "limanulu"), (40, "haatnulu"), (30, "tolunulu"),
            (20, "ruanulu")
        ]
        self.low_numwords = [
            "sanulu",
            "sia", "ualu", "hitu", "neen", "lima", "haat", "tolu", "rua",
            "ida", "mamuk"
        ]
        self.ords = [
            {
                0: "",
                1: "dahuluk",
                2: "daruak",
                3: "datoluk",
                4: "dahaat",
                5: "dalimak",
                6: "daneen",
                7: "dahituk",
                8: "daualuk",
                9: "dasiak",
            },
            {
                0: "",
                1: "dasanuluk",
                2: "daruanuluk",
                3: "datolunuluk",
                4: "dahaatnuluk",
                5: "dalimanuluk",
                6: "daneenuluk",
                7: "dahitunuluk",
                8: "daualunuk",
                9: "dasianuluk",
            },
            {
                0: "",
                1: "daatus idak",
                2: "daatus ruak",
                3: "daatus toluk",
                4: "daatus haat",
                5: "daatus limak",
                6: "daatus neen",
                7: "daatus hituk",
                8: "daatus ualuk",
                9: "daatus siak",
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
            1: "atus",
            2: "atus rua",
            3: "atus tolu",
            4: "atus haat",
            5: "atus lima",
            6: "atus neen",
            7: "atus hitu",
            8: "atus ualu",
            9: "atus sia",
        }

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1 and nnum < 100:
            return next

        if nnum < cnum:
            if nnum < 10:
                return ("%s resin %s" % (ctext, ntext), cnum + nnum)
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
            if re.match('.*{} resin \\w*entus? (?=.*resin)'.format(ext), result):
                result = result.replace(
                    f'{ext} resin', f'{ext}'
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
        try:
            assert int(value) == value
        except (ValueError, TypeError, AssertionError):
            return self.to_cardinal_float(value)

        out = ""
        if value < 0:
            value = abs(value)
            out = "%s " % self.negword.strip()

        if value >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (value, self.MAXVAL))

        val = self.splitnum(value)
        outs = val
        while len(val) != 1:
            outs = []
            left, right = val[:2]
            if isinstance(left, tuple) and isinstance(right, tuple):
                outs.append(self.merge(left, right))
                if val[2:]:
                    outs.append(val[2:])
            else:
                for elem in val:
                    if isinstance(elem, list):
                        if len(elem) == 1:
                            outs.append(elem[0])
                        else:
                            outs.append(self.clean(elem))
                    else:
                        outs.append(elem)
            val = outs
        words, num = outs[0]
        if num in [90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 5, 3, 2]:
            words = 'da'+words+'k'
        if num in [6,4]:
            words = 'da'+words
        if num == 1:
            words = 'dahuluk'
        if num in [900, 800, 700, 500, 300, 200, 100]:
            words = 'da'+words+'k'
        if num in [600, 400]:
            words = 'da'+words

        liafuan = words.split()
        if len(liafuan) >= 3 and num < 100:
            lia_primeiro = 'da'+liafuan[0]+'k'
            lia_segundo = " ".join(liafuan[1:])
            words = lia_primeiro+" "+lia_segundo

        liafuan_primeiro =  'da'+liafuan[0]
        if liafuan_primeiro == 'daatus' and len(liafuan) >=3:
            test_lia = liafuan[1]
            if test_lia in ['haat', 'neen']:
                liafuan_segundo = liafuan[1]
            else:
                liafuan_segundo = liafuan[1]+'k'
            liafuan_terseiro = " ".join(liafuan[2:])
            words = liafuan_primeiro+" "+liafuan_segundo+" "+liafuan_terseiro

        if len(str(num)) >= 4:
            words = 'da'+words

        return self.title(out + words)

    def to_ordinal_num(self, value):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        self.verify_ordinal(value)
        return "%sº" % (value)

    def to_year(self, val, longval=True):
        # Before changing this function remember this is used by pt-BR
        # so act accordingly
        if val < 0:
            return self.to_cardinal(abs(val)) + ' antes Kristu'
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

        return u'%s%s %s %s %s' % (
            minus_str,
            self.pluralize(left, cr1),
            money_str,
            self.pluralize(right, cr2),
            cents_str
        )

