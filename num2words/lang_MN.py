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

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = ("тэг",)

ONES = {
    1: ("нэг", "нэгэн"),
    2: ("хоёр", "хоёр"),
    3: ("гурав", "гурван"),
    4: ("дөрөв", "дөрвөн"),
    5: ("тав", "таван"),
    6: ("зургаа", "зургаан"),
    7: ("долоо", "долоон"),
    8: ("найм", "найман"),
    9: ("ес", "есөн"),
}

TENS = ("арав", "арван", "аравны")

TWENTIES = {
    2: ("хорь", "хорин"),
    3: ("гуч", "гучин"),
    4: ("дөч", "дөчин"),
    5: ("тавь", "тавин"),
    6: ("жар", "жаран"),
    7: ("дал", "далан"),
    8: ("ная", "наян"),
    9: ("ер", "ерэн"),
}

HUNDREDS = ("зуу", "зуун", "зууны")

THOUSANDS = {
    1: ("мянга", "мянган", "мянганы"),  # 10^3
    2: ("сая", "сая", "саяны"),  # 10^6
    3: ("тэрбум", "тэрбум", "тэрбумны"),  # 10^9
    4: ("их наяд", "их наяд", "их наядны"),  # 10^12
    5: ("тунамал", "тунамал", "тунамлын"),  # 10^15
    6: ("их ингүүмэл", "их ингүүмэл", "их ингүүмлийн"),  # 10^18
    7: ("ялгаруулагч", "ялгаруулагч", "ялгаруулагчийн"),  # 10^21
    8: ("их өвөр дээр", "их өвөр дээр", "их өвөр дээрийн"),  # 10^24
    9: ("хязгаар үзэгдэл", "хязгаар үзэгдэл", "хязгаар үзэдлийн"),  # 10^27
    10: (
        "их шалтгааны зүйл",
        "их шалтгааны зүйл",
        "их шалтгааны зүйлийн",
    ),  # 10^30
}


class Num2Word_MN(Num2Word_Base):
    YEAR = False
    CURRENCY = False
    CURRENCY_FORMS = {
        "MNT": (("төгрөг",), ("мөнгө",)),
        "USD": (("доллар",), ("цент",)),
        "EUR": (("евро",), ("цент",)),
        "RUB": (("рубль",), ("копейк",)),
        "CNY": (("юань",), ("мао",)),
    }

    def setup(self):
        self.negword = "хасах"
        self.pointword = ""

    def to_cardinal(self, number):
        n = str(number).replace(",", ".")
        if "." in n:
            left, right = n.split(".")
            decimal = len(right)
            leading_zero_count = decimal - len(right.lstrip("0"))
            decimal_part = ("") * leading_zero_count + self._int2word(
                int(right)
            )

            if decimal == 1:
                self.pointword = TENS[2]
            elif decimal == 2:
                self.pointword = HUNDREDS[2]
            elif decimal > 2:
                if decimal % 3 == 1:
                    self.pointword += TENS[1] + " "
                elif decimal % 3 == 2:
                    self.pointword += HUNDREDS[1] + " "
                self.pointword += THOUSANDS[decimal // 3][2]

            return "%s %s %s" % (
                self._int2word(int(left)),
                self.pointword,
                decimal_part,
            )
        else:
            return self._int2word(int(n))

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        outwords = self.to_cardinal(number).split(" ")
        lastword = outwords[-1].lower()
        lastword += (
            "дүгээр"
            if any(c in lastword for c in "еөэү")
            and not any(c in lastword for c in "аоу")
            else "дугаар"
        )
        outwords[-1] = self.title(lastword)
        return " ".join(outwords).strip()

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "-р")

    def pluralize(self, n, forms):
        return forms[0]

    def to_currency(
        self,
        val,
        currency="MNT",
        cents=False,
        separator="",
        adjective=False,
    ):
        self.CURRENCY = True

        result = super(Num2Word_MN, self).to_currency(
            val, currency, True, separator, adjective
        )

        return (
            result.replace("мянга төгрөг", "мянган төгрөг")
            .replace("мянга доллар", "мянган доллар")
            .replace("мянга евро", "мянган евро")
            .replace("мянга рубль", "мянган рубль")
            .replace("мянга юань", "мянган юань")
            .replace(" тэг мөнгө", "")
            .replace(" тэг цент", "")
            .replace(" тэг копейк", "")
            .replace(" тэг мао", "")
        )

    def _int2word(self, n, feminine=False):
        if n < 0:
            return " ".join([self.negword, self._int2word(abs(n))])

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
                words.append(ONES[n3][1 if n3 > 1 else 0])
                words.append(
                    HUNDREDS[
                        1
                        if (n1 + n2 + i > 0 or self.CURRENCY or self.YEAR)
                        else 0
                    ]
                )

            if n2 > 1:
                words.append(
                    TWENTIES[n2][
                        1 if (n1 + i or self.CURRENCY or self.YEAR) else 0
                    ]
                )

            if n2 == 1:
                if n1 > 0:
                    words.append(TENS[1])
                    words.append(
                        ONES[n1][
                            1 if (i > 0 or self.CURRENCY or self.YEAR) else 0
                        ]
                    )
                else:
                    words.append(
                        TENS[
                            1 if (i > 0 or self.CURRENCY or self.YEAR) else 0
                        ]
                    )

            elif n1 > 0:
                words.append(
                    ONES[n1][
                        1
                        if (
                            (i > 0 or self.CURRENCY or self.YEAR)
                            and (n1 > 1 or n2 > 0)
                        )
                        else 0
                    ]
                )

            if i > 0:
                words.append(THOUSANDS[i][0])

        return " ".join(words)

    def to_year(self, val, suffix=None, longval=True):
        self.YEAR = True
        result = super(Num2Word_MN, self).to_year(val, longval=longval)

        if result.startswith(self.negword):
            suffix = "НТӨ" if not suffix else suffix
            result = result.replace(self.negword, "").strip()

        if suffix:
            result = " ".join([suffix, result])
        result = " ".join([result, "он"])
        return result.replace("нэг мянга", "мянга").replace(
            "мянга он", "мянган он"
        )
