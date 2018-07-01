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
import re
from decimal import Decimal, getcontext
from math import floor

# class CurrencyInfo:
#
#     def __init__(self):
#         self.isCurrencyNameFeminine = False
#         self.arabic1CurrencyName = "ريال"
#         self.arabic2CurrencyName = "ريالان"
#         self.arabic310CurrencyName = "ريالات"
#         self.arabic1199CurrencyName = "ريالاً"
#         self.arabic1CurrencyPartName = "هللة"
#         self.arabic2CurrencyPartName = "هللتان"
#         self.arabic310CurrencyPartName = "هللات"
#         self.arabic1199CurrencyPartName = "هللة"
#         self.partPrecision = 2
#
#         self.isCurrencyPartNameFeminine = True

CURRENCY_UNIT = ("ريال", "ريالان", "ريالات", "ريالاً")
CURRENCY_SUBUNIT = ("هللة", "هللتان", "هللات", "هللة")

ARABIC_ONES = [
    "", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة",
    "عشرة", "أحد عشر", "اثنا عشر", "ثلاثة عشر", "أربعة عشر", "خمسة عشر", "ستة عشر", "سبعة عشر", "ثمانية عشر",
    "تسعة عشر"
]


class Num2Word_AR(object):
    errmsg_toobig = "Too large"
    max_num = 10 ** 36

    def __init__(self):
        self.number = 0
        self.arabicPrefixText = ""
        self.arabicSuffixText = ""
        self._intergerValue = 0
        self._decimalValue = Decimal(0)
        self.partPrecision = 2
        self.currency_unit = CURRENCY_UNIT
        self.currency_subunit = CURRENCY_SUBUNIT
        self.isCurrencyPartNameFeminine = True
        self.isCurrencyNameFeminine = False
        self.spreated = 'و'

        self.arabicOnes = ARABIC_ONES
        self.arabicFeminineOnes = [
            "", "إحدى", "اثنتان", "ثلاث", "أربع", "خمس", "ست", "سبع", "ثمان", "تسع",
            "عشر", "إحدى عشرة", "اثنتا عشرة", "ثلاث عشرة", "أربع عشرة", "خمس عشرة", "ست عشرة", "سبع عشرة", "ثماني عشرة",
            "تسع عشرة"
        ]
        self.arabicTens = [
            "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون", "تسعون"
        ]
        self.arabicHundreds = [
            "", "مائة", "مئتان", "ثلاثمائة", "أربعمائة", "خمسمائة", "ستمائة", "سبعمائة", "ثمانمائة", "تسعمائة"
        ]
        self.arabicAppendedTwos = [
            "مئتا", "ألفا", "مليونا", "مليارا", "تريليونا", "كوادريليونا", "كوينتليونا", "سكستيليونا"
        ]
        self.arabicTwos = [
            "مئتان", "ألفان", "مليونان", "ملياران", "تريليونان", "كوادريليونان", "كوينتليونان", "سكستيليونان"
        ]
        self.arabicGroup = [
            "مائة", "ألف", "مليون", "مليار", "تريليون", "كوادريليون", "كوينتليون", "سكستيليون"
        ]
        self.arabicAppendedGroup = [
            "", "ألفاً", "مليوناً", "ملياراً", "تريليوناً", "كوادريليوناً", "كوينتليوناً", "سكستيليوناً"
        ]
        self.arabicPluralGroups = [
            "", "آلاف", "ملايين", "مليارات", "تريليونات", "كوادريليونات", "كوينتليونات", "سكستيليونات"
        ]

    def number_to_arabic(self, arabic_prefix_text, arabic_suffix_text):
        self.arabicPrefixText = arabic_prefix_text
        self.arabicSuffixText = arabic_suffix_text
        self.extractIntegerAndDecimalParts()

    def extractIntegerAndDecimalParts(self):
        re.split('\\.', str(self.number))
        splits = re.split('\\.', str(self.number))

        self._intergerValue = int(splits[0])

        if len(splits) > 1:
            self._decimalValue = int(self.getDecimalValue(splits[1]))
        else:
            self._decimalValue = 0

    def getDecimalValue(self, decimalPart):

        if self.partPrecision is not len(decimalPart):
            decimalPartLength = len(decimalPart)

            decimalPartBuilder = decimalPart
            for i in range(0, self.partPrecision - decimalPartLength):
                decimalPartBuilder += '0'
            decimalPart = decimalPartBuilder

            if len(decimalPart) <= self.partPrecision:
                dec = len(decimalPart)
            else:
                dec = self.partPrecision
            result = decimalPart[0: dec]
        else:
            result = decimalPart

        for i in range(len(result), self.partPrecision):
            result += '0'
        return result

    def getDigitFeminineStatus(self, digit, groupLevel):
        if groupLevel == -1:
            if self.isCurrencyPartNameFeminine:
                return self.arabicFeminineOnes[digit]
            else:
                return self.arabicOnes[digit]
        elif groupLevel == 0:
            if self.isCurrencyNameFeminine:
                return self.arabicFeminineOnes[digit]
            else:
                return self.arabicOnes[digit]

        else:
            return self.arabicOnes[digit]

    def processArabicGroup(self, groupNumber, groupLevel, remainingNumber):
        tens = groupNumber % 100
        hundreds = groupNumber / 100
        retVal = ""

        if hundreds > 0:
            if tens == 0 and hundreds == 2:
                retVal = "{}".format(self.arabicAppendedTwos[0])
            else:
                retVal = "{}".format(self.arabicHundreds[int(hundreds)])

        if tens > 0:
            if tens < 20:
                if tens == 2 and hundreds == 0 and groupLevel > 0:
                    if self._intergerValue in [2000, 2000000, 2000000000, 2000000000000, 2000000000000000,
                                               2000000000000000000]:
                        retVal = "{}".format(self.arabicAppendedTwos[groupLevel])
                    else:
                        retVal = "{}".format(self.arabicTwos[groupLevel])
                else:
                    if retVal is not "":
                        retVal += " و "

                    if tens == 1 and groupLevel > 0 and hundreds == 0:
                        retVal += " "
                    elif (tens == 1 or tens == 2) and (
                            groupLevel == 0 or groupLevel == -1) and hundreds == 0 and remainingNumber == 0:
                        retVal += ""
                    else:
                        retVal += self.getDigitFeminineStatus(int(tens), groupLevel)
            else:
                ones = tens % 10
                tens = (tens / 10) - 2

                if ones > 0:
                    if retVal is not "":
                        retVal += " و "

                    retVal += self.getDigitFeminineStatus(ones, groupLevel)
                if retVal is not "":
                    retVal += " و "

                retVal += self.arabicTens[int(tens)]

        return retVal

    def convert(self, value):
        getcontext().prec = self.partPrecision
        self.number = Decimal(value)
        self.number_to_arabic(self.arabicPrefixText, self.arabicSuffixText)

        return self.convertToArabic()

    def convertToArabic(self):
        tempNumber = self.number

        if tempNumber == Decimal(0):
            return "صفر"

        decimalString = self.processArabicGroup(self._decimalValue, -1, Decimal(0))
        retVal = ""
        group = 0
        while tempNumber > Decimal(0):

            numberToProcess = int(int(tempNumber) % 1000)

            tempNumber = int(tempNumber / 1000)
            groupDescription = self.processArabicGroup(numberToProcess, group, Decimal(floor(tempNumber)))
            if groupDescription is not '':
                if group > 0:
                    if retVal is not "":
                        retVal = "{} {}".format("و", retVal)
                    if numberToProcess != 2:
                        if numberToProcess % 100 != 1:
                            if 3 <= numberToProcess <= 10:
                                retVal = "{} {}".format(self.arabicPluralGroups[group], retVal)
                            else:
                                if retVal is not "":
                                    retVal = "{} {}".format(self.arabicAppendedGroup[group], retVal)
                                else:
                                    retVal = "{} {}".format(self.arabicGroup[group], retVal)

                        else:
                            retVal = "{} {}".format(self.arabicGroup[group], retVal)
                retVal = "{} {}".format(groupDescription, retVal)
            group += 1
        formattedNumber = ""
        if self.arabicPrefixText is not "":
            formattedNumber += self.arabicPrefixText
        formattedNumber += retVal
        if self._intergerValue != 0:
            remaining100 = int(self._intergerValue % 100)

            if remaining100 == 0:
                formattedNumber += self.currency_unit[0]
            elif remaining100 == 1:
                formattedNumber += self.currency_unit[0]
            elif remaining100 == 2:
                if self._intergerValue == 2:
                    formattedNumber += self.currency_unit[1]
                else:
                    formattedNumber += self.currency_unit[0]
            elif 3 <= remaining100 <= 10:
                formattedNumber += self.currency_unit[2]
            elif 11 <= remaining100 <= 99:
                formattedNumber += self.currency_unit[3]
        if self._decimalValue != 0:
            formattedNumber += " {} ".format(self.spreated)
            formattedNumber += decimalString

        if self._decimalValue != 0:
            formattedNumber += " "
            remaining100 = self._decimalValue % 100

            if remaining100 == 0:
                formattedNumber += self.currency_subunit[0]
            elif remaining100 == 1:
                formattedNumber += self.currency_subunit[0]
            elif remaining100 == 2:
                formattedNumber += self.currency_subunit[1]
            elif 3 <= remaining100 <= 10:
                formattedNumber += self.currency_subunit[2]
            elif 11 <= remaining100 <= 99:
                formattedNumber += self.currency_subunit[3]

        if self.arabicSuffixText is not "":
            formattedNumber += self.arabicSuffixText

        return formattedNumber

    def to_currency(self, value):
        self.spreated = "و"
        self.currency_subunit = CURRENCY_SUBUNIT
        self.currency_unit = CURRENCY_UNIT
        self.arabicOnes = ARABIC_ONES
        return self.convert(value=value)

    # TODO: fix this
    def to_ordinal(self, number):
        self.arabicOnes = [
            "", "اول", "ثاني", "ثالث", "رابع", "خامس", "سادس", "سابع", "ثامن", "تاسع",
            "عاشر", "حادي عشر", "ثاني عشر", "ثالث عشر", "رابع عشر", "خامس عشر", "سادس عشر", "سابع هشر",
            "ثامن عشر",
            "تاسع عشر"
        ]
        self.currency_subunit = ('', '', '', '')
        self.currency_unit = ('', '', '', '')
        return "ال{}".format(self.convert(abs(number)))

    # TODO: fix this
    def to_year(self, value):
        return self.to_cardinal(value)

    # TODO: fix this
    def to_ordinal_num(self, value):
        return self.to_cardinal(value)

    def to_cardinal(self, number):
        if number >= self.max_num:
            raise OverflowError(self.errmsg_toobig % (number, self.max_num))
        minus = ''
        if number < 0:
            minus = 'سالب '
        self.spreated = ','
        self.currency_subunit = ('', '', '', '')
        self.currency_unit = ('', '', '', '')
        self.arabicOnes = ARABIC_ONES
        return minus + self.convert(value=abs(number))

