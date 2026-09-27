# -*- coding: utf-8 -*-
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
CONSTRUCTIONS = ('genitive', 'agreement')

ZERO = ('nula', 'nuly', 'nule', 'nulu', 'nulou', 'nule')
# the masculine accusative follows animacy
ONE = {
    'masculine': ('jeden', 'jedného', 'jednému', None, 'jedným', 'jednom'),
    'feminine': ('jedna', 'jednej', 'jednej', 'jednu', 'jednou', 'jednej'),
    'neuter': ('jedno', 'jedného', 'jednému', 'jedno', 'jedným', 'jednom'),
}
# nominative, masculine personal nominative, genitive, dative,
# instrumental, locative
SMALL = {
    2: ('dva', 'dvaja', 'dvoch', 'dvom', 'dvoma', 'dvoch'),
    3: ('tri', 'traja', 'troch', 'trom', 'troma', 'troch'),
    4: ('štyri', 'štyria', 'štyroch', 'štyrom', 'štyrmi', 'štyroch'),
}
# nominative and the stem of the other cases
PAT = {
    5: ('päť', 'piat'), 6: ('šesť', 'šiest'), 7: ('sedem', 'siedm'),
    8: ('osem', 'ôsm'), 9: ('deväť', 'deviat'), 10: ('desať', 'desiat'),
    11: ('jedenásť', 'jedenást'), 12: ('dvanásť', 'dvanást'),
    13: ('trinásť', 'trinást'), 14: ('štrnásť', 'štrnást'),
    15: ('pätnásť', 'pätnást'), 16: ('šestnásť', 'šestnást'),
    17: ('sedemnásť', 'sedemnást'), 18: ('osemnásť', 'osemnást'),
    19: ('devätnásť', 'devätnást'), 20: ('dvadsať', 'dvadsiat'),
    30: ('tridsať', 'tridsiat'), 40: ('štyridsať', 'štyridsiat'),
    50: ('päťdesiat', 'päťdesiat'), 60: ('šesťdesiat', 'šesťdesiat'),
    70: ('sedemdesiat', 'sedemdesiat'), 80: ('osemdesiat', 'osemdesiat'),
    90: ('deväťdesiat', 'deväťdesiat'),
}
PAT_ENDINGS = {GEN: 'ich', DAT: 'im', INS: 'imi', LOC: 'ich'}
HUNDREDS = {
    1: 'sto', 2: 'dvesto', 3: 'tristo', 4: 'štyristo', 5: 'päťsto',
    6: 'šesťsto', 7: 'sedemsto', 8: 'osemsto', 9: 'deväťsto',
}


def _masculine_noun(stem):
    return ((stem, stem + 'a', stem + 'u', stem, stem + 'om', stem + 'e'),
            (stem + 'y', stem + 'ov', stem + 'om', stem + 'y', stem + 'mi',
             stem + 'och'))


def _feminine_noun(stem, genitive_plural):
    return ((stem + 'a', stem + 'y', stem + 'e', stem + 'u', stem + 'ou',
             stem + 'e'),
            (stem + 'y', genitive_plural, stem + 'ám', stem + 'y',
             stem + 'ami', stem + 'ách'))


# exponent, gender, singular and plural forms
SCALES = (
    (30, 'masculine') + _masculine_noun('kvintilión'),
    (27, 'feminine') + _feminine_noun('kvadriliard', 'kvadriliárd'),
    (24, 'masculine') + _masculine_noun('kvadrilión'),
    (21, 'feminine') + _feminine_noun('triliard', 'triliárd'),
    (18, 'masculine') + _masculine_noun('trilión'),
    (15, 'feminine') + _feminine_noun('biliard', 'biliárd'),
    (12, 'masculine') + _masculine_noun('bilión'),
    (9, 'feminine') + _feminine_noun('miliard', 'miliárd'),
    (6, 'masculine') + _masculine_noun('milión'),
)

