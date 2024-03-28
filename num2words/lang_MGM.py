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

from .lang_EU import Num2Word_EU

DOLLAR = ('dólar', 'dólares')
CENTS = ('cêntimu', 'cêntimus')


class Num2Word_MGM(Num2Word_EU):

    CURRENCY_FORMS = {
        'AUD': (DOLLAR, CENTS),
        'CAD': (DOLLAR, CENTS),
        'EUR': (('euru', 'eurus'), CENTS),
        'GBP': (('libra', 'libras'), ('péni', 'pence')),
        'USD': (DOLLAR, CENTS),
    }

    GIGA_SUFFIX = None
    MEGA_SUFFIX = "iliaunid"

    def setup(self):
        super().setup()
        lows = ["quatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menus "
        self.pointword = "vírgula"
        self.exclude_title = ["resi", "vírgula", "menus"]

        self.mid_numwords = [
            (1000, "rihunid"), (100, "atusid"), (90, "gulhohopat"),
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
                1: "primeir",
                2: "segund",
                3: "terceir",
                4: "quart",
                5: "quint",
                6: "sext",
                7: "sétim",
                8: "oitav",
                9: "non",
            },
            {
                0: "",
                1: "décim",
                2: "vigésim",
                3: "trigésim",
                4: "quadragésim",
                5: "quinquagésim",
                6: "sexagésim",
                7: "septuagésim",
                8: "octogésim",
                9: "nonagésim",
            },
            {
                0: "",
                1: "centésim",
                2: "ducentésim",
                3: "tricentésim",
                4: "quadrigentésim",
                5: "quingentésim",
                6: "seiscentésim",
                7: "septigentésim",
                8: "octigentésim",
                9: "nongentésim",
            },
        ]
        self.thousand_separators = {
            3: "milésim",
            6: "milionésim",
            9: "milésim milionésim",
            12: "bilionésim",
            15: "milésim bilionésim"
        }
        self.hundreds = {
            1: "atusid",
            2: "atusid ru",
            3: "atusid teil",
            4: "atusid pat",
            5: "atusid lim",
            6: "atusid hohonid",
            7: "atusid hohoru",
            8: "atusid hohoteil",
            9: "atusid hohopat",
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
                'rihunid', 'miliaunid','miliaunid rihunid',
                'biliaunid', 'biliaunid rihunid'):
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

        if result.startswith('primeir') and value != '1':
            # avoiding "primeiro milésimo", "primeiro milionésimo" and so on
            result = result[9:]

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

    def to_currency(self, val, currency='EUR', cents=True, separator=' resi',
                    adjective=False):
        # change negword because base.to_currency() does not need space after
        backup_negword = self.negword
        self.negword = self.negword[:-1]
        result = super().to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # undo the change on negword
        self.negword = backup_negword

        # transforms "milhões euros" em "milhões de euros"
        cr1, _ = self.CURRENCY_FORMS[currency]

        for ext in (
                'miliaunid','biliaunid','triliaunid'):
            if re.match('.*{} (?={})'.format(ext, cr1[1]), result):
                result = result.replace(
                    f'{ext}', f'{ext}', 1
                )
        # do not print "e zero cêntimos"
        result = result.replace(' resi mamu cêntimus', '')
        return result
