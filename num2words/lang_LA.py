# -*- coding: utf-8 -*-
# Copyright (c) 2026, Piotr Jan Balwierz.  All Rights Reserved.

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

"""Latin (Lingua Latina) cardinal-numeral support.

Latin cardinals are partially declined:

* ``unus`` (1), ``duo`` (2), ``tres`` (3) decline for gender (m/f/n)
  and case (nom/gen/dat/acc/abl/voc).
* Hundreds 200..900 (``ducenti, ducentae, ducenta``; ``trecenti``;
  ...; ``nongenti``) decline like 1st/2nd-declension adjectives.
* Everything else (4..99, 100, 1000) is invariant.
* For 10^3 and above we follow the long-scale Neo-Latin convention
  used in continental scientific writing and Vatican publications:
  ``milia`` (10^3 plural noun, neut.); ``milio`` / ``miliones``
  (10^6); ``miliardus`` / ``miliardi`` (10^9); ``billio`` /
  ``biliones`` (10^12); ``biliardus`` / ``biliardi`` (10^15).

The default citation form is **masculine nominative** (what
dictionaries and grammars list). Two language-specific kwargs let
the caller request a different agreement:

* ``gender``: ``"m"`` (default), ``"f"``, ``"n"``.
* ``case``: ``"nom"`` (default), ``"gen"``, ``"dat"``, ``"acc"``,
  ``"abl"``, ``"voc"``.

By default the output carries Classical-Latin macrons (long-vowel
diacritics, e.g. ``ūnus``, ``trēs``, ``mīlle``, ``vīgintī``). They
distinguish case forms that would otherwise be ambiguous —
e.g. ``ūnā`` (abl.sg.fem.) vs ``ūna`` (nom.sg.fem.). Pass
``macrons=False`` for a plain-ASCII rendering.

Examples::

    >>> from num2words import num2words
    >>> num2words(50, lang='la')
    'quīnquāgintā'
    >>> num2words(50, lang='la', macrons=False)
    'quinquaginta'
    >>> num2words(38_630_666, lang='la', macrons=False)
    'triginta octo miliones sescenta triginta milia sescenti sexaginta sex'
    >>> num2words(1, lang='la', gender='f', case='abl')
    'ūnā'
    >>> num2words(200, lang='la', gender='n', case='abl')
    'ducentīs'
    >>> num2words(2024, lang='la', to='year')
    'duo mīlia vīgintī quattuor'

Ordinals are partially supported: 1st..20th, the decadal forms
(20th, 30th, …, 90th), 100th, 1000th, and a placeholder
``deciēs centiēs mīllēsimus`` for 10^6. Compound ordinals (21st,
33rd, …) fall back to the cardinal form.
"""
from __future__ import print_function, unicode_literals

from .base import Num2Word_Base

# ── declension data ─────────────────────────────────────────────────────────
#
# Each declined cardinal carries up to 18 forms: 3 genders × 6 cases.
# Storage layout: `_DECL[n][gender][case]` → form string.
# Gender keys: "m", "f", "n". Case keys: "nom", "gen", "dat", "acc",
# "abl", "voc".
#
# For 1 the singular forms are used; for 2, 3 and the hundreds, the
# plural forms (in the case of 1 the cardinal modifies a singular
# noun; in the case of 2+ it modifies a plural noun — except when 1
# appears inside a higher group, e.g. "1 million" → "unus milio"
# where "unus" agrees with masc.sg. "milio").

# Tables carry the macron-bearing forms (long-vowel diacritics)
# used in modern Classical-Latin orthography. Macrons distinguish
# otherwise-identical case forms (e.g. ``ūnā`` abl.sg.fem. vs ``ūna``
# nom.sg.fem.). Pass ``macrons=False`` to strip them and get plain
# ASCII output.

