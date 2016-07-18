# -*- encoding: utf-8 -*-
# The PHP License, version 3.01
# Copyright (c) 1999 - 2010 The PHP Group. All rights reserved.
#
# This source file is subject to version 3.01 of the PHP license,
# that is available at http://www.php.net/license/3_01.txt
# If you did not receive a copy of the PHP license and are unable to
# obtain it through the world-wide-web, please send a note to
# license@php.net so we can mail you a copy immediately.
#
# This code is a direct port to Python of the PHP code of the
# Number_Words package that can be found on pear at the URL :
# http://pear.php.net/package/Numbers_Words
#

from __future__ import unicode_literals
from .lang_EU import Num2Word_EU

import re
import math

class Num2Word_IT(object):
    def __init__(self):
        self._minus = "meno "

        self._exponent = {
            0 : ('',''),
            3 : ('mille','mila'),
            6 : ('milione','miloni'),
            12 : ('miliardo','miliardi'),
            18 : ('trillone','trilloni'),
            24 : ('quadrilione','quadrilioni')}

        self._digits = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']

        self._sep = ''

    def _toWords(self, num, power=0):
        str_num = str(num)
        # The return string;
        ret = ''

        # add a the word for the minus sign if necessary
        if num < 0:
            ret = self._sep + self._minus

        if len(str_num) > 6:
            current_power = 6
            # check for highest power
            if self._exponent.has_key(power):
                # convert the number above the first 6 digits
                # with it's corresponding $power.
                snum = str_num[0:-6]
                if snum != '':
                    ret = ret + self._toWords(int(snum), power + 6)

            num = int(str_num[-6:])
            if num == 0:
                return ret

        elif num == 0 or str_num == '':
            return ' ' + self._digits[0] + ' '
        else:
            current_power = len(str_num)

        # See if we need "thousands"
        thousands = math.floor(num / 1000)
        if thousands == 1:
            ret = ret + self._sep + 'mille' + self._sep
        elif thousands > 1:
            ret = ret + self._toWords(int(thousands), 3) + self._sep

        # values for digits, tens and hundreds
        h = int(math.floor((num / 100) % 10))
        t = int(math.floor((num / 10) % 10))
        d = int(math.floor(num % 10))

        # centinaia: duecento, trecento, etc...
        if h == 1:
            if ((d==0) and (t == 0)):# is it's '100' use 'cien'
                ret = ret + self._sep + 'cento'
            else:
                ret = ret + self._sep + 'cento'
        elif h == 2 or h == 3 or h == 4 or h == 6 or h == 8:
            ret = ret + self._sep + self._digits[h] + 'cento'
        elif h == 5:
            ret = ret + self._sep + 'cinquecento'
        elif h == 7:
            ret = ret + self._sep + 'settecento'
        elif h == 9:
            ret = ret + self._sep + 'novecento'

        # decine: venti trenta, etc...
        if t == 9:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'novant'
            else:
                ret = ret + self._sep + 'novanta'
        if t == 8:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'ottant'
            else:
                ret = ret + self._sep + 'ottanta'
        if t == 7:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'settant'
            else:
                ret = ret + self._sep + 'settanta'
        if t == 6:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'sessant'
            else:
                ret = ret + self._sep + 'sessanta'
        if t == 5:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'cinquant'
            else:
                ret = ret + self._sep + 'cinquanta'
        if t == 4:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'quarant'
            else:
                ret = ret + self._sep + 'quaranta'
        if t == 3:
            if d == 1 or d == 8:
                ret = ret + self._sep + 'trent'
            else:
                ret = ret + self._sep + 'trenta'
        if t == 2:
            if d == 0:
                ret = ret + self._sep + 'venti'
            elif (d == 1 or d == 8):
                ret = ret + self._sep + 'vent' + self._digits[d]
            else:
                ret = ret + self._sep + 'venti' + self._digits[d]
        if t == 1:
            if d == 0:
                ret = ret + self._sep + 'dieci'
            elif d == 1:
                ret = ret + self._sep + 'undici'
            elif d == 2:
                ret = ret + self._sep + 'dodici'
            elif d == 3:
                ret = ret + self._sep + 'tredici'
            elif d == 4:
                ret = ret + self._sep + 'quattordici'
            elif d == 5:
                ret = ret + self._sep + 'quindici'
            elif d == 6:
                ret = ret + self._sep + 'sedici'
            elif d == 7:
                ret = ret + self._sep + 'diciassette'
            elif d == 8:
                ret = ret + self._sep + 'diciotto'
            elif d == 9:
                ret = ret + self._sep + 'diciannove'

        # add digits only if it is a multiple of 10 and not 1x or 2x
        if t != 1 and t != 2 and d > 0:
            # don't add 'e' for numbers below 10
            if t != 0:
                # use 'un' instead of 'uno' when there is a suffix ('mila', 'milloni', etc...)
                if (power > 0) and ( d == 1):
                    ret = ret + self._sep + 'e un'
                else:
                    ret = ret + self._sep + '' + self._digits[d]
            else:
                if power > 0 and d == 1:
                    ret = ret + self._sep + 'un '
                else:
                    ret = ret + self._sep + self._digits[d]

        if power > 0:
            if self._exponent.has_key(power):
                lev = self._exponent[power]

            if lev is None:
                return None

            # if it's only one use the singular suffix
            if d == 1 and t == 0 and h == 0:
                suffix = lev[0]
            else:
                suffix = lev[1]

            if num != 0:
                ret = ret + self._sep + suffix

        return ret


    def to_cardinal(self, number):
        return self._toWords(number)

    def to_ordinal_num(self, number):
        pass

    def to_ordinal(self,value):
        raise NotImplementedError()

n2w = Num2Word_IT()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num
