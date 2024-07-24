from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, "un"),
    (2, "dos"),
    (3, "tres"),
    (5.5, "cinc punt cinc"),
    (11, "onze"),
    (12, "dotze"),
    (16, "setze"),
    (17.42, "disset punt quatre dos"),
    (19, "dinou"),
    (20, "vint"),
    (21, "vint-i-un"),
    (26, "vint-i-sis"),
    (27.312, "vint-i-set punt tres un dos"),
    (28, "vint-i-vuit"),
    (30, "trenta"),
    (31, "trenta-un"),
    (40, "quaranta"),
    (44, "quaranta-quatre"),
    (50, "cinquanta"),
    (53.486, "cinquanta-tres punt quatre vuit sis"),
    (55, "cinquanta-cinc"),
    (60, "seixanta"),
    (67, "seixanta-set"),
    (70, "setanta"),
    (79, "setanta-nou"),
    (89, "vuitanta-nou"),
    (95, "noranta-cinc"),
    (100, "cent"),
    (101, "cent un"),
    (199, "cent noranta-nou"),
    (203, "dos-cents tres"),
    (287, "dos-cents vuitanta-set"),
    (300.42, "tres-cents punt quatre dos"),
    (356, "tres-cents cinquanta-sis"),
    (400, "quatre-cents"),
    (434, "quatre-cents trenta-quatre"),
    (555, "cinc-cents cinquanta-cinc"),
    (578, "cinc-cents setanta-vuit"),
    (666, "sis-cents seixanta-sis"),
    (689, "sis-cents vuitanta-nou"),
    (729, "set-cents vint-i-nou"),
    (777, "set-cents setanta-set"),
    (888, "vuit-cents vuitanta-vuit"),
    (894, "vuit-cents noranta-quatre"),
    (999, "nou-cents noranta-nou"),
    (1000, "mil"),
    (1001, "mil un"),
    (1097, "mil noranta-set"),
    (1104, "mil cent quatre"),
    (1243, "mil dos-cents quaranta-tres"),
    (2385, "dos mil tres-cents vuitanta-cinc"),
    (3766, "tres mil set-cents seixanta-sis"),
    (4196, "quatre mil cent noranta-sis"),
    (4196.42, "quatre mil cent noranta-sis punt quatre dos"),
    (5846, "cinc mil vuit-cents quaranta-sis"),
    (6459, "sis mil quatre-cents cinquanta-nou"),
    (7232, "set mil dos-cents trenta-dos"),
    (8569, "vuit mil cinc-cents seixanta-nou"),
    (9539, "nou mil cinc-cents trenta-nou"),
    (1000000, "un milió"),
    (1000001, "un milió un"),
    (4000000, "quatre milions"),
    (10000000000000, "deu bilions"),
    (100000000000000, "cent bilions"),
    (1000000000000000000, "un trilió"),
    (1000000000000000000000, "mil trilions"),
    (10000000000000000000000000, "deu quadrilions"),
)

TEST_CASES_ORDINAL = (
    (1, "primer"),
    (2, "segon"),
    (8, "vuitè"),
    (12, "dotzè"),
    (14, "catorzè"),
    (28, "vint-i-vuitè"),
    (33, "trenta-tresè"),
    (88, "vuitanta-vuitè"),
    (100, "centè"),
    (128, "cent vint-i-vuitè"),
    (199, "cent noranta-novè"),
    (1000, "milè"),
    (1827, "mil vuit-cents vint-i-setè"),
    (12345, "dotze mil tres-cents quaranta-cinquè"),
    (1000000, "milionè"),
    (1000000000000000, "mil bilionè"),
    (1000000000000000, "mil bilionè"),
    (1000000000000000000, "un trilionè"),  # over 1e18 is not supported
)

TEST_CASES_ORDINAL_NUM = (
    (1, "1r"),
    (8, "8è"),
    (12, "12è"),
    (14, "14è"),
    (28, "28è"),
    (100, "100è"),
    (1000, "1000è"),
    (1000000, "1000000è"),
)

TEST_CASES_TO_CURRENCY = (
    (1.00, "un euro amb zero cèntims"),
    (1.01, "un euro amb un cèntim"),
    (2.00, "dos euros amb zero cèntims"),
    (8.00, "vuit euros amb zero cèntims"),
    (12.00, "dotze euros amb zero cèntims"),
    (21.00, "vint-i-un euros amb zero cèntims"),
    (81.25, "vuitanta-un euros amb vint-i-cinc cèntims"),
    (350.90, "tres-cents cinquanta euros amb noranta cèntims"),
    (100.00, "cent euros amb zero cèntims"),
)

TEST_CASES_TO_CURRENCY_ESP = (
    (1.00, "una pesseta amb zero cèntims"),
    (1.01, "una pesseta amb un cèntim"),
    (2.00, "dues pessetes amb zero cèntims"),
    (8.00, "vuit pessetes amb zero cèntims"),
    (12.00, "dotze pessetes amb zero cèntims"),
    (21.00, "vint-i-una pessetes amb zero cèntims"),
    (81.25, "vuitanta-una pessetes amb vint-i-cinc cèntims"),
    (350.90, "tres-centes cinquanta pessetes amb noranta cèntims"),
    (100.00, "cent pessetes amb zero cèntims"),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, "un dòlar amb zero centaus"),
    (2.00, "dos dòlars amb zero centaus"),
    (8.00, "vuit dòlars amb zero centaus"),
    (12.00, "dotze dòlars amb zero centaus"),
    (21.00, "vint-i-un dòlars amb zero centaus"),
    (81.25, "vuitanta-un dòlars amb vint-i-cinc centaus"),
    (350.90, "tres-cents cinquanta dòlars amb noranta centaus"),
    (100.00, "cent dòlars amb zero centaus"),
)


TEST_CASES_TO_CURRENCY_GBP = (
    (1.00, "una lliura amb zero penics"),
    (1.01, "una lliura amb un penic"),
    (2.00, "dues lliures amb zero penics"),
    (8.00, "vuit lliures amb zero penics"),
    (12.00, "dotze lliures amb zero penics"),
    (21.00, "vint-i-una lliures amb zero penics"),
    (81.25, "vuitanta-una lliures amb vint-i-cinc penics"),
    (350.90, "tres-centes cinquanta lliures amb noranta penics"),
    (100.00, "cent lliures amb zero penics"),
)


class TestNum2WordsCA(TestCase):
    def _test_cases(self, cases, lang="ca", to="cardinal", **kwargs):
        for case in cases:
            self.assertEqual(num2words(case[0], lang=lang,
                                       to=to, **kwargs), case[1])

    def test_cardinal(self):
        self._test_cases(TEST_CASES_CARDINAL)

    def test_ordinal(self):
        self._test_cases(TEST_CASES_ORDINAL, to="ordinal")

    def test_ordinal_num(self):
        self._test_cases(TEST_CASES_ORDINAL_NUM, to="ordinal_num")

    def test_currency(self):
        self._test_cases(TEST_CASES_TO_CURRENCY, to="currency", currency="EUR")

    def test_currency_esp(self):
        self._test_cases(TEST_CASES_TO_CURRENCY_ESP,
                         to="currency", currency="ESP")

    def test_currency_usd(self):
        self._test_cases(TEST_CASES_TO_CURRENCY_USD,
                         to="currency", currency="USD")

    def test_currency_gbp(self):
        self._test_cases(TEST_CASES_TO_CURRENCY_GBP,
                         to="currency", currency="GBP")
