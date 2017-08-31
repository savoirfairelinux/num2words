# -*- encoding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2017, Tufan Kaynak, Framras.  All Rights Reserved.

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


class Num2Word_TR(object):
    def __init__(self):
        self.precision = 2
        self.negword = u"eksi"
        self.pointword = u"virgül"
        self.CURRENCY_UNIT = (u"lira",)
        self.CURRENCY_SUBUNIT = (u"kuruş",)
        # type(%s) not in [long, int, float]
        self.errmsg_nonnum = u"Sadece sayılar yazıya çevrilebilir."
        # Cannot treat float %s as ordinal.
        self.errmsg_floatord = u"Tam sayı olmayan {} sıralamada kullanılamaz."
        # Cannot treat negative num %s as ordinal.
        self.errmsg_negord = u"Pozitif olmayan {} sıralamada kullanılamaz."
        # abs(%s) must be less than %s.
        self.errmsg_toobig = u"abs({}) sayı yazıya çevirmek için çok büyük. Yazıya çevrilebilecek en büyük rakam {}."
        self.exclude_title = ["et", "virgule", "moins"]
        # ordered number tuples in Turkish
        self.ORDINAL_SIGN = (",",)
        self.CARDINAL_ONES = (
            u"sıfır", u"bir", u"iki", u"üç", u"dört", u"beş", u"altı", u"yedi", u"sekiz", u"dokuz",)
        self.ORDINAL_ONES = (
            u"", u"birinci", u"ikinci", u"üçüncü", u"dördüncü", u"beşinci", u"altıncı", u"yedinci", u"sekizinci",
            u"dokuzuncu",)
        self.CARDINAL_TEN = (
            u"", u"on", u"yirmi", u"otuz", u"kırk", u"elli", u"altmış", u"yetmiş", u"seksen", u"doksan",)
        self.ORDINAL_TENS = (
            u"", u"onuncu", u"yirminci", u"otuzuncu", u"kırkıncı", u"ellinci", u"altmışıncı", u"yetmişinci",
            u"sekseninci", u"doksanıncı",)
        self.CARDINAL_HUNDREDS = (u"yüz",)
        self.ORDINAL_HUNDREDS = (u"yüzüncü",)
        self.CARDINAL_TRIPLETS = (u"", u"bin", u"milyon", u"milyar", u"trilyon", u"katrilyon", u"kentilyon",)
        self.ORDINAL_TRIPLETS = (
            u"", u"bininci", u"milyonuncu", u"milyarıncı", u"trilyonuncu", u"katrilyonuncu", u"kentilyon",)
        self.MAXVAL = (10 ** (len(self.CARDINAL_TRIPLETS) * 3)) - 1

        self.integers_to_read = []
        self.total_triplets_to_read = 0
        self.total_digits_outside_triplets = 0
        self.order_of_last_zero_digit = 0

    # def set_numwords(self):

    # def gen_high_numwords(self, units, tens, lows):

    # def set_mid_numwords(self, mid):

    # def set_low_numwords(self, numwords):

    def splitnum(self, value):
        return self.to_splitnum(value)

    def to_cardinal(self, value):
        oku = ""
        is_cardinal = self.verify_cardinal(value)
        if is_cardinal:
            if not int(value) == value:
                return self.to_cardinal_float(value)
            self.splitnum(value)

            if self.order_of_last_zero_digit >= len(self.integers_to_read[0]):
                # number like 00 and all 0s and even more, raise error
                return oku

            if self.total_triplets_to_read == 1:
                if self.total_digits_outside_triplets == 2:
                    if self.order_of_last_zero_digit == 1:
                        # number like x0, read cardinal x0 and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        return oku
                    if self.order_of_last_zero_digit == 0:
                        # number like xy, read cardinal xy and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                    if not self.integers_to_read[0][0] == "0":
                        oku += self.CARDINAL_ONES[int(self.integers_to_read[0][1])]
                    return oku

                if self.total_digits_outside_triplets == 1:
                    if self.order_of_last_zero_digit == 0:
                        # number like x, read ordinal x and return
                        oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        return oku

                if self.total_digits_outside_triplets == 0:
                    if self.order_of_last_zero_digit == 2:
                        # number like x00, read cardinal x00 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        return oku
                    if self.order_of_last_zero_digit == 1:
                        # number like xy0, read cardinal xy0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        return oku
                    if self.order_of_last_zero_digit == 0:
                        # number like xyz, read cardinal xyz and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        if not self.integers_to_read[0][2] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][2])]
                        return oku

            if self.total_triplets_to_read >= 2:
                if self.total_digits_outside_triplets == 2:
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 1:
                        # number like x0 and all 0s, read cardinal x0 0..0 and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 2:
                        # number like xy and all 0s, read cardinal xy 0..0 and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        if not self.integers_to_read[0][1] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][1])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit < len(self.integers_to_read[0]) - 2:
                        # number like xy and others, read cardinal xy n..n and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        if not self.integers_to_read[0][1] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][1])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]

                if self.total_digits_outside_triplets == 1:
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 1:
                        # number like x and all 0s, read cardinal x 0..0 and return
                        if not (self.total_triplets_to_read == 2 and self.integers_to_read[0][0] == "1"):
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit < len(self.integers_to_read[0]) - 1:
                        # number like x and others, read cardinal x n..n and return
                        if not (self.total_triplets_to_read == 2 and self.integers_to_read[0][0] == "1"):
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]

                if self.total_digits_outside_triplets == 0:
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 1:
                        # number like x00 and all 0s, read cardinal x00 0..0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 2:
                        # number like xy0 and all 0s, read cardinal xy0 0..0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 3:
                        # number like xyz and all 0s, read cardinal xyz 0..0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        if not self.integers_to_read[0][2] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][2])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit < len(self.integers_to_read[0]) - 3:
                        # number like xyz and all others, read cardinal xyz n..n
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        if not self.integers_to_read[0][2] == "0":
                            if not (self.total_triplets_to_read == 2 and self.integers_to_read[0][2] == "1"):
                                oku += self.CARDINAL_ONES[int(self.integers_to_read[0][2])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]

                for i in list(range(self.total_triplets_to_read - 1, 0, -1)):
                    okunan_grup_sirasi = self.total_triplets_to_read - i
                    if self.total_digits_outside_triplets == 0:
                        son_okunan_basamak_sirasi = okunan_grup_sirasi * 3
                    else:
                        son_okunan_basamak_sirasi = (okunan_grup_sirasi - 1) * 3 + self.total_digits_outside_triplets

                    if not self.integers_to_read[0][son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 3] == "000":
                        if not self.integers_to_read[0][son_okunan_basamak_sirasi] == "0":
                            if not self.integers_to_read[0][son_okunan_basamak_sirasi] == "1":
                                oku += self.CARDINAL_ONES[
                                    int(self.integers_to_read[0][son_okunan_basamak_sirasi])]
                            if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - (
                                    son_okunan_basamak_sirasi) - 1:
                                if i == 1:
                                    oku += self.CARDINAL_HUNDREDS[0]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_HUNDREDS[0]
                                    oku += self.CARDINAL_TRIPLETS[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_HUNDREDS[0]

                        if not self.integers_to_read[0][son_okunan_basamak_sirasi + 1] == "0":
                            if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - (
                                    son_okunan_basamak_sirasi) - 2:
                                if i == 1:
                                    oku += self.CARDINAL_TEN[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 1])]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_TEN[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 1])]
                                    oku += self.CARDINAL_TRIPLETS[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_TEN[
                                    int(self.integers_to_read[0][son_okunan_basamak_sirasi + 1])]

                        if not self.integers_to_read[0][son_okunan_basamak_sirasi + 2] == "0":
                            if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - (
                                    son_okunan_basamak_sirasi) - 3:
                                if i == 1:
                                    oku += self.CARDINAL_ONES[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    return oku
                                if i == 2:
                                    if not self.integers_to_read[0][
                                           son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                        oku += self.CARDINAL_ONES[
                                            int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    elif not self.integers_to_read[0][son_okunan_basamak_sirasi + 2] == "1":
                                        oku += self.CARDINAL_ONES[
                                            int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.CARDINAL_TRIPLETS[i - 1]
                                    return oku
                                if i > 2:
                                    oku += self.CARDINAL_ONES[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.CARDINAL_TRIPLETS[i - 1]
                                    return oku
                            else:
                                if not self.integers_to_read[0][
                                       son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                    oku += self.CARDINAL_ONES[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                else:
                                    if i == 2:
                                        if not self.integers_to_read[0][
                                               son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                            oku += self.CARDINAL_ONES[
                                                int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                        elif not self.integers_to_read[0][son_okunan_basamak_sirasi + 2] == "1":
                                            oku += self.CARDINAL_ONES[
                                                int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]

                        oku += self.CARDINAL_TRIPLETS[i - 1]

        return oku

    def to_cardinal_float(self, value):
        self.splitnum(value)
        oku = ""
        oku += self.pointword
        if len(self.integers_to_read[1]) >= 1:
            if not self.integers_to_read[1][0] == "0":
                oku += self.CARDINAL_TEN[int(self.integers_to_read[1][0])]
        if len(self.integers_to_read[1]) == 2:
            if not self.integers_to_read[1][1] == "0":
                oku += self.CARDINAL_ONES[int(self.integers_to_read[1][1])]
        oku = self.to_cardinal(int(self.integers_to_read[0])) + oku
        return oku

    # def merge(self, curr, next):

    # def clean(self, val):

    # def title(self, value):

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

    # def verify_num(self, value):

    # def set_wordnums(self):

    def to_ordinal(self, value):
        oku = ""
        isordinal = self.verify_ordinal(value)
        if isordinal:
            self.splitnum(value)

            if self.order_of_last_zero_digit >= len(self.integers_to_read[0]):
                # number like 00 and all 0s and even more, raise error
                return oku

            if self.total_triplets_to_read == 1:
                if self.total_digits_outside_triplets == 2:
                    if self.order_of_last_zero_digit == 1:
                        # number like x0, read ordinal x0 and return
                        oku += self.ORDINAL_TENS[int(self.integers_to_read[0][0])]
                        return oku
                    if self.order_of_last_zero_digit == 0:
                        # number like xy, read ordinal xy and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                    if not self.integers_to_read[0][0] == "0":
                        oku += self.ORDINAL_ONES[int(self.integers_to_read[0][1])]
                    return oku

                if self.total_digits_outside_triplets == 1:
                    if self.order_of_last_zero_digit == 0:
                        # number like x, read ordinal x and return
                        oku += self.ORDINAL_ONES[int(self.integers_to_read[0][0])]
                        return oku

                if self.total_digits_outside_triplets == 0:
                    if self.order_of_last_zero_digit == 2:
                        # number like x00, read ordinal x00 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.ORDINAL_HUNDREDS[0]
                        return oku
                    if self.order_of_last_zero_digit == 1:
                        # number like xy0, read ordinal xy0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.ORDINAL_TENS[int(self.integers_to_read[0][1])]
                        return oku
                    if self.order_of_last_zero_digit == 0:
                        # number like xyz, read ordinal xyz and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        if not self.integers_to_read[0][2] == "0":
                            oku += self.ORDINAL_ONES[int(self.integers_to_read[0][2])]
                        return oku

            if self.total_triplets_to_read >= 2:
                if self.total_digits_outside_triplets == 2:
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 1:
                        # number like x0 and all 0s, read ordinal x0 0..0 and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        oku += self.ORDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 2:
                        # number like xy and all 0s, read ordinal xy 0..0 and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        if not self.integers_to_read[0][1] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][1])]
                        oku += self.ORDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit < len(self.integers_to_read[0]) - 2:
                        # number like xy and others, read cardinal xy n..n and return
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][0])]
                        if not self.integers_to_read[0][1] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][1])]

                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]

                if self.total_digits_outside_triplets == 1:
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 1:
                        # number like x and all 0s, read ordinal x 0..0 and return
                        if not (self.total_triplets_to_read == 2 and self.integers_to_read[0][0] == "1"):
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.ORDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit < len(self.integers_to_read[0]) - 1:
                        # number like x and others, read cardinal x n..n and return
                        if not (self.total_triplets_to_read == 2 and self.integers_to_read[0][0] == "1"):
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]

                if self.total_digits_outside_triplets == 0:
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 1:
                        # number like x00 and all 0s, read ordinal x00 0..0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.ORDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 2:
                        # number like xy0 and all 0s, read ordinal xy0 0..0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        oku += self.ORDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - 3:
                        # number like xyz and all 0s, read ordinal xyz 0..0 and return
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        if not self.integers_to_read[0][2] == "0":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][2])]
                        oku += self.ORDINAL_TRIPLETS[self.total_triplets_to_read - 1]
                        return oku
                    if self.order_of_last_zero_digit < len(self.integers_to_read[0]) - 3:
                        # number like xyz and all others, read cardinal xyz n..n
                        if not self.integers_to_read[0][0] == "1":
                            oku += self.CARDINAL_ONES[int(self.integers_to_read[0][0])]
                        oku += self.CARDINAL_HUNDREDS[0]
                        oku += self.CARDINAL_TEN[int(self.integers_to_read[0][1])]
                        if not self.integers_to_read[0][2] == "0":
                            if not (self.total_triplets_to_read == 2 and self.integers_to_read[0][2] == "1"):
                                oku += self.CARDINAL_ONES[int(self.integers_to_read[0][2])]
                        oku += self.CARDINAL_TRIPLETS[self.total_triplets_to_read - 1]

                for i in list(range(self.total_triplets_to_read - 1, 0, -1)):
                    okunan_grup_sirasi = self.total_triplets_to_read - i
                    if self.total_digits_outside_triplets == 0:
                        son_okunan_basamak_sirasi = okunan_grup_sirasi * 3
                    else:
                        son_okunan_basamak_sirasi = (okunan_grup_sirasi - 1) * 3 + self.total_digits_outside_triplets

                    if not self.integers_to_read[0][son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 3] == "000":
                        if not self.integers_to_read[0][son_okunan_basamak_sirasi] == "0":
                            if not self.integers_to_read[0][son_okunan_basamak_sirasi] == "1":
                                oku += self.CARDINAL_ONES[
                                    int(self.integers_to_read[0][son_okunan_basamak_sirasi])]
                            if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - (
                                    son_okunan_basamak_sirasi) - 1:
                                if i == 1:
                                    oku += self.ORDINAL_HUNDREDS[0]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_HUNDREDS[0]
                                    oku += self.ORDINAL_TRIPLETS[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_HUNDREDS[0]

                        if not self.integers_to_read[0][son_okunan_basamak_sirasi + 1] == "0":
                            if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - (
                                    son_okunan_basamak_sirasi) - 2:
                                if i == 1:
                                    oku += self.ORDINAL_TENS[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 1])]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_TEN[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 1])]
                                    oku += self.ORDINAL_TRIPLETS[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_TEN[
                                    int(self.integers_to_read[0][son_okunan_basamak_sirasi + 1])]

                        if not self.integers_to_read[0][son_okunan_basamak_sirasi + 2] == "0":
                            if self.order_of_last_zero_digit == len(self.integers_to_read[0]) - (
                                    son_okunan_basamak_sirasi) - 3:
                                if i == 1:
                                    oku += self.ORDINAL_ONES[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    return oku
                                if i == 2:
                                    if not self.integers_to_read[0][
                                           son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                        oku += self.CARDINAL_ONES[
                                            int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    elif not self.integers_to_read[0][son_okunan_basamak_sirasi + 2] == "1":
                                        oku += self.CARDINAL_ONES[
                                            int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.ORDINAL_TRIPLETS[i - 1]
                                    return oku
                                if i > 2:
                                    oku += self.CARDINAL_ONES[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.ORDINAL_TRIPLETS[i - 1]
                                    return oku
                            else:
                                if not self.integers_to_read[0][
                                       son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                    oku += self.CARDINAL_ONES[
                                        int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                else:
                                    if not self.integers_to_read[0][
                                           son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                        oku += self.CARDINAL_ONES[
                                            int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]
                                    elif not self.integers_to_read[0][son_okunan_basamak_sirasi + 2] == "1":
                                        oku += self.CARDINAL_ONES[
                                            int(self.integers_to_read[0][son_okunan_basamak_sirasi + 2])]

                        oku += self.CARDINAL_TRIPLETS[i - 1]

        return oku

    def to_ordinal_num(self, value):
        oku = ""
        isordinal = self.verify_ordinal(value)
        if isordinal:
            self.splitnum(value)
            oku = self.integers_to_read[0] + self.ORDINAL_SIGN[0]

        return oku

    # def inflect(self, value, text):

    def to_splitnum(self, val, hightxt="", lowtxt="", jointxt="", divisor=100, longval=True, cents=True):
        kesirlibolum = str(int(val * 10 ** self.precision))
        self.integers_to_read = [str(int(val)), kesirlibolum[len(kesirlibolum) - self.precision:]]
        if len(self.integers_to_read[0]) % 3 > 0:
            self.total_triplets_to_read = (len(self.integers_to_read[0]) // 3) + 1
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

    def to_year(self, value, **kwargs):
        return self.to_cardinal(value)

    def to_currency(self, value, **kwargs):
        valueparts = self.to_cardinal(value).split(self.pointword)
        if len(valueparts) == 1:
            return valueparts[0] + self.CURRENCY_UNIT[0]
        if len(valueparts) == 2:
            return self.CURRENCY_UNIT[0].join(valueparts) + self.CURRENCY_SUBUNIT[0]

            # def base_setup(self):

            # def setup(self):

            # def test(self, value):
