# -*- coding: utf-8 -*-
__author__ = 'smg'


def anagram(s):
    """
    :type s str

    >>> anagram('mnop')
    2
    >>> anagram('b')
    -1
    >>> anagram('abc')
    -1
    >>> anagram('mnom')
    1
    >>> anagram('zyyx')
    1
    """
    if len(s) % 2 == 1:
        return -1
    # TODO разобраться в верном решении

    diff = [0] * 26
    for ch in s[:len(s) / 2]:
        diff[ord(ch) - ord('a')] += 1
    for ch in s[len(s) / 2:]:
        diff[ord(ch) - ord('a')] -= 1

    return sum(filter(lambda x: x > 0, diff))

    s1 = sorted(s[:len(s) / 2])
    s2 = sorted(s[len(s) / 2:])
    return abs(sum((0 if t[0] == t[1] else 1 for t in zip(s1, s2))))


def bigger_greater(word):
    """
    >>> bigger_greater('ab')
    'ba'
    >>> bigger_greater('ba')
    'no answer'
    >>> bigger_greater('dkhc')
    'hcdk'
    """
    i = len(word) - 1
    while i > 0:
        if word[i] > word[i - 1]:
            greater = list(filter(lambda x: x > word[i - 1], word[i:]))
            min_greater = min(greater)

            remain = list(word[i:])
            remain.remove(min_greater)
            remain.append(word[i - 1])
            remain.sort()
            return word[:i - 1] + min_greater + ''.join(remain)
        i -= 1

    return 'no answer'


def sherlock_and_anagrams(str):
    """
    >>> sherlock_and_anagrams('abba')
    4
    >>> sherlock_and_anagrams('acbabc')
    9
    """
    import string

    n = len(str)
    res = 0

    # равное количество всех букв
    def is_anagram(str1, str2):
        for x in string.ascii_lowercase:
            if str1.count(x) != str2.count(x):
                return False

        return True

    # ищем пару подстроке в оставщейся части строки со следующей позиции
    def find_pair(start, substr):
        sub_n = len(substr)
        if sub_n > n - start:
            return 0

        res = 0
        while start <= n - sub_n:
            if is_anagram(str[start:start + sub_n], substr):
                res += 1
            start += 1

        return res

    # генерируем все подстроки
    for i in range(n):
        for j in range(i + 1, n):
            res += find_pair(i + 1, str[i:j])

    return res


def palindrome_index(str):
    """
    >>> palindrome_index('abba')
    -1
    >>> palindrome_index('ambba')
    1
    >>> palindrome_index('ambxba')
    1
    >>> palindrome_index('abbxbbma')
    6
    >>> palindrome_index('fwcwwcf')
    1
    """
    middle = len(str) // 2

    def is_pal(str):
        m = len(str) // 2
        for k in range(m):
            if str[k] != str[-k - 1]:
                return False
        return True

    for k in range(middle if len(str) % 2 == 1 else middle + 1):
        if str[k] != str[-k - 1]:
            ii = len(str) - k
            if is_pal(str[k + 1:ii]):
                return k
            return ii - 1
    return -1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    t = input()
    for i in range(t):
        str = raw_input()
        print palindrome_index(str)
