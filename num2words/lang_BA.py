# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2017, Tufan Kaynak, Framras.  All Rights Reserved.
# Copyright (c) 2021, Marsel Ishimbaev.  All Rights Reserved.

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

from __future__ import unicode_literals, with_statement

from .base import Num2Word_Base


class Num2Word_BA(Num2Word_Base):
    def __init__(self):
        self.precision = 2
        self.negword = u"минус"
        self.pointword = u"бөтөн"
        self.CURRENCY_UNIT = u"һум"
        self.CURRENCY_SUBUNIT = u"тин"
        self.errmsg_nonnum = u"Ысын һандар ғына яҙырға була."
        self.errmsg_floatord = u"Кәсер һандан {} рәт һанын яһап булмай."
        self.errmsg_negord = u"Тиҫкәре һандан {} рәт һанын яһап булмай."
        self.errmsg_toobig = u"abs({}) һан яҙыу өсөн артыҡ ҙур. " \
                             u"Иң ҙур яҙып була торған һан {}."
        self.errmsg_nonint = u"Бөтөн һандар ғына яҙырға була."
        self.exclude_title = []
        self.DECIMAL_SIGN = ","
        self.ORDINAL_SIGN = "."
        self.ZERO = u"ноль"
        self.CARDINAL_ONES = {
            "1": u"бер",
            "2": u"ике",
            "3": u"өс",
            "4": u"дүрт",
            "5": u"биш",
            "6": u"алты",
            "7": u"ете",
            "8": u"һигеҙ",
            "9": u"туғыҙ"
        }
        self.ORDINAL_ONES = {
            "1": u"беренсе",
            "2": u"икенсе",
            "3": u"өсөнсө",
            "4": u"дүртенсе",
            "5": u"бишенсе",
            "6": u"алтынсы",
            "7": u"етенсе",
            "8": u"һигеҙенсе",
            "9": u"туғыҙынсы"
        }
        self.CARDINAL_TENS = {
            "1": u"ун",
            "2": u"егерме",
            "3": u"утыҙ",
            "4": u"ҡырҡ",
            "5": u"илле",
            "6": u"алтмыш",
            "7": u"етмеш",
            "8": u"һикһән",
            "9": u"туҡһан"
        }
        self.ORDINAL_TENS = {
            "1": u"унынсы",
            "2": u"егерменсе",
            "3": u"утыҙынсы",
            "4": u"ҡырҡынсы",
            "5": u"илленсе",
            "6": u"алтмышынсы",
            "7": u"етмешенсе",
            "8": u"һикһәненсе",
            "9": u"туҡһанынсы"
        }
        self.HUNDREDS = {
            "2": u"ике",
            "3": u"өс",
            "4": u"дүрт",
            "5": u"биш",
            "6": u"алты",
            "7": u"ете",
            "8": u"һигеҙ",
            "9": u"туғыҙ"
        }
        self.CARDINAL_HUNDRED = (u"йөҙ",)
        self.ORDINAL_HUNDRED = (u"йөҙөнсө",)
        self.CARDINAL_TRIPLETS = {
            1: u"мең",
            2: u"миллион",
            3: u"миллиард",
            4: u"триллион",
            5: u"квадриллион",
            6: u"квинтиллион",
            7: u"секстиллион",
            8: u"септиллион",
            9: u"октиллион",
            10: u"нониллион",
        }
        self.ORDINAL_TRIPLETS = {
            1: u"меңенсе",
            2: u"миллионынсы",
            3: u"миллиардынсы",
            4: u"триллионынсы",
            5: u"квадриллионынсы",
            6: u"квинтиллионынсы",
            7: u"секстиллионынсы",
            8: u"септиллионынсы",
            9: u"октиллионынсы",
            10: u"нониллионынсы"
        }

        self.FRACTION_DENOMINATORS = {
            1: u"ундан",
            2: u"йөҙҙән",
            3: u"меңдән",
            6: u"миллиондан",
            9: u"миллиардтан",
            12: u"триллиондан",
            15: u"квадриллиондан",
            18: u"квинтиллиондан",
            21: u"секстиллиондан",
            24: u"септиллиондан",
            27: u"октиллиондан",
            30: u"нониллиондан"

        }
        self.MAXVAL = (10 ** ((len(self.CARDINAL_TRIPLETS) + 1) * 3)) - 1
        self.MAXFRAC = list(self.FRACTION_DENOMINATORS.keys())[-1]

        self.integers_to_read = []
        self.total_triplets_to_read = 0
        self.total_digits_outside_triplets = 0
        self.order_of_last_zero_digit = 0

    def to_cardinal(self, value, currency=False):
        wrdlst = []
        is_cardinal = self.verify_cardinal(value)
        if not is_cardinal:
            raise ValueError(self.errmsg_nonint)

        if not int(value) == value:
            return self.to_cardinal_float(value, currency=currency)
        self.to_splitnum(value)

        if self.order_of_last_zero_digit >= len(self.integers_to_read[0]):
            # number like 00 and all 0s and even more, raise error
            wrd = " ".join(filter(lambda x: x != "", wrdlst))
            return wrd

        if self.total_triplets_to_read == 1:
            if self.total_digits_outside_triplets == 2:
                if self.order_of_last_zero_digit == 1:
                    # number like x0, read ordinal x0 and return
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit == 0:
                    # number like xy, read ordinal xy and return
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_ONES.get(
                        self.integers_to_read[0][1], ""
                    )]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd

            if self.total_digits_outside_triplets == 1:
                if self.order_of_last_zero_digit == 0:
                    # number like x, read ordinal x and return
                    wrdlst += [self.CARDINAL_ONES.get(
                        self.integers_to_read[0][0], ""
                    )]
                    if self.integers_to_read[0][0] == "0":
                        return u"ноль"
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd

            if self.total_digits_outside_triplets == 0:
                if self.order_of_last_zero_digit == 2:
                    # number like x00, read ordinal x00 and return
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit == 1:
                    # number like xy0, read ordinal xy0 and return
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][1], ""
                    )]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit == 0:
                    # number like xyz, read ordinal xyz and return
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][1], ""
                    )]
                    if not self.integers_to_read[0][2] == "0":
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][2], ""
                        )]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd

        if self.total_triplets_to_read >= 2:
            if self.total_digits_outside_triplets == 2:
                if self.order_of_last_zero_digit == len(
                        self.integers_to_read[0]) - 1:
                    # number like x0 and all 0s, read ordinal x0 0..0
                    #  and return
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit == len(
                        self.integers_to_read[0]) - 2:
                    # number like xy and all 0s, read ordinal xy 0..0
                    #  and return
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_ONES.get(
                        self.integers_to_read[0][1], ""
                    )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit < len(
                        self.integers_to_read[0]) - 2:
                    # number like xy and others, read cardinal xy n..n
                    #  and return
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_ONES.get(
                        self.integers_to_read[0][1], ""
                    )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]

            if self.total_digits_outside_triplets == 1:
                if self.order_of_last_zero_digit == len(
                        self.integers_to_read[0]) - 1:
                    # number like x and all 0s, read ordinal x 0..0
                    #  and return
                    if not (self.total_triplets_to_read == 2 and
                            self.integers_to_read[0][0] == "1"):
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][0], ""
                        )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit < len(
                        self.integers_to_read[0]) - 1:
                    # number like x and others, read cardinal x n..n
                    #  and return
                    if not (self.total_triplets_to_read == 2 and
                            self.integers_to_read[0][0] == "1"):
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][0], ""
                        )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]

            if self.total_digits_outside_triplets == 0:
                if self.order_of_last_zero_digit == len(
                        self.integers_to_read[0]) - 1:
                    # number like x00 and all 0s, read ordinal x00 0..0
                    #  and return
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit == len(
                        self.integers_to_read[0]) - 2:
                    # number like xy0 and all 0s, read ordinal xy0 0..0
                    #  and return
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][1], ""
                    )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit == len(
                        self.integers_to_read[0]) - 3:
                    # number like xyz and all 0s, read ordinal xyz 0..0
                    #  and return
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][1], ""
                    )]
                    wrdlst += [self.CARDINAL_ONES.get(
                        self.integers_to_read[0][2], ""
                    )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]
                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                    return wrd
                if self.order_of_last_zero_digit < len(
                        self.integers_to_read[0]) - 3:
                    # number like xyz and all others, read cardinal
                    #  xyz n..n
                    wrdlst += [self.HUNDREDS.get(
                        self.integers_to_read[0][0], ""
                    )]
                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                    wrdlst += [self.CARDINAL_TENS.get(
                        self.integers_to_read[0][1], ""
                    )]
                    if not (self.total_triplets_to_read == 2 and
                            self.integers_to_read[0][2] == "1"):
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][2], ""
                        )]
                    wrdlst += [self.CARDINAL_TRIPLETS[
                        self.total_triplets_to_read - 1
                    ]]

            for i in list(range(self.total_triplets_to_read - 1, 0, -1)):
                reading_triplet_order = self.total_triplets_to_read - i
                if self.total_digits_outside_triplets == 0:
                    last_read_digit_order = reading_triplet_order * 3
                else:
                    last_read_digit_order = \
                        (reading_triplet_order - 1) * 3 + \
                        self.total_digits_outside_triplets

                if not self.integers_to_read[0][
                        last_read_digit_order: last_read_digit_order + 3
                        ] == "000":
                    if not self.integers_to_read[0][
                        last_read_digit_order
                    ] == "0":
                        if not self.integers_to_read[0][
                            last_read_digit_order
                        ] == "1":
                            wrdlst += [self.CARDINAL_ONES.get(
                                self.integers_to_read[0][
                                    last_read_digit_order
                                ], ""
                            )]
                        if self.order_of_last_zero_digit == len(
                                self.integers_to_read[0]) - (
                                last_read_digit_order) - 1:
                            if i == 1:
                                wrdlst += [self.CARDINAL_HUNDRED[0]]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                            elif i > 1:
                                wrdlst += [self.CARDINAL_HUNDRED[0]]
                                wrdlst += [self.CARDINAL_TRIPLETS[i - 1]]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                        else:
                            wrdlst += [self.CARDINAL_HUNDRED[0]]

                    if not self.integers_to_read[0][
                                last_read_digit_order + 1
                    ] == "0":
                        if self.order_of_last_zero_digit == len(
                                self.integers_to_read[0]) - (
                                last_read_digit_order) - 2:
                            if i == 1:
                                wrdlst += [self.CARDINAL_TENS.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order + 1], ""
                                )]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                            elif i > 1:
                                wrdlst += [self.CARDINAL_TENS.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order + 1], ""
                                )]
                                wrdlst += [self.CARDINAL_TRIPLETS[i - 1]]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                        else:
                            wrdlst += [self.CARDINAL_TENS.get(
                                self.integers_to_read[0][
                                    last_read_digit_order + 1], ""
                            )]

                    if not self.integers_to_read[0][
                                last_read_digit_order + 2
                    ] == "0":
                        if self.order_of_last_zero_digit == len(
                                self.integers_to_read[0]) - (
                                last_read_digit_order) - 3:
                            if i == 1:
                                wrdlst += [self.CARDINAL_ONES.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order + 2], ""
                                )]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                            if i == 2:
                                if not self.integers_to_read[0][
                                    last_read_digit_order:
                                        last_read_digit_order + 2] == "00":
                                    wrdlst += [self.CARDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]
                                elif not self.integers_to_read[0][
                                            last_read_digit_order + 2
                                ] == "1":
                                    wrdlst += [self.CARDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]
                                wrdlst += [self.CARDINAL_TRIPLETS[i - 1]]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                            if i > 2:
                                wrdlst += [self.CARDINAL_ONES.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order + 2], ""
                                )]
                                wrdlst += [self.CARDINAL_TRIPLETS[i - 1]]
                                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                return wrd
                        else:
                            if not self.integers_to_read[0][
                                last_read_digit_order:
                                    last_read_digit_order + 2] == "00":
                                wrdlst += [self.CARDINAL_ONES.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order + 2], ""
                                )]
                            else:
                                if not self.integers_to_read[0][
                                    last_read_digit_order:
                                        last_read_digit_order + 2] == "00":
                                    wrdlst += [self.CARDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]
                                elif not self.integers_to_read[0][
                                        last_read_digit_order + 2] == "1":
                                    wrdlst += [self.CARDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]

                    wrdlst += [self.CARDINAL_TRIPLETS[i - 1]]

        wrd = " ".join(filter(lambda x: x != "", wrdlst))
        return wrd

    def to_cardinal_float(self, value, currency=False):

        self.to_splitnum(value)
        wrd = ""
        wrdlst = []
            
        if currency:
             
            wrdlst += [self.pointword]
            if len(self.integers_to_read[1]) >= 1:
                wrdlst += [self.CARDINAL_TENS.get(self.integers_to_read[1][0], "")]

            if len(self.integers_to_read[1]) == 2:
                wrdlst += [self.CARDINAL_ONES.get(self.integers_to_read[1][1], "")]


            if self.integers_to_read[0] == "0":
                wrdlst = [self.ZERO] + wrdlst
            else:
                wrdlst = [self.to_cardinal(int(self.integers_to_read[0]))] + wrdlst
            
            wrd = " ".join(filter(lambda x: x != "", wrdlst))
            return wrd

        
        for k in list(self.FRACTION_DENOMINATORS.keys()):
            if len(self.integers_to_read[1]) <= k:
                wrdlst += [self.FRACTION_DENOMINATORS.get(k, "")]
                break
        
        len_zeros = k - len(self.integers_to_read[1])

        wrdlst += [self.to_cardinal(int(self.integers_to_read[1]+'0'*len_zeros))]

        self.to_splitnum(value)
        if self.integers_to_read[0] != "0":
            wrdlst = [self.to_cardinal(int(self.integers_to_read[0]))] + [self.pointword] + wrdlst
            
        wrd = " ".join(filter(lambda x: x != "", wrdlst))
        return wrd

    def verify_cardinal(self, value):
        iscardinal = True
        try:
            if not float(value) == value:
                iscardinal = False
        except (ValueError, TypeError):
            raise TypeError(self.errmsg_nonnum)
        if abs(value) >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig.format(value, self.MAXVAL))
        return iscardinal

    def verify_ordinal(self, value):
        isordinal = True
        try:
            if not int(value) == value:
                isordinal = False
            if not abs(value) == value:
                raise TypeError(self.errmsg_negord.format(value))
        except (ValueError, TypeError):
            raise TypeError(self.errmsg_nonnum)
        if abs(value) >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig.format(value, self.MAXVAL))
        return isordinal

    def to_ordinal(self, value):
        wrd = ""
        wrdlst = []
        is_ordinal = self.verify_ordinal(value)
        if is_ordinal:
            self.to_splitnum(value)

            if self.order_of_last_zero_digit >= len(self.integers_to_read[0]):
                # number like 00 and all 0s and even more, raise error
                wrd = " ".join(filter(lambda x: x != "", wrdlst))
                return wrd

            if self.total_triplets_to_read == 1:
                if self.total_digits_outside_triplets == 2:
                    if self.order_of_last_zero_digit == 1:
                        # number like x0, read ordinal x0 and return
                        wrdlst += [self.ORDINAL_TENS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit == 0:
                        # number like xy, read ordinal xy and return
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.ORDINAL_ONES.get(
                            self.integers_to_read[0][1], ""
                        )]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd

                if self.total_digits_outside_triplets == 1:
                    if self.order_of_last_zero_digit == 0:
                        # number like x, read ordinal x and return
                        wrdlst += [self.ORDINAL_ONES.get(
                            self.integers_to_read[0][0], ""
                        )]
                        if self.integers_to_read[0][0] == "0":
                            return u"нуленсе"
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd

                if self.total_digits_outside_triplets == 0:
                    if self.order_of_last_zero_digit == 2:
                        # number like x00, read ordinal x00 and return
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.ORDINAL_HUNDRED[0]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit == 1:
                        # number like xy0, read ordinal xy0 and return
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_HUNDRED[0]]
                        wrdlst += [self.ORDINAL_TENS.get(
                            self.integers_to_read[0][1], ""
                        )]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit == 0:
                        # number like xyz, read ordinal xyz and return
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_HUNDRED[0]]
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][1], ""
                        )]
                        if not self.integers_to_read[0][2] == "0":
                            wrdlst += [self.ORDINAL_ONES.get(
                                self.integers_to_read[0][2], ""
                            )]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd

            if self.total_triplets_to_read >= 2:
                if self.total_digits_outside_triplets == 2:
                    if self.order_of_last_zero_digit == len(
                            self.integers_to_read[0]) - 1:
                        # number like x0 and all 0s, read ordinal x0 0..0
                        #  and return
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.ORDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit == len(
                            self.integers_to_read[0]) - 2:
                        # number like xy and all 0s, read ordinal xy 0..0
                        #  and return
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][1], ""
                        )]
                        wrdlst += [self.ORDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit < len(
                            self.integers_to_read[0]) - 2:
                        # number like xy and others, read cardinal xy n..n
                        #  and return
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][1], ""
                        )]
                        wrdlst += [self.CARDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]

                if self.total_digits_outside_triplets == 1:
                    if self.order_of_last_zero_digit == len(
                            self.integers_to_read[0]) - 1:
                        # number like x and all 0s, read ordinal x 0..0
                        #  and return
                        if not (self.total_triplets_to_read == 2 and
                                self.integers_to_read[0][0] == "1"):
                            wrdlst += [self.CARDINAL_ONES.get(
                                self.integers_to_read[0][0], ""
                            )]
                        wrdlst += [self.ORDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit < len(
                            self.integers_to_read[0]) - 1:
                        # number like x and others, read cardinal x n..n
                        #  and return
                        if not (self.total_triplets_to_read == 2 and
                                self.integers_to_read[0][0] == "1"):
                            wrdlst += [self.CARDINAL_ONES.get(
                                self.integers_to_read[0][0], ""
                            )]
                        wrdlst += [self.CARDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]

                if self.total_digits_outside_triplets == 0:
                    if self.order_of_last_zero_digit == len(
                            self.integers_to_read[0]) - 1:
                        # number like x00 and all 0s, read ordinal x00 0..0
                        #  and return
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_HUNDRED[0]]
                        wrdlst += [self.ORDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit == len(
                            self.integers_to_read[0]) - 2:
                        # number like xy0 and all 0s, read ordinal xy0 0..0
                        #  and return
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_HUNDRED[0]]
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][1], ""
                        )]
                        wrdlst += [self.ORDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit == len(
                            self.integers_to_read[0]) - 3:
                        # number like xyz and all 0s, read ordinal xyz 0..0
                        #  and return
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_HUNDRED[0]]
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][1], ""
                        )]
                        wrdlst += [self.CARDINAL_ONES.get(
                            self.integers_to_read[0][2], ""
                        )]
                        wrdlst += [self.ORDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]
                        wrd = " ".join(filter(lambda x: x != "", wrdlst))
                        return wrd
                    if self.order_of_last_zero_digit < len(
                            self.integers_to_read[0]) - 3:
                        # number like xyz and all others, read cardinal
                        #  xyz n..n
                        wrdlst += [self.HUNDREDS.get(
                            self.integers_to_read[0][0], ""
                        )]
                        wrdlst += [self.CARDINAL_HUNDRED[0]]
                        wrdlst += [self.CARDINAL_TENS.get(
                            self.integers_to_read[0][1], ""
                        )]
                        if not (self.total_triplets_to_read == 2 and
                                self.integers_to_read[0][2] == "1"):
                            wrdlst += [self.CARDINAL_ONES.get(
                                self.integers_to_read[0][2], ""
                            )]
                        wrdlst += [self.CARDINAL_TRIPLETS[
                            self.total_triplets_to_read - 1
                        ]]

                for i in list(range(self.total_triplets_to_read - 1, 0, -1)):
                    reading_triplet_order = self.total_triplets_to_read - i
                    if self.total_digits_outside_triplets == 0:
                        last_read_digit_order = reading_triplet_order * 3
                    else:
                        last_read_digit_order = \
                            (reading_triplet_order - 1) * 3 + \
                            self.total_digits_outside_triplets

                    if not self.integers_to_read[0][
                           last_read_digit_order: last_read_digit_order + 3
                           ] == "000":
                        if not self.integers_to_read[0][
                            last_read_digit_order
                        ] == "0":
                            if not self.integers_to_read[0][
                                last_read_digit_order
                            ] == "1":
                                wrdlst += [self.CARDINAL_ONES.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order
                                    ], ""
                                )]
                            if self.order_of_last_zero_digit == len(
                                    self.integers_to_read[0]) - (
                                    last_read_digit_order) - 1:
                                if i == 1:
                                    wrdlst += [self.ORDINAL_HUNDRED[0]]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                                elif i > 1:
                                    wrdlst += [self.CARDINAL_HUNDRED[0]]
                                    wrdlst += [self.ORDINAL_TRIPLETS[i - 1]]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                            else:
                                wrdlst += [self.CARDINAL_HUNDRED[0]]

                        if not self.integers_to_read[0][
                                    last_read_digit_order + 1
                        ] == "0":
                            if self.order_of_last_zero_digit == len(
                                    self.integers_to_read[0]) - (
                                    last_read_digit_order) - 2:
                                if i == 1:
                                    wrdlst += [self.ORDINAL_TENS.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 1], ""
                                    )]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                                elif i > 1:
                                    wrdlst += [self.CARDINAL_TENS.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 1], ""
                                    )]
                                    wrdlst += [self.ORDINAL_TRIPLETS[i - 1]]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                            else:
                                wrdlst += [self.CARDINAL_TENS.get(
                                    self.integers_to_read[0][
                                        last_read_digit_order + 1], ""
                                )]

                        if not self.integers_to_read[0][
                                    last_read_digit_order + 2
                        ] == "0":
                            if self.order_of_last_zero_digit == len(
                                    self.integers_to_read[0]) - (
                                    last_read_digit_order) - 3:
                                if i == 1:
                                    wrdlst += [self.ORDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                                if i == 2:
                                    if not self.integers_to_read[0][
                                       last_read_digit_order:
                                            last_read_digit_order + 2] == "00":
                                        wrdlst += [self.CARDINAL_ONES.get(
                                            self.integers_to_read[0][
                                                last_read_digit_order + 2], ""
                                        )]
                                    elif not self.integers_to_read[0][
                                                last_read_digit_order + 2
                                    ] == "1":
                                        wrdlst += [self.CARDINAL_ONES.get(
                                            self.integers_to_read[0][
                                                last_read_digit_order + 2], ""
                                        )]
                                    wrdlst += [self.ORDINAL_TRIPLETS[i - 1]]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                                if i > 2:
                                    wrdlst += [self.CARDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]
                                    wrdlst += [self.ORDINAL_TRIPLETS[i - 1]]
                                    wrd = " ".join(filter(lambda x: x != "", wrdlst))
                                    return wrd
                            else:
                                if not self.integers_to_read[0][
                                   last_read_digit_order:
                                        last_read_digit_order + 2] == "00":
                                    wrdlst += [self.CARDINAL_ONES.get(
                                        self.integers_to_read[0][
                                            last_read_digit_order + 2], ""
                                    )]
                                else:
                                    if not self.integers_to_read[0][
                                       last_read_digit_order:
                                           last_read_digit_order + 2] == "00":
                                        wrdlst += [self.CARDINAL_ONES.get(
                                            self.integers_to_read[0][
                                                last_read_digit_order + 2], ""
                                        )]
                                    elif not self.integers_to_read[0][
                                            last_read_digit_order + 2] == "1":
                                        wrdlst += [self.CARDINAL_ONES.get(
                                            self.integers_to_read[0][
                                                last_read_digit_order + 2], ""
                                        )]

                        wrdlst += [self.CARDINAL_TRIPLETS[i - 1]]

        wrd = " ".join(filter(lambda x: x != "", wrdlst))
        return wrd

    def to_splitnum(self, val, currency=False):

        # all meaningful digits 
        num_parts = str(val).split('.')

        whole_part = num_parts[0]
        if len(num_parts) == 1:
            local_precision = 0
            frac_part = ''
        else:
            local_precision = min(self.MAXFRAC, len(num_parts[1]))
            frac_part = num_parts[1][:local_precision]


        float_digits = whole_part+frac_part

        if currency:
            float_digits = str(int(val * 10 ** self.precision))
            local_precision = self.precision

        # if integer part is not zero
        if not int(val) == 0:
            #integer part
            self.integers_to_read = [
                str(int(val)),
                float_digits[len(float_digits) - local_precision:]
            ]
        else:
            self.integers_to_read = [
                "0",
                "0" * (local_precision - len(float_digits)) +
                float_digits[len(float_digits) - local_precision:]
            ]
        if len(self.integers_to_read[0]) % 3 > 0:
            self.total_triplets_to_read = (len(self.integers_to_read[0]) // 3)\
                                        + 1
        elif len(self.integers_to_read[0]) % 3 == 0:
            self.total_triplets_to_read = len(self.integers_to_read[0]) // 3
        self.total_digits_outside_triplets = len(self.integers_to_read[0]) % 3

        okunacak = list(self.integers_to_read[0][::-1])
        self.order_of_last_zero_digit = 0
        found = 0
        for i in range(len(okunacak) - 1):
            if int(okunacak[i]) == 0 and found == 0:
                self.order_of_last_zero_digit = i + 1
            else:
                found = 1

    
    def to_currency(self, value):
        if int(value) == 0:
            return u"бушлай"
        parts = self.to_cardinal(value, currency=True).split(self.pointword)
        if len(parts) == 1:
            return f"{parts[0].strip()} {self.CURRENCY_UNIT}"
        if len(parts) == 2:
            return f"{parts[0].strip()} {self.CURRENCY_UNIT} {parts[1].strip()} {self.CURRENCY_SUBUNIT}"
