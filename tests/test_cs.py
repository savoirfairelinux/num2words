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
# IJP: Internetová jazyková příručka, ÚJČ AV ČR (prirucka.ujc.cas.cz):
#      chapters 670 (dva), 671 (tři, čtyři), 791 (spelling, long
#      numbers, decimals), 792 (the counted noun); IJP:word is the
#      dictionary entry for the word
# WIKI-ČČ, WIKI-ŘČ: cs.wikipedia, "České číslovky", "Řadová číslovka"
# NESČ: Nový encyklopedický slovník češtiny, "ŘADOVÁ ČÍSLOVKA"
# ČRo-05: Český rozhlas, Málková, "Skloňování číslovek" (2005)
# NK-07: Národní knihovna ČR, "Ptejte se knihovny" (2007), citing the
#      ÚJČ language helpline
# ÚJOP: Univerzita Karlova, "Česky v Česku - gramatické tabulky", T.4.2
# HRD: Hrdlička, "K užívání českých číslovek a číselných výrazů",
#      Studie z aplikované lingvistiky 2011/2
# CHL: Chlumská, "Řadové číslovky v současné češtině" (FF UK 2009),
#      quoting Sedláček and Gebauer
# SSJČ: Slovník spisovného jazyka českého, as quoted in IJP:tisíc
# review: the sources are silent or allow variants, and the form was
#      chosen in a review of this implementation

CASES = ('nominative', 'genitive', 'dative', 'accusative', 'instrumental',
         'locative')
GENDERS = ('masculine', 'feminine', 'neuter')


def n2w(number, **kwargs):
    return num2words(number, lang='cs', **kwargs)


def paradigm(number, **kwargs):
    return [n2w(number, case=case, **kwargs) for case in CASES]


