# -*- coding: utf-8 -*-

__author__ = 'smg'


def insertion_sort(ar):
    """
    >>> insertion_sort('2 4 6 8 3')
    2 4 6 8 8
    2 4 6 6 8
    2 4 4 6 8
    2 3 4 6 8
    """
    ar = list(map(int, ar.split()))

    i = len(ar) - 1
    e = ar[i]
    while i > 0 and e < ar[i - 1]:
        ar[i] = ar[i - 1]
        i -= 1
        print ' '.join([str(a) for a in ar])
    ar[i] = e
    print ' '.join([str(a) for a in ar])


def insertion_sort2(ar):
    """
    >>> insertion_sort2('1 4 3 5 6 2')
    1 4 3 5 6 2
    1 3 4 5 6 2
    1 3 4 5 6 2
    1 3 4 5 6 2
    1 2 3 4 5 6
    """
    ar = list(map(int, ar.split()))

    for i in range(1, len(ar)):
        e = ar[i]
        j = i
        while j > 0 and e < ar[j - 1]:
            ar[j] = ar[j - 1]
            j -= 1
        ar[j] = e
        print ' '.join([str(a) for a in ar])


def insertion_sort_shifts(ar):
    """
    >>> insertion_sort2('1 4 3 5 6 2')
    1 4 3 5 6 2
    1 3 4 5 6 2
    1 3 4 5 6 2
    1 3 4 5 6 2
    1 2 3 4 5 6
    """
    ar = list(map(int, ar.split()))

    for i in range(1, len(ar)):
        e = ar[i]
        j = i
        while j > 0 and e < ar[j - 1]:
            ar[j] = ar[j - 1]
            j -= 1
        ar[j] = e
        print ' '.join([str(a) for a in ar])


def insertion_sort_shifts_count(ar):
    """
    >>> insertion_sort_shifts_count('2 1 3 1 2')
    4
    """
    ar = list(map(int, ar.split()))
    shifts = 0
    for i in range(1, len(ar)):
        e = ar[i]
        j = i
        while j > 0 and e < ar[j - 1]:
            ar[j] = ar[j - 1]
            j -= 1
            shifts += 1
        ar[j] = e
    print shifts


def quicksort1(ar):
    """
    >>> quicksort1('4 5 3 7 2')
    3 2 4 5 7
    """
    ar = list(map(int, ar.split()))
    left = filter(lambda x: x < ar[0], ar)
    right = filter(lambda x: x >= ar[0], ar)
    print ' '.join([str(a) for a in left + right])


def quicksort2(ar):
    """
    >>> quicksort2('5 8 1 3 7 9 2')
    2 3
    1 2 3
    7 8 9
    1 2 3 5 7 8 9
    """
    ar = list(map(int, ar.split()))

    def inner(subarray):
        if len(subarray) <= 1:
            return subarray
        left = []
        right = []
        for i in range(1, len(subarray)):
            if subarray[i] < subarray[0]:
                left.append(subarray[i])
            else:
                right.append(subarray[i])

        l = inner(left)
        l.append(subarray[0])
        l_and_r = l + inner(right)
        print ' '.join([str(a) for a in l_and_r])
        return l_and_r

    inner(ar)


def quicksort3(ar):
    """
    >>> quicksort3('1 3 9 8 2 7 5')
    1 3 2 5 9 7 8
    1 2 3 5 9 7 8
    1 2 3 5 7 8 9
    """
    ar = list(map(int, ar.split()))

    def partition(a, lo, hi):
        pivot_index = hi
        j = lo
        for i in range(lo, hi):
            if a[i] < a[pivot_index]:
                a[i], a[j] = a[j], a[i]
                j += 1
        a[pivot_index], a[j] = a[j], a[pivot_index]

        print ' '.join([str(a) for a in a])
        return j

    def inner(subarray, left, right):
        if right <= left:
            return

        pivot_index = partition(subarray, left, right)
        inner(subarray, left, pivot_index - 1)
        inner(subarray, pivot_index + 1, right)

    inner(ar, 0, len(ar) - 1)


def find_median(ar):
    """
    >>> find_median('0 1 2 4 6 5 3')
    3
    >>> find_median('0 1 2 1 1 5 3')
    1
    >>> find_median('3 4 2 5 1')
    3
    """
    ar = list(map(int, ar.split()))

    def partition(a, lo, hi):
        pivot_index = hi
        j = lo
        for i in range(lo, hi):
            if a[i] < a[pivot_index]:
                a[i], a[j] = a[j], a[i]
                j += 1
        a[pivot_index], a[j] = a[j], a[pivot_index]

        return j

    def median_index(a, pos, left, right):
        """
        :param pos: Позиция в подмассиве
        :return:
        """
        if right <= left:
            return left + pos

        pivot_index = partition(a, left, right)

        # размер подмассива через глобальные индексы
        leftside_len = pivot_index - left

        if pos <= leftside_len:
            # не меняется в левом подмассиве
            return median_index(a, pos, left, pivot_index - 1)
        else:
            # меньше на размер левого в правом подмассиве
            return median_index(a, pos - leftside_len - 1, pivot_index + 1, right)

    # искомая позиция - середина сортированного массива
    pos = len(ar) // 2
    print ar[median_index(ar, pos, 0, len(ar) - 1)]


def sherlock_watson(spec, ar, qs):
    """
    >>> sherlock_watson('3 5 3', '1 2 3', [0, 1])
    2
    3
    """
    spec = map(int, spec.split())
    n = spec[0]
    k = spec[1] % n
    ar = list(map(int, ar.split()))
    for q in qs:
        print ar[q - k]


def almost_sorted(a):
    """
    >>> almost_sorted([2])
    yes
    >>> almost_sorted([4,2])
    yes
    swap 1 2
    >>> almost_sorted([1,4,3,2])
    yes
    swap 2 4
    >>> almost_sorted([3,1,2])
    no
    >>> almost_sorted([2,1,4,3])
    no
    >>> almost_sorted([1,5,4,3,2,6])
    yes
    reverse 2 5
    """

    def test_after_swap(l, r):
        assert -1 < l < r
        assert l < len(a) - 1
        assert r < len(a)

        return (l == 0 or a[l - 1] <= a[r]) and a[r] <= a[l + 1] \
               and a[r - 1] <= a[l] and (r == len(a) - 1 or a[l] <= a[r + 1])

    bads = []
    for i in range(len(a) - 1):
        if a[i + 1] < a[i]:
            bads.append(i)

    if len(bads) == 0:
        print 'yes'
        return

    if len(bads) == 1:
        bads.append(len(a) - 2)  # обмен с последним

    start = bads[0]
    end = bads[-1] + 1

    if not test_after_swap(start, end):
        print 'no'
        return

    if len(bads) > 2:
        for i in range(1, len(bads)):
            if bads[i] - bads[i - 1] > 1:
                print 'no'
                return

        print 'yes'
        print 'reverse %s %s' % (start + 1, end + 1)
        return

    print 'yes'
    print 'swap %s %s' % (start + 1, end + 1)


def sherlock_pairs(a):
    """
    >>> sherlock_pairs([1,1,2])
    2
    >>> sherlock_pairs([5,6,1,5,6,5])
    8
    """
    from itertools import groupby

    a.sort()
    result = 0
    for k, g in groupby(a, lambda x: x):
        l = sum(1 for _ in g)
        if l > 1:
            result += l * (l - 1)

    print result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