ORDINALS = {
    0: 'nultý', 1: 'prvý', 2: 'druhý', 3: 'tretí', 4: 'štvrtý', 5: 'piaty',
    6: 'šiesty', 7: 'siedmy', 8: 'ôsmy', 9: 'deviaty', 10: 'desiaty',
    11: 'jedenásty', 12: 'dvanásty', 13: 'trinásty', 14: 'štrnásty',
    15: 'pätnásty', 16: 'šestnásty', 17: 'sedemnásty', 18: 'osemnásty',
    19: 'devätnásty', 20: 'dvadsiaty', 30: 'tridsiaty', 40: 'štyridsiaty',
    50: 'päťdesiaty', 60: 'šesťdesiaty', 70: 'sedemdesiaty',
    80: 'osemdesiaty', 90: 'deväťdesiaty', 100: 'stý', 200: 'dvojstý',
    300: 'trojstý', 400: 'štvorstý', 500: 'päťstý', 600: 'šesťstý',
    700: 'sedemstý', 800: 'osemstý', 900: 'deväťstý',
}
MULTIPLIER = {2: 'dvoj', 3: 'troj', 4: 'štvor'}
# dvestý and dvetisíci are more frequent than the codified dvojstý and
# dvojtisíci; *tritisíci and *štyritisíci are unattested
UNCODIFIED = {2: 'dve', 3: 'troj', 4: 'štvor'}

# endings by case; None is the masculine accusative, which follows animacy
HARD_LONG = {  # prvý, druhý, stý
    'masculine': ('ý', 'ého', 'ému', None, 'ým', 'om'),
    'feminine': ('á', 'ej', 'ej', 'ú', 'ou', 'ej'),
    'neuter': ('é', 'ého', 'ému', 'é', 'ým', 'om'),
    'plural': ('é', 'ých', 'ým', 'é', 'ými', 'ých'),
    'personal': ('í', 'ých', 'ým', 'ých', 'ými', 'ých'),
}
HARD_SHORT = {  # rhythmic law after a long syllable: piaty, miliónty
    'masculine': ('y', 'eho', 'emu', None, 'ym', 'om'),
    'feminine': ('a', 'ej', 'ej', 'u', 'ou', 'ej'),
    'neuter': ('e', 'eho', 'emu', 'e', 'ym', 'om'),
    'plural': ('e', 'ych', 'ym', 'e', 'ymi', 'ych'),
    'personal': ('i', 'ych', 'ym', 'ych', 'ymi', 'ych'),
}
SOFT_LONG = {  # tretí
    'masculine': ('í', 'ieho', 'iemu', None, 'ím', 'om'),
    'feminine': ('ia', 'ej', 'ej', 'iu', 'ou', 'ej'),
    'neuter': ('ie', 'ieho', 'iemu', 'ie', 'ím', 'om'),
    'plural': ('ie', 'ích', 'ím', 'ie', 'ími', 'ích'),
    'personal': ('í', 'ích', 'ím', 'ích', 'ími', 'ích'),
}
SOFT_SHORT = {  # rhythmic law: tisíci, tisíca, tisíce
    'masculine': ('i', 'eho', 'emu', None, 'im', 'om'),
    'feminine': ('a', 'ej', 'ej', 'u', 'ou', 'ej'),
    'neuter': ('e', 'eho', 'emu', 'e', 'im', 'om'),
    'plural': ('e', 'ich', 'im', 'e', 'imi', 'ich'),
    'personal': ('i', 'ich', 'im', 'ich', 'imi', 'ich'),
}
ENDINGS = {'ý': HARD_LONG, 'y': HARD_SHORT, 'í': SOFT_LONG, 'i': SOFT_SHORT}
SOFTEN = {'t': 'ť', 'd': 'ď', 'n': 'ň', 'l': 'ľ'}  # treťom, treťou

# 1, 2-4, 5 and up
WHOLE = ('celá', 'celé', 'celých')
DENOMINATORS = {
    1: ('desatina', 'desatiny', 'desatín'),
    2: ('stotina', 'stotiny', 'stotín'),
    3: ('tisícina', 'tisíciny', 'tisícin'),
    4: ('desaťtisícina', 'desaťtisíciny', 'desaťtisícin'),
    5: ('stotisícina', 'stotisíciny', 'stotisícin'),
    6: ('milióntina', 'milióntiny', 'milióntin'),
}


