# encoding: UTF-8

from __future__ import print_function, unicode_literals

from .lang_ES import Num2Word_ES
from .currency import parse_currency_parts, prefix_currency


class Num2Word_ES_PE(Num2Word_ES):
    CURRENCY_FORMS = {
        'PEN': (('sol', 'soles'), ('centimo', 'centimos')),
        'USD': (('dolar americano', 'dolares americanos'), ('centimo', 'centimos'))
    }

    def to_currency(self, val, currency='PEN', cents=True, seperator=' con', adjective=False):
        left, right, is_negative = parse_currency_parts(val, is_int_with_cents=False)

        try:
            cr1, cr2 = self.CURRENCY_FORMS[currency]

        except KeyError:
            raise NotImplementedError(
                'Currency code "%s" not implemented for "%s"' %
                (currency, self.__class__.__name__))

        if adjective and currency in self.CURRENCY_ADJECTIVES:
            cr1 = prefix_currency(self.CURRENCY_ADJECTIVES[currency], cr1)

        minus_str = "%s " % self.negword if is_negative else ""
        if right > 0:
            cents_str = self._cents_verbose(right, currency) \
                if cents else "%02d" % right
            cents_str_currency = "%s %s %s" % (seperator, cents_str, self.pluralize(right, cr2))
        else:
            cents_str_currency = ""

        result = u'%s%s %s%s' % (
            minus_str,
            self.to_cardinal(left),
            self.pluralize(left, cr1),
            cents_str_currency
        )

        # Handle exception, in spanish is "un sol" and not "uno sol"
        return result.replace("uno", "un")