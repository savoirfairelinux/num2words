# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2018, Abdullah Alhazmy, Alhazmy13.  All Rights Reserved.


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

import decimal
import math
import re
from decimal import Decimal
from math import floor

from .base import Num2Word_Base

CURRENCY_SR = [("ريال", "ريالان", "ريالات", "ريالاً"),
               ("هللة", "هللتان", "هللات", "هللة")]
CURRENCY_EGP = [("جنيه", "جنيهان", "جنيهات", "جنيهاً"),
                ("قرش", "قرشان", "قروش", "قرش")]
CURRENCY_KWD = [("دينار", "ديناران", "دينارات", "ديناراً"),
                ("فلس", "فلسان", "فلس", "فلس")]
CURRENCY_TND = [("دينار", "ديناران", "دينارات", "ديناراً"),
                ("مليماً", "ميلمان", "مليمات", "مليم")]

ARABIC_ONES = [
    "", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية",
    "تسعة",
    "عشرة", "أحد عشر", "اثنا عشر", "ثلاثة عشر", "أربعة عشر", "خمسة عشر",
    "ستة عشر", "سبعة عشر", "ثمانية عشر",
    "تسعة عشر"
]


class Num2Word_AR(Num2Word_Base):
    errmsg_toobig = "abs(%s) must be less than %s."
    MAXVAL = 10**51

    def __init__(self):
        super().__init__()
        
        self.number = 0
        self.arabicPrefixText = ""
        self.arabicSuffixText = ""
        self.integer_value = 0
        self._decimalValue = ""
        self.partPrecision = 2
        self.currency_unit = CURRENCY_SR[0]
        self.currency_subunit = CURRENCY_SR[1]
        self.isCurrencyPartNameFeminine = True
        self.isCurrencyNameFeminine = False
        self.separator = 'و'
        self.rafea = True        # to check in which grammatical case we are in
        self.flag = False
        self.arabicOnes = ARABIC_ONES
        self.arabicFeminineOnes = [
            "", "إحدى", "اثنتان", "ثلاث", "أربع", "خمس", "ست", "سبع", "ثمان",
            "تسع",
            "عشر", "إحدى عشرة", "اثنتا عشرة", "ثلاث عشرة", "أربع عشرة",
            "خمس عشرة", "ست عشرة", "سبع عشرة", "ثماني عشرة",
            "تسع عشرة"
        ]
        self.arabicOrdinal = [
            "", "اول", "ثاني", "ثالث", "رابع", "خامس", "سادس", "سابع", "ثامن",
            "تاسع", "عاشر", "حادي عشر", "ثاني عشر", "ثالث عشر", "رابع عشر",
            "خامس عشر", "سادس عشر", "سابع عشر", "ثامن عشر", "تاسع عشر"
        ]
        self.arabicTens = [
            "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون",
            "تسعون"
        ]
        self.arabicHundreds = [
            "", "مائة", "مئتان", "ثلاثمائة", "أربعمائة", "خمسمائة", "ستمائة",
            "سبعمائة", "ثمانمائة", "تسعمائة"
        ]

        self.arabicAppendedTwos = [
            "مئتا", "ألفا", "مليونا", "مليارا", "تريليونا", "كوادريليونا",
            "كوينتليونا", "سكستيليونا", "سبتيليونا", "أوكتيليونا ",
            "نونيليونا", "ديسيليونا", "أندسيليونا", "دوديسيليونا",
            "تريديسيليونا", "كوادريسيليونا", "كوينتينيليونا"
        ]
        self.arabicTwos = [
            "مئتان", "ألفان", "مليونان", "ملياران", "تريليونان",
            "كوادريليونان", "كوينتليونان", "سكستيليونان", "سبتيليونان",
            "أوكتيليونان ", "نونيليونان ", "ديسيليونان", "أندسيليونان",
            "دوديسيليونان", "تريديسيليونان", "كوادريسيليونان", "كوينتينيليونان"
        ]
        self.arabicGroup = [
            "مائة", "ألف", "مليون", "مليار", "تريليون", "كوادريليون",
            "كوينتليون", "سكستيليون", "سبتيليون", "أوكتيليون", "نونيليون",
            "ديسيليون", "أندسيليون", "دوديسيليون", "تريديسيليون",
            "كوادريسيليون", "كوينتينيليون"
        ]
        self.arabicAppendedGroup = [
            "", "ألفاً", "مليوناً", "ملياراً", "تريليوناً", "كوادريليوناً",
            "كوينتليوناً", "سكستيليوناً", "سبتيليوناً", "أوكتيليوناً",
            "نونيليوناً", "ديسيليوناً", "أندسيليوناً", "دوديسيليوناً",
            "تريديسيليوناً", "كوادريسيليوناً", "كوينتينيليوناً"
        ]
        self.arabicPluralGroups = [
            "", "آلاف", "ملايين", "مليارات", "تريليونات", "كوادريليونات",
            "كوينتليونات", "سكستيليونات", "سبتيليونات", "أوكتيليونات",
            "نونيليونات", "ديسيليونات", "أندسيليونات", "دوديسيليونات",
            "تريديسيليونات", "كوادريسيليونات", "كوينتينيليونات"
        ]
        assert len(self.arabicAppendedGroup) == len(self.arabicGroup)
        assert len(self.arabicPluralGroups) == len(self.arabicGroup)
        assert len(self.arabicAppendedTwos) == len(self.arabicTwos)

    def number_to_arabic(self, arabic_prefix_text, arabic_suffix_text):
        self.arabicPrefixText = arabic_prefix_text
        self.arabicSuffixText = arabic_suffix_text
        self.extract_integer_and_decimal_parts()

    def extract_integer_and_decimal_parts(self):
        splits = re.split('\\.', str(self.number))

        self.integer_value = int(splits[0])
        if len(splits) > 1:
            self._decimalValue = int(self.decimal_value(splits[1]))
            # print("extract_integer_and_decimal_parts",self.decimal_value)
        else:
            self._decimalValue = 0

    def decimal_value(self, decimal_part):

        # if self.partPrecision is not len(decimal_part):
        #     decimal_part_length = len(decimal_part)

        #     decimal_part_builder = decimal_part
        #     for i in range(0, self.partPrecision - decimal_part_length):
        #         decimal_part_builder += '0'
        #     decimal_part = decimal_part_builder

        #     if len(decimal_part) <= self.partPrecision:
        #         dec = len(decimal_part)
        #     else:
        #         dec = self.partPrecision
        #     result = decimal_part[0: dec]
        # else:
        result = decimal_part

        # The following is useless (never happens)
        # for i in range(len(result), self.partPrecision):
        #     result += '0'
        return result

    def digit_feminine_status(self, digit, group_level, currencyPartName= True,rafea=True):
        self.isCurrencyPartNameFeminine = currencyPartName
        if group_level == -1:
            if self.isCurrencyPartNameFeminine:
                conversion = self.arabicFeminineOnes[int(digit)]
            else:
                # Note: this never happens
                conversion = self.arabicOnes[int(digit)]
        elif group_level == 0:
            if self.isCurrencyNameFeminine:
                conversion = self.arabicFeminineOnes[int(digit)]
            else:
                conversion = self.arabicOnes[int(digit)]
        else:
            conversion = self.arabicOnes[int(digit)]
            # Change "اثنا" to "اثني"            
        if not rafea:
            if conversion == "اثنا عشر":
                conversion = "اثني عشر"
            if conversion == "اثنتا عشر":
                conversion = "اثنتي عشر"
        return conversion


    def change_arabic_word_end(self,word):
        if word == "ثمان" or word == "مليون":
            return word
        # Check if the word ends with "ان" and replace with "ين"
        if word.endswith("ان"):
            word = word[:-2] + "ين"
        elif word.endswith("ون"):
            word = word[:-2] + "ين"
        # Check if the word ends with "ا" and replace with "ي"
        else:
            if word.endswith("ا"):
                word = word[:-1] + "ي"
        return word




    def process_arabic_group(self, group_number, group_level,
                             remaining_number, rafea):
        tens = Decimal(group_number) % Decimal(100)
        hundreds = Decimal(group_number) / Decimal(100)
        ret_val = ""

        if int(hundreds) > 0:
            if tens == 0 and int(hundreds) == 2:
                if rafea:
                            ret_val = "{}".format(
                            self.arabicAppendedTwos[0])
                else:
                    ret_val = "{}".format(
                    self.change_arabic_word_end(self.arabicAppendedTwos[0]))
            else:
                if rafea:
                    ret_val = "{}".format(
                    self.arabicHundreds[int(hundreds)])
                else:
                    ret_val = "{}".format(
                    self.change_arabic_word_end(self.arabicHundreds[int(hundreds)]))
                    # print("returned arabic hundreds",ret_val)
                if ret_val != "" and tens != 0:
                    ret_val += " و"

        if tens > 0:
            if tens < 20:
                # if int(group_level) >= len(self.arabicTwos):
                #     raise OverflowError(self.errmsg_toobig %
                #                         (self.number, self.MAXVAL))
                assert int(group_level) < len(self.arabicTwos)
                if tens == 2 and int(hundreds) == 0 and group_level > 0:
                    pow = int(math.log10(self.integer_value))
                    if self.integer_value > 10 and pow % 3 == 0 and \
                            self.integer_value == 2 * (10 ** pow):
                        if rafea:
                            ret_val = "{}".format(
                            self.arabicAppendedTwos[int(group_level)])
                        else:
                            ret_val = "{}".format(
                            self.change_arabic_word_end(self.arabicAppendedTwos[int(group_level)]))
                    else:
                        if rafea:
                            ret_val = "{}".format(
                            self.arabicTwos[int(group_level)])
                        else:
                            ret_val = "{}".format(
                            self.change_arabic_word_end(self.arabicTwos[int(group_level)]))
                else:

                    if tens == 1 and group_level > 0 and hundreds == 0:
                        # Note: this never happens
                        # (hundreds == 0 only if group_number is 0)
                        ret_val += ""
                    elif (tens == 1 or tens == 2) and (
                            group_level == 0 or group_level == -1) and \
                            hundreds == 0 and remaining_number == 0:
                        # Note: this never happens (idem)
                        ret_val += ""
                    elif tens == 1 and group_level > 0:
                        if rafea:
                            ret_val += self.arabicGroup[int(group_level)]
                        else:
                            ret_val += self.change_arabic_word_end(self.arabicGroup[int(group_level)])

                    else:
                        if rafea:
                            ret_val += self.digit_feminine_status(int(tens),
                                                              group_level,False, rafea)
                        else:
                            ret_val += self.change_arabic_word_end(self.digit_feminine_status(int(tens),
                                                              group_level,False, rafea))
                    
                #     else:
                #         if tens >= 20:
                        
                #             ones = tens % 10
                #             tens = (tens / 10) - 2
                #             if ones > 0:
                #                 ret_val += self.digit_feminine_status(ones, group_level, rafea)
                #             if ret_val != "" and ones != 0:
                #                 ret_val += " و "


                #             # ret_val += self.arabicTens[int(tens)]
                #             if rafea:
                #                 ret_val += self.arabicTens[int(tens)]
                #             else:
                #                 ret_val += self.change_arabic_word_end(self.arabicTens[int(tens)])

                # return ret_val
                #    else:
                #         if tens >= 20:
                        
                #             ones = tens % 10
                #             tens = (tens / 10) - 2
                #             if ones > 0:
                #                 ret_val += self.digit_feminine_status(ones, group_level, rafea)
                #             if ret_val != "" and ones != 0:
                #                 ret_val += " و "


                #             # ret_val += self.arabicTens[int(tens)]
                #             if rafea:
                #                 ret_val += self.arabicTens[int(tens)]
                #             else:
                #                 ret_val += self.change_arabic_word_end(self.arabicTens[int(tens)])

                # return ret_val
            else:
                    # Handling tens (20 and above)
                    ones = tens % 10
                    tens = (tens // 10) - 2  # Tens is decremented because array starts at 20
                    if ones > 0:
                        if group_level == -1:
                            if rafea:
                                ret_val += self.digit_feminine_status(ones, group_level, False,rafea)
                            else:
                                ret_val += self.change_arabic_word_end(self.digit_feminine_status(ones, group_level, False,rafea))
                        else:
                            if rafea:
                                ret_val += self.digit_feminine_status(ones, group_level, rafea)
                            else:
                                ret_val += self.change_arabic_word_end(self.digit_feminine_status(ones, group_level, rafea))

                    if ret_val != "" and ones != 0:
                        ret_val += " و"
                    if rafea:
                        ret_val += self.arabicTens[int(tens)]
                    else:
                        ret_val += self.change_arabic_word_end(self.arabicTens[int(tens)])

        return ret_val

    # We use this instead of built-in `abs` function,
    # because `abs` suffers from loss of precision for big numbers
    def abs(self, number):
        return number if number >= 0 else -number

    # We use this instead of `"{:09d}".format(number)`,
    # because the string conversion suffers from loss of
    # precision for big numbers
    def to_str(self, number):
        integer = int(number)
        if integer == number:
            return str(integer)
        decimal = round((number - integer) * 10**9)
        # print("decimal in to str", decimal)
        # print("returned decimal string{:09d}".format(decimal).rstrip("0"))
        return str(integer) + "." + "{:09d}".format(decimal).rstrip("0")


    def convert(self, value, rafea):
        # print(f"Converting value: {value}")

        self.number = self.to_str(value)
        # print(f"Converted number: {self.number}")
  
        self.number_to_arabic(self.arabicPrefixText, self.arabicSuffixText)
        # print("x",x)
        return self.convert_to_arabic(rafea)

    def convert_fraction_to_text(self, number_str, number,rafea= False):
        if self.flag:
            return number_str
        # print("convert to fraction function in")
        # decimal_value = self.extract_integer_and_decimal_parts()
        # number = int(decimal_value)
        # number_str = str(number)
        # print("number",self.to_str(number))
        number_converted = str(number)
        decimalPart = number_converted.split(".")
        # print("decimalPart", decimalPart)
        # print(len(decimalPart))
        
        if len(decimalPart) > 1:
                decimalPart_length = len(str(decimalPart[1]))
                decimalPart = int(decimalPart[1])
                
                if decimalPart != 0:
                    decimalPart = int(decimalPart)
                    # print(number)

                    if decimalPart_length == 1:
                        if decimalPart == 1:
                            return f"جزءاً {number_str} من العشر"
                        elif decimalPart == 2:
                            if self.rafea == True:
                                    return f"جزءان من العشر"
                            else:
                                    return f"جزئين من العشر"
                        elif 3<=decimalPart<10:
                            
                            return f"{number_str} أجزاء من العشر"
                        # impossible case, just to close if case 
                        else:
                            return f"{number_str} جزءاً من العشر"
                    elif decimalPart_length == 2:
                        if decimalPart == 1:
                            return f"جزءاً {number_str} من المئة"
                        elif decimalPart == 2:
                            if self.rafea == True:
                                    return f"جزءان من المئة"
                            else:
                                    return f"جزئين من المئة"
                        elif 3<=decimalPart<10:
                            
                            return f"{number_str} أجزاء من المئة"
                        
                        else:
                            return f"{number_str} جزءاً من المئة"
                    elif decimalPart_length == 3:
                        if decimalPart == 1:
                            return f"جزءاً {number_str} من اﻷلف"
                        if decimalPart == 2:
                            if self.rafea == True:
                                    return f"جزءان من اﻷلف"
                            else:
                                    return f"جزئين من اﻷلف"
                        elif 3<=decimalPart<10:
                            
                            return f"{number_str} أجزاء من اﻷلف"
                        
                        else:
                            return f"{number_str} جزءاً من اﻷلف"
                        
                    else:
                        return f"{number_str} جزءاً من اﻷلف"
            


    def convert_to_arabic(self, rafea):
        temp_number = Decimal(self.number)
        # print("temp_number",temp_number)
        if temp_number == Decimal(0):
            return "صفر"

        decimal_string = self.process_arabic_group(self._decimalValue,
                                                   -1,
                                                   Decimal(0), rafea=rafea)
        # print("decimal string before", decimal_string)
        # print(self.process_arabic_group(self._decimalValue,
                                                #    -1,
          
                                                # Decimal(0), rafea=rafea))
        decimal_string = self.convert_fraction_to_text(decimal_string, temp_number,rafea=rafea)
        
        if decimal_string == "اثنتا عشرة جزءاً من المئة":
            if not rafea:
                decimal_string = "اثنتي عشرة جزءاً من المئة"
        
        # print("decimal_string",decimal_string)
        ret_val = ""
        group = 0

        while temp_number > Decimal(0):

            temp_number_dec = Decimal(str(temp_number))
            try:
                number_to_process = int(temp_number_dec % Decimal(str(1000)))
            except decimal.InvalidOperation:
                decimal.getcontext().prec = len(
                    temp_number_dec.as_tuple().digits
                )
                number_to_process = int(temp_number_dec % Decimal(str(1000)))

            temp_number = int(temp_number_dec / Decimal(1000))

            group_description = \
                self.process_arabic_group(number_to_process,
                                          group,
                                          Decimal(floor(temp_number)), rafea=rafea)
            if group_description != '':
                if group > 0:
                    if ret_val != "":
                        if rafea:
                            ret_val = "و{}".format(ret_val)
                        else: 
                            ret_val = "و{}".format(self.change_arabic_word_end(ret_val))
                    if number_to_process != 2 and number_to_process != 1:
                        # if group >= len(self.arabicGroup):
                        #     raise OverflowError(self.errmsg_toobig %
                        #                         (self.number, self.MAXVAL)
                        #     )
                        assert group < len(self.arabicGroup)
                        if number_to_process % 100 != 1:
                            if 3 <= number_to_process <= 10:
                                if rafea:
                                    ret_val = "{} {}".format(
                                    self.arabicPluralGroups[group], ret_val)
                                else:
                                     ret_val = "{} {}".format((self.change_arabic_word_end(self.arabicPluralGroups[group])), ret_val)
                                    
                            else:
                                if ret_val != "":
                                    if rafea:
                                        ret_val = "{} {}".format(
                                        self.arabicAppendedGroup[group],
                                        ret_val)
                                    else:
                                        ret_val = "{} {}".format(
                                            self.change_arabic_word_end(self.arabicAppendedGroup[group]),
                                        ret_val)
                                else:
                                    if rafea:
                                        ret_val = "{} {}".format(
                                        self.arabicGroup[group], ret_val)
                                    else:
                                        ret_val = "{} {}".format(self.change_arabic_word_end(self.arabicGroup[group]),
                                            ret_val)
                                     
                        else:
                            if rafea:
                                ret_val = "{} {}".format(self.arabicGroup[group],
                                                     ret_val)
                            else:
                                ret_val = "{} {}".format(self.change_arabic_word_end(self.arabicGroup[group]),
                                                     ret_val)
                           
                                #########################################
                if rafea:
                    ret_val = "{} {}".format(group_description, ret_val)
                else:
                    ret_val = "{} {}".format(group_description, self.change_arabic_word_end(ret_val))


            group += 1
        formatted_number = ""
        if self.arabicPrefixText != "":
            formatted_number += "{} ".format(self.arabicPrefixText)
        formatted_number += ret_val
        if self.integer_value != 0:
            remaining100 = int(self.integer_value % 100)

            if remaining100 == 0:
                formatted_number += self.currency_unit[0]
            elif remaining100 == 1:
                formatted_number += self.currency_unit[0]
            elif remaining100 == 2:
                if self.integer_value == 2:
                    formatted_number += self.currency_unit[1]
                else:
                    formatted_number += self.currency_unit[0]
            elif 3 <= remaining100 <= 10:
                formatted_number += self.currency_unit[2]
            elif 11 <= remaining100 <= 99:
                formatted_number += self.currency_unit[3]
        if self._decimalValue != 0:
            formatted_number += "{}".format(self.separator)
            if decimal_string:
                formatted_number += decimal_string

        if self._decimalValue != 0:
            formatted_number += " "
            remaining100 = int(self._decimalValue % 100)

            if remaining100 == 0:
                formatted_number += self.currency_subunit[0]
            elif remaining100 == 1:
                formatted_number += self.currency_subunit[0]
            elif remaining100 == 2:
                formatted_number += self.currency_subunit[1]
            elif 3 <= remaining100 <= 10:
                formatted_number += self.currency_subunit[2]
            elif 11 <= remaining100 <= 99:
                formatted_number += self.currency_subunit[3]

        if self.arabicSuffixText != "":
            formatted_number += " {}".format(self.arabicSuffixText)

        return formatted_number

    def validate_number(self, number):
        if number >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))
        return number

    # def set_currency_prefer(self, currency, rafea=True):
    #     if currency == 'EGP':
    #         if rafea:
    #             self.currency_unit = CURRENCY_EGP[0]
    #             self.currency_subunit = CURRENCY_EGP[1]
    #         else:
    #             self.currency_unit = CURRENCY_EGP[0]
    #             self.change_arabic_word_end(self.currency_unit)
    #             self.currency_subunit = CURRENCY_EGP[1]
    #             self.change_arabic_word_end(self.currency_subunit)
    #     elif currency == 'KWD':
    #         if rafea:
    #             self.currency_unit = CURRENCY_KWD[0]
    #             self.currency_subunit = CURRENCY_KWD[1]
    #         else:
    #             self.currency_unit = CURRENCY_KWD[0]
    #             self.change_arabic_word_end(self.currency_unit)
    #             self.currency_subunit = CURRENCY_KWD[1]
    #             self.change_arabic_word_end(self.currency_subunit)
    #     else:
    #         if rafea:
    #             self.currency_unit = CURRENCY_SR[0]
    #             self.currency_subunit = CURRENCY_SR[1]
    #             # print(self.currency_unit, self.currency_subunit)
    #         else:
    #             self.currency_unit = CURRENCY_SR[0]
    #             self.change_arabic_word_end(self.currency_unit)
    #             self.currency_subunit = CURRENCY_SR[1]
    #             self.change_arabic_word_end(self.currency_subunit)

    def set_currency_prefer(self, currency):
        if currency == 'TND':
            self.currency_unit = CURRENCY_TND[0]
            self.currency_subunit = CURRENCY_TND[1]
            self.partPrecision = 3
        elif currency == 'EGP':
            self.currency_unit = CURRENCY_EGP[0]
            self.currency_subunit = CURRENCY_EGP[1]
            self.partPrecision = 2
        elif currency == 'KWD':
            self.currency_unit = CURRENCY_KWD[0]
            self.currency_subunit = CURRENCY_KWD[1]
            self.partPrecision = 2
        else:
            self.currency_unit = CURRENCY_SR[0]
            self.currency_subunit = CURRENCY_SR[1]
            self.partPrecision = 2

    # def to_currency(self, value, currency='SR', prefix='', suffix='', rafea=True):
    #     self.set_currency_prefer(currency,rafea=True)
    #     self.isCurrencyNameFeminine = False
    #     self.separator = "و"
    #     self.arabicOnes = ARABIC_ONES
    #     self.arabicPrefixText = prefix
    #     # print("suffix",suffix)
    #     if rafea:
    #         self.arabicSuffixText = suffix
    #         # print("suffix_rafea",suffix)
    #     else:
    #         self.arabicSuffixText = suffix
    #         # print("suffix",suffix)
    #         # self.change_arabic_word_end(self.arabicSuffixText)
    #     # print(self.arabicSuffixText)
    #     return self.convert(value=value, rafea=rafea)
    def to_currency(self, value, currency='SR', prefix='', suffix='', rafea=True):
        self.set_currency_prefer(currency)
        self.isCurrencyNameFeminine = False
        self.separator = " و"
        self.arabicOnes = ARABIC_ONES
        self.arabicPrefixText = prefix
        self.arabicSuffixText = suffix
        self.flag = True
        
        return self.convert(value=value, rafea=rafea)


    # def to_ordinal(self, number, prefix='', rafea=True):
    #     if number <= 19:
    #         return "{}".format(self.arabicOrdinal[number])
    #     if number < 100:
    #         self.isCurrencyNameFeminine = True
    #     else:
    #         self.isCurrencyNameFeminine = False
    #     self.currency_subunit = ('', '', '', '')
    #     self.currency_unit = ('', '', '', '')
    #     self.arabicPrefixText = prefix
    #     self.arabicSuffixText = ""
    #     return "{}".format(self.convert(self.abs(number)).strip())

    def to_ordinal(self, number, prefix='', rafea=True):
        if number <= 19:
            return "{}".format(self.arabicOrdinal[number])
        if number < 100:
            self.isCurrencyNameFeminine = True
        else:
            self.isCurrencyNameFeminine = False
        self.currency_subunit = ('', '', '', '')
        self.currency_unit = ('', '', '', '')
        self.arabicPrefixText = prefix
        self.arabicSuffixText = ""

        # Modify the output based on the value of the rafea argument
        if rafea:
            return "{}".format(self.convert(self.abs(number), rafea).strip())

        else:
            return "{}".format(self.convert(self.abs(number), rafea).strip())


    def to_year(self, value,rafea=True):
        value = self.validate_number(value)
        return self.to_cardinal(value, rafea)

    def to_ordinal_num(self, value, rafea=True):
        return self.to_ordinal(value).strip()

    def to_cardinal(self, number, rafea= True):
        self.isCurrencyNameFeminine = False
        number = self.validate_number(number)
        minus = ''
        if number < 0:
            minus = 'سالب '
        # separator in case of decimal is ',' self.separator
        self.separator = ','
        self.currency_subunit = ('', '', '', '')
        self.currency_unit = ('', '', '', '')
        self.arabicPrefixText = ""
        self.arabicSuffixText = ""
        self.arabicOnes = ARABIC_ONES
        return minus + self.convert(value=self.abs(number), rafea=rafea).strip()
# Example Usage:
# num_converter = Num2Word_AR()
# num_converter.rafea = False  # Set to True for رفع (rafea) case
# result_rafea = num_converter.convert(12.345,rafea = False)
# # print(result_rafea)
# num_converter.rafea = False  # Set to False for نصب (nasb) case
# result_nasb = num_converter.convert(value=200000)
# # print(result_nasb)


