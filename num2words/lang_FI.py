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

from __future__ import division, print_function, unicode_literals

from . import lang_EU
from .currency import parse_currency_parts


def numword_inflect_partitive(rpair):
    """Inflect a numword to the partitive case"""
    # should be used only if lnum < rnum and lnum is not 1
    # inflects rtext to the partitive case
    # references:
    # https://fi.wikipedia.org/wiki/Partitiivi <-- about the partitive case
    # https://fi.wiktionary.org/wiki/sata#Taivutus <-- cardinal 100
    # https://fi.wiktionary.org/wiki/tuhat#Taivutus <-- cardinal 1000
    # etc.
    rtext, rnum = rpair
    if rnum == 100:
        return "sataa"
    elif rnum == 1000:
        return "tuhatta"
    # miljoona+a, miljardi+a, biljoona+a, triljoona+a, ...
    elif rnum == 10 ** 9 or rnum % 10 ** 6 == 0:
        return rtext + "a"
    # shouldn't happen
    else:
        raise ValueError(
            "'%s' can't be inflected to the partitive case" % rtext)


def pluralize_currency(value, unit):
    """Inflect currency unit (euro or sentti) to partitive when value is
    not 1"""
    if value == 1:
        return unit
    else:
        if unit == "euro":
            return "euroa"
        elif unit == "sentti":
            return "senttiä"
        else:
            raise NotImplementedError


class Num2Word_FI(lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        # references:
        # https://fi.wikipedia.org/wiki/Suurten_lukujen_nimet
        # https://en.wikipedia.org/wiki/Names_of_large_numbers#Standard_dictionary_numbers  # NOQA

        # translate to Finnish
        replacements = [
            ("qu", "kv"),
            ("x", "ks"),
            ("c", "k"),
            ("kent", "sent"),  # applied after c -> k to cent
        ]
        translated = []
        for i, numword in enumerate(high):
            # notes:
            # - 1e6**9 can be either noviljoona or noniljoona
            # - 1e6**38 and above are untested

            # 1e6**6 is sekstiljoona but 1e6**16 is sedekiljoona
            if numword.startswith("sex") and numword != "sext":
                numword = numword.replace("sex", "se")
            # 1e6**7 is septiljoona but 1e6**17 is septendekiljoona
            elif numword.startswith("sept") and numword != "sept":
                numword = "septen" + numword[len("sept"):]
            # 1e6**8 is oktiljoona but 1e6**18 is duodevigintiljoona
            # (2 from 20)
            elif numword.startswith("octo"):
                numword = high[i + -10]
                numword = "duode" + numword[len("octo"):]
            # 1e6**9 is noniljoona but 1e6**19 is undevigintiljoona (1 from 20)
            elif numword.startswith("nove"):
                numword = high[i + -10]
                numword = "unde" + numword[len("nove") + 1:]

            # apply general replacements to all numwords
            for repl in replacements:
                numword = numword.replace(repl[0], repl[1])
            translated.append(numword)

        max = 6 * len(translated)
        for word, n in zip(translated, range(max, 0, -6)):
            if n == 6:
                # irregularity considering short scale and long scale
                self.cards[10 ** 9] = "miljardi"
            self.cards[10 ** n] = word + "iljoona"

    def setup(self):
        self.negword = "miinus "
        self.pointword = "pilkku"
        self.errmsg_nornum = "Vain numerot voidaan muuttaa sanoiksi."
        self.exclude_title = ["pilkku", "miinus"]

        self.mid_numwords = [
            (1000, "tuhat"),
            (100, "sata"),
            (90, "yhdeksänkymmentä"),
            (80, "kahdeksankymmentä"),
            (70, "seitsemänkymmentä"),
            (60, "kuusikymmentä"),
            (50, "viisikymmentä"),
            (40, "neljäkymmentä"),
            (30, "kolmekymmentä"),
        ]

        self.low_numwords = [
            "kaksikymmentä",
            "yhdeksäntoista",
            "kahdeksantoista",
            "seitsemäntoista",
            "kuusitoista",
            "viisitoista",
            "neljätoista",
            "kolmetoista",
            "kaksitoista",
            "yksitoista",
            "kymmenen",
            "yhdeksän",
            "kahdeksan",
            "seitsemän",
            "kuusi",
            "viisi",
            "neljä",
            "kolme",
            "kaksi",
            "yksi",
            "nolla",
        ]

        self.ords = {
            "nolla": "nollas",
            "yksi": "ensimmäinen",
            "kaksi": "toinen",
            "kolme": "kolmas",
            "neljä": "neljäs",
            "viisi": "viides",
            "kuusi": "kuudes",
            "seitsemän": "seitsemäs",
            "kahdeksan": "kahdeksas",
            "yhdeksän": "yhdeksäs",
            "kymmenen": "kymmenes",
            "yksitoista": "yhdestoista",
            "kaksitoista": "kahdestoista",
            "kolmetoista": "kolmastoista",
            "neljätoista": "neljästoista",
            "viisitoista": "viidestoista",
            "kuusitoista": "kuudestoista",
            "seitsemäntoista": "seitsemästoista",
            "kahdeksantoista": "kahdeksastoista",
            "yhdeksäntoista": "yhdeksästoista",
            "kaksikymmentä": "kahdeskymmenes",
        }

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        # http://www.kielitoimistonohjepankki.fi/ohje/49
        fmt = "%s%s"
        # ignore lpair if lnum is 1
        if lnum == 1:
            return rpair
        # rnum is added to lnum
        elif lnum > rnum:
            # separate groups with space
            if lnum >= 1000:
                fmt = "%s %s"
            return (fmt % (ltext, rtext), lnum + rnum)
        # rnum is multiplied by lnum
        elif lnum < rnum:
            rtext = numword_inflect_partitive(rpair)
            return (fmt % (ltext, rtext), lnum * rnum)

    def to_ordinal(self, value):
        """Not very useful without all the possible inflections the ordinal can
        have. Hard to implement"""
        raise NotImplementedError

    def to_ordinal_num(self, value):
        """Not very useful without all the possible inflections the ordinal can
        have. Hard to implement"""
        raise NotImplementedError

    def to_year(self, val, suffix=None, longval=True):
        suffix = suffix or ""
        if val < 0:
            val = abs(val)
            suffix = suffix or " ennen ajanlaskun alkua"
        return self.to_cardinal(val).replace(" ", "") + suffix

    def to_currency(self, val, currency="EUR", cents=True, seperator=" ja",
                    adjective=False):
        if currency != "EUR":
            raise NotImplementedError

        left, right, is_negative = parse_currency_parts(val)
        cr1, cr2 = ("euro", "sentti")
        minus_str = self.negword if is_negative else ""
        cents_str = self.to_cardinal(right)

        return u'%s%s %s%s %s %s' % (
            minus_str,
            self.to_cardinal(left),
            pluralize_currency(left, cr1),
            seperator,
            cents_str,
            pluralize_currency(right, cr2)
        )
