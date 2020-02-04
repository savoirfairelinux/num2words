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

from . import lang_ID


class Num2Word_MS(lang_ID.Num2Word_ID):
    BASE = {0: [],
            1: ["satu"],
            2: ["dua"],
            3: ["tiga"],
            4: ["empat"],
            5: ["lima"],
            6: ["enam"],
            7: ["tujuh"],
            8: ["lapan"],
            9: ["sembilan"]}

    TENS_TO = {3: "ribu",
               6: "juta",
               9: "bilion",
               12: "trilion",
               15: "kuadrilion",
               18: "kuantilion",
               21: "sekstilion",
               24: "septilion",
               27: "oktilion",
               30: "nonilion",
               33: "desilion"}

    ZERO = "kosong"
    DECIMAL_SEPARATOR = "perpuluhan"
    CURRENCY = "ringgit"
    MINUS_SIGN = "negatif"
