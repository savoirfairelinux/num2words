
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

import re
from decimal import Decimal
from unittest import TestCase

from num2words import num2words

# Sources quoted below:
# MSJ: Ružička (ed.), Morfológia slovenského jazyka, SAV 1966, pp. 300-327
# PSP: Pravidlá slovenského pravopisu 1991 and 1998, as quoted by JAR
# JAR: Jarošová, "Zložené číslovky so zreteľom na písanie spolu
#      a oddelene", Slovenská reč 86 (2021)
# NAV: Navrátil, "Neohybnosť v ohybných slovných druhoch",
#      Kultúra slova 37 (2003)
# BEL: Encyclopaedia Beliana, "číslovky"
# PAL: Páleníková (JÚĽŠ SAV), "Číslovky dvadsaťjeden, tridsaťjeden,
#      štyridsaťjeden"
# POV: Považaj (JÚĽŠ SAV), on sedem, osem, sedemdesiat, osemdesiat
# TASR: "Ako písať jednoslovné a viacslovné číslovky", TASR 2018
# SRA: Šrámeková, "K potenciálnej variantnosti číslovkových tvarov
#      dvojstý, dvestý", Kultúra slova 57 (2023), quoting SSSJ
# DUCH: Duchková (JÚĽŠ SAV), "Ako čítame a skloňujeme desatinné čísla"
# native review: the sources are silent or allow variants, and a native
#      speaker chose the form

CASES = ('nominative', 'genitive', 'dative', 'accusative', 'instrumental',
         'locative')
GENDERS = ('masculine', 'feminine', 'neuter')


def n2w(number, **kwargs):
    return num2words(number, lang='sk', **kwargs)


def paradigm(number, **kwargs):
    return [n2w(number, case=case, **kwargs) for case in CASES]


class Num2WordsSKTest(TestCase):
    def check(self, cases):
        for number, kwargs, words in cases:
            with self.subTest(number=number, **kwargs):
                self.assertEqual(n2w(number, **kwargs), words)

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='sk'), "sto")
        self.assertEqual(num2words(101, lang='sk'), "stojeden")
        self.assertEqual(num2words(110, lang='sk'), "stodesať")
        self.assertEqual(num2words(115, lang='sk'), "stopätnásť")
        self.assertEqual(num2words(123, lang='sk'), "stodvadsaťtri")
        self.assertEqual(num2words(1000, lang='sk'), "tisíc")
        self.assertEqual(num2words(1001, lang='sk'), "tisícjeden")
        self.assertEqual(num2words(2012, lang='sk'), "dvetisícdvanásť")
        self.assertEqual(
            num2words(10.02, lang='sk'),
            "desať celých dve stotiny"
        )
        self.assertEqual(
            num2words(15.007, lang='sk'),
            "pätnásť celých sedem tisícin"
        )
        self.assertEqual(
            num2words(12519.85, lang='sk'),
            "dvanásťtisícpäťstodevätnásť celých osemdesiatpäť stotín"
        )
        self.assertEqual(
            num2words(123.50, lang='sk'),
            "stodvadsaťtri celých päť desatín"
        )
        self.assertEqual(
            num2words(1234567890, lang='sk'),
            "miliarda dvestotridsaťštyri miliónov päťstošesťdesiat"
            "sedemtisícosemstodeväťdesiat"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='sk'),
            "dvestopätnásť kvintiliónov štyristošesťdesiatjeden kvadriliárd "
            "štyristosedem kvadriliónov osemstodeväťdesiatdva triliárd "
            "tridsaťdeväť triliónov dve biliardy stopäťdesiatsedem biliónov "
            "stoosemdesiatdeväť miliárd osemstoosemdesiattri miliónov "
            "deväťstojedentisícšesťstosedemdesiatšesť"
        )
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='sk'),
            "sedemstodevätnásť kvintiliónov deväťdesiatštyri kvadriliárd "
            "dvestotridsaťštyri kvadriliónov šesťstodeväťdesiattri triliárd "
            "šesťstošesťdesiattri triliónov tridsaťštyri biliárd "
            "osemstodvadsaťdva biliónov osemstodvadsaťštyri miliárd "
            "tristoosemdesiatštyri miliónov "
            "dvestodvadsaťtisícdvestodeväťdesiatjeden"
        )

    def test_jeden_by_gender_and_animacy(self):
        # MSJ pp. 318-323
        self.assertEqual(paradigm(1), ['jeden', 'jedného', 'jednému',
                                       'jeden', 'jedným', 'jednom'])
        self.assertEqual(n2w(1, case='accusative', animacy='animate'),
                         'jedného')
        self.assertEqual(paradigm(1, gender='feminine'),
                         ['jedna', 'jednej', 'jednej', 'jednu', 'jednou',
                          'jednej'])
        self.assertEqual(paradigm(1, gender='neuter'),
                         ['jedno', 'jedného', 'jednému', 'jedno', 'jedným',
                          'jednom'])

    def test_dva_tri_styri_with_masculine_personal_forms(self):
        # MSJ pp. 318-323; the accusative of people is the genitive
        self.assertEqual(paradigm(2), ['dva', 'dvoch', 'dvom', 'dva',
                                       'dvoma', 'dvoch'])
        self.assertEqual(paradigm(2, gender='feminine'),
                         ['dve', 'dvoch', 'dvom', 'dve', 'dvomi', 'dvoch'])
        self.assertEqual(paradigm(2, animacy='personal')[0::3],
                         ['dvaja', 'dvoch'])
        self.assertEqual(paradigm(3, animacy='personal')[0::3],
                         ['traja', 'troch'])
        self.assertEqual(paradigm(4, animacy='personal')[0::3],
                         ['štyria', 'štyroch'])
        self.assertEqual(paradigm(3)[0::3], ['tri', 'tri'])
        # MSJ and the Slovak National Corpus list dvoma/dvomi and
        # troma/tromi as standard: dvoma, troma with masculine and neuter
        # nouns, dvomi, tromi with feminine nouns (native review)
        self.assertEqual(n2w(3, case='instrumental'), 'troma')
        self.assertEqual(n2w(3, gender='feminine', case='instrumental'),
                         'tromi')
        for gender in GENDERS:
            with self.subTest(gender=gender):
                self.assertEqual(n2w(4, gender=gender, case='instrumental'),
                                 'štyrmi')

    def test_pat_paradigm(self):
        # MSJ p. 324; the stems of 7, 8, 70 and 80 after POV
        self.assertEqual(paradigm(5), ['päť', 'piatich', 'piatim', 'päť',
                                       'piatimi', 'piatich'])
        self.check([
            (5, {'animacy': 'personal', 'construction': 'agreement'},
             'piati'),
            (5, {'animacy': 'personal', 'construction': 'agreement',
                 'case': 'accusative'}, 'piatich'),
            (7, {'case': 'genitive'}, 'siedmich'),
            (8, {'case': 'genitive'}, 'ôsmich'),
            (17, {'case': 'genitive'}, 'sedemnástich'),
            (20, {'case': 'genitive'}, 'dvadsiatich'),
            (70, {'case': 'genitive'}, 'sedemdesiatich'),
            (80, {'case': 'genitive'}, 'osemdesiatich'),
        ])

    def test_compounds_ending_in_jeden_never_decline(self):
        # PAL, NAV, MSJ p. 326: they never decline and keep "jeden"
        for gender in GENDERS:
            with self.subTest(gender=gender):
                self.assertEqual(set(paradigm(21, gender=gender)),
                                 {'dvadsaťjeden'})
        self.check([
            (61, {'case': 'instrumental'}, 'šesťdesiatjeden'),
            (41, {'case': 'locative', 'gender': 'feminine'},
             'štyridsaťjeden'),
        ])

    def test_22_declines_both_parts_as_cardinals(self):
        self.check([
            # MSJ p. 326: dvadsiatich dvoch žiakov, dvadsiatim dvom žiakom
            (22, {'case': 'genitive'}, 'dvadsiatich dvoch'),
            (22, {'case': 'dative'}, 'dvadsiatim dvom'),
            (22, {'case': 'instrumental'}, 'dvadsiatimi dvoma'),
            # MSJ p. 326: "jeden a dva má pri všetkých podstatných menách
            # mužský tvar"
            (22, {'gender': 'feminine'}, 'dvadsaťdva'),
            (22, {'case': 'locative', 'declined': False}, 'dvadsaťdva'),
            # NAV
            (25, {'animacy': 'personal', 'construction': 'agreement'},
             'dvadsiati piati'),
        ])

    def test_psp_and_tasr_quotes(self):
        self.check([
            # PSP 1991
            (124, {'case': 'genitive', 'animacy': 'personal'},
             'stodvadsiatich štyroch'),
            (124, {'animacy': 'personal', 'construction': 'agreement'},
             'stodvadsiati štyria'),
            # TASR
            (245, {'case': 'instrumental'}, 'dvestoštyridsiatimi piatimi'),
            (352, {'case': 'dative'}, 'tristopäťdesiatim dvom'),
            # JAR p. 214
            (1225, {'case': 'genitive'}, 'tisícdvestodvadsiatich piatich'),
        ])

    def test_invariable_with_counted_nouns(self):
        # BEL, MSJ p. 317, NAV: sto and -tisíc do not decline
        for number in (100, 200, 500, 900, 1000, 2000, 5000, 21000, 100000,
                       101, 121, 1001):
            for gender in GENDERS:
                with self.subTest(number=number, gender=gender):
                    self.assertEqual(
                        len(set(paradigm(number, gender=gender))), 1)

    def test_milion_miliarda_are_declined_nouns_written_apart(self):
        # NAV, BEL, JAR fn. 18
        self.assertEqual(paradigm(10 ** 6),
                         ['milión', 'milióna', 'miliónu', 'milión',
                          'miliónom', 'milióne'])
        self.assertEqual(paradigm(2 * 10 ** 6),
                         ['dva milióny', 'dvoch miliónov', 'dvom miliónom',
                          'dva milióny', 'dvoma miliónmi',
                          'dvoch miliónoch'])
        self.assertEqual(paradigm(5 * 10 ** 6),
                         ['päť miliónov', 'piatich miliónov',
                          'piatim miliónom', 'päť miliónov',
                          'piatimi miliónmi', 'piatich miliónoch'])
        self.assertEqual(paradigm(2 * 10 ** 9),
                         ['dve miliardy', 'dvoch miliárd', 'dvom miliardám',
                          'dve miliardy', 'dvomi miliardami',
                          'dvoch miliardách'])
        self.check([
            (5 * 10 ** 9, {}, 'päť miliárd'),
            (5234567, {},
             'päť miliónov dvestotridsaťštyritisícpäťstošesťdesiatsedem'),
        ])

    def test_undeclined_variant_keeps_every_compound_invariable(self):
        # MSJ p. 326: compounds "sa alebo neskloňujú, alebo sa skloňujú
        # v oboch častiach"; PSP 1991 writes declined units apart
        self.check([
            (202, {'case': 'genitive'}, 'dvesto dvoch'),
            (202, {'case': 'genitive', 'declined': False}, 'dvestodva'),
            (112, {'case': 'instrumental', 'declined': False},
             'stodvanásť'),
            (1000005, {'case': 'genitive'}, 'milióna piatich'),
            (1000005, {'case': 'genitive', 'declined': False},
             'milióna päť'),
            (5, {'case': 'genitive', 'declined': False}, 'piatich'),
        ])

    def test_scale_groups_always_decline(self):
        # milión and miliarda are nouns, also before a smaller part
        # (native review)
        self.check([
            (2000005, {'case': 'genitive'}, 'dvoch miliónov piatich'),
            (2500000, {'case': 'dative'}, 'dvom miliónom päťstotisíc'),
            (1500000000, {'case': 'dative'}, 'miliarde päťsto miliónom'),
            (1000002000000, {'case': 'instrumental'},
             'biliónom dvoma miliónmi'),
        ])

    def test_native_review_decisions(self):
        self.check([
            (22000, {}, 'dvadsaťdvatisíc'),
            # stodve knihy, not stodva kníh; after tens MSJ applies
            (102, {'gender': 'feminine'}, 'stodve'),
            (102, {'gender': 'neuter'}, 'stodve'),
            (102, {}, 'stodva'),
            (122, {'gender': 'feminine'}, 'stodvadsaťdva'),
            (2002, {'gender': 'feminine'}, 'dvetisícdve'),
            (1000002, {'gender': 'feminine'}, 'milión dve'),
            # dvoma stromami, dvoma mestami, troma mužmi; dvomi stenami
            (2, {'case': 'instrumental'}, 'dvoma'),
            (2, {'gender': 'neuter', 'case': 'instrumental'}, 'dvoma'),
            (2, {'gender': 'feminine', 'case': 'instrumental'}, 'dvomi'),
            (22, {'gender': 'feminine', 'case': 'instrumental'},
             'dvadsiatimi dvomi'),
            (3, {'case': 'instrumental'}, 'troma'),
            (3, {'gender': 'feminine', 'case': 'instrumental'}, 'tromi'),
            # like stodve knihy; the genitive plural after 5 and up and
            # after tens
            (102 * 10 ** 6, {}, 'stodva milióny'),
            (102 * 10 ** 9, {}, 'stodve miliardy'),
            (105 * 10 ** 6, {}, 'stopäť miliónov'),
            (22 * 10 ** 9, {}, 'dvadsaťdva miliárd'),
            # decimals are read in the nominative
            (2.5, {'case': 'genitive'}, 'dve celé päť desatín'),
            (300, {'to': 'ordinal'}, 'trojstý'),
            (400, {'to': 'ordinal'}, 'štvorstý'),
            (1000001, {'to': 'ordinal'}, 'milión prvý'),
            (5000, {'to': 'ordinal'}, 'päťtisíci'),
            (21000, {'to': 'ordinal'}, 'dvadsaťjedentisíci'),
        ])

    def test_nula_declines_as_a_noun(self):
        self.assertEqual(paradigm(0), ['nula', 'nuly', 'nule', 'nulu',
                                       'nulou', 'nule'])

    def test_no_ordinal_forms_in_cardinals(self):
        # an earlier version of these rules declined 21 as
        # "dvadsiatehojedného", 100 as "stého" and 1000 as "tisíceho"
        ordinal = re.compile(r'(ého|ému|eho|emu|ým|ym)\b|stej\b|tisícej\b')
        # masculine and neuter 1 are left out: jedného, jednému and jedným
        # are cardinal forms
        for words in paradigm(1, gender='feminine'):
            self.assertIsNone(ordinal.search(words), words)
        for number in [0] + list(range(2, 130)) + [
                200, 345, 999, 1000, 1001, 2024, 21000, 10 ** 6,
                2 * 10 ** 6, 10 ** 9]:
            for gender in GENDERS:
                for words in paradigm(number, gender=gender):
                    self.assertIsNone(ordinal.search(words),
                                      (number, gender, words))

    def test_to_ordinal(self):
        self.assertEqual(paradigm(1, to='ordinal'),
                         ['prvý', 'prvého', 'prvému', 'prvý', 'prvým',
                          'prvom'])
        self.assertEqual(paradigm(3, to='ordinal'),
                         ['tretí', 'tretieho', 'tretiemu', 'tretí',
                          'tretím', 'treťom'])
        self.assertEqual(paradigm(3, to='ordinal', gender='feminine'),
                         ['tretia', 'tretej', 'tretej', 'tretiu', 'treťou',
                          'tretej'])
        # rhythmic law
        self.assertEqual(paradigm(5, to='ordinal')[:3],
                         ['piaty', 'piateho', 'piatemu'])
        self.check([
            (1, {'to': 'ordinal', 'case': 'accusative',
                 'animacy': 'animate'}, 'prvého'),
            (7, {'to': 'ordinal', 'case': 'genitive'}, 'siedmeho'),
            (1, {'to': 'ordinal', 'plural': True, 'animacy': 'personal'},
             'prví'),
            (5, {'to': 'ordinal', 'plural': True, 'animacy': 'personal'},
             'piati'),
            (1, {'to': 'ordinal', 'plural': True, 'gender': 'feminine'},
             'prvé'),
            (5, {'to': 'ordinal', 'plural': True, 'case': 'genitive'},
             'piatych'),
        ])

    def test_special_ordinals(self):
        self.check([
            # SSSJ via SRA: tisíci, tisíca, tisíce
            (1000, {'to': 'ordinal', 'gender': 'feminine'}, 'tisíca'),
            (1000, {'to': 'ordinal', 'gender': 'neuter'}, 'tisíce'),
            (1000, {'to': 'ordinal', 'case': 'genitive'}, 'tisíceho'),
            # SRA: dvestý, dvetisíci are more frequent than the codified
            # dvojstý, dvojtisíci (native review), *tritisíci is unattested
            (2000, {'to': 'ordinal'}, 'dvetisíci'),
            (2000, {'to': 'ordinal', 'codified': True}, 'dvojtisíci'),
            (200, {'to': 'ordinal'}, 'dvestý'),
            (200, {'to': 'ordinal', 'codified': True}, 'dvojstý'),
            (3000, {'to': 'ordinal'}, 'trojtisíci'),
            (1200, {'to': 'ordinal'}, 'tisícdvestý'),
            (100, {'to': 'ordinal'}, 'stý'),
            (0, {'to': 'ordinal'}, 'nultý'),
            (10 ** 6, {'to': 'ordinal', 'case': 'genitive'}, 'miliónteho'),
            (2 * 10 ** 6, {'to': 'ordinal'}, 'dvemiliónty'),
            (5 * 10 ** 6, {'to': 'ordinal'}, 'päťmiliónty'),
            (10 ** 9, {'to': 'ordinal'}, 'miliardtý'),
            (10 ** 9 + 10 ** 6, {'to': 'ordinal'}, 'miliarda miliónty'),
        ])

    def test_compound_ordinals_keep_cardinal_prefixes(self):
        self.check([
            # BEL: two words
            (21, {'to': 'ordinal'}, 'dvadsiaty prvý'),
            (21, {'to': 'ordinal', 'case': 'genitive'},
             'dvadsiateho prvého'),
            # PSP 1998
            (101, {'to': 'ordinal'}, 'stoprvý'),
            (2002, {'to': 'ordinal'}, 'dvetisícdruhý'),
            # PSP 1991
            (124, {'to': 'ordinal', 'animacy': 'personal'},
             'stodvadsiaty štvrtý'),
            (124, {'to': 'ordinal', 'case': 'genitive',
                   'animacy': 'personal'}, 'stodvadsiateho štvrtého'),
            (1985, {'to': 'ordinal', 'case': 'locative'},
             'tisícdeväťstoosemdesiatom piatom'),
            (2024, {'to': 'ordinal'}, 'dvetisícdvadsiaty štvrtý'),
            # JAR p. 217
            (102, {'to': 'ordinal', 'case': 'genitive'}, 'stodruhého'),
        ])

    def test_decimals(self):
        self.check([
            # DUCH
            (0.25, {}, 'nula celých dvadsaťpäť stotín'),
            (1.9, {}, 'jedna celá deväť desatín'),
            (2.84, {}, 'dve celé osemdesiatštyri stotín'),
            (41.2, {}, 'štyridsaťjeden celých dve desatiny'),
            (396.4, {}, 'tristodeväťdesiatšesť celých štyri desatiny'),
            (2.531, {}, 'dve celé päťstotridsaťjeden tisícin'),
            (3.14, {}, 'tri celé štrnásť stotín'),
            (-2.5, {}, 'mínus dve celé päť desatín'),
            # a bare 2-4 after sto- counts as 2-4 (native review)
            (102.3, {}, 'stodve celé tri desatiny'),
            (0.102, {}, 'nula celých stodve tisíciny'),
        ])

    def test_number_forms(self):
        self.check([
            ('68,50', {}, 'šesťdesiatosem celých päť desatín'),
            ('1.50', {}, 'jedna celá päť desatín'),
            (1.5, {}, 'jedna celá päť desatín'),
            (-0.5, {}, 'mínus nula celých päť desatín'),
            (1e-05, {}, 'nula celých jedna stotisícina'),
            (Decimal('1E+3'), {}, 'tisíc'),
            ('-0', {}, 'nula'),
            (-5, {'case': 'genitive'}, 'mínus piatich'),
            # more than six decimal places are read digit by digit
            (0.1234567, {},
             'nula celých jedna dve tri štyri päť šesť sedem'),
            # integer values keep every option
            (2.0, {'animacy': 'personal'}, 'dvaja'),
            (Decimal('5'), {'case': 'genitive'}, 'piatich'),
            ('22', {'case': 'dative', 'declined': False}, 'dvadsaťdva'),
        ])

    def test_range(self):
        self.check([
            (10 ** 30, {}, 'kvintilión'),
            (10 ** 30, {'case': 'genitive'}, 'kvintilióna'),
            (2 * 10 ** 30, {}, 'dva kvintilióny'),
            (10 ** 30, {'to': 'ordinal'}, 'kvintiliónty'),
            (10 ** 33 - 1, {},
             'deväťstodeväťdesiatdeväť kvintiliónov '
             'deväťstodeväťdesiatdeväť kvadriliárd '
             'deväťstodeväťdesiatdeväť kvadriliónov '
             'deväťstodeväťdesiatdeväť triliárd '
             'deväťstodeväťdesiatdeväť triliónov '
             'deväťstodeväťdesiatdeväť biliárd '
             'deväťstodeväťdesiatdeväť biliónov '
             'deväťstodeväťdesiatdeväť miliárd '
             'deväťstodeväťdesiatdeväť miliónov '
             'deväťstodeväťdesiatdeväťtisícdeväťstodeväťdesiatdeväť'),
        ])
        for number, kwargs in ((10 ** 33, {}), (-10 ** 33, {}),
                               (float('inf'), {}),
                               (10 ** 33, {'to': 'ordinal'})):
            with self.subTest(number=number, **kwargs):
                with self.assertRaises(OverflowError):
                    n2w(number, **kwargs)

    def test_errors(self):
        for error, number, kwargs in (
                (ValueError, float('nan'), {}),
                (ValueError, 5, {'case': 'vocative'}),
                (ValueError, 5, {'gender': 'plural'}),
                (ValueError, 5, {'animacy': 'animal'}),
                (ValueError, 5, {'construction': 'inverted'}),
                (ValueError, 5, {'to': 'ordinal', 'case': 'vocative'}),
                (TypeError, 5, {'animate': True}),
                (TypeError, 5, {'to': 'ordinal', 'declined': False}),
                (TypeError, -1, {'to': 'ordinal'}),
                (TypeError, 1.5, {'to': 'ordinal'}),
                (TypeError, -1, {'to': 'ordinal_num'})):
            with self.subTest(number=number, **kwargs):
                with self.assertRaises(error):
                    n2w(number, **kwargs)

    def test_ordinal_num_and_year(self):
        self.check([
            (1, {'to': 'ordinal_num'}, '1.'),
            (2024, {'to': 'ordinal_num'}, '2024.'),
            (1989, {'to': 'year'}, 'tisícdeväťstoosemdesiatdeväť'),
            (2024, {'to': 'year'}, 'dvetisícdvadsaťštyri'),
        ])

    def test_currency(self):
        self.assertEqual(
            num2words(10.0, lang='sk', to='currency', currency='EUR'),
            "desať eur, nula centov")
        self.assertEqual(
            num2words(1234.56, lang='sk', to='currency', currency='EUR'),
            "tisícdvestotridsaťštyri eur, päťdesiatšesť centov")
        self.assertEqual(
            num2words(101.11, lang='sk', to='currency', currency='EUR',
                      separator=' a'),
            "stojeden eur a jedenásť centov")
        self.assertEqual(
            num2words(-12519.85, lang='sk', to='currency', cents=False),
            "mínus dvanásťtisícpäťstodevätnásť eur, 85 centov"
        )
        self.assertEqual(
            num2words(19.50, lang='sk', to='currency', cents=False),
            "devätnásť eur, 50 centov"
        )
        # the numeral agrees with euro (neuter) and cent (masculine)
        self.check([
            (1.01, {'to': 'currency'}, 'jedno euro, jeden cent'),
            (2.02, {'to': 'currency'}, 'dve eurá, dva centy'),
            (4.04, {'to': 'currency'}, 'štyri eurá, štyri centy'),
            (22.22, {'to': 'currency'}, 'dvadsaťdva eur, dvadsaťdva centov'),
            ('102.00', {'to': 'currency'}, 'stodve eurá, nula centov'),
        ])