_DECL_1 = {
    "m": {"nom": "ūnus", "gen": "ūnīus", "dat": "ūnī", "acc": "ūnum",
          "abl": "ūnō",  "voc": "ūne"},
    "f": {"nom": "ūna",  "gen": "ūnīus", "dat": "ūnī", "acc": "ūnam",
          "abl": "ūnā",  "voc": "ūna"},
    "n": {"nom": "ūnum", "gen": "ūnīus", "dat": "ūnī", "acc": "ūnum",
          "abl": "ūnō",  "voc": "ūnum"},
}

_DECL_2 = {
    "m": {"nom": "duo",     "gen": "duōrum", "dat": "duōbus",
          "acc": "duōs",    "abl": "duōbus", "voc": "duo"},
    "f": {"nom": "duae",    "gen": "duārum", "dat": "duābus",
          "acc": "duās",    "abl": "duābus", "voc": "duae"},
    "n": {"nom": "duo",     "gen": "duōrum", "dat": "duōbus",
          "acc": "duo",     "abl": "duōbus", "voc": "duo"},
}

_DECL_3 = {
    "m": {"nom": "trēs", "gen": "trium", "dat": "tribus",
          "acc": "trēs", "abl": "tribus", "voc": "trēs"},
    "f": {"nom": "trēs", "gen": "trium", "dat": "tribus",
          "acc": "trēs", "abl": "tribus", "voc": "trēs"},
    "n": {"nom": "tria", "gen": "trium", "dat": "tribus",
          "acc": "tria", "abl": "tribus", "voc": "tria"},
}

_DECLINED_LOW = {1: _DECL_1, 2: _DECL_2, 3: _DECL_3}


def _hundred_paradigm(stem):
    """Build the 3-gender × 6-case table for a 200..900 cardinal.

    All of them decline like 1st/2nd-declension adjectives in the
    plural — ``ducentī, ducentae, ducenta`` etc. The endings carry
    macrons (long ī / ō / ā) wherever Classical orthography has them.
    """
    return {
        "m": {"nom": stem + "ī",   "gen": stem + "ōrum", "dat": stem + "īs",
              "acc": stem + "ōs",  "abl": stem + "īs",   "voc": stem + "ī"},
        "f": {"nom": stem + "ae",  "gen": stem + "ārum", "dat": stem + "īs",
              "acc": stem + "ās",  "abl": stem + "īs",   "voc": stem + "ae"},
        "n": {"nom": stem + "a",   "gen": stem + "ōrum", "dat": stem + "īs",
              "acc": stem + "a",   "abl": stem + "īs",   "voc": stem + "a"},
    }


# Hundreds stems carry macrons where the stem itself has a long
# vowel (e.g. ``quīngent-``, ``nōngent-``).
_HUNDREDS = {
    2: _hundred_paradigm("ducent"),
    3: _hundred_paradigm("trecent"),
    4: _hundred_paradigm("quadringent"),
    5: _hundred_paradigm("quīngent"),
    6: _hundred_paradigm("sescent"),
    7: _hundred_paradigm("septingent"),
    8: _hundred_paradigm("octingent"),
    9: _hundred_paradigm("nōngent"),
}


_UNDER_20_INVARIANT = {
    4: "quattuor",  5: "quīnque",  6: "sex",        7: "septem",
    8: "octō",      9: "novem",   10: "decem",     11: "ūndecim",
    12: "duodecim", 13: "tredecim", 14: "quattuordecim",
    15: "quīndecim", 16: "sēdecim", 17: "septendecim",
    18: "duodēvīgintī", 19: "ūndēvīgintī",
}

_TENS_INVARIANT = {
    2: "vīgintī",       3: "trīgintā",    4: "quadrāgintā",
    5: "quīnquāgintā",  6: "sexāgintā",   7: "septuāgintā",
    8: "octōgintā",     9: "nōnāgintā",
}


# ── thousands / millions / etc. ─────────────────────────────────────────────
#
# "mille" (10^3 exactly) is indeclinable; for 2000+ the noun is
# "milia" (neut. pl.). Its case forms (used by callers requesting
# anything other than nominative for the whole number):

_MILIA_DECL = {
    # neut. pl. only — gender is fixed. Long ī throughout, matching
    # the singular ``mīlle``.
    "nom": "mīlia",  "gen": "mīlium", "dat": "mīlibus",
    "acc": "mīlia",  "abl": "mīlibus", "voc": "mīlia",
}

