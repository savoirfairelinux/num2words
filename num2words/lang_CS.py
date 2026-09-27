# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2026, Martin Ambruš.  All Rights Reserved.

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

from decimal import Decimal

from .base import Num2Word_Base

CASES = ('nominative', 'genitive', 'dative', 'accusative', 'instrumental',
         'locative')
NOM, GEN, DAT, ACC, INS, LOC = range(6)
GENDERS = ('masculine', 'feminine', 'neuter')
ANIMACY = ('inanimate', 'animate', 'personal')
CONSTRUCTIONS = ('genitive', 'agreement', 'inverted')
OBLIQUE_STYLES = ('auto', 'full', 'partial')
ORDINAL_STYLES = ('mixed', 'all')

ZERO = ('nula', 'nuly', 'nule', 'nulu', 'nulou', 'nule')
# the masculine accusative follows animacy
ONE = {
    'masculine': ('jeden', 'jednoho', 'jednomu', None, 'jedním', 'jednom'),
    'feminine': ('jedna', 'jedné', 'jedné', 'jednu', 'jednou', 'jedné'),
    'neuter': ('jedno', 'jednoho', 'jednomu', 'jedno', 'jedním', 'jednom'),
}
TWO_OBLIQUE = {GEN: 'dvou', DAT: 'dvěma', INS: 'dvěma', LOC: 'dvou'}
THREE = ('tři', 'tří', 'třem', 'tři', 'třemi', 'třech')
FOUR = ('čtyři', 'čtyř', 'čtyřem', 'čtyři', 'čtyřmi', 'čtyřech')
# nominative and the other cases
PET = {
    5: ('pět', 'pěti'), 6: ('šest', 'šesti'), 7: ('sedm', 'sedmi'),
    8: ('osm', 'osmi'), 9: ('devět', 'devíti'), 10: ('deset', 'deseti'),
    11: ('jedenáct', 'jedenácti'), 12: ('dvanáct', 'dvanácti'),
    13: ('třináct', 'třinácti'), 14: ('čtrnáct', 'čtrnácti'),
    15: ('patnáct', 'patnácti'), 16: ('šestnáct', 'šestnácti'),
    17: ('sedmnáct', 'sedmnácti'), 18: ('osmnáct', 'osmnácti'),
    19: ('devatenáct', 'devatenácti'), 20: ('dvacet', 'dvaceti'),
    30: ('třicet', 'třiceti'), 40: ('čtyřicet', 'čtyřiceti'),
    50: ('padesát', 'padesáti'), 60: ('šedesát', 'šedesáti'),
    70: ('sedmdesát', 'sedmdesáti'), 80: ('osmdesát', 'osmdesáti'),
    90: ('devadesát', 'devadesáti'),
}
# jedn-a-dvacet, pět-a-dvacet
INVERTED_UNIT = {1: 'jedn', 2: 'dva', 3: 'tři', 4: 'čtyři', 5: 'pět',
                 6: 'šest', 7: 'sedm', 8: 'osm', 9: 'devět'}


def _hundreds(nominative, oblique):
    return ('%s set' % nominative, '%s set' % oblique, '%s stům' % oblique,
            '%s set' % nominative, '%s sty' % oblique, '%s stech' % oblique)


# sto declines as a noun
HUNDREDS = {
    1: ('sto', 'sta', 'stu', 'sto', 'stem', 'stu'),
    2: ('dvě stě', 'dvou set', 'dvěma stům', 'dvě stě', 'dvěma sty',
        'dvou stech'),
    3: ('tři sta', 'tří set', 'třem stům', 'tři sta', 'třemi sty',
        'třech stech'),
    4: ('čtyři sta', 'čtyř set', 'čtyřem stům', 'čtyři sta', 'čtyřmi sty',
        'čtyřech stech'),
}
HUNDREDS.update((h, _hundreds(*PET[h])) for h in range(5, 10))


def _hrad(stem):
    return ((stem, stem + 'u', stem + 'u', stem, stem + 'em', stem + 'u'),
            (stem + 'y', stem + 'ů', stem + 'ům', stem + 'y', stem + 'y',
             stem + 'ech'))


def _zena(stem):
    return ((stem + 'a', stem + 'y', stem + 'ě', stem + 'u', stem + 'ou',
             stem + 'ě'),
            (stem + 'y', stem, stem + 'ám', stem + 'y', stem + 'ami',
             stem + 'ách'))


TISIC = (('tisíc', 'tisíce', 'tisíci', 'tisíc', 'tisícem', 'tisíci'),
         ('tisíce', 'tisíc', 'tisícům', 'tisíce', 'tisíci', 'tisících'))
# exponent, gender, singular and plural forms, ordinal
SCALES = (
    (30, 'masculine') + _hrad('kvintilion') + ('kvintiliontý',),
    (27, 'feminine') + _zena('kvadriliard') + ('kvadriliardtý',),
    (24, 'masculine') + _hrad('kvadrilion') + ('kvadriliontý',),
    (21, 'feminine') + _zena('triliard') + ('triliardtý',),
    (18, 'masculine') + _hrad('trilion') + ('triliontý',),
    (15, 'feminine') + _zena('biliard') + ('biliardtý',),
    (12, 'masculine') + _hrad('bilion') + ('biliontý',),
    (9, 'feminine') + _zena('miliard') + ('miliardtý',),
    (6, 'masculine') + _hrad('milion') + ('miliontý',),
    (3, 'masculine') + TISIC + ('tisící',),
)

ORDINALS = {
    0: 'nultý', 1: 'první', 2: 'druhý', 3: 'třetí', 4: 'čtvrtý', 5: 'pátý',
    6: 'šestý', 7: 'sedmý', 8: 'osmý', 9: 'devátý', 10: 'desátý',
    11: 'jedenáctý', 12: 'dvanáctý', 13: 'třináctý', 14: 'čtrnáctý',
    15: 'patnáctý', 16: 'šestnáctý', 17: 'sedmnáctý', 18: 'osmnáctý',
    19: 'devatenáctý', 20: 'dvacátý', 30: 'třicátý', 40: 'čtyřicátý',
    50: 'padesátý', 60: 'šedesátý', 70: 'sedmdesátý', 80: 'osmdesátý',
    90: 'devadesátý', 100: 'stý', 200: 'dvoustý', 300: 'třístý',
    400: 'čtyřstý', 500: 'pětistý', 600: 'šestistý', 700: 'sedmistý',
    800: 'osmistý', 900: 'devítistý',
}
# dvoutisící, pětitisící, dvacetitisící, stotisící
COMBINING = {
    2: 'dvou', 3: 'tří', 4: 'čtyř', 5: 'pěti', 6: 'šesti', 7: 'sedmi',
    8: 'osmi', 9: 'devíti', 10: 'deseti', 11: 'jedenácti', 12: 'dvanácti',
    13: 'třinácti', 14: 'čtrnácti', 15: 'patnácti', 16: 'šestnácti',
    17: 'sedmnácti', 18: 'osmnácti', 19: 'devatenácti', 20: 'dvaceti',
    30: 'třiceti', 40: 'čtyřiceti', 50: 'padesáti', 60: 'šedesáti',
    70: 'sedmdesáti', 80: 'osmdesáti', 90: 'devadesáti', 100: 'sto',
}

# endings by case; None is the masculine accusative, which follows animacy
HARD = {  # mladý
    'masculine': ('ý', 'ého', 'ému', None, 'ým', 'ém'),
    'feminine': ('á', 'é', 'é', 'ou', 'ou', 'é'),
    'neuter': ('é', 'ého', 'ému', 'é', 'ým', 'ém'),
}
HARD_PLURAL = {
    'masculine': ('é', 'ých', 'ým', 'é', 'ými', 'ých'),
    'feminine': ('é', 'ých', 'ým', 'é', 'ými', 'ých'),
    'neuter': ('á', 'ých', 'ým', 'á', 'ými', 'ých'),
}
SOFT = {  # jarní
    'masculine': ('í', 'ího', 'ímu', None, 'ím', 'ím'),
    'feminine': ('í', 'í', 'í', 'í', 'í', 'í'),
    'neuter': ('í', 'ího', 'ímu', 'í', 'ím', 'ím'),
}
SOFT_PLURAL = ('í', 'ích', 'ím', 'í', 'ími', 'ích')

# 1, 2-4, 5 and up
WHOLE = ('celá', 'celé', 'celých')
DENOMINATORS = {
    1: ('desetina', 'desetiny', 'desetin'),
    2: ('setina', 'setiny', 'setin'),
    3: ('tisícina', 'tisíciny', 'tisícin'),
    4: ('desetitisícina', 'desetitisíciny', 'desetitisícin'),
    5: ('stotisícina', 'stotisíciny', 'stotisícin'),
    6: ('miliontina', 'miliontiny', 'miliontin'),
}


