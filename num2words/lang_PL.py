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

from __future__ import unicode_literals

import itertools

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = ("zero",)

NAME_TO_CASE = {
    "nominative": 0,
    "genitive": 1,
    "dative": 2,
    "accusative": 3,
    "instrumental": 4,
    "locative": 5,
    "vocative": 6
}

DECIMAL_LEVELS = {
    1: ("dziesiąta", "dziesiąte", "dziesiątych",),
    2: ("setna", "setne", "setnych",),
    3: ("tysięczna", "tysięczne", "tysięcznych",),
    4: ("dziesięciotysięczna", "dziesięciotysięczne", "dziesięciotysięcznych",),
    5: ("stutysięczna", "stutysięczne", "stutysięcznych",),
    6: ("milionowa", "milionowe", "milionowych",),
    7: ("dziesięciomilionowa", "dziesięciomilionowe", "dziesięciomilionowych",),
    8: ("stumilionowa", "stumilionowe", "stumilionowych",),
    9: ("miliardowa", "miliardowe", "miliardowych",),
}

ONES = {
    1: (("jeden", "jednego"), ("jedna", "jednej")),
    2: (("dwa", "dwóch"), ("dwie", "dwóch")),
    3: (("trzy", "trzech"), ("trzy", "trzech")),
    4: (("cztery", "czterech"), ("cztery", "czterech")),
    5: (("pięć", "pięciu"), ("pięć", "pięciu")),
    6: (("sześć", "sześciu"), ("sześć", "sześciu")),
    7: (("siedem", "siedmiu"), ("siedem", "siedmiu")),
    8: (("osiem", "ośmiu"), ("osiem", "ośmiu")),
    9: (("dziewięć", "dziewięciu"), ("dziewięć", "dziewięciu")),
}

ONES_ORDINALS = {
    1: ('pierwszy', "pierwszo"),
    2: ('drugi', "dwu"),
    3: ('trzeci', "trzy"),
    4: ('czwarty', "cztero"),
    5: ('piąty', "pięcio"),
    6: ('szósty', "sześcio"),
    7: ('siódmy', "siedmio"),
    8: ('ósmy', "ośmio"),
    9: ('dziewiąty', "dziewięcio"),
    10: ('dziesiąty', "dziesięcio"),
    11: ('jedenasty', "jedenasto"),
    12: ('dwunasty', "dwunasto"),
    13: ('trzynasty', "trzynasto"),
    14: ('czternasty', "czternasto"),
    15: ('piętnasty', "piętnasto"),
    16: ('szesnasty', "szesnasto"),
    17: ('siedemnasty', "siedemnasto"),
    18: ('osiemnasty', "osiemnasto"),
    19: ('dziewiętnasty', "dziewiętnasto"),
}

TENS = {
    0: ("dziesięć", "dziesięciu"),
    1: ("jedenaście", "jedenastu"),
    2: ("dwanaście", "dwunastu"),
    3: ("trzynaście", "trzynastu"),
    4: ("czternaście", "czternastu"),
    5: ("piętnaście", "piętnastu"),
    6: ("szesnaście", "szesnastu"),
    7: ("siedemnaście", "siedemnastu"),
    8: ("osiemnaście", "osiemnastu"),
    9: ("dziewiętnaście", "dziewiętnastu"),
}

TWENTIES = {
    2: ("dwadzieścia", "dwudziestu"),
    3: ("trzydzieści", "trzydziestu"),
    4: ("czterdzieści", "czterdziestu"),
    5: ("pięćdziesiąt", "pięćdziesięciu"),
    6: ("sześćdziesiąt", "sześćdziesięciu"),
    7: ("siedemdziesiąt", "siedemdziesięciu"),
    8: ("osiemdziesiąt", "osiemdziesięciu"),
    9: ("dziewięćdziesiąt", "dziewięćdziesięciu"),
}

TWENTIES_ORDINALS = {
    2: ('dwudziesty', "dwudziesto"),
    3: ('trzydziesty', "trzydziesto"),
    4: ('czterdziesty', "czterdziesto"),
    5: ('pięćdziesiąty', "pięćdziesięcio"),
    6: ('sześćdziesiąty', "sześćdziesięcio"),
    7: ('siedemdziesiąty', "siedemdziesięcio"),
    8: ('osiemdziesiąty', "osiemdziesięcio"),
    9: ('dziewięćdziesiąty', "dziewięćdziesięcio"),
}

HUNDREDS = {
    1: ("sto", "stu"),
    2: ("dwieście", "dwustu"),
    3: ("trzysta", "trzystu"),
    4: ("czterysta", "czterystu"),
    5: ("pięćset", "pięciuset"),
    6: ("sześćset", "sześciuset"),
    7: ("siedemset", "siedmiuset"),
    8: ("osiemset", "ośmiuset"),
    9: ("dziewięćset", "dziewięciuset"),
}

HUNDREDS_ORDINALS = {
    1: ('setny', "stu"),
    2: ('dwusetny', "dwustu"),
    3: ('trzechsetny', "trzystu"),
    4: ('czterechsetny', "czterystu"),
    5: ('pięćsetny', "pięćset"),
    6: ('sześćsetny', "sześćset"),
    7: ('siedemsetny', "siedemset"),
    8: ('osiemsetny', "osiemset"),
    9: ('dziewięćsetny', "dziewięćset"),
}

