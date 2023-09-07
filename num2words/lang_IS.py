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

# Genders
KK = 0  # Karlkyn (male)
KVK = 1  # Kvenkyn (female)
HK = 2  # Hvorugkyn (neuter)

GENDERS = {
    "einn": ("einn", "ein", "eitt"),
    "tveir": ("tveir", "tvær", "tvö"),
    "þrír": ("þrír", "þrjár", "þrjú"),
    "fjórir": ("fjórir", "fjórar", "fjögur"),
}

PLURALS = {
    "hundrað": "hundruð",
    "illjón": "illjónir",
    "illjarður": "illjarðar"
}


class Num2Word_IS(lang_EU.Num2Word_EU):

    GIGA_SUFFIX = "illjarður"
    MEGA_SUFFIX = "illjón"

    def setup(self):
        lows = ["non", "okt", "sept", "sext", "kvint", "kvaðr", "tr", "b", "m"]
        units = ["", "un", "dúó", "tre", "kvaður", "kvin", "sex", "sept",
                 "októ", "nóvem"]
        tens = ["des", "vigint", "trigint", "kvaðragint", "kvinkvagint",
                "sexagint", "septúagint", "októgint", "nonagint"]

        self.high_numwords = self.gen_high_numwords(units, tens, lows)

        self.negword = "mínus "
        self.pointword = "komma"

        # All words should be excluded, title case is not used in Icelandic
        self.exclude_title = ["og", "komma", "mínus"]

        self.mid_numwords = [(1000, "þúsund"), (100, "hundrað"),
                             (90, "níutíu"), (80, "áttatíu"), (70, "sjötíu"),
                             (60, "sextíu"), (50, "fimmtíu"), (40, "fjörutíu"),
                             (30, "þrjátíu"), (20, "tuttugu")]
        self.low_numwords = ["nítján", "átján", "sautján",
                             "sextán", "fimmtán", "fjórtán", "þrettán",
                             "tólf", "ellefu", "tíu", "níu", "átta",
                             "sjö", "sex", "fimm", "fjórir", "þrír",
                             "tveir", "einn", "núll"]
        self.ords = {"núll": "núllti",
                     "einn": "fyrsti",
                     "tveir": "annar",
                     "þrír": "þriðji",
                     "fjórir": "fjórði",
                     "fimm": "fimmti",
                     "sex": "sjötti",
                     "sjö": "sjöundi",
                     "átta": "áttundi",
                     "níu": "níundi",
                     "tíu": "tíundi",
                     "ellefu": "ellefti",
                     "tólf": "tólfti",
                     "tuttugu": "tuttugasti",
                     "þrjátíu": "þrítugasti",
                     "fjörutíu": "fertugasti",
                     "fimmtíu": "fimmtugasti",
                     "sextíu": "sextugasti",
                     "sjötíu": "sjötugasti",
                     "áttatíu": "áttugasti",
                     "níutíu": "nítugasti"}

    def pluralize(self, n, forms):
        form = 0 if (n % 10 == 1 and n % 100 != 11) else 1
        return forms[form]

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair

        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif lnum < rnum:
            rtext = self._pluralize(lnum, rtext)
            ltext = self._genderize(ltext, rtext)
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        elif lnum > rnum and rnum in self.cards:
            rtext = self._pluralize(lnum, rtext)
            ltext = self._genderize(ltext, rtext)
            return ("%s og %s" % (ltext, rtext), lnum + rnum)
        return ("%s %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        if outwords[-1] in self.low_numwords and len(outwords) > 1:
            outwords[-3] = self._to_ordinal(outwords[-3])
        outwords[-1] = self._to_ordinal(outwords[-1])
        return " ".join(outwords)

    def _to_ordinal(self, word):
        try:
            return self.ords[word]
        except KeyError:
            if word in self.low_numwords:
                return word + "di"
            elif self.GIGA_SUFFIX[:-2] in word or word[-2:] == "ir":
                word = word[:-2]
            return word + "asti"

    def to_ordinal_num(self, value):
        return "%s." % value

    def to_year(self, val, suffix=None, longval=True):
        raise NotImplementedError

    def to_currency(self, val, longval=True):
        raise NotImplementedError

    def _pluralize(self, val, singular):
        if self.GIGA_SUFFIX in singular:
            suffix = self.GIGA_SUFFIX
            plural = singular.replace(suffix, PLURALS[suffix])
        elif self.MEGA_SUFFIX in singular:
            suffix = self.MEGA_SUFFIX
            plural = singular.replace(suffix, PLURALS[suffix])
        else:
            plural = PLURALS.get(singular, singular)
        forms = (singular, plural)
        return self.pluralize(val, forms)

    def _genderize(self, adj, noun):
        last = adj.split()[-1]
        if last not in GENDERS:
            return adj
        if "hund" in noun or "þús" in noun:
            gender = HK
        elif "illjón" in noun:
            gender = KVK
        else:
            gender = KK
        return adj.replace(last, GENDERS[last][gender])