class Num2WordsCSTest(TestCase):
    def check(self, cases):
        for number, kwargs, words in cases:
            with self.subTest(number=number, **kwargs):
                self.assertEqual(n2w(number, **kwargs), words)

    def test_cardinal(self):
        self.assertEqual(num2words(100, lang='cs'), "sto")
        self.assertEqual(num2words(101, lang='cs'), "sto jedna")
        self.assertEqual(num2words(110, lang='cs'), "sto deset")
        self.assertEqual(num2words(115, lang='cs'), "sto patnáct")
        self.assertEqual(num2words(123, lang='cs'), "sto dvacet tři")
        self.assertEqual(num2words(1000, lang='cs'), "tisíc")
        self.assertEqual(num2words(1001, lang='cs'), "tisíc jedna")
        self.assertEqual(num2words(2012, lang='cs'), "dva tisíce dvanáct")
        self.assertEqual(
            num2words(10.02, lang='cs'),
            "deset celých dvě setiny"
        )
        self.assertEqual(
            num2words(15.007, lang='cs'),
            "patnáct celých sedm tisícin"
        )
        self.assertEqual(
            num2words(12519.85, lang='cs'),
            "dvanáct tisíc pět set devatenáct celých osmdesát pět setin"
        )
        self.assertEqual(
            num2words(123.50, lang='cs'),
            "sto dvacet tři celé pět desetin"
        )
        self.assertEqual(
            num2words(1234567890, lang='cs'),
            "miliarda dvě stě třicet čtyři milionů pět set šedesát "
            "sedm tisíc osm set devadesát"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='cs'),
            "dvě stě patnáct kvintilionů čtyři sta šedesát jedna "
            "kvadriliard čtyři sta sedm kvadrilionů osm set devadesát dva "
            "triliard třicet devět trilionů dvě biliardy sto padesát sedm "
            "bilionů sto osmdesát devět miliard osm set osmdesát tři "
            "milionů devět set jedna tisíc šest set sedmdesát šest"
        )
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='cs'),
            "sedm set devatenáct kvintilionů devadesát čtyři kvadriliard "
            "dvě stě třicet čtyři kvadrilionů šest set devadesát tři "
            "triliard šest set šedesát tři trilionů třicet čtyři biliard "
            "osm set dvacet dva bilionů osm set dvacet čtyři miliard "
            "tři sta osmdesát čtyři milionů dvě stě dvacet tisíc dvě stě "
            "devadesát jedna"
        )

    def test_jeden_by_gender_and_animacy(self):
        # IJP:jeden
        self.assertEqual(paradigm(1, gender='masculine'),
                         ['jeden', 'jednoho', 'jednomu', 'jeden', 'jedním',
                          'jednom'])
        self.assertEqual(n2w(1, gender='masculine', case='accusative',
                             animacy='animate'), 'jednoho')
        self.assertEqual(paradigm(1, gender='feminine'),
                         ['jedna', 'jedné', 'jedné', 'jednu', 'jednou',
                          'jedné'])
        self.assertEqual(paradigm(1, gender='neuter'),
                         ['jedno', 'jednoho', 'jednomu', 'jedno', 'jedním',
                          'jednom'])

    def test_counting_form_without_gender(self):
        # counting: jedna, dva, tři; "od jedné do deseti"
        self.check([
            (1, {}, 'jedna'),
            (1, {'case': 'genitive'}, 'jedné'),
            (-1, {}, 'mínus jedna'),
            (2, {}, 'dva'),
            (21, {}, 'dvacet jedna'),
        ])

    def test_dva_tri_ctyri(self):
        # IJP-670, IJP-671
        self.assertEqual(paradigm(2), ['dva', 'dvou', 'dvěma', 'dva',
                                       'dvěma', 'dvou'])
        self.assertEqual(paradigm(2, gender='feminine'),
                         ['dvě', 'dvou', 'dvěma', 'dvě', 'dvěma', 'dvou'])
        self.assertEqual(paradigm(3), ['tři', 'tří', 'třem', 'tři', 'třemi',
                                       'třech'])
        self.assertEqual(paradigm(4, gender='feminine'),
                         ['čtyři', 'čtyř', 'čtyřem', 'čtyři', 'čtyřmi',
                          'čtyřech'])
        self.check([
            (2, {'gender': 'neuter'}, 'dvě'),
            # no animacy split for dva
            (2, {'case': 'accusative', 'animacy': 'animate'}, 'dva'),
        ])

    def test_pet_paradigm(self):
        # IJP:pět, IJP:devět, IJP:dvacet
        self.assertEqual(paradigm(5), ['pět', 'pěti', 'pěti', 'pět', 'pěti',
                                       'pěti'])
        self.check([
            (9, {'case': 'genitive'}, 'devíti'),
            (10, {'case': 'genitive'}, 'deseti'),
            (11, {'case': 'genitive'}, 'jedenácti'),
            (19, {'case': 'genitive'}, 'devatenácti'),
            (20, {'case': 'genitive'}, 'dvaceti'),
            (40, {'case': 'genitive'}, 'čtyřiceti'),
            (90, {'case': 'genitive'}, 'devadesáti'),
        ])

    def test_compounds_are_separate_words(self):
        # IJP-791: "Vypisujeme-li číslovky slovy, píšeme každé slovo
        # zvlášť, např. dvacet jedna"
        self.check([
            (21, {}, 'dvacet jedna'),
            (54, {}, 'padesát čtyři'),
            (99, {}, 'devadesát devět'),
        ])

    def test_three_constructions_for_x1_to_x4(self):
        # IJP-792: dvacet jeden žák, dvacet jedna žáků, jednadvacet žáků;
        # the genitive type is "běžnější"; WIKI-ČČ: "dvacet dva žen"
        for gender in GENDERS:
            with self.subTest(gender=gender):
                self.assertEqual(n2w(21, gender=gender), 'dvacet jedna')
                self.assertEqual(n2w(22, gender=gender), 'dvacet dva')
        self.check([
            (21, {'construction': 'agreement', 'gender': 'masculine'},
             'dvacet jeden'),
            (21, {'construction': 'agreement', 'gender': 'neuter'},
             'dvacet jedno'),
            (22, {'construction': 'agreement', 'gender': 'feminine'},
             'dvacet dvě'),
            (21, {'construction': 'inverted'}, 'jednadvacet'),
            # IJP-791
            (54, {'construction': 'inverted'}, 'čtyřiapadesát'),
            (99, {'construction': 'inverted'}, 'devětadevadesát'),
        ])

    def test_compound_obliques_decline_both_words(self):
        self.check([
            # IJP-791: "k dvaceti sedmi stupňům"
            (27, {'case': 'dative'}, 'dvaceti sedmi'),
            (27, {'case': 'dative', 'construction': 'inverted'},
             'sedmadvaceti'),
            # ČRo-05: "k dvaceti pěti lidem", "padesáti dvěma korunami"
            (25, {'case': 'dative'}, 'dvaceti pěti'),
            (52, {'case': 'instrumental'}, 'padesáti dvěma'),
            # NK-07, IJP-791
            (23, {'case': 'genitive'}, 'dvaceti tří'),
            (23, {'case': 'dative'}, 'dvaceti třem'),
            (23, {'case': 'locative'}, 'dvaceti třech'),
            (22, {'case': 'dative', 'gender': 'feminine'}, 'dvaceti dvěma'),
            (22, {'case': 'dative', 'construction': 'inverted'},
             'dvaadvaceti'),
        ])

    def test_agreement_type_is_nominative_accusative_only(self):
        # review: "dvaceti jednoho" is not acceptable
        self.check([
            (21, {'construction': 'agreement', 'gender': 'masculine'},
             'dvacet jeden'),
            (21, {'case': 'genitive', 'construction': 'agreement',
                  'gender': 'masculine'}, 'jednadvaceti'),
            (21, {'case': 'genitive', 'construction': 'agreement',
                  'gender': 'feminine'}, 'jednadvaceti'),
            (201, {'case': 'genitive', 'construction': 'agreement'},
             'dvou set jedna'),
            (21000, {'construction': 'agreement'}, 'dvacet jeden tisíc'),
            (21000, {'case': 'genitive', 'construction': 'agreement'},
             'jednadvaceti tisíc'),
            (25000, {'construction': 'agreement'}, 'dvacet pět tisíc'),
            (29999, {'construction': 'agreement'},
             'dvacet devět tisíc devět set devadesát devět'),
            (1001, {'construction': 'agreement', 'gender': 'masculine'},
             'tisíc jeden'),
            (1001, {'construction': 'agreement', 'gender': 'masculine',
                    'case': 'accusative', 'animacy': 'animate'},
             'tisíc jednoho'),
            (1001, {'construction': 'agreement', 'gender': 'masculine',
                    'case': 'genitive'}, 'tisíce jedna'),
        ])

    def test_review_decisions(self):
        self.check([
            (101, {'case': 'genitive'}, 'sto jedna'),
            (101, {'case': 'instrumental', 'gender': 'feminine'},
             'sto jedna'),
            (1001, {'case': 'dative'}, 'tisíci jedna'),
            (1001, {'case': 'genitive'}, 'tisíce jedna'),
            (101000, {'case': 'genitive'}, 'sto jedna tisíc'),
            ('21,3', {}, 'dvacet jedna celá tři desetiny'),
            (10 ** 12, {}, 'bilion'),
            (21000, {'to': 'ordinal'}, 'jednadvacetitisící'),
            # up to two parts everything declines, from three only the last
            (2300, {'case': 'genitive'}, 'dvou tisíc tří set'),
            (1847, {'case': 'genitive'}, 'tisíc osm set čtyřiceti sedmi'),
        ])

    def test_x1_obliques_use_the_inverted_form(self):
        # no source gives "dvaceti jedné" or "dvaceti jednoho"
        for case in CASES[1:3] + CASES[4:]:
            for gender in GENDERS:
                with self.subTest(case=case, gender=gender):
                    self.assertEqual(n2w(21, case=case, gender=gender),
                                     'jednadvaceti')
        self.assertEqual(n2w(91, case='genitive'), 'jednadevadesáti')

    def test_hundreds_are_nouns(self):
        # IJP:sto, ÚJOP
        self.assertEqual(paradigm(100), ['sto', 'sta', 'stu', 'sto', 'stem',
                                         'stu'])
        self.assertEqual(paradigm(200),
                         ['dvě stě', 'dvou set', 'dvěma stům', 'dvě stě',
                          'dvěma sty', 'dvou stech'])
        self.assertEqual(paradigm(500),
                         ['pět set', 'pěti set', 'pěti stům', 'pět set',
                          'pěti sty', 'pěti stech'])
        # stá and sté are ordinals
        for gender in GENDERS:
            with self.subTest(gender=gender):
                self.assertEqual(n2w(100, gender=gender), 'sto')
                self.assertEqual(n2w(100, gender=gender, case='genitive'),
                                 'sta')
        self.check([
            # IJP:tři: "před třemi sty lety"
            (300, {'case': 'instrumental'}, 'třemi sty'),
            # ČRo-05: "k dvěma stům posluchačům", "s pěti sty padesáti
            # lidmi"
            (200, {'case': 'dative'}, 'dvěma stům'),
            (550, {'case': 'instrumental'}, 'pěti sty padesáti'),
        ])

    def test_sto_followed_by_a_numeral_stays_sto(self):
        # IJP-792: "ve sto dvaceti případech, po sto padesáti letech"
        self.check([
            (120, {'case': 'locative'}, 'sto dvaceti'),
            (150, {'case': 'locative'}, 'sto padesáti'),
            (121, {'case': 'genitive'}, 'sto jednadvaceti'),
        ])

    def test_tisic(self):
        self.assertEqual(paradigm(1000), ['tisíc', 'tisíce', 'tisíci',
                                          'tisíc', 'tisícem', 'tisíci'])
        self.assertEqual(paradigm(2000),
                         ['dva tisíce', 'dvou tisíc', 'dvěma tisícům',
                          'dva tisíce', 'dvěma tisíci', 'dvou tisících'])
        self.assertEqual(paradigm(5000),
                         ['pět tisíc', 'pěti tisíc', 'pěti tisícům',
                          'pět tisíc', 'pěti tisíci', 'pěti tisících'])
        # review: "bez sta tisíc korun"
        self.assertEqual(paradigm(100000),
                         ['sto tisíc', 'sta tisíc', 'stu tisícům',
                          'sto tisíc', 'stem tisíci', 'stu tisících'])
        self.check([
            # IJP-792: "s třemi tisíci diváků"; IJP:sto
            (3000, {'case': 'instrumental'}, 'třemi tisíci'),
            (333000, {}, 'tři sta třicet tři tisíc'),
            (21000, {}, 'dvacet jedna tisíc'),
            (22000, {}, 'dvacet dva tisíc'),
            (22000, {'construction': 'agreement'}, 'dvacet dva tisíce'),
            (21000, {'construction': 'inverted'}, 'jednadvacet tisíc'),
        ])

    def test_milion_miliarda(self):
        self.assertEqual(paradigm(10 ** 6),
                         ['milion', 'milionu', 'milionu', 'milion',
                          'milionem', 'milionu'])
        self.assertEqual(paradigm(2 * 10 ** 6),
                         ['dva miliony', 'dvou milionů', 'dvěma milionům',
                          'dva miliony', 'dvěma miliony', 'dvou milionech'])
        self.assertEqual(paradigm(5 * 10 ** 6),
                         ['pět milionů', 'pěti milionů', 'pěti milionům',
                          'pět milionů', 'pěti miliony', 'pěti milionech'])
        self.assertEqual(paradigm(10 ** 9),
                         ['miliarda', 'miliardy', 'miliardě', 'miliardu',
                          'miliardou', 'miliardě'])
        self.assertEqual(paradigm(2 * 10 ** 9),
                         ['dvě miliardy', 'dvou miliard', 'dvěma miliardám',
                          'dvě miliardy', 'dvěma miliardami',
                          'dvou miliardách'])
        self.check([
            # IJP:miliarda; IJP:milion: "53 miliony i 53 milionů"
            (3 * 10 ** 9, {}, 'tři miliardy'),
            (53 * 10 ** 6, {}, 'padesát tři milionů'),
            (53 * 10 ** 6, {'construction': 'agreement'},
             'padesát tři miliony'),
            (22 * 10 ** 9, {'construction': 'agreement'},
             'dvacet dvě miliardy'),
            (1234567890, {'construction': 'agreement'},
             'miliarda dvě stě třicet čtyři miliony pět set šedesát sedm '
             'tisíc osm set devadesát'),
        ])

    def test_nominative_long_numbers(self):
        self.check([
            # WIKI-ČČ, IJP-791, IJP:pět, IJP:milion
            (2345, {}, 'dva tisíce tři sta čtyřicet pět'),
            (2231, {}, 'dva tisíce dvě stě třicet jedna'),
            (5225, {}, 'pět tisíc dvě stě dvacet pět'),
            (12157582, {},
             'dvanáct milionů sto padesát sedm tisíc pět set osmdesát dva'),
            (1300783, {}, 'milion tři sta tisíc sedm set osmdesát tři'),
        ])

    def test_oblique_styles(self):
        self.check([
            # IJP-791 (a): every part declines
            (365, {'case': 'instrumental'}, 'třemi sty šedesáti pěti'),
            (365, {'case': 'instrumental', 'construction': 'inverted'},
             'třemi sty pětašedesáti'),
            (2300, {'case': 'genitive'}, 'dvou tisíc tří set'),
            # IJP-791 (b), NK-07, WIKI-ČČ: from three parts only the last
            (1847, {'case': 'genitive'}, 'tisíc osm set čtyřiceti sedmi'),
            (1847, {'case': 'genitive', 'construction': 'inverted'},
             'tisíc osm set sedmačtyřiceti'),
            (1358423, {'case': 'locative'},
             'milion tři sta padesát osm tisíc čtyři sta dvaceti třech'),
            (1223, {'case': 'genitive'}, 'tisíc dvě stě dvaceti tří'),
            (1223, {'case': 'dative'}, 'tisíc dvě stě dvaceti třem'),
            (11255, {'case': 'instrumental'},
             'jedenáct tisíc dvě stě padesáti pěti'),
            # oblique_style overrides
            (1847, {'case': 'genitive', 'oblique_style': 'full'},
             'tisíce osmi set čtyřiceti sedmi'),
            (1223, {'case': 'genitive', 'oblique_style': 'full'},
             'tisíce dvou set dvaceti tří'),
            (1223, {'case': 'dative', 'oblique_style': 'full'},
             'tisíci dvěma stům dvaceti třem'),
            (2152, {'case': 'instrumental', 'oblique_style': 'full'},
             'dvěma tisíci sto padesáti dvěma'),
            (11255, {'case': 'instrumental', 'oblique_style': 'full'},
             'jedenácti tisíci dvěma sty padesáti pěti'),
            (365, {'case': 'instrumental', 'oblique_style': 'partial'},
             'tři sta šedesáti pěti'),
        ])

    def test_nula_declines_as_a_noun(self):
        # IJP:nula
        self.assertEqual(paradigm(0), ['nula', 'nuly', 'nule', 'nulu',
                                       'nulou', 'nule'])

    def test_every_word_is_a_dictionary_word(self):
        # an earlier version of these rules wrote "dvacetjeden", "dvěstě",
        # "dvoutisícdvacetčtyři" and "dvamiliony"
        inverted = re.compile(
            '^(?:jedn|dva|tři|čtyři|pět|šest|sedm|osm|devět)a'
            '(?:dvacet|třicet|čtyřicet|padesát|šedesát|sedmdesát|osmdesát'
            '|devadesát)i?$')
        words = set("""
            nula nuly nule nulu nulou jeden jednoho jednomu jedním jednom
            jedna jedné jednu jednou jedno dva dvě dvou dvěma tři tří třem
            třemi třech čtyři čtyř čtyřem čtyřmi čtyřech
            sto sta stu stem stě set stům sty stech
            tisíc tisíce tisíci tisícem tisícům tisících
            milion milionu milionem miliony milionů milionům milionech
            miliarda miliardy miliardě miliardu miliardou miliard
            miliardám miliardami miliardách
        """.split())
        for k in list(range(5, 21)) + list(range(30, 100, 10)):
            words |= {n2w(k), n2w(k, case='genitive')}
        for number in list(range(0, 1200)) + [
                1999, 2000, 2024, 2345, 5000, 21000, 100000, 10 ** 6,
                2 * 10 ** 6, 1234567, 10 ** 9, 2 * 10 ** 9]:
            for gender in GENDERS:
                for case in CASES:
                    for style in ('auto', 'full'):
                        for word in n2w(number, gender=gender, case=case,
                                        oblique_style=style).split():
                            self.assertTrue(
                                word in words or inverted.match(word),
                                (number, gender, case, style, word))

    def test_no_ordinal_forms_in_cardinals(self):
        # an earlier version of these rules declined 21 as
        # "dvacátéhojednoho", 100 as "stého" and 1000 as "tisícího"
        ordinal = re.compile(
            r'(ého|ému|ém|ým|ých|tý|tá|té)\b|\bst[áéý]\b|tisící(ho|mu|m)?\b')
        for number in list(range(0, 130)) + [
                200, 345, 999, 1000, 1001, 2000, 2024, 21000, 10 ** 6,
                2 * 10 ** 6, 10 ** 9]:
            for gender in GENDERS:
                for words in paradigm(number, gender=gender):
                    self.assertIsNone(ordinal.search(words),
                                      (number, gender, words))

    def test_to_ordinal(self):
        # WIKI-ŘČ, IJP-791, IJP:tisíc
        self.assertEqual(paradigm(1, to='ordinal'),
                         ['první', 'prvního', 'prvnímu', 'první', 'prvním',
                          'prvním'])
        self.assertEqual(paradigm(1, to='ordinal', gender='feminine'),
                         ['první'] * 6)
        self.assertEqual(paradigm(2, to='ordinal'),
                         ['druhý', 'druhého', 'druhému', 'druhý', 'druhým',
                          'druhém'])
        self.assertEqual(paradigm(100, to='ordinal', gender='feminine'),
                         ['stá', 'sté', 'sté', 'stou', 'stou', 'sté'])
        self.assertEqual(paradigm(100, to='ordinal', gender='neuter'),
                         ['sté', 'stého', 'stému', 'sté', 'stým', 'stém'])
        # soft, like jarní
        self.assertEqual(paradigm(3, to='ordinal')[:3],
                         ['třetí', 'třetího', 'třetímu'])
        self.check([
            (1, {'to': 'ordinal', 'case': 'accusative',
                 'animacy': 'animate'}, 'prvního'),
            (2, {'to': 'ordinal', 'case': 'accusative',
                 'animacy': 'animate'}, 'druhého'),
            # IJP:nula
            (0, {'to': 'ordinal'}, 'nultý'),
        ])

    def test_ordinal_plurals(self):
        self.check([
            (2, {'to': 'ordinal', 'plural': True, 'animacy': 'animate'},
             'druzí'),
            (4, {'to': 'ordinal', 'plural': True, 'animacy': 'animate'},
             'čtvrtí'),
            (100, {'to': 'ordinal', 'plural': True, 'animacy': 'animate'},
             'stí'),
            (2, {'to': 'ordinal', 'plural': True}, 'druhé'),
            (2, {'to': 'ordinal', 'plural': True, 'gender': 'neuter'},
             'druhá'),
            (2, {'to': 'ordinal', 'plural': True, 'case': 'accusative',
                 'animacy': 'animate'}, 'druhé'),
            (2, {'to': 'ordinal', 'plural': True, 'case': 'genitive'},
             'druhých'),
            (1, {'to': 'ordinal', 'plural': True, 'animacy': 'animate'},
             'první'),
            (1, {'to': 'ordinal', 'plural': True, 'case': 'instrumental'},
             'prvními'),
        ])

    def test_round_ordinals(self):
        self.check([
            (200, {'to': 'ordinal'}, 'dvoustý'),
            (300, {'to': 'ordinal'}, 'třístý'),
            (400, {'to': 'ordinal'}, 'čtyřstý'),
            (500, {'to': 'ordinal'}, 'pětistý'),
            (900, {'to': 'ordinal'}, 'devítistý'),
            (1000, {'to': 'ordinal'}, 'tisící'),
            (1000, {'to': 'ordinal', 'case': 'genitive'}, 'tisícího'),
            # WIKI-ŘČ, NESČ
            (2000, {'to': 'ordinal'}, 'dvoutisící'),
            (25000, {'to': 'ordinal'}, 'pětadvacetitisící'),
            (100000, {'to': 'ordinal'}, 'stotisící'),
            (345000, {'to': 'ordinal'}, 'tři sta čtyřicet pět tisící'),
            (10 ** 6, {'to': 'ordinal'}, 'miliontý'),
            (10 ** 9, {'to': 'ordinal'}, 'miliardtý'),
        ])

    def test_compound_ordinals_every_part_ordinal(self):
        # ordinal_style='all', the basic type in IJP-791 and WIKI-ŘČ
        every = {'to': 'ordinal', 'ordinal_style': 'all'}
        self.check([
            # IJP-791
            (25, every, 'dvacátý pátý'),
            (150, every, 'stý padesátý'),
            (478, every, 'čtyřstý sedmdesátý osmý'),
            (1956, every, 'tisící devítistý padesátý šestý'),
            # WIKI-ŘČ, WIKI-ČČ, IJP:tisíc, CHL (Gebauer)
            (152, every, 'stý padesátý druhý'),
            (215, every, 'dvoustý patnáctý'),
            (368, every, 'třístý šedesátý osmý'),
            (2345, every, 'dvoutisící třístý čtyřicátý pátý'),
            (1520, every, 'tisící pětistý dvacátý'),
            (5205, every, 'pětitisící dvoustý pátý'),
            (1345000, every, 'miliontý tři sta čtyřicet pět tisící'),
            # IJP-791, NESČ
            (25, {'to': 'ordinal', 'inverted': True}, 'pětadvacátý'),
            (21, {'to': 'ordinal', 'inverted': True}, 'jednadvacátý'),
        ])

    def test_compound_ordinals_decline_every_part(self):
        every = {'to': 'ordinal', 'ordinal_style': 'all'}
        self.assertEqual(paradigm(101, gender='feminine', **every),
                         ['stá první', 'sté první', 'sté první',
                          'stou první', 'stou první', 'sté první'])
        self.check([
            # WIKI-ŘČ, SSJČ
            (1875, dict(every, case='genitive'),
             'tisícího osmistého sedmdesátého pátého'),
            (1905, dict(every, case='genitive'),
             'tisícího devítistého pátého'),
            (2024, dict(every, case='genitive'),
             'dvoutisícího dvacátého čtvrtého'),
            (2024, dict(every, case='genitive', gender='feminine'),
             'dvoutisící dvacáté čtvrté'),
        ])

    def test_mixed_ordinal_style_is_the_default(self):
        # chosen in review for years; attested in CHL and WIKI-ŘČ
        self.check([
            (1991, {'to': 'ordinal'}, 'tisíc devět set devadesátý první'),
            (1991, {'to': 'ordinal', 'ordinal_style': 'mixed'},
             'tisíc devět set devadesátý první'),
            # WIKI-ŘČ (Brus 1877), CHL (Sedláček)
            (1875, {'to': 'ordinal', 'case': 'genitive'},
             'tisíc osm set sedmdesátého pátého'),
            (101, {'to': 'ordinal'}, 'sto první'),
            (158, {'to': 'ordinal'}, 'sto padesátý osmý'),
            (365, {'to': 'ordinal'}, 'tři sta šedesátý pátý'),
            (2024, {'to': 'ordinal'}, 'dva tisíce dvacátý čtvrtý'),
            (2024, {'to': 'ordinal', 'case': 'genitive',
                    'gender': 'feminine'}, 'dva tisíce dvacáté čtvrté'),
            # a number of one part stays a single ordinal
            (2000, {'to': 'ordinal'}, 'dvoutisící'),
            (1345000, {'to': 'ordinal'},
             'milion tři sta čtyřicet pět tisící'),
        ])

    def test_decimals(self):
        self.check([
            # IJP-791, HRD
            (0.1, {}, 'nula celá jedna desetina'),
            (0.2, {}, 'nula celá dvě desetiny'),
            (0.5, {}, 'nula celá pět desetin'),
            (0.26, {}, 'nula celá dvacet šest setin'),
            (1.2, {}, 'jedna celá dvě desetiny'),
            (1.9, {}, 'jedna celá devět desetin'),
            (2.3, {}, 'dvě celé tři desetiny'),
            (3.14, {}, 'tři celé čtrnáct setin'),
            (5.1, {}, 'pět celých jedna desetina'),
            (25.4, {}, 'dvacet pět celých čtyři desetiny'),
            (100.6, {}, 'sto celých šest desetin'),
            (103.8, {}, 'sto tři celé osm desetin'),
            (112.5, {}, 'sto dvanáct celých pět desetin'),
            (121.5, {}, 'sto dvacet jedna celá pět desetin'),
            (1000.05, {}, 'tisíc celých pět setin'),
            (1024.007, {}, 'tisíc dvacet čtyři celé sedm tisícin'),
            ('2,5', {}, 'dvě celé pět desetin'),
            (-2.5, {}, 'mínus dvě celé pět desetin'),
            # always the nominative reading (review)
            (2.5, {'case': 'genitive'}, 'dvě celé pět desetin'),
        ])

    def test_number_forms(self):
        self.check([
            # #458: a string with a trailing zero reads as the number
            ('1.50', {}, 'jedna celá pět desetin'),
            (1.5, {}, 'jedna celá pět desetin'),
            (-0.5, {}, 'mínus nula celá pět desetin'),
            (1e-05, {}, 'nula celá jedna stotisícina'),
            (Decimal('1E+3'), {}, 'tisíc'),
            ('-0', {}, 'nula'),
            (-5, {'case': 'genitive'}, 'mínus pěti'),
            # more than six decimal places are read digit by digit
            (0.1234567, {}, 'nula celá jedna dvě tři čtyři pět šest sedm'),
            # integer values keep every option
            (1.0, {'gender': 'masculine', 'case': 'accusative',
                   'animacy': 'animate'}, 'jednoho'),
            (Decimal('5'), {'case': 'genitive'}, 'pěti'),
            ('22', {'construction': 'agreement', 'gender': 'feminine'},
             'dvacet dvě'),
        ])

    def test_range(self):
        self.check([
            (10 ** 24, {}, 'kvadrilion'),
            (2 * 10 ** 27, {}, 'dvě kvadriliardy'),
            (10 ** 30, {}, 'kvintilion'),
            (10 ** 30, {'case': 'genitive'}, 'kvintilionu'),
            (10 ** 30, {'to': 'ordinal'}, 'kvintiliontý'),
            (10 ** 33 - 1, {},
             'devět set devadesát devět kvintilionů '
             'devět set devadesát devět kvadriliard '
             'devět set devadesát devět kvadrilionů '
             'devět set devadesát devět triliard '
             'devět set devadesát devět trilionů '
             'devět set devadesát devět biliard '
             'devět set devadesát devět bilionů '
             'devět set devadesát devět miliard '
             'devět set devadesát devět milionů '
             'devět set devadesát devět tisíc '
             'devět set devadesát devět'),
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
                (ValueError, 5, {'construction': 'type A'}),
                (ValueError, 5, {'oblique_style': 'none'}),
                (ValueError, 5, {'to': 'ordinal', 'gender': None}),
                (ValueError, 5, {'to': 'ordinal', 'ordinal_style': 'last'}),
                (TypeError, 5, {'animate': True}),
                (TypeError, 5, {'to': 'ordinal', 'construction': 'genitive'}),
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
            (1989, {'to': 'year'}, 'tisíc devět set osmdesát devět'),
            (2001, {'to': 'year'}, 'dva tisíce jedna'),
        ])

    def test_currency(self):
        self.assertEqual(
            num2words(10.0, lang='cs', to='currency', currency='EUR'),
            "deset eur, nula centů")
        self.assertEqual(
            num2words(1.0, lang='cs', to='currency', currency='CZK'),
            "jedna koruna, nula haléřů")
        self.assertEqual(
            num2words(1234.56, lang='cs', to='currency', currency='EUR'),
            "tisíc dvě stě třicet čtyři eura, padesát šest centů")
        self.assertEqual(
            num2words(1234.56, lang='cs', to='currency', currency='CZK'),
            "tisíc dvě stě třicet čtyři koruny, padesát šest haléřů")
        self.assertEqual(
            num2words(101.11, lang='cs', to='currency', currency='EUR',
                      separator=' a'),
            "sto jedna eur a jedenáct centů")
        self.assertEqual(
            num2words(101.21, lang='cs', to='currency', currency='CZK',
                      separator=' a'),
            "sto jedna korun a dvacet jedna haléřů"
        )
        self.assertEqual(
            num2words(-12519.85, lang='cs', to='currency', cents=False),
            "mínus dvanáct tisíc pět set devatenáct eur, 85 centů"
        )
        self.assertEqual(
            num2words(123.50, lang='cs', to='currency', currency='CZK',
                      separator=' a'),
            "sto dvacet tři koruny a padesát haléřů"
        )
        self.assertEqual(
            num2words(19.50, lang='cs', to='currency', cents=False),
            "devatenáct eur, 50 centů"
        )
        # the numeral agrees with the noun; IJP:euro: "eur" after 5 and up,
        # IJP:haléř
        self.check([
            (1.01, {'to': 'currency'}, 'jedno euro, jeden cent'),
            (2.02, {'to': 'currency'}, 'dvě eura, dva centy'),
            (5.05, {'to': 'currency'}, 'pět eur, pět centů'),
            (2.02, {'to': 'currency', 'currency': 'CZK'},
             'dvě koruny, dva haléře'),
            (22.22, {'to': 'currency', 'currency': 'CZK'},
             'dvacet dvě koruny, dvacet dva haléře'),
            (21.21, {'to': 'currency', 'currency': 'CZK'},
             'dvacet jedna korun, dvacet jedna haléřů'),
        ])