def _check(name, value, allowed):
    if value not in allowed:
        raise ValueError('%s must be one of %s, got %r'
                         % (name, ', '.join(map(repr, allowed)), value))


def _case_index(gender, case, animacy):
    _check('gender', gender, GENDERS)
    _check('case', case, CASES)
    _check('animacy', animacy, ANIMACY)
    return CASES.index(case)


def _simple(n, c, gender, animacy, construction, compound):
    # 1-20 and round tens; in a compound, 1 is "jeden" for every gender
    personal = gender == 'masculine' and animacy == 'personal'
    if n == 1:
        if compound:
            return 'jeden'
        if c == ACC and gender == 'masculine':
            return 'jedného' if animacy != 'inanimate' else 'jeden'
        return ONE[gender][c]
    if n in SMALL:
        nom, pers, gen, dat, ins, loc = SMALL[n]
        if c in (NOM, ACC):
            if personal and (not compound or construction == 'agreement'):
                return pers if c == NOM else gen
            if n == 2 and gender != 'masculine':
                # also after sto-/tisíc-: "stodve knihy" (native review)
                return 'dve'
            return nom
        if c == INS and gender == 'feminine' and n in (2, 3):
            # dvomi stenami, but dvoma stromami (native review)
            return 'dvomi' if n == 2 else 'tromi'
        return {GEN: gen, DAT: dat, INS: ins, LOC: loc}[c]
    nom, stem = PAT[n]
    if c in (NOM, ACC):
        if personal and construction == 'agreement':
            return stem + ('i' if c == NOM else 'ich')
        return nom
    return stem + PAT_ENDINGS[c]


def _below_100(n, c, gender, animacy, construction, declined, compound):
    # (head, tail): the head joins a sto-/tisíc- prefix, the tail is a
    # separate word, as PSP 1991 writes declined units apart
    if n <= 20 or n % 10 == 0:
        if compound and not declined and c not in (NOM, ACC):
            return _simple(n, NOM, gender, 'inanimate', 'genitive',
                           True), ''
        return _simple(n, c, gender, animacy, construction, compound), ''
    tens, unit = n - n % 10, n % 10
    if unit == 1:
        # -jeden compounds never decline and never change gender
        return PAT[tens][0] + 'jeden', ''
    personal = gender == 'masculine' and animacy == 'personal'
    oblique = c not in (NOM, ACC)
    congruent = personal and construction == 'agreement'
    if (oblique and declined) or (congruent and not oblique):
        return (_simple(tens, c, gender, animacy, construction, True),
                _simple(unit, c, gender, animacy, construction, True))
    return PAT[tens][0] + _simple(unit, NOM, 'masculine', 'inanimate',
                                  'genitive', True), ''


def _below_1000(n, c, gender, animacy, construction, declined, prefix='',
                in_compound=False):
    # in_compound: the number follows a milión group (milión päť)
    hundreds, rest = divmod(n, 100)
    prefix = prefix + (HUNDREDS[hundreds] if hundreds else '')
    if rest == 0:
        # sto, dvesto ... and -tisíc compounds are invariable
        return prefix
    compound = bool(prefix) or in_compound
    head, tail = _below_100(rest, c, gender, animacy, construction,
                            declined, compound)
    personal = gender == 'masculine' and animacy == 'personal'
    declined_unit = c not in (NOM, ACC) and declined
    congruent = personal and construction == 'agreement'
    if prefix and 1 < rest < 10 and (declined_unit or congruent):
        # written apart: "sto piatich", "sto dvaja"
        return '%s %s' % (prefix, head)
    word = prefix + head
    return '%s %s' % (word, tail) if tail else word


def _thousands_prefix(thousands):
    # invariable: tisíc, dvetisíc, päťtisíc, dvadsaťjedentisíc, stotisíc
    if thousands == 1:
        return 'tisíc'
    if thousands == 2:
        return 'dvetisíc'
    return _below_1000(thousands, NOM, 'masculine', 'inanimate', 'genitive',
                       False) + 'tisíc'


