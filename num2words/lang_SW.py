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

ONES_STR = {
    0: 'sifuri',
    1: 'moja',
    2: 'mbili',
    3: 'tatu',
    4: 'nne',
    5: 'tano',
    6: 'sita',
    7: 'saba',
    8: 'nane',
    9: 'tisa',
}

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

EXPONENT_PREFIXES = {
    6: 'm',
    9: 'b',
    12: 'tr',
    15: 'quadr',
    18: 'quint',
    21: 'sext',
    24: 'sept',
    27: 'oct',
    30: 'non',
    33: 'dec',
}


class Num2Word_SW(Num2Word_Base):
    MINUS_PREFIX_WORD = 'hasi '

    def tens_to_cardinal(self, number):
        '''Converts a number less than 100 to a string.'''
        tens = number // 10
        remainder = number % 10

        prefix = TENS_STR[tens]
        postfix = ONES[remainder]

        if remainder == 0:
            return prefix

        return f'{prefix} na {postfix}'

    def hundreds_to_cardinal(self, number):
        '''Converts a number less than 1000 to a string.'''
        hundreds = number // 100
        remainder = number % 100

        if remainder == 0:
            return f'mia {ONES[hundreds]}'
        elif remainder < 10:
            return f'mia {ONES[hundreds]} na {ONES[remainder]}'
        else:
            return f'mia {ONES[hundreds]} {self.tens_to_cardinal(remainder)}'

    def thousands_to_cardinal(self, number):
        '''Converts a number less than 1_000_000 to a string.'''
        thousands = number // 1000
        remainder = number % 1000

        if remainder == 0:
            if thousands < 10:
                # thousands = 1 - 9
                return f'elfu {ONES[thousands]}'
            elif thousands < 100:
                # thousands = 10 - 99
                return f'{self.tens_to_cardinal(thousands)} elfu'
            else:
                # thousands = 100 - 999
                return f'{self.hundreds_to_cardinal(thousands)} elfu'
        elif remainder < 10:
            if thousands < 10:
                # thousands = 1 - 9
                return f'{ONES[thousands]} elfu na {ONES[remainder]}'
            elif thousands < 100:
                # thousands = 10 - 99
                return f'{self.tens_to_cardinal(thousands)} elfu na {ONES[remainder]}'
            elif thousands < 1000:
                # thousands = 100 - 999
                return (
                    f'{self.hundreds_to_cardinal(thousands)} elfu na {ONES[remainder]}'
                )
        elif remainder < 100:
            if thousands < 10:
                # thousands = 1 - 9
                return f'{ONES[thousands]} elfu na {self.tens_to_cardinal(remainder)}'
            elif thousands < 100:
                # thousands = 10 - 99
                return (
                    f'{self.tens_to_cardinal(thousands)} elfu na '
                    f'{self.tens_to_cardinal(remainder)}'
                )
            elif thousands < 1000:
                # thousands = 100 - 999
                return (
                    f'{self.hundreds_to_cardinal(thousands)} elfu, '
                    f'{self.tens_to_cardinal(remainder)}'
                )
        elif remainder < 1000:
            if thousands < 10:
                # thousands = 1 - 9
                return f'{ONES[thousands]} elfu, {self.hundreds_to_cardinal(remainder)}'
            elif thousands < 100:
                # thousands = 10 - 99
                return (
                    f'{self.tens_to_cardinal(thousands)} elfu, '
                    f'{self.hundreds_to_cardinal(remainder)}'
                )
            else:
                # thousands = 100 - 999
                return (
                    f'{self.hundreds_to_cardinal(thousands)} elfu, '
                    f'{self.hundreds_to_cardinal(remainder)}'
                )

    def big_number_to_cardinal(self, number):
        digits = [c for c in str(number)]
        length = len(digits)
        if length >= 66:
            raise NotImplementedError('The given number is too large.')

        predigits = length % 3 or 3
        num = int(''.join(digits[:predigits]))
        if num < 10:
            num_in_words = ONES_STR[num]
        elif num < 100:
            num_in_words = self.tens_to_cardinal(num)
        else:
            num_in_words = self.hundreds_to_cardinal(num)

        word = EXPONENT_PREFIXES[len(digits[predigits:])] + 'ilioni'
        base = f'{num_in_words} {word}'
        number = int(''.join(digits[predigits:]))  # remaining number

        if number == 0:
            return f'{word} {num_in_words}'
        elif number < 10:
            return f'{base} na {ONES[number]}'
        elif number < 100:
            return f'{base} na {self.tens_to_cardinal(number)}'
        elif number < 1000:
            return f'{base}, {self.hundreds_to_cardinal(number)}'
        elif number < 1_000_000:
            return f'{base}, {self.thousands_to_cardinal(number)}'
        else:
            return f'{base}, {self.big_number_to_cardinal(number)}'

    def to_cardinal(self, number):
        if number < 0:
            # negative number
            string = self.MINUS_PREFIX_WORD + self.to_cardinal(-number)
        elif number < 10:
            # 1 - 9
            string = ONES[int(number)]
        elif number < 100:
            # 10 - 99
            string = self.tens_to_cardinal(int(number))
        elif number < 1000:
            # 100 - 999
            string = self.hundreds_to_cardinal(number)
        elif number < 1_000_000:
            # 100 - 999999
            string = self.thousands_to_cardinal(int(number))
        else:
            # 1_000_000 - Infinity
            string = self.big_number_to_cardinal(int(number))
        return string

    def to_ordinal(self, number):
        '''Converts number to ordinal.'''
        if number <= 0:
            raise Exception('number must be greater than zero to convert to ordinal')
        if number == 1:
            return 'kwanza'
        if number == 2:
            return 'pili'
        return self.to_cardinal(number)
