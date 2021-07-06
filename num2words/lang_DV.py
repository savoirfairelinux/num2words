from decimal import BasicContext, Decimal, InvalidOperation, ROUND_FLOOR, getcontext, localcontext
import decimal
from itertools import tee
from collections import OrderedDict


class Num2Word_DV:
    def __init__(self):
        
        self.negword = "މައިނަސް"
        self.pointword = "ޕޮއިންޓް"
        self.ordword = "ވަނަ"
        self.bcword = "ބީ.ސީ"
        self.base_stem = {
            0: "ސުން",
            1: "އެއް",
            2: "ދެ",
            3: "ތިން",
            4: "ހަތަރު",
            5: "ފަސް",
            6: "ހަ",
            7: "ހަތް",
            8: "އައް",
            9: "ނުވަ",
            10: "ދިހަ",
            100: "ސަތޭކަ",
            200: "ދުއިސައްތަ"
        }

        self.cards = OrderedDict()
        self.high_numwords = [
            "ނޮނިލި",
            "އޮކްޓިލި",
            "ސެޕްޓިލި",
            "ސެކްސްޓިލި",
            "ކުއިންޓިލި",
            "ކުއަޑްރި",
            "ޓްރި",
            "ބިލި",
            "މިލި"
        ]
        self.set_high_numwords(self.high_numwords)
        self.cards[100000] = "ލައްކަ"
        self.cards[1000] = "ހާސް"

        self.MAXVAL = Decimal(list(self.cards.keys())[0] * 1000)
        #getcontext().prec = 34
        #getcontext().rounding = ROUND_FLOOR

        self.grouping = [-3, -5] + [(x*3 + 6)*-1 for x in range(len(self.cards))] 

        self.base_nominal = {
            0: "ސުމެއް",
            1: "އެކެއް",
            2: "ދޭއް",
            3: "ތިނެއް",
            4: "ހަތަރެއް",
            5: "ފަހެއް",
            6: "ހައެއް",
            7: "ހަތެއް",
            8: "އަށެއް",
            9: "ނުވައެއް",
            10: "ދިހައެއް",
            11: "އެގާރަ",
            12: "ބާރަ",
            13: "ތޭރަ",
            14: "ސައުދަ",
            15: "ފަނަރަ",
            16: "ސޯޅަ",
            17: "ސަތާރަ",
            18: "އަށާރަ",
            19: "ނަވާރަ",
            20: "ވިހި",
            21: "އެކާވީސް",
            22: "ބާވީސް",
            23: "ތޭވީސް",
            24: "ސައުވީސް",
            25: "ފަންސަވީސް",
            26: "ސައްބީސް",
            27: "ހަތާވީސް",
            28: "އަށާވީސް",
            29: "ނަވާވީސް",
            30: "ތިރީސް",
            40: "ސާޅީސް",
            50: "ފަންސާސް",
            60: "ފަސްދޮޅަސް",
            70: "ހަތްދިހަ",
            80: "އައްޑިހަ",
            90: "ނުވަދިހަ",
        }
        self.errmsg_nonnum = "{} is not a valid value."
        self.errmsg_floatord = "Cannot treat float {} as ordinal."
        self.errmsg_negord = "Cannot treat negative num {} as ordinal."
        self.errmsg_toobig = "abs({}) must be less than {}."


    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10 ** n] = word + "ޔަން"


    def pairwise(self, iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = tee(iterable)
        next(b, 0)
        return zip(a, b)


    def convert_decade2nominal(self, decade):
        return self.base_nominal[int(decade) * 10]


    def convert_decade2stem(self, decade):
        if int(decade) == 1:
            return self.base_stem[10]
        return self.convert_decade2nominal(decade)


    def convert_two2nominal(self, digits_str):
        if int(digits_str) < 30:
            return self.base_nominal[int(digits_str)]

        if int(digits_str[1]) == 0:
            return self.convert_decade2stem(digits_str[0])
        
        return self.convert_decade2stem(digits_str[0]) + self.base_nominal[int(digits_str[1])]


    def convert_two2stem(self, digits_str):
        digits_str = str(int(digits_str)) #trim leading zeros
    
        if int(digits_str) < 11:
            return self.base_stem[int(digits_str)]

        if int(digits_str) < 30:
            return self.base_nominal[int(digits_str)]

        if int(digits_str[1]) == 0:
            return self.convert_decade2stem(digits_str[0])

        return self.convert_decade2stem(digits_str[0]) + self.base_stem[int(digits_str[1])]


    def convert_three2stem(self, digits_str):
        digits_str = str(int(digits_str)) #trim leading zeros

        if len(digits_str) < 3:
            return self.convert_two2stem(digits_str)

        if int(digits_str[0]) == 1:
            if int(digits_str[1:3]) == 0:
                return self.base_stem[100]
            return self.base_stem[100] + self.convert_two2stem(digits_str[1:3])

        if int(digits_str[0]) == 2:
            if int(digits_str[1:3]) == 0:
                return self.base_stem[200]
            return self.base_stem[200] + self.convert_two2stem(digits_str[1:3])

        if int(digits_str[1:3]) == 0:
            return self.convert_two2stem(digits_str[0]) + self.base_stem[100]

        return self.convert_two2stem(digits_str[0]) + self.base_stem[100] + " " + self.convert_two2stem(digits_str[1:3])


    def convert_three2nominal(self, digits_str):
        digits_str = str(int(digits_str)) #trim leading zeros

        if len(digits_str) < 3:
            return self.convert_two2nominal(digits_str)

        if int(digits_str[0]) == 1:
            if int(digits_str[1:3]) == 0:
                return self.base_stem[100]
            return self.base_stem[100] + self.convert_two2nominal(digits_str[1:3])

        if int(digits_str[0]) == 2:
            if int(digits_str[1:3]) == 0:
                return self.base_stem[200]
            return self.base_stem[200] + self.convert_two2nominal(digits_str[1:3])

        if int(digits_str[1:3]) == 0:
            return self.convert_two2nominal(digits_str[0]) + self.base_stem[100]

        return self.convert_two2stem(digits_str[0]) + self.base_stem[100] + " " + self.convert_two2nominal(digits_str[1:3])



    def convert_discrete(self, digits, nominal):
        if not nominal:
            return " ".join(
                [self.base_stem[d] for d in digits]
            )
        return " ".join(
            [self.base_nominal[d] for d in digits]
        )


    def convert_int(self, digits, nominal=True):
        digits_str = "".join([str(d) for d in digits])

        if digits_str == "0":
            if not nominal:
                return self.base_stem[0]
            return self.base_nominal[0]

        parts = list(filter(lambda x: x, (
            digits_str[start:end]
            for end, start 
            in self.pairwise([len(digits_str)] + self.grouping)
        )))

        part_words = [
            self.convert_three2stem(num) + word
            for
                num, (base, word)
            in zip(
                parts[1:],
                reversed(self.cards.items())
            )
            if int(num) != 0
        ]

        part_words.reverse()

        if int(parts[0]) == 0:
            return " ".join(part_words)

        if not nominal:
            return " ".join(part_words) + " " + self.convert_three2stem(parts[0])    

        return " ".join(part_words) + " " + self.convert_three2nominal(parts[0])
 
    
    def to_decimal(self, value):
        if isinstance(value, float):
            #This is to fix rounding error when directly converting floats to
            #Decimal 12.51 to 12.509999....
            value = str(value)
        try:
            return Decimal(value)
        except InvalidOperation:
            raise TypeError(self.errmsg_nonnum.format(value))


    def to_cardinal_float(self, value, nominal=True):
        decimal_value = self.to_decimal(value)

        if Decimal(self.MAXVAL).compare(abs(decimal_value).to_integral(ROUND_FLOOR)) < 1:
            raise OverflowError(self.errmsg_toobig.format(decimal_value, self.MAXVAL))

        sign, digits, exponent = decimal_value.as_tuple()
        
        result = []

        if exponent < 0:
            result = " ".join([
                self.convert_int(digits[:exponent]),
                self.pointword,
                self.convert_discrete(digits[exponent:len(digits)], nominal)
            ])
        else:
            result = self.convert_int(digits, nominal)

        if sign == 1:
            return " ".join([
                self.negword,
                result
            ])
        return result.strip()


    def verify_ordinal(self, value):
        if not value == int(value):
            raise TypeError(self.errmsg_floatord.format(value))
        if not abs(value) == value:
            raise TypeError(self.errmsg_negord.format(value))

    
    def to_cardinal(self, value, nominal=True):
        return self.to_cardinal_float(value, nominal)


    def to_ordinal(self, value):
        self.verify_ordinal(value)
        return self.to_cardinal_float(value, nominal=False) + " " + self.ordword


    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "{} {}".format(value, self.ordword)


    def to_year(self, value, suffix=""):
        if value < 0:
            value = abs(value)
            suffix = self.bcword if not suffix else suffix
        high, low = (value // 100, value % 100)
        if value < 2000 and value > 1000:
            return " ".join([
                self.to_cardinal(high),
                "ސަތޭކަ",
                " ",
                self.to_cardinal(low),
                suffix
            ])
        return " ".join([
            self.to_cardinal(value),
            suffix
        ])


    def to_currency(self, value, currency="ރުފިޔާ", cents="ލާރި"):
        return self.to_cardinal(value)


    def str_to_number(self, string):
        return self.to_decimal(string)
