# -*- encoding: utf-8 -*-
"""
>>> ' '.join([str(i) for i in splitby3('1')])
'1'
>>> ' '.join([str(i) for i in splitby3('1123')])
'1 123'
>>> ' '.join([str(i) for i in splitby3('1234567890')])
'1 234 567 890'

>>> ' '.join([n2w(i) for i in range(10)])
u'nulis vienas du trys keturi penki \u0161e\u0161i septyni a\u0161tuoni devyni'
>>> ' '.join([n2w(i+10) for i in range(10)])
u'de\u0161imt vienuolika dvylika trylika keturiolika penkiolika \u0161e\u0161iolika septiniolika a\u0161tuoniolika devyniolika'
>>> ' '.join([n2w(i*10) for i in range(10)])
u'nulis de\u0161imt dvide\u0161imt trisde\u0161imt keturiasde\u0161imt penkiasde\u0161imt \u0161e\u0161iasde\u0161imt septyniasde\u0161imt a\u0161tuoniasde\u0161imt devyniasde\u0161imt'

>>> n2w(123)
u'\u0161imtas dvide\u0161imt trys'
>>> n2w(100)
u'\u0161imtas'
>>> n2w(101)
u'\u0161imtas vienas'
>>> n2w(110)
u'\u0161imtas de\u0161imt'
>>> n2w(115)
u'\u0161imtas penkiolika'
>>> n2w(1000)
u't\u016bkstantis'
>>> n2w(1001)
u't\u016bkstantis vienas'
>>> n2w(2012)
u'du t\u016bkstan\u010diai dvylika'
>>> n2w(1234567890)
u'milijardas du \u0161imtai trisde\u0161imt keturi milijonai penki \u0161imtai \u0161e\u0161iasde\u0161imt septyni t\u016bkstan\u010diai a\u0161tuoni \u0161imtai devyniasde\u0161imt'

#>>> to_currency(1234.56, 'LTL')

"""

ZERO = (u'nulis',)

ONES = {
    1: (u'vienas',),
    2: (u'du',),
    3: (u'trys',),
    4: (u'keturi',),
    5: (u'penki',),
    6: (u'šeši',),
    7: (u'septyni',),
    8: (u'aštuoni',),
    9: (u'devyni',),
}

TENS = {
    0: (u'dešimt',),
    1: (u'vienuolika',),
    2: (u'dvylika',),
    3: (u'trylika',),
    4: (u'keturiolika',),
    5: (u'penkiolika',),
    6: (u'šešiolika',),
    7: (u'septiniolika',),
    8: (u'aštuoniolika',),
    9: (u'devyniolika',),
}

TWENTIES = {
    2: (u'dvidešimt',),
    3: (u'trisdešimt',),
    4: (u'keturiasdešimt',),
    5: (u'penkiasdešimt',),
    6: (u'šešiasdešimt',),
    7: (u'septyniasdešimt',),
    8: (u'aštuoniasdešimt',),
    9: (u'devyniasdešimt',),
}

HUNDRED = (u'šimtas', u'šimtai')

THOUSANDS = {
    1: (u'tūkstantis', u'tūkstančiai', u'tūkstančių'),
    2: (u'milijonas', u'milijonai', u'milijonų'),
    3: (u'milijardas', u'milijardai', u'milijardų'),
    4: (u'trilijonas', u'trilijonai', u'trilijonų'),
    5: (u'kvadrilijonas', u'kvadrilijonai', u'kvadrilijonų'),
    6: (u'kvintilijonas', u'kvintilijonai', u'kvintilijonų'),
    7: (u'sikstilijonas', u'sikstilijonai', u'sikstilijonų'),
    8: (u'septilijonas', u'septilijonai', u'septilijonų'),
    9: (u'oktilijonas', u'oktilijonai', u'oktilijonų'),
    10: (u'naintilijonas', u'naintilijonai', u'naintilijonų'),
}

CURRENCIES = {
    'LTL': (('litas', 'litai', 'litų'), ('centas', 'centai', 'centų')),
}

def splitby3(n):
    length = len(n)
    if length > 3:
        start = length % 3
        if start > 0:
            yield int(n[:start])
        for i in range(start, length, 3):
            yield int(n[i:i+3])
    else:
        yield int(n)


def get_digits(n):
    n1 = n2 = n3 = 0
    if n > 99:
        n3 = (n % 1000)//100
    if n > 9:
        n2 = (n % 100)//10
    n1 = n % 10
    return (n1, n2, n3)


def int2word(n):
    if n == 0:
        return ZERO[0]

    words = []
    chunks = list(splitby3(str(n)))
    i = len(chunks)
    for x in chunks:
        i -= 1
        n1, n2, n3 = get_digits(x)

        if n3 > 0:
            if n3 > 1:
                words.append(ONES[n3][0])
                words.append(HUNDRED[1])
            else:
                words.append(HUNDRED[0])

        if n2 > 1:
            words.append(TWENTIES[n2][0])

        if n2 == 1:
            words.append(TENS[n1][0])
        elif n1 > 0 and not (i > 0 and n1 == 1):
            words.append(ONES[n1][0])

        if i > 0:
            if n1 == 1 and n2 != 1:
                words.append(THOUSANDS[i][0])
            elif n1 > 1:
                words.append(THOUSANDS[i][1])
            else:
                words.append(THOUSANDS[i][2])

    return ' '.join(words)

def n2w(n):
    n = str(n).replace(',', '.')
    if '.' in n:
        left, right = n.split('.')
        return u'%s kablelis %s' % (int2word(int(left)), int2word(int(right)))
    else:
        return int2word(int(n))

def to_currency(n, currency='LTL'):
    n = str(n).replace(',', '.')
    if '.' in n:
        left, right = n.split('.')
    else:
        left, right = n, 0
    left, right = int(left), int(right)
    return u'%s kablelis %s' % (int2word(left), int2word(right))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