def _check(name, value, allowed):
    if value not in allowed:
        raise ValueError('%s must be one of %s, got %r'
                         % (name, ', '.join(map(repr, allowed)), value))


def _case_index(case, animacy):
    _check('case', case, CASES)
    _check('animacy', animacy, ANIMACY)
    return CASES.index(case)


def _simple(n, c, gender, animacy):
    # 1-20 and round tens
    if n == 1:
        if c == ACC and gender == 'masculine':
            return 'jednoho' if animacy != 'inanimate' else 'jeden'
        return ONE[gender][c]
    if n == 2:
        if c in (NOM, ACC):
            return 'dva' if gender == 'masculine' else 'dvě'
        return TWO_OBLIQUE[c]
    if n == 3:
        return THREE[c]
    if n == 4:
        return FOUR[c]
    nominative, oblique = PET[n]
    return nominative if c in (NOM, ACC) else oblique


def _below_100(n, c, gender, animacy, construction):
    if n <= 20 or n % 10 == 0:
        return _simple(n, c, gender, animacy)
    tens, unit = n - n % 10, n % 10
    oblique = c not in (NOM, ACC)
    if construction == 'inverted' or (unit == 1 and oblique):
        # jednadvacet, pětadvaceti; never "dvaceti jednoho" (review)
        return INVERTED_UNIT[unit] + 'a' + PET[tens][1 if oblique else 0]
    tens_word = PET[tens][1 if oblique else 0]
    if not oblique and construction == 'genitive' and unit in (1, 2):
        # invariable before a genitive plural: dvacet jedna žáků
        return '%s %s' % (tens_word, 'jedna' if unit == 1 else 'dva')
    return '%s %s' % (tens_word, _simple(unit, c, gender, animacy))


def _below_1000(n, c, gender, animacy, construction):
    hundreds, rest = divmod(n, 100)
    words = []
    if hundreds:
        # "sto" followed by another numeral does not decline (IJP)
        sto = hundreds == 1 and rest > 0 and c not in (NOM, ACC)
        words.append(HUNDREDS[hundreds][NOM if sto else c])
    if rest:
        if hundreds and rest == 1 and c not in (NOM, ACC):
            # 101 has no inverted form, so the unit stays invariable
            words.append('jedna')
        elif (hundreds and rest in (1, 2) and c in (NOM, ACC)
              and construction == 'genitive'):
            words.append('jedna' if rest == 1 else 'dva')
        else:
            words.append(_below_100(rest, c, gender, animacy, construction))
    return ' '.join(words)


def _count_noun(count, singular, plural, scale_gender, c, construction):
    # tisíc, milion and miliarda are nouns, so both parts decline
    if count == 1:
        return singular[c]
    if count in (2, 3, 4):
        return '%s %s' % (_simple(count, c, scale_gender, 'inanimate'),
                          plural[c])
    noun = plural[GEN] if c in (NOM, ACC) else plural[c]
    if count == 100:
        # sto declines before tisíc and milion: "bez sta tisíc" (review)
        return '%s %s' % (HUNDREDS[1][c], noun)
    if c in (NOM, ACC) and construction == 'agreement':
        # the noun agrees with the last word: dvacet jeden milion,
        # dvacet dvě miliardy
        last_two = count % 100
        if last_two > 20:
            unit = last_two % 10
        else:
            unit = last_two if last_two < 5 else 0
        if unit in (1, 2, 3, 4):
            number = _below_1000(count, c, scale_gender, 'inanimate',
                                 'agreement')
            return '%s %s' % (number, singular[c] if unit == 1 else plural[c])
    if construction == 'agreement':
        construction = 'genitive'
    number = _below_1000(count, c, scale_gender, 'inanimate', construction)
    return '%s %s' % (number, noun)


def _components(n):
    # (value, scale) pairs: the scale groups, the hundreds and the rest
    components = []
    for exponent, scale_gender, singular, plural, lemma in SCALES:
        count, n = divmod(n, 10 ** exponent)
        if count:
            components.append((count, (singular, plural, scale_gender,
                                       lemma)))
    hundreds, rest = divmod(n, 100)
    if hundreds:
        components.append((hundreds * 100, None))
    if rest:
        components.append((rest, None))
    return components


