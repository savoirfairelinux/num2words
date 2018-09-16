# encoding: UTF-8

from __future__ import unicode_literals

from num2words import num2words

from . import test_es

TEST_CASES_TO_CURRENCY = (
    (1, 'un sol'),
    (2, 'dos soles'),
    (8, 'ocho soles'),
    (12, 'doce soles'),
    (21, 'veintiun soles'),
    (81.25, 'ochenta y un soles con veinticinco centimos'),
    (81.01, 'ochenta y un soles con un centimo'),
    (81.1, 'ochenta y un soles con diez centimos'),
    (100, 'cien soles'),
)


class Num2WordsESPETest(test_es.Num2WordsESTest):

    def test_number(self):
        for test in test_es.TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='es_PE'), test[1])

    def test_ordinal(self):
        for test in test_es.TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='es_PE', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in test_es.TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='es', to='ordinal_num'),
                test[1]
            )

    def test_currency(self):
        for test in TEST_CASES_TO_CURRENCY:
            self.assertEqual(
                num2words(test[0], lang='es_PE', to='currency'),
                test[1]
            )
