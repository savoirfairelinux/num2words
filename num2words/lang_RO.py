import num2words
import num2words.lang_EU

class Num2Word_RO(num2words.lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        max = 3 + 3*len(high)
        for word, n in zip(high, list(range(max, 3, -3))):
            self.cards[10**n] = word + "ilion"

    def setup(self):
        self.negword = "minus "
        self.pointword = "punct"
        self.errmsg_nornum = "Only numbers may be converted to words."
        self.exclude_title = ["si", "punct", "minus"]

        self.mid_numwords = [(1000000, "milio/n/ane"), (1000, "mi/e/i"), (100, "sut/a/e"),
                             (90, "nouazeci"), (80, "optzeci"), (70, "saptezeci"),
                             (60, "saizeci"), (50, "cincizeci"), (40, "patruzeci"),
                             (30, "treizeci"), (20, "douazeci")]
        self.low_numwords = ["douazeci", "nouasprezece", "optisprezece", "saptisprezece",
                             "saisprezece", "cincisprezece", "paisprezece", "treisprezece",
                             "doisprezece", "unsprezece", "zece", "noua", "opt",
                             "sapte", "sase", "cinci", "patru", "trei", "doi",
                             "unu", "zero"]
        self.ords = { "unu"    : "primul",
                      "doi"    : "al doilea",
                      "trei"   : "al treilea",
                      "cinci"  : "al patrulea",
                      "opt"  : "al optulea",
                      "noua"   : "al noualea",
                      "doisprezece" : "al doisprezecelea" }
        self._ro_feminine = { "unu": "una", "doi": "doua" }
        self._ro_short = {'unu': 'un', 'una': 'o'}
        self._ro_should_feminine = [1000, 100]

    def merge(self, xxx_todo_changeme, xxx_todo_changeme1):
        (ltext, lnum) = xxx_todo_changeme
        (rtext, rnum) = xxx_todo_changeme1
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum :
            return ("%s si %s"%(ltext, rtext), lnum + rnum)
        # elif lnum >= 100 > rnum:
        #     return ("%s si %s"%(ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            # turn left into feminine
            if rnum in self._ro_should_feminine:
                ltext_split = ltext.split(' ')
                ltext = ' '.join(ltext_split[:-1] + [self.to_feminine(ltext_split[-1])])
            ret = "%s %s"%(self.to_shortened(ltext), self.inflect(lnum, rtext)), lnum * rnum
            return ret
        return ("%s %s"%(ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 1:
            return "primul"
        word = self.to_cardinal(value)
        return "al " + word + "lea"


    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s"%(value, self.to_ordinal(value)[-2:])


    def to_year(self, val, longval=True):
	return self.to_cardinal(val)

    def to_currency(self, val, longval=True, hightxt="le/u/i", lowtxt="ban/i", divisor=100,
                    high_feminine=False, low_feminine=False):
        return self.to_splitnum(val, hightxt=hightxt, lowtxt=lowtxt,
                                jointxt="si", longval=longval, cents = True, divisor=divisor,
                                high_feminine=high_feminine, low_feminine=low_feminine)

    def to_shortened(self, value):
        return self._ro_short.get(value, value)

    def to_feminine(self, value):
        return self._ro_feminine.get(value, value)

    def inflect(self, value, text):
        text = text.split('/')
        if len(text) == 1:
            return text[0]
        if value == 1:
            if len(text) < 3:
                return text[0]
            return ''.join(text[0:2])
        if len(text)<3:
            return "".join(text)
        return ''.join([text[0], text[2]])

    def to_splitnum(self, val, hightxt="", lowtxt="", jointxt="",
                    divisor=100, longval=True, cents = True,
                    high_feminine=False, low_feminine=False):
        out = []
        try:
            high, low = val
        except TypeError:
            high, low = divmod(val, divisor)
        if high:
            hightxt = self.title(self.inflect(high, hightxt))
            high_val = self.to_cardinal(high)
            if high_feminine:
                high_val = self.to_feminine(high_val)
            out.append(self.to_shortened(high_val))
            if low:
                if longval:
                    if hightxt:
                        out.append(hightxt)
                    if jointxt:
                        out.append(self.title(jointxt))
            elif hightxt:
                out.append(hightxt)
        if low:
            if cents:
                low_val = self.to_cardinal(low)
                if low_feminine:
                    low_val = self.to_feminine(low_val)
                out.append(self.to_shortened(low_val))
            else:
                out.append("%02d" % low)
            if lowtxt and longval:
                out.append(self.title(self.inflect(low, lowtxt)))
        return " ".join(out)
