# -*- encoding: utf-8 -*-
u"""
>>> from textwrap import fill

>>> ' '.join([str(i) for i in splitby3('1')])
'1'
>>> ' '.join([str(i) for i in splitby3('1123')])
'1 123'
>>> ' '.join([str(i) for i in splitby3('1234567890')])
'1 234 567 890'

>>> print(' '.join([n2w(i) for i in range(10)]))
nulis vienas du trys keturi penki šeši septyni aštuoni devyni

>>> print(fill(' '.join([n2w(i+10) for i in range(10)])))
dešimt vienuolika dvylika trylika keturiolika penkiolika šešiolika
septyniolika aštuoniolika devyniolika

>>> print(fill(' '.join([n2w(i*10) for i in range(10)])))
nulis dešimt dvidešimt trisdešimt keturiasdešimt penkiasdešimt
šešiasdešimt septyniasdešimt aštuoniasdešimt devyniasdešimt

>>> print(n2w(100))
šimtas
>>> print(n2w(101))
šimtas vienas
>>> print(n2w(110))
šimtas dešimt
>>> print(n2w(115))
šimtas penkiolika
>>> print(n2w(123))
šimtas dvidešimt trys
>>> print(n2w(1000))
tūkstantis
>>> print(n2w(1001))
tūkstantis vienas
>>> print(n2w(2012))
du tūkstančiai dvylika

>>> print(fill(n2w(1234567890)))
milijardas du šimtai trisdešimt keturi milijonai penki šimtai
šešiasdešimt septyni tūkstančiai aštuoni šimtai devyniasdešimt

>>> print(fill(n2w(215461407892039002157189883901676)))
du šimtai penkiolika naintilijonų keturi šimtai šešiasdešimt vienas
oktilijonas keturi šimtai septyni septilijonai aštuoni šimtai
devyniasdešimt du sikstilijonai trisdešimt devyni kvintilijonai du
kvadrilijonai šimtas penkiasdešimt septyni trilijonai šimtas
aštuoniasdešimt devyni milijardai aštuoni šimtai aštuoniasdešimt trys
milijonai devyni šimtai vienas tūkstantis šeši šimtai septyniasdešimt
šeši

>>> print(fill(n2w(719094234693663034822824384220291)))
septyni šimtai devyniolika naintilijonų devyniasdešimt keturi
oktilijonai du šimtai trisdešimt keturi septilijonai šeši šimtai
devyniasdešimt trys sikstilijonai šeši šimtai šešiasdešimt trys
kvintilijonai trisdešimt keturi kvadrilijonai aštuoni šimtai dvidešimt
du trilijonai aštuoni šimtai dvidešimt keturi milijardai trys šimtai
aštuoniasdešimt keturi milijonai du šimtai dvidešimt tūkstančių du
šimtai devyniasdešimt vienas

>>> print(to_currency(1, 'LTL'))
vienas litas, nulis centų

>>> print(to_currency(1234.56, 'LTL'))
tūkstantis du šimtai trisdešimt keturi litai, penkiasdešimt šeši centai

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
    7: (u'septyniolika',),
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
    'LTL': ((u'litas', u'litai', u'litų'), (u'centas', u'centai', u'centų')),
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
    return [int(x) for x in reversed(list(('%03d' % n)[-3:]))]

def pluralize(n, forms):
    n1, n2, n3 = get_digits(n)
    if n2 == 1 or n1 == 0 or n == 0:
        return forms[2]
    elif n1 == 1:
        return forms[0]
    else:
        return forms[1]

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
        elif n1 > 0 and not (i > 0 and x == 1):
            words.append(ONES[n1][0])

        if i > 0:
            words.append(pluralize(x, THOUSANDS[i]))

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
    cr1, cr2 = CURRENCIES[currency]
    return u'%s %s, %s %s' % (int2word(left), pluralize(left, cr1),
                              int2word(right), pluralize(right, cr2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