def _cardinal(n, c=NOM, gender='masculine', animacy='inanimate',
              construction='genitive', oblique_style='auto'):
    if n == 0:
        return ZERO[c]
    components = _components(n)
    if oblique_style == 'auto':
        # IJP: every part declines, or from three parts only the last
        oblique_style = 'partial' if len(components) >= 3 else 'full'
    words = []
    for k, (value, scale) in enumerate(components):
        last = k == len(components) - 1
        if oblique_style == 'full' or last or c in (NOM, ACC):
            part_case = c
        else:
            part_case = NOM
        if scale is not None:
            singular, plural, scale_gender, _ = scale
            words.append(_count_noun(value, singular, plural, scale_gender,
                                     part_case, construction))
        elif value >= 100:
            sto = value == 100 and not last and part_case not in (NOM, ACC)
            words.append(HUNDREDS[value // 100][NOM if sto else part_case])
        elif len(components) > 1 and value == 1:
            # tisíc jedna; the agreement type: tisíc jeden (muž)
            if construction == 'agreement' and part_case in (NOM, ACC):
                words.append(_simple(1, part_case, gender, animacy))
            else:
                words.append('jedna')
        elif (len(components) > 1 and value == 2
              and part_case in (NOM, ACC) and construction == 'genitive'):
            words.append('dva')
        else:
            words.append(_below_100(value, part_case, gender, animacy,
                                    construction))
    return ' '.join(words)


def _combining(count):
    if count in COMBINING:
        return COMBINING[count]
    # pětadvacetitisící
    return INVERTED_UNIT[count % 10] + 'a' + PET[count - count % 10][1]


def _decline_ordinal(lemma, c, gender, animacy, plural):
    stem = lemma[:-1]
    animate = gender == 'masculine' and animacy != 'inanimate'
    soft = lemma.endswith('í')
    if plural:
        if soft:
            return stem + SOFT_PLURAL[c]
        if animate and c == NOM:
            # druzí, pátí, stí; the accusative is -é for all animacy
            if stem.endswith('h'):
                stem = stem[:-1] + 'z'
            return stem + 'í'
        return stem + HARD_PLURAL[gender][c]
    table = SOFT if soft else HARD
    ending = table[gender][c]
    if ending is None:
        ending = table[gender][GEN if animate else NOM]
    return stem + ending


def _ordinal_parts(n, ordinal_style, inverted):
    # the words in order, each with True if it is an ordinal to decline
    components = _components(n)
    parts = []
    for k, (value, scale) in enumerate(components):
        prefix = ordinal_style == 'mixed' and k < len(components) - 1
        if scale is not None:
            singular, plural, scale_gender, lemma = scale
            if prefix:
                parts.append((_count_noun(value, singular, plural,
                                          scale_gender, NOM, 'genitive'),
                              False))
            elif value == 1:
                parts.append((lemma, True))
            elif value <= 100:
                parts.append((_combining(value) + lemma, True))
            else:
                # 345 000th: a cardinal count and an ordinal scale word
                parts.append((_below_1000(value, NOM, scale_gender,
                                          'inanimate', 'genitive'), False))
                parts.append((lemma, True))
        elif value >= 100:
            if prefix:
                parts.append((HUNDREDS[value // 100][NOM], False))
            else:
                parts.append((ORDINALS[value], True))
        elif value in ORDINALS:
            parts.append((ORDINALS[value], True))
        elif inverted:
            # jednadvacátý, pětadvacátý
            parts.append((INVERTED_UNIT[value % 10] + 'a' +
                          ORDINALS[value - value % 10], True))
        else:
            parts.append((ORDINALS[value - value % 10], True))
            parts.append((ORDINALS[value % 10], True))
    return parts


def _ordinal(n, c, gender, animacy, plural, ordinal_style, inverted):
    if n == 0:
        return _decline_ordinal(ORDINALS[0], c, gender, animacy, plural)
    return ' '.join(
        _decline_ordinal(word, c, gender, animacy, plural) if ordinal
        else word
        for word, ordinal in _ordinal_parts(n, ordinal_style, inverted))


def _counted(n, forms, agreement):
    # "celá" agrees with the last word (dvacet jedna celá); a fraction
    # takes the genitive plural after compounds (dvacet dva setin)
    if n == 0:
        return 'nula %s' % forms[0]
    last = n % 100 if n % 100 < 20 else n % 10
    number = _cardinal(n, gender='feminine',
                       construction='agreement' if agreement else 'genitive')
    if last == 1 and (n == 1 or agreement):
        return '%s %s' % (number, forms[0])
    if last in (2, 3, 4) and (n < 5 or agreement):
        return '%s %s' % (number, forms[1])
    return '%s %s' % (number, forms[2])


def _decimal(value):
    # nominative only: "dvě celé pět desetin"; longer fractions are read
    # digit by digit
    whole, fraction = format(value, 'f').split('.')
    fraction = fraction.rstrip('0')
    words = _counted(int(whole), WHOLE, True)
    if len(fraction) > len(DENOMINATORS):
        return '%s %s' % (words, ' '.join(
            _cardinal(int(digit), gender='feminine') for digit in fraction))
    return '%s %s' % (words, _counted(int(fraction),
                                      DENOMINATORS[len(fraction)], False))


def _currency_form(n):
    if n == 1:
        return 0
    if 1 < n % 10 < 5 and (n % 100 < 10 or n % 100 > 20):
        return 1
    return 2


class Num2Word_CS(Num2Word_Base):
    CURRENCY_FORMS = {
        'CZK': (
            ('koruna', 'koruny', 'korun'), ('haléř', 'haléře', 'haléřů')
        ),
        'EUR': (
            ('euro', 'eura', 'eur'), ('cent', 'centy', 'centů')
        ),
    }
    CURRENCY_GENDERS = {
        'CZK': ('feminine', 'masculine'),
        'EUR': ('neuter', 'masculine'),
    }
    MAXVAL = 10 ** 33

    def setup(self):
        self.negword = 'mínus'

    def str_to_number(self, value):
        return Decimal(value.replace(',', '.'))

    def to_cardinal(self, number, gender=None, case='nominative',
                    animacy='inanimate', construction='genitive',
                    oblique_style='auto'):
        """
        gender: None (counting: "jedna, dva, tři"), 'masculine',
            'feminine' or 'neuter'
        case: 'nominative', 'genitive', 'dative', 'accusative',
            'instrumental' or 'locative'
        animacy: 'inanimate', 'animate' or 'personal'
        construction: 'genitive' ("dvacet jedna žáků"), 'agreement'
            ("dvacet jeden žák") or 'inverted' ("jednadvacet žáků")
        oblique_style: 'full' declines every part ("tisíce osmi set
            čtyřiceti sedmi"), 'partial' only the last ("tisíc osm set
            čtyřiceti sedmi"); 'auto' is 'full' for numbers of up to
            two parts and 'partial' from three
        A number with a fraction is read in the nominative:
        "dvě celé pět desetin".
        """
        _check('gender', gender, (None,) + GENDERS)
        c = _case_index(case, animacy)
        _check('construction', construction, CONSTRUCTIONS)
        _check('oblique_style', oblique_style, OBLIQUE_STYLES)
        value = Decimal(str(number))
        if value.is_nan():
            raise ValueError('%s is not a number' % number)
        if value.copy_abs() >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))
        sign = '%s ' % self.negword if value < 0 else ''
        value = value.copy_abs()
        if value != value.to_integral_value():
            return sign + _decimal(value)
        n = int(value)
        if gender is None:
            gender = 'feminine' if n == 1 else 'masculine'
        return sign + _cardinal(n, c, gender, animacy, construction,
                                oblique_style)

    def to_ordinal(self, number, gender='masculine', case='nominative',
                   animacy='inanimate', plural=False, ordinal_style='mixed',
                   inverted=False):
        """
        gender, case, animacy: as for to_cardinal
        plural: plural forms ("druzí", "druhých")
        ordinal_style: 'mixed' keeps the leading parts cardinal ("tisíc
            devět set devadesátý první"), 'all' makes every part ordinal
            ("tisící devítistý devadesátý první")
        inverted: "jednadvacátý" instead of "dvacátý první"
        """
        _check('gender', gender, GENDERS)
        c = _case_index(case, animacy)
        _check('ordinal_style', ordinal_style, ORDINAL_STYLES)
        self.verify_ordinal(number)
        if number >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))
        return _ordinal(int(number), c, gender, animacy, plural,
                        ordinal_style, inverted)

    def to_ordinal_num(self, number):
        self.verify_ordinal(number)
        return '%d.' % number

    def pluralize(self, n, forms):
        return forms[_currency_form(n)]

    def _money_verbose(self, number, currency):
        return self._currency_cardinal(number,
                                       self.CURRENCY_GENDERS[currency][0])

    def _cents_verbose(self, number, currency):
        return self._currency_cardinal(number,
                                       self.CURRENCY_GENDERS[currency][1])

    def _currency_cardinal(self, number, gender):
        # "koruny" after 22 needs the agreeing "dvacet dvě"
        if _currency_form(number) == 1:
            return self.to_cardinal(number, gender=gender,
                                    construction='agreement')
        return self.to_cardinal(number, gender=gender)
