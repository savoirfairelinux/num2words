from num2words.base import Num2Word_Base

ONES = [
    'sifuri',
    'moja',
    'mbili',
    'tatu',
    'nne',
    'tano',
    'sita',
    'saba',
    'nane',
    'tisa',
]

TENS_STR = {
    1: 'kumi',
    2: 'ishirini',
    3: 'thelathini',
    4: 'arobaini',
    5: 'hamsini',
    6: 'sitini',
    7: 'sabini',
    8: 'themanini',
    9: 'tisini',
}


class Num2Word_SW(Num2Word_Base):
    MINUS_PREFIX_WORD = 'hasi '

    def tens_to_cardinal(self, number):
        tens = number // 10
        units = number % 10

        if tens in TENS_STR:
            prefix = TENS_STR[tens]

        postfix = ONES[units]

        if units == 0:
            return prefix

        return f'{prefix} na {postfix}'

    def hundreds_to_cardinal(self, number):
        hundreds = number // 100
        remainder = number % 100

        if remainder == 0:
            return f'mia {ONES[hundreds]}'
        elif remainder < 10:
            return f'mia {ONES[hundreds]} na {ONES[remainder]}'
        elif remainder < 100:
            return f'mia {ONES[hundreds]} {self.tens_to_cardinal(remainder)}'

    def thousands_to_cardinal(self, number):
        thousands = number // 1000
        remainder = number % 1000

        if remainder == 0:
            return f'elfu {ONES[thousands]}'
        elif remainder < 10:
            return f'{ONES[thousands]} elfu na {ONES[remainder]}'
        elif remainder < 100:
            return f'{ONES[thousands]} elfu na {self.tens_to_cardinal(remainder)}'
        elif remainder < 1000:
            return f'{ONES[thousands]} elfu, {self.hundreds_to_cardinal(remainder)}'

    def to_cardinal(self, number):
        if number < 0:
            string = self.MINUS_PREFIX_WORD + self.to_cardinal(-number)
        elif number < 10:
            string = ONES[number]
        elif number < 100:
            string = self.tens_to_cardinal(number)
        elif number < 1000:
            string = self.hundreds_to_cardinal(number)
        elif number < 10_000:
            string = self.thousands_to_cardinal(number)
        return string