# The 10^(6n) and 10^(6n+3) families. Each entry: (sg.nom, pl.nom,
# gender, sg.gen, pl.gen, sg.abl, pl.abl). For brevity we store the
# common cases the caller is likely to use; less-common cases fall
# back to the nominative form.
#
# Long scale (Neo-Latin / European convention):
#   10^6:  milio       (3rd-decl. masc.)   pl miliones
#   10^9:  miliardus   (2nd-decl. masc.)   pl miliardi
#   10^12: billio      (3rd-decl. masc.)   pl biliones
#   10^15: biliardus   (2nd-decl. masc.)   pl biliardi


def _milio_like(stem):
    """3rd-declension masculine: stem → stem + 'o' (sg.) / 'ones' (pl.)."""
    return {
        "gender": "m",
        "sg": {"nom": stem + "o",   "gen": stem + "onis", "dat": stem + "oni",
               "acc": stem + "onem", "abl": stem + "one",  "voc": stem + "o"},
        "pl": {"nom": stem + "ones", "gen": stem + "onum",
               "dat": stem + "onibus", "acc": stem + "ones",
               "abl": stem + "onibus", "voc": stem + "ones"},
    }


def _miliardus_like(stem):
    """2nd-declension masculine: stem → stem + 'us' / 'i'."""
    return {
        "gender": "m",
        "sg": {"nom": stem + "us", "gen": stem + "i",   "dat": stem + "o",
               "acc": stem + "um", "abl": stem + "o",   "voc": stem + "e"},
        "pl": {"nom": stem + "i",  "gen": stem + "orum", "dat": stem + "is",
               "acc": stem + "os", "abl": stem + "is",   "voc": stem + "i"},
    }


# Mapping from the 10^k exponent to its noun paradigm.
_HIGH_UNITS = {
    1_000_000:             _milio_like("mili"),         # milio / miliones
    1_000_000_000:         _miliardus_like("miliard"),  # miliardus / miliardi
    1_000_000_000_000:     _milio_like("billi"),         # billio / billiones
    1_000_000_000_000_000: _miliardus_like("billiard"),  # billiardus, -i
}

# Iterated in descending order when splitting a number.
_HIGH_POWERS = sorted(_HIGH_UNITS, reverse=True)


# ── ordinal data (basic subset) ──────────────────────────────────────────────
#
# Ordinals decline as 1st/2nd-declension adjectives. We expose only
# the masc.nom.sg. citation form here; callers needing other forms
# can apply standard 1st/2nd-decl. endings to the stem (drop the
# final "us"/"um" → add -i / -o / -um / -a / -ae / …).

_ORDINALS_LOW = {
    1: "prīmus",       2: "secundus",      3: "tertius",
    4: "quārtus",      5: "quīntus",       6: "sextus",
    7: "septimus",     8: "octāvus",       9: "nōnus",
    10: "decimus",     11: "ūndecimus",    12: "duodecimus",
    13: "tertius decimus",  14: "quārtus decimus",
    15: "quīntus decimus",  16: "sextus decimus",
    17: "septimus decimus", 18: "duodēvīcēsimus",
    19: "ūndēvīcēsimus",
    20: "vīcēsimus",     30: "trīcēsimus",   40: "quadrāgēsimus",
    50: "quīnquāgēsimus", 60: "sexāgēsimus", 70: "septuāgēsimus",
    80: "octōgēsimus",   90: "nōnāgēsimus",
    100: "centēsimus",   200: "ducentēsimus",
    300: "trecentēsimus", 400: "quadringentēsimus",
    500: "quīngentēsimus", 600: "sescentēsimus",
    700: "septingentēsimus", 800: "octingentēsimus",
    900: "nōngentēsimus",
    1000: "mīllēsimus",  1_000_000: "deciēs centiēs mīllēsimus",
}


# ── helpers ─────────────────────────────────────────────────────────────────


def _form(n, gender, case):
    """Look up the inflected form for a small declined cardinal
    (1, 2, 3 or 200..900). Caller must guarantee `n` is in the table."""
    if n in _DECLINED_LOW:
        return _DECLINED_LOW[n][gender][case]
    return _HUNDREDS[n // 100][gender][case]


def _low(n, gender, case):
    """Cardinal 1..19 (or 0 → empty)."""
    if n == 0:
        return ""
    if n in _DECLINED_LOW:
        return _form(n, gender, case)
    return _UNDER_20_INVARIANT[n]


def _under_1000(n, gender, case):
    """Cardinal 0..999. Form-sensitive only for 1, 2, 3 and 200..900."""
    if n == 0:
        return ""
    if n < 0 or n >= 1000:
        raise ValueError(
            "_under_1000 expects 0..999, got %d" % n
        )
    h, rest = divmod(n, 100)
    t, u = divmod(rest, 10)
    parts = []
    if h:
        if h == 1:
            parts.append("centum")    # indeclinable in singular
        else:
            parts.append(_form(h * 100, gender, case))
    if rest == 0:
        pass
    elif rest <= 19:
        parts.append(_low(rest, gender, case))
    else:
        if t:
            parts.append(_TENS_INVARIANT[t])
        if u:
            parts.append(_low(u, gender, case))
    return " ".join(parts)


# ── public API ──────────────────────────────────────────────────────────────


class Num2Word_LA(Num2Word_Base):
    """Latin (la). Cardinals fully supported across 3 genders × 6
    cases for the declined forms (1, 2, 3, 200..900); higher
    invariant cardinals are returned as-is.

    The default citation form is **masculine nominative**, matching
    standard Latin grammars and dictionaries.
    """

    # Generous cap so we can grow without rewriting; chosen to be
    # one more than the largest cardinal we can spell with the
    # current `_HIGH_UNITS` table (10^18 = quintilion in long scale).
    MAXVAL = 10 ** 18

    # Maximum value the long-scale table can spell as words.
    # Numbers >= MAXVAL_WORDS raise OverflowError below.
    MAXVAL_WORDS = 10 ** 18

    def __init__(self):
        super(Num2Word_LA, self).__init__()

    def setup(self):
        self.negword = "minus "
        self.pointword = "virgula"     # "little rod" — comma / decimal point
        self.errmsg_nonnum = "Sōlum numerī verbīs exprimī possunt."
        self.errmsg_floatord = (
            "Numerus frāctus %s ōrdinālis fierī nōn potest."
        )
        self.errmsg_negord = (
            "Numerus negātīvus %s ōrdinālis fierī nōn potest."
        )
        self.errmsg_toobig = "abs(%s) maius esse nōn dēbet quam %s."
        self.exclude_title = ["et", "minus", "virgula"]

    # The base class only sets up `cards` when high/mid/low_numwords
    # are defined on the subclass. We bypass that machinery and
    # implement `to_cardinal` directly.

    # ── macron handling ─────────────────────────────────────────────────
    #
    # Tables carry the macron-bearing forms (Classical-Latin
    # orthography). `_apply_macrons(s, True)` returns the string
    # as-is; `_apply_macrons(s, False)` strips macrons to plain ASCII.

    _MACRON_STRIP = str.maketrans({
        "ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u",
        "Ā": "A", "Ē": "E", "Ī": "I", "Ō": "O", "Ū": "U",
        # Less common but worth covering for completeness:
        "ȳ": "y", "Ȳ": "Y",
    })

    @classmethod
    def _apply_macrons(cls, s, macrons):
        if macrons:
            return s
        return s.translate(cls._MACRON_STRIP)

    # ── to_cardinal ─────────────────────────────────────────────────────

    def to_cardinal(self, value, gender="m", case="nom", macrons=True):
        """Return the Latin cardinal for `value`.

        `gender`: ``"m"``, ``"f"`` or ``"n"``. Only affects the
        declined cardinals (1, 2, 3, 200..900).
        `case`:   ``"nom"``, ``"gen"``, ``"dat"``, ``"acc"``,
        ``"abl"`` or ``"voc"``. Same.
        `macrons`: ``True`` (default) emits Classical orthography
        with long-vowel diacritics (``ūnus``, ``trēs``, ``mīlle``…).
        ``False`` strips them to plain ASCII.
        """
        try:
            if int(value) != value:
                return self._apply_macrons(
                    self.to_cardinal_float(value), macrons
                )
        except (ValueError, TypeError):
            return self._apply_macrons(
                self.to_cardinal_float(value), macrons
            )

        gender, case = self._normalize_grammar(gender, case)

        if value < 0:
            inner = self.to_cardinal(
                -value, gender=gender, case=case, macrons=True
            )
            return self._apply_macrons(
                self.negword.strip() + " " + inner, macrons
            )
        if value >= self.MAXVAL_WORDS:
            raise OverflowError(
                self.errmsg_toobig % (value, self.MAXVAL_WORDS)
            )
        return self._apply_macrons(
            self._to_cardinal_pos(int(value), gender, case), macrons
        )

    def _normalize_grammar(self, gender, case):
        if gender not in ("m", "f", "n"):
            raise ValueError(
                "gender must be 'm', 'f' or 'n'; got %r" % gender
            )
        if case not in ("nom", "gen", "dat", "acc", "abl", "voc"):
            raise ValueError(
                "case must be one of nom/gen/dat/acc/abl/voc; got %r" % case
            )
        return gender, case

    def _to_cardinal_pos(self, n, gender, case):
        """Compose the cardinal for a non-negative integer < MAXVAL_WORDS."""
        if n == 0:
            # "nullus" (m), "nulla" (f), "nullum" (n) — 1st/2nd-decl. adj.
            # Decline like a regular -us/-a/-um adjective.
            return self._zero(gender, case)
        if n == 1:
            return _form(1, gender, case)

        parts = []
        rest = n
        # Compose high-units in descending power.
        for power in _HIGH_POWERS:
            count, rest = divmod(rest, power)
            if count == 0:
                continue
            unit = _HIGH_UNITS[power]
            number_form = "sg" if count == 1 else "pl"
            unit_word = unit[number_form]["nom"]
            unit_gender = unit["gender"]
            if count == 1:
                # "unus" agrees with the singular noun.
                modifier = _form(1, unit_gender, "nom")
                parts.append(modifier + " " + unit_word)
            else:
                # The modifier is a 1..999 cardinal in the unit's gender,
                # nominative case (it's the subject of the noun phrase).
                modifier = _under_1000(count, unit_gender, "nom")
                parts.append(modifier + " " + unit_word)

        # The thousands position (10^3) is special:
        #   1000  → "mīlle" (indeclinable)
        #   2000+ → "[neut.pl. cardinal] mīlia"  (with mīlia in `case`)
        thousands, rest = divmod(rest, 1000)
        if thousands == 1:
            parts.append("mīlle")
        elif thousands >= 2:
            modifier = _under_1000(thousands, "n", "nom")
            parts.append(modifier + " " + _MILIA_DECL[case])

        # The final 1..999 modifies the implicit/explicit noun the
        # whole numeral describes — caller-supplied gender + case.
        if rest > 0:
            parts.append(_under_1000(rest, gender, case))

        return " ".join(parts)

    def _zero(self, gender, case):
        """Decline 'nullus, nulla, nullum' like a 1st/2nd-decl. adjective."""
        endings = {
            "m": {"nom": "nullus", "gen": "nullius", "dat": "nulli",
                  "acc": "nullum", "abl": "nullo",   "voc": "nulle"},
            "f": {"nom": "nulla",  "gen": "nullius", "dat": "nulli",
                  "acc": "nullam", "abl": "nulla",   "voc": "nulla"},
            "n": {"nom": "nullum", "gen": "nullius", "dat": "nulli",
                  "acc": "nullum", "abl": "nullo",   "voc": "nullum"},
        }
        return endings[gender][case]

    # ── to_ordinal ──────────────────────────────────────────────────────

    def to_ordinal(self, value, gender="m", case="nom", macrons=True):
        """Return the Latin ordinal for `value` (masc.nom.sg. by default).

        Coverage: 1..20, 30, 40, ..., 90, 100, 200, ..., 900, 1000,
        10^6 (a placeholder Roman-style ``decies centies millesimus``).
        Compound ordinals (e.g. 21st, 33rd) currently fall back to
        the cardinal form — Latin grammar allows both
        ``unus et vicesimus`` and ``vicesimus primus`` so an
        unambiguous algorithm is debatable.

        The returned form is the masculine nominative singular stem.
        Decline to other genders / cases by changing the ending
        following the standard 1st/2nd-declension paradigm.
        """
        self.verify_ordinal(value)
        n = int(value)
        if n in _ORDINALS_LOW:
            stem = _ORDINALS_LOW[n]
        else:
            return self.to_cardinal(
                n, gender=gender, case=case, macrons=macrons,
            )
        # Decline the stem from masc.nom.sg ("-us"/"-um") to the
        # requested gender/case using 1st/2nd-decl. paradigm.
        return self._apply_macrons(
            self._decline_us_um_adj(stem, gender, case), macrons
        )

    def to_ordinal_num(self, value):
        """Roman numeral for the ordinal (e.g. 4 → 'IV')."""
        self.verify_ordinal(value)
        return _to_roman(int(value))

    def _decline_us_um_adj(self, stem, gender, case):
        """Decline a 1st/2nd-decl. adjective from its masc.nom.sg.
        citation form ("primus", "secundus", ...) to any other slot.
        Handles single-word stems only; compound forms (e.g.
        "tertius decimus") get the first word inflected.
        """
        if gender == "m" and case == "nom":
            return stem
        head, _, tail = stem.partition(" ")
        if tail:
            return self._decline_us_um_adj(head, gender, case) + " " + \
                self._decline_us_um_adj(tail, gender, case)
        if stem.endswith("us"):
            base = stem[:-2]
        elif stem.endswith("um"):
            base = stem[:-2]
        else:
            return stem    # invariant — shouldn't happen in our tables
        # 1st/2nd-decl. adjective endings with Classical macrons:
        #   m.gen / n.gen: -ī (long)        m.dat / n.dat: -ō (long)
        #   m.abl / n.abl: -ō (long)        f.abl: -ā (long)
        # Other endings have short vowels (or are diphthongs / closed
        # syllables) — left without diacritics.
        endings = {
            "m": {"nom": "us", "gen": "ī",  "dat": "ō",  "acc": "um",
                  "abl": "ō",  "voc": "e"},
            "f": {"nom": "a",  "gen": "ae", "dat": "ae", "acc": "am",
                  "abl": "ā",  "voc": "a"},
            "n": {"nom": "um", "gen": "ī",  "dat": "ō",  "acc": "um",
                  "abl": "ō",  "voc": "um"},
        }
        return base + endings[gender][case]

    # ── to_year ─────────────────────────────────────────────────────────

    def to_year(self, value, macrons=True, **kwargs):
        """Latin years are normally spelled as full cardinals
        (masc.nom.sg.). Negative years are prefixed with ``ante
        Chrīstum`` (BC); the absolute year follows."""
        n = int(value)
        if n < 0:
            body = "ante Chrīstum " + self.to_cardinal(-n, macrons=True)
            return self._apply_macrons(body, macrons)
        return self.to_cardinal(n, macrons=macrons)


# ── tiny Roman-numeral helper, used by to_ordinal_num ───────────────────────


_ROMAN_TABLE = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100,  "C"), (90,  "XC"), (50,  "L"), (40,  "XL"),
    (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
    (1,    "I"),
)


def _to_roman(n):
    if n <= 0 or n >= 4000:
        # Romans didn't standardise notation above 3999 ("MMMCMXCIX").
        # Fall back to plain digits rather than guess (overlines etc.
        # aren't representable in plain ASCII).
        return str(n)
    out = []
    for v, sym in _ROMAN_TABLE:
        while n >= v:
            out.append(sym)
            n -= v
    return "".join(out)