def _scale_group(count, singular, plural, scale_gender, c, declined):
    # milión and miliarda are nouns, so both parts decline
    if count == 1:
        return singular[c]
    number = _below_1000(count, c, scale_gender, 'inanimate', 'genitive',
                         declined)
    if c in (NOM, ACC) and count % 100 not in (2, 3, 4):
        # päť miliónov, dvadsaťdva miliónov; but stodva milióny, like
        # "stodve knihy" (native review)
        return '%s %s' % (number, plural[GEN])
    return '%s %s' % (number, plural[c])


def _cardinal(n, c=NOM, gender='masculine', animacy='inanimate',
              construction='genitive', declined=True):
    if n == 0:
        return ZERO[c]
    groups = []
    for exponent, scale_gender, singular, plural in SCALES:
        count, n = divmod(n, 10 ** exponent)
        if count:
            groups.append(_scale_group(count, singular, plural, scale_gender,
                                       c, declined))
    if n:
        thousands, rest = divmod(n, 1000)
        prefix = _thousands_prefix(thousands) if thousands else ''
        if rest:
            groups.append(_below_1000(rest, c, gender, animacy, construction,
                                      declined, prefix, bool(groups)))
        else:
            groups.append(prefix)
    return ' '.join(groups)


def _decline_ordinal(lemma, c, gender, animacy, plural):
    table = ENDINGS[lemma[-1]]
    stem = lemma[:-1]
    if plural:
        personal = gender == 'masculine' and animacy == 'personal'
        ending = table['personal' if personal else 'plural'][c]
    else:
        ending = table[gender][c]
        if ending is None:
            ending = table[gender][GEN if animacy != 'inanimate' else NOM]
    if table is SOFT_LONG and ending.startswith('o') and stem[-1] in SOFTEN:
        stem = stem[:-1] + SOFTEN[stem[-1]]
    return stem + ending


def _ordinal_lemmas(n, codified):
    # (cardinal prefix, ordinal lemmas); the prefix is glued to the first
    multiplier = MULTIPLIER if codified else UNCODIFIED
    parts = []
    for exponent, scale_gender, singular, plural in SCALES:
        count, n = divmod(n, 10 ** exponent)
        if count and n == 0:
            # the scale noun is the ordinal: miliónty, dvojmiliardtý
            base = singular[NOM]
            if scale_gender == 'feminine':
                base = base[:-1]
            lemma = base + ('tý' if base.endswith('d') else 'ty')
            if count == 1:
                pre = ''
            elif count in multiplier:
                pre = multiplier[count]
            else:
                pre = _below_1000(count, NOM, 'masculine', 'inanimate',
                                  'genitive', False)
            lead = ' '.join(parts) + ' ' if parts else ''
            return lead, [pre + lemma]
        if count:
            parts.append(_scale_group(count, singular, plural, scale_gender,
                                      NOM, False))
    lead = ' '.join(parts) + ' ' if parts else ''
    thousands, rest = divmod(n, 1000)
    if rest == 0 and thousands:
        # tisíci, dvetisíci, päťtisíci
        if thousands == 1:
            pre = ''
        elif thousands in multiplier:
            pre = multiplier[thousands]
        else:
            pre = _thousands_prefix(thousands)[:-len('tisíc')]
        return lead, [pre + 'tisíci']
    prefix = _thousands_prefix(thousands) if thousands else ''
    hundreds, tens_units = divmod(rest, 100)
    if tens_units == 0:
        # stý, dvestý, tisícstý
        if hundreds == 2 and not codified:
            return lead + prefix, ['dvestý']
        return lead + prefix, [ORDINALS[hundreds * 100]]
    prefix = prefix + (HUNDREDS[hundreds] if hundreds else '')
    if tens_units in ORDINALS:
        return lead + prefix, [ORDINALS[tens_units]]
    return lead + prefix, [ORDINALS[tens_units - tens_units % 10],
                           ORDINALS[tens_units % 10]]


