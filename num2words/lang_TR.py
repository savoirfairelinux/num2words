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
        self.negword = "eksi "
        self.pointword = "virgül"
        self.CURRENCY_UNIT = ("lira",)
        self.CURRENCY_SUBUNIT = ("kuruş",)
        # type(%s) not in [long, int, float]
        self.errmsg_nonnum = "Sadece sayılar yazıya çevrilebilir."
        # Cannot treat float %s as ordinal.
        self.errmsg_floatord = "Tam sayı olmayan {} sıralamada kullanılamaz."
        # Cannot treat negative num %s as ordinal.
        self.errmsg_negord = "Pozitif olmayan {} sıralamada kullanılamaz."
        # abs(%s) must be less than %s.
        self.errmsg_toobig = "abs({}) sayı yazıya çevirmek için çok büyük. Yazıya çevrilebilecek en büyük rakam {}."
        self.exclude_title = ["et", "virgule", "moins"]
        # ordered number tuples in Turkish
        self.ORDINAL_SIGN = (",",)
        self.CARDINAL_BIRLER = (
            "sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz",)
        self.ORDINAL_BIRLER = (
            "", "birinci", "ikinci", "üçüncü", "dördüncü", "beşinci", "altıncı", "yedinci", "sekizinci", "dokuzuncu",)
        self.CARDINAL_ONLAR = (
            "", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan",)
        self.ORDINAL_ONLAR = (
            "", "onuncu", "yirminci", "otuzuncu", "kırkıncı", "ellinci", "altmışıncı", "yetmişinci", "sekseninci",
            "doksanıncı",)
        self.CARDINAL_YUZLER = ("yüz",)
        self.ORDINAL_YUZLER = ("yüzüncü",)
        self.CARDINAL_UCLU_GRUPLAR = ("", "bin", "milyon", "milyar", "trilyon", "katrilyon", "kentilyon",)
        self.ORDINAL_UCLU_GRUPLAR = (
            "", "bininci", "milyonuncu", "milyarıncı", "trilyonuncu", "katrilyonuncu", "kentilyon",)
        self.MAXVAL = (10 ** (len(self.CARDINAL_UCLU_GRUPLAR) * 3)) - 1

        self.okunacak_ham_sayi = []
        self.okunacak_tam_sayi = []
        self.okunacak_uclu_grup_sayisi = 0
        self.okunacak_artik_basamak_sayisi = 0
        self.son_sifir_basamagi = 0
        self.okunan_sayi = {}

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

            if self.son_sifir_basamagi >= len(self.okunacak_tam_sayi[0]):
                # number like 00 and all 0s and even more, raise error
                return oku

            if self.okunacak_uclu_grup_sayisi == 1:
                if self.okunacak_artik_basamak_sayisi == 2:
                    if self.son_sifir_basamagi == 1:
                        # number like x0, read cardinal x0 and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        return oku
                    if self.son_sifir_basamagi == 0:
                        # number like xy, read cardinal xy and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                    if not self.okunacak_tam_sayi[0][0] == "0":
                        oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][1])]
                    return oku

                if self.okunacak_artik_basamak_sayisi == 1:
                    if self.son_sifir_basamagi == 0:
                        # number like x, read ordinal x and return
                        oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        return oku

                if self.okunacak_artik_basamak_sayisi == 0:
                    if self.son_sifir_basamagi == 2:
                        # number like x00, read cardinal x00 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        return oku
                    if self.son_sifir_basamagi == 1:
                        # number like xy0, read cardinal xy0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        return oku
                    if self.son_sifir_basamagi == 0:
                        # number like xyz, read cardinal xyz and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        if not self.okunacak_tam_sayi[0][2] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][2])]
                        return oku

            if self.okunacak_uclu_grup_sayisi >= 2:
                if self.okunacak_artik_basamak_sayisi == 2:
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x0 and all 0s, read cardinal x0 0..0 and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 2:
                        # number like xy and all 0s, read cardinal xy 0..0 and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        if not self.okunacak_tam_sayi[0][1] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][1])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi < len(self.okunacak_tam_sayi[0]) - 2:
                        # number like xy and others, read cardinal xy n..n and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        if not self.okunacak_tam_sayi[0][1] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][1])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]

                if self.okunacak_artik_basamak_sayisi == 1:
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x and all 0s, read cardinal x 0..0 and return
                        if not (self.okunacak_uclu_grup_sayisi == 2 and self.okunacak_tam_sayi[0][0] == "1"):
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi < len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x and others, read cardinal x n..n and return
                        if not (self.okunacak_uclu_grup_sayisi == 2 and self.okunacak_tam_sayi[0][0] == "1"):
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]

                if self.okunacak_artik_basamak_sayisi == 0:
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x00 and all 0s, read cardinal x00 0..0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 2:
                        # number like xy0 and all 0s, read cardinal xy0 0..0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 3:
                        # number like xyz and all 0s, read cardinal xyz 0..0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        if not self.okunacak_tam_sayi[0][2] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][2])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi < len(self.okunacak_tam_sayi[0]) - 3:
                        # number like xyz and all others, read cardinal xyz n..n
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        if not self.okunacak_tam_sayi[0][2] == "0":
                            if not (self.okunacak_uclu_grup_sayisi == 2 and self.okunacak_tam_sayi[0][2] == "1"):
                                oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][2])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]

                for i in list(range(self.okunacak_uclu_grup_sayisi - 1, 0, -1)):
                    okunan_grup_sirasi = self.okunacak_uclu_grup_sayisi - i
                    if self.okunacak_artik_basamak_sayisi == 0:
                        son_okunan_basamak_sirasi = okunan_grup_sirasi * 3
                    else:
                        son_okunan_basamak_sirasi = (okunan_grup_sirasi - 1) * 3 + self.okunacak_artik_basamak_sayisi

                    if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 3] == "000":
                        if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi] == "0":
                            if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi] == "1":
                                oku += self.CARDINAL_BIRLER[
                                    int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi])]
                            if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - (
                                    son_okunan_basamak_sirasi) - 1:
                                if i == 1:
                                    oku += self.CARDINAL_YUZLER[0]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_YUZLER[0]
                                    oku += self.CARDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_YUZLER[0]

                        if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1] == "0":
                            if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - (
                                    son_okunan_basamak_sirasi) - 2:
                                if i == 1:
                                    oku += self.CARDINAL_ONLAR[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1])]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_ONLAR[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1])]
                                    oku += self.CARDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_ONLAR[
                                    int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1])]

                        if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2] == "0":
                            if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - (
                                    son_okunan_basamak_sirasi) - 3:
                                if i == 1:
                                    oku += self.CARDINAL_BIRLER[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    return oku
                                if i == 2:
                                    if not self.okunacak_tam_sayi[0][
                                           son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                        oku += self.CARDINAL_BIRLER[
                                            int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    elif not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2] == "1":
                                        oku += self.CARDINAL_BIRLER[
                                            int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.CARDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                                if i > 2:
                                    oku += self.CARDINAL_BIRLER[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.CARDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                            else:
                                if not self.okunacak_tam_sayi[0][
                                       son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                    oku += self.CARDINAL_BIRLER[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                else:
                                    if i == 2:
                                        if not self.okunacak_tam_sayi[0][
                                               son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                            oku += self.CARDINAL_BIRLER[
                                                int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                        elif not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2] == "1":
                                            oku += self.CARDINAL_BIRLER[
                                                int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]

                        oku += self.CARDINAL_UCLU_GRUPLAR[i - 1]

        return oku

    def to_cardinal_float(self, value):
        self.splitnum(value)
        oku = ""
        oku += self.pointword
        if not self.okunacak_tam_sayi[1][0] == "0":
            oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[1][0])]
        try:
            if not self.okunacak_tam_sayi[1][1] == "0":
                oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[1][1])]
        except:
            raise
        finally:
            oku = self.to_cardinal(int(self.okunacak_tam_sayi[0])) + oku
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
            iscardinal = False
            raise TypeError(self.errmsg_nonnum)
        if abs(value) >= self.MAXVAL:
            iscardinal = False
            raise OverflowError(self.errmsg_toobig.format(value, self.MAXVAL))
        return iscardinal

    def verify_ordinal(self, value):
        isordinal = True
        try:
            if not int(value) == value:
                isordinal = False
            if not abs(value) == value:
                isordinal = False
                raise TypeError(self.errmsg_negord.format(value))
        except (ValueError, TypeError):
            isordinal = False
            raise TypeError(self.errmsg_nonnum)
        if abs(value) >= self.MAXVAL:
            isordinal = False
            raise OverflowError(self.errmsg_toobig.format(value, self.MAXVAL))
        return isordinal

    # def verify_num(self, value):

    # def set_wordnums(self):

    def to_ordinal(self, value):
        oku = ""
        isordinal = self.verify_ordinal(value)
        if isordinal:
            self.splitnum(value)

            if self.son_sifir_basamagi >= len(self.okunacak_tam_sayi[0]):
                # number like 00 and all 0s and even more, raise error
                return oku

            if self.okunacak_uclu_grup_sayisi == 1:
                if self.okunacak_artik_basamak_sayisi == 2:
                    if self.son_sifir_basamagi == 1:
                        # number like x0, read ordinal x0 and return
                        oku += self.ORDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        return oku
                    if self.son_sifir_basamagi == 0:
                        # number like xy, read ordinal xy and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                    if not self.okunacak_tam_sayi[0][0] == "0":
                        oku += self.ORDINAL_BIRLER[int(self.okunacak_tam_sayi[0][1])]
                    return oku

                if self.okunacak_artik_basamak_sayisi == 1:
                    if self.son_sifir_basamagi == 0:
                        # number like x, read ordinal x and return
                        oku += self.ORDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        return oku

                if self.okunacak_artik_basamak_sayisi == 0:
                    if self.son_sifir_basamagi == 2:
                        # number like x00, read ordinal x00 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.ORDINAL_YUZLER[0]
                        return oku
                    if self.son_sifir_basamagi == 1:
                        # number like xy0, read ordinal xy0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.ORDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        return oku
                    if self.son_sifir_basamagi == 0:
                        # number like xyz, read ordinal xyz and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        if not self.okunacak_tam_sayi[0][2] == "0":
                            oku += self.ORDINAL_BIRLER[int(self.okunacak_tam_sayi[0][2])]
                        return oku

            if self.okunacak_uclu_grup_sayisi >= 2:
                if self.okunacak_artik_basamak_sayisi == 2:
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x0 and all 0s, read ordinal x0 0..0 and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.ORDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 2:
                        # number like xy and all 0s, read ordinal xy 0..0 and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        if not self.okunacak_tam_sayi[0][1] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][1])]
                        oku += self.ORDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi < len(self.okunacak_tam_sayi[0]) - 2:
                        # number like xy and others, read cardinal xy n..n and return
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][0])]
                        if not self.okunacak_tam_sayi[0][1] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][1])]

                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]

                if self.okunacak_artik_basamak_sayisi == 1:
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x and all 0s, read ordinal x 0..0 and return
                        if not (self.okunacak_uclu_grup_sayisi == 2 and self.okunacak_tam_sayi[0][0] == "1"):
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.ORDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi < len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x and others, read cardinal x n..n and return
                        if not (self.okunacak_uclu_grup_sayisi == 2 and self.okunacak_tam_sayi[0][0] == "1"):
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]

                if self.okunacak_artik_basamak_sayisi == 0:
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 1:
                        # number like x00 and all 0s, read ordinal x00 0..0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.ORDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 2:
                        # number like xy0 and all 0s, read ordinal xy0 0..0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        oku += self.ORDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - 3:
                        # number like xyz and all 0s, read ordinal xyz 0..0 and return
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        if not self.okunacak_tam_sayi[0][2] == "0":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][2])]
                        oku += self.ORDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]
                        return oku
                    if self.son_sifir_basamagi < len(self.okunacak_tam_sayi[0]) - 3:
                        # number like xyz and all others, read cardinal xyz n..n
                        if not self.okunacak_tam_sayi[0][0] == "1":
                            oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][0])]
                        oku += self.CARDINAL_YUZLER[0]
                        oku += self.CARDINAL_ONLAR[int(self.okunacak_tam_sayi[0][1])]
                        if not self.okunacak_tam_sayi[0][2] == "0":
                            if not (self.okunacak_uclu_grup_sayisi == 2 and self.okunacak_tam_sayi[0][2] == "1"):
                                oku += self.CARDINAL_BIRLER[int(self.okunacak_tam_sayi[0][2])]
                        oku += self.CARDINAL_UCLU_GRUPLAR[self.okunacak_uclu_grup_sayisi - 1]

                for i in list(range(self.okunacak_uclu_grup_sayisi - 1, 0, -1)):
                    okunan_grup_sirasi = self.okunacak_uclu_grup_sayisi - i
                    if self.okunacak_artik_basamak_sayisi == 0:
                        son_okunan_basamak_sirasi = okunan_grup_sirasi * 3
                    else:
                        son_okunan_basamak_sirasi = (okunan_grup_sirasi - 1) * 3 + self.okunacak_artik_basamak_sayisi

                    if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 3] == "000":
                        if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi] == "0":
                            if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi] == "1":
                                oku += self.CARDINAL_BIRLER[
                                    int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi])]
                            if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - (
                                    son_okunan_basamak_sirasi) - 1:
                                if i == 1:
                                    oku += self.ORDINAL_YUZLER[0]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_YUZLER[0]
                                    oku += self.ORDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_YUZLER[0]

                        if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1] == "0":
                            if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - (
                                    son_okunan_basamak_sirasi) - 2:
                                if i == 1:
                                    oku += self.ORDINAL_ONLAR[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1])]
                                    return oku
                                elif i > 1:
                                    oku += self.CARDINAL_ONLAR[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1])]
                                    oku += self.ORDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                            else:
                                oku += self.CARDINAL_ONLAR[
                                    int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 1])]

                        if not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2] == "0":
                            if self.son_sifir_basamagi == len(self.okunacak_tam_sayi[0]) - (
                                    son_okunan_basamak_sirasi) - 3:
                                if i == 1:
                                    oku += self.ORDINAL_BIRLER[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    return oku
                                if i == 2:
                                    if not self.okunacak_tam_sayi[0][
                                           son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                        oku += self.CARDINAL_BIRLER[
                                            int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    elif not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2] == "1":
                                        oku += self.CARDINAL_BIRLER[
                                            int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.ORDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                                if i > 2:
                                    oku += self.CARDINAL_BIRLER[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    oku += self.ORDINAL_UCLU_GRUPLAR[i - 1]
                                    return oku
                            else:
                                if not self.okunacak_tam_sayi[0][
                                       son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                    oku += self.CARDINAL_BIRLER[
                                        int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                else:
                                    if not self.okunacak_tam_sayi[0][
                                           son_okunan_basamak_sirasi: son_okunan_basamak_sirasi + 2] == "00":
                                        oku += self.CARDINAL_BIRLER[
                                            int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]
                                    elif not self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2] == "1":
                                        oku += self.CARDINAL_BIRLER[
                                            int(self.okunacak_tam_sayi[0][son_okunan_basamak_sirasi + 2])]

                        oku += self.CARDINAL_UCLU_GRUPLAR[i - 1]

        return oku

    def to_ordinal_num(self, value):
        oku = ""
        isordinal = self.verify_ordinal(value)
        if isordinal:
            self.splitnum(value)
            oku = self.okunacak_tam_sayi[0] + self.ORDINAL_SIGN[0]

        return oku

    # def inflect(self, value, text):

    def to_splitnum(self, val, hightxt="", lowtxt="", jointxt="", divisor=100, longval=True, cents=True):
        self.okunan_sayi = {}
        self.okunacak_ham_sayi = str(val)
        self.okunacak_tam_sayi = self.okunacak_ham_sayi.split(".")
        if len(self.okunacak_tam_sayi[0]) % 3 > 0:
            self.okunacak_uclu_grup_sayisi = (len(self.okunacak_tam_sayi[0]) // 3) + 1
        elif len(self.okunacak_tam_sayi[0]) % 3 == 0:
            self.okunacak_uclu_grup_sayisi = len(self.okunacak_tam_sayi[0]) // 3
        self.okunacak_artik_basamak_sayisi = len(self.okunacak_tam_sayi[0]) % 3

        okunacak = list(self.okunacak_tam_sayi[0][::-1])
        self.son_sifir_basamagi = 0
        for i in range(len(okunacak) - 1):
            if okunacak[i] == "0":
                self.son_sifir_basamagi = i + 1
            else:
                break

    def to_year(self, value, **kwargs):
        return self.to_cardinal(value)

    def to_currency(self, value, **kwargs):
        return self.to_cardinal(value)

        # def base_setup(self):

        # def setup(self):

        # def test(self, value):