THOUSANDS = {
    1: ('tysiąc', 'tysiące', 'tysięcy'),  # 10^3
}

prefixes_ordinal = {
    1: "tysięczny",
    2: "milionowy",
    3: "miliardowy"
}

prefixes = (   # 10^(6*x)
    "mi",      # 10^6
    "bi",      # 10^12
    "try",     # 10^18
    "kwadry",  # 10^24
    "kwinty",  # 10^30
    "seksty",  # 10^36
    "septy",   # 10^42
    "okty",    # 10^48
    "nony",    # 10^54
    "decy"     # 10^60
)
suffixes = ("lion", "liard")  # 10^x or 10^(x+3)

for idx, (p, s) in enumerate(itertools.product(prefixes, suffixes)):
    name = p + s
    THOUSANDS[idx+2] = (name, name + 'y', name + 'ów')


class Num2Word_PL(Num2Word_Base):
    CURRENCY_FORMS = {
        'PLN': (
            ('złoty', 'złote', 'złotych'), ('grosz', 'grosze', 'groszy')
        ),
        'EUR': (
            ('euro', 'euro', 'euro'), ('cent', 'centy', 'centów')
        ),
    }

    def setup(self):
        self.negword = "minus"
        self.pointword = "i"

    def to_cardinal(self, number, gender="m_inanimate", case="nominative") -> str:
        """Convert number to cardinal numeral.

        Args:
            number: Number to convert.
            gender: Gender of the numberal (see self._int2word() for
                supported values).
            case: Grammatical case of the numeral (see self._int2word()
                for supported values).

        Returns:
            Converted number.
        """
        case_number = NAME_TO_CASE[case]
        n = str(number).replace(",", ".")
        base_str, n = self.parse_minus(n)
        if "." in n:
            left, right = n.rstrip("0").split(".")
            n1, n2, n3 = get_digits(int(right))
            last_two = n2*10+n1
            if last_two == 1:
                decimal_index = 0
            elif n1 in {2, 3, 4} and last_two not in {12, 13, 14}:
                decimal_index = 1
            else:
                decimal_index = 2
            decimal_part = self._int2word(int(right), gender="f", case=case_number)
            decimal_level = DECIMAL_LEVELS[len(right)][decimal_index]
            decimal_part += f" {decimal_level}"
            if n == "0.5":
                return base_str + "pół"
            elif n == "1.5":
                return base_str + ("półtorej" if gender == "f" else "półtora")
            elif right == "5":
                decimal_part = "pół"
            return u"%s%s %s %s" % (
                base_str,
                self._int2word(int(left), gender=gender, case=case_number),
                self.pointword,
                decimal_part
            )
        else:
            return base_str + self._int2word(int(n), gender=gender, case=case_number)

    def pluralize(self, n, forms):
        if n == 1:
            form = 0
        elif 5 > n % 10 > 1 and (n % 100 < 10 or n % 100 > 20):
            form = 1
        else:
            form = 2
        return forms[form]

    def last_fragment_to_ordinal(self, last, words, level):
        n1, n2, n3 = get_digits(last)
        last_two = n2*10+n1
        if last_two == 0:
            words.append(HUNDREDS_ORDINALS[n3][level])
        elif level == 1 and last == 1:
            return
        elif last_two < 20:
            if n3 > 0:
                words.append(HUNDREDS[n3][level])
            words.append(ONES_ORDINALS[last_two][level])
        elif last_two % 10 == 0:
            if n3 > 0:
                words.append(HUNDREDS[n3][level])
            words.append(TWENTIES_ORDINALS[n2][level])
        else:
            if n3 > 0:
                words.append(HUNDREDS[n3][0])
            words.append(TWENTIES_ORDINALS[n2][0])
            words.append(ONES_ORDINALS[n1][0])

    def to_ordinal(self, number):
        if number % 1 != 0:
            raise NotImplementedError()
        words = []
        fragments = list(splitbyx(str(number), 3))
        level = 0
        last = fragments[-1]
        while last == 0:
            level = level+1
            fragments.pop()
            last = fragments[-1]
        if len(fragments) > 1:
            pre_part = self._int2word(number-(last*1000**level))
            words.append(pre_part)
        self.last_fragment_to_ordinal(last, words, 0 if level == 0 else 1)
        output = " ".join(words)
        if last == 1 and level > 0 and output != "":
            output = output + " "
        if level > 0:
            output = output + prefixes_ordinal[level]
        return output

    def _int2word(self, n: int, gender="m_inanimate", case: int = 0) -> str:
        """Convert integer `n` to word.

        Args:
            n: Number to convert.
            gender:  Use "f" for feminine, any other value defaults to the masculine inanimate.
            case: Currently supports 0 (nominative) and 1 (genitive).

        Returns:
            Converted number.
        """
        if case not in {0, 1}:
            raise NotImplementedError()
        if gender == "f":
            gender_index = 1
        elif gender in {"m_inanimate", "neuter"}:
            gender_index = 0
        else:
            raise NotImplementedError()

        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            if n3 > 0:
                words.append(HUNDREDS[n3][case])

            if n2 > 1:
                words.append(TWENTIES[n2][case])

            if n2 == 1:
                words.append(TENS[n1][case])
            elif n1 > 0 and not (i > 0 and x == 1):
                words.append(ONES[n1][gender_index][case])

            if i > 0:
                words.append(self.pluralize(x, THOUSANDS[i]))

        return " ".join(words)