def _ordinal(n, c, gender, animacy, plural, codified):
    # the cardinal prefix is glued to the first ordinal word (PSP 1998)
    prefix, lemmas = _ordinal_lemmas(n, codified)
    return prefix + ' '.join(
        _decline_ordinal(lemma, c, gender, animacy, plural)
        for lemma in lemmas)


def _plural_form(n):
    # index into (1, 2-4, 5 and up); a bare 2-4 after sto-/tisíc- counts
    # as 2-4: "stodve knihy" (native review)
    if n == 1:
        return 0
    if n % 100 in (2, 3, 4):
        return 1
    return 2


def _counted(n, forms):
    return '%s %s' % (_cardinal(n, gender='feminine'),
                      forms[_plural_form(n)])


def _decimal(value):
    # nominative only: "dve celé päť desatín"; the whole part agrees with
    # "celá", longer fractions are read digit by digit
    whole, fraction = format(value, 'f').split('.')
    fraction = fraction.rstrip('0')
    words = _counted(int(whole), WHOLE)
    if len(fraction) > len(DENOMINATORS):
        return '%s %s' % (words, ' '.join(
            _cardinal(int(digit), gender='feminine') for digit in fraction))
    return '%s %s' % (words, _counted(int(fraction),
                                      DENOMINATORS[len(fraction)]))


class Num2Word_SK(Num2Word_Base):
    CURRENCY_FORMS = {
        'EUR': (
            ('euro', 'eurá', 'eur'), ('cent', 'centy', 'centov')
        ),
    }
    CURRENCY_GENDERS = {
        'EUR': ('neuter', 'masculine'),
    }
    MAXVAL = 10 ** 33

    def setup(self):
        self.negword = 'mínus'

    def str_to_number(self, value):
        return Decimal(value.replace(',', '.'))

    def to_cardinal(self, number, gender='masculine', case='nominative',
                    animacy='inanimate', construction='genitive',
                    declined=True):
        """
        gender: 'masculine', 'feminine' or 'neuter'
        case: 'nominative', 'genitive', 'dative', 'accusative',
            'instrumental' or 'locative'
        animacy: 'inanimate', 'animate' or 'personal' (people: "dvaja")
        construction: 'genitive' ("dvadsaťdva žiakov") or 'agreement'
            ("dvadsiati dvaja žiaci")
        declined: False keeps compounds undeclined ("so stodva žiakmi")
        A number with a fraction is read in the nominative:
        "dve celé päť desatín".
        """
        c = _case_index(gender, case, animacy)
        _check('construction', construction, CONSTRUCTIONS)
        value = Decimal(str(number))
        if value.is_nan():
            raise ValueError('%s is not a number' % number)
        if value.copy_abs() >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))
        sign = '%s ' % self.negword if value < 0 else ''
        value = value.copy_abs()
        if value == value.to_integral_value():
            return sign + _cardinal(int(value), c, gender, animacy,
                                    construction, declined)
        return sign + _decimal(value)

    def to_ordinal(self, number, gender='masculine', case='nominative',
                   animacy='inanimate', plural=False, codified=False):
        """
        gender, case, animacy: as for to_cardinal
        plural: plural forms ("prví", "prvých")
        codified: the codified "dvojstý", "dvojtisíci" instead of the
            more frequent "dvestý", "dvetisíci"
        """
        c = _case_index(gender, case, animacy)
        self.verify_ordinal(number)
        if number >= self.MAXVAL:
            raise OverflowError(self.errmsg_toobig % (number, self.MAXVAL))
        return _ordinal(int(number), c, gender, animacy, plural, codified)

    def to_ordinal_num(self, number):
        self.verify_ordinal(number)
        return '%d.' % number

    def pluralize(self, n, forms):
        return forms[_plural_form(n)]

    def _money_verbose(self, number, currency):
        return self.to_cardinal(number,
                                gender=self.CURRENCY_GENDERS[currency][0])

    def _cents_verbose(self, number, currency):
        return self.to_cardinal(number,
                                gender=self.CURRENCY_GENDERS[currency][1])
