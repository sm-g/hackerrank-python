# -*- coding: utf-8 -*-
__author__ = 'smg'


def python_quest():
    for i in range(1, 5):
        print i * sum([10 ** x for x in range(i)])

    # репьюниты
    for i in range(1, 5):
        print i * (10 ** i - 1) / 9


def mutate_str(str, ch, i):
    res = str[:i] + ch + str[i + 1:]

    l = list(str)
    l[i] = ch
    res2 = ''.join(l)
    return res


class Complex:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i

    def __add__(self, other):
        """
        >>> Complex(1,1) + Complex(2,-3)
        3.00 - 2.00i
        """
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        """
        >>> Complex(1,1) - Complex(2,1)
        -1.00
        """
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        """
        >>> Complex(3,4) * Complex(0,2)
        -8.00 + 6.00i
        """
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __div__(self, other):
        """
        >>> Complex(3,4) / Complex(0,2)
        2.00 - 1.50i
        """
        denom = float(other.r ** 2 + other.i ** 2)
        return Complex((self.r * other.r + self.i * other.i) / denom,
                       (self.i * other.r - self.r * other.i) / denom)

    def module(self):
        """
        >>> Complex(2,1).module()
        2.24
        """
        return round((self.r ** 2 + self.i ** 2) ** 0.5, 2)

    def __repr__(self):
        if self.r != 0 and self.i != 0:
            return '{0:.2f} {2} {1:.2f}i'.format(self.r, abs(self.i), '+' if self.i > 0 else '-')
        if self.i == 0:
            return '{0:.2f}'.format(self.r)
        if self.r == 0:
            return '{0:.2f}i'.format(self.i)
        return '0.00'


def map_cube(n):
    """
    >>> map_cube(4)
    [0, 1, 1, 8]
    """
    l = []
    for i in range(n):
        x = l[i - 1] + l[i - 2] if len(l) >= 2 else 0 if i == 0 else 1
        l.append(x)
    l = map(lambda x: x ** 3, l)
    print l


def valid_emails(emails):
    """
    >>> valid_emails(['la@1d.ru', 'l_@1d.long','l-3@d_.ru','la@1.d.ru','aa@1d.ru', 'la@1dru','la1d.ru'])
    ['aa@1d.ru', 'la@1d.ru']
    """
    import string

    username_chars = string.lowercase + string.uppercase + '0123456789-_'
    sitename_chars = string.lowercase + string.uppercase + '0123456789'

    l = filter(lambda x: x.count('@') == 1 and x.count('.') == 1, emails)
    l = filter(lambda x: len(x[:x.find('@')]) > 0 and
                         len(x[x.find('@') + 1:x.find('.')]) > 0 and
                         len(x[x.find('.') + 1:]) <= 3, l)
    l = filter(lambda x: len(x[:x.find('@')].translate(None, username_chars)) == 0, l)
    l = filter(lambda x: not any(ch not in sitename_chars
                                 for ch in (x[x.find('@') + 1:x.find('.')] + x[x.find('.') + 1:])), l)

    print sorted(l)


def mobile_decorator(f):
    def shaper(strs):
        shaped = ['+91 {0} {1}'.format(str[-10:-5], str[-5:]) for str in strs]
        ret = f(shaped)
        return ret

    return shaper


@mobile_decorator
def sort(strs):
    return sorted(strs)


def standartize_numbers(numbers):
    """
    >>> standartize_numbers(['07895462130','919875641230','9195969878'])
    +91 78954 62130
    +91 91959 69878
    +91 98756 41230
    """
    for n in sort(numbers):
        print n


if __name__ == '__main__':
    r, i = map(float, '-91 -99'.split())
    c1 = Complex(r, i)
    r, i = map(float, '-52 -60'.split())
    c2 = Complex(r, i)
    print c1 + c2
    print c1 - c2
    print c1 * c2
    print c1 / c2
    print c1.module()
    print c2.module()

    import doctest

    doctest.testmod()
