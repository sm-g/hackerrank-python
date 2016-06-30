# -*- coding: utf-8 -*-

__author__ = 'smg'


def fibonacci_modified(a, b, n):
    """
    >>> fibonacci_modified(0,1,5)
    5
    >>> fibonacci_modified(2,2,3)
    6
    """
    for i in xrange(2, n):
        a, b = b, a + b * b
    print b


def max_subarray(arr):
    """
    Print largest possible sum of any continuous and Non-contiguous subarray.

    Uses Kadane algorithm.

    >>> max_subarray([])
    0 0
    >>> max_subarray([-1,-2])
    0 0
    >>> max_subarray([1, 2, 3, -4, 5])
    7 11
    >>> max_subarray([1, 2, 3, -4, 3])
    6 9
    """
    best_sum = s = 0
    for i in xrange(len(arr)):
        s += arr[i]
        if s > best_sum:
            best_sum = s
        if s < 0:
            s = 0

    non_contiguous = sum(filter(lambda x: x > 0, arr))

    print best_sum, non_contiguous


def coin_change(n, coins):
    """
    >>> coin_change(4, [1,2,3])
    4
    >>> coin_change(10, [2,5,3,6])
    5
    """
    coins.sort(reverse=True)
    case_map = {}  # запоминаем сколько решений на случай (index, goal)

    def step(index, goal):
        # print index, goal
        if (index, goal) in case_map:
            return case_map[(index, goal)]

        x = 0  # способов добрать монеты для (index, goal)
        for i, coin in enumerate(coins[index:]):
            if goal == coin:
                x += 1
                # print "+ %s" % coin
                continue

            remain = goal - coin
            k = index + i  # индекс после текущего, с которого монеты не больше остатка
            while k < len(coins) and coins[k] > remain:
                k += 1

            if k == len(coins):
                # нет монет не больше остатка
                continue

            x += step(k, remain)

        # print "= %s" % x
        case_map[(index, goal)] = x
        return x

    step(0, n)

    print case_map[(0, n)]


def candies(ratings):
    """
    :type ratings: list
    >>> candies([1,2,2])
    4
    >>> candies([2,4,2,6,1,7,8,9,2,1])
    19
    """
    can = [1] * len(ratings)
    m = min(ratings)
    i = ratings.index(m)

    while i < len(ratings) - 1:
        # if ratings[i + 1] == ratings[i]:
        #     can[i + 1] = can[i]
        # el
        if ratings[i + 1] > ratings[i]:
            can[i + 1] = can[i] + 1
        else:
            if can[i] > 1:
                can[i + 1] = 1
            else:
                # возврат до границы разрыва рейтинга
                j = i
                while j > 0 and abs(can[j] - can[j - 1]) <= 1:
                    can[j] += 1
                    j -= 1
                can[j] += 1

        i += 1

    i = ratings.index(m)
    while i > 0:
        # if ratings[i - 1] == ratings[i]:
        #     can[i - 1] = can[i]
        # el
        if ratings[i - 1] > ratings[i]:
            can[i - 1] = can[i] + 1
        else:
            if can[i] > 1:
                can[i - 1] = 1
            else:
                # возврат до границы разрыва рейтинга
                j = i
                while j < len(ratings) - 1 and abs(can[j] - can[j + 1]) <= 1:
                    can[j] += 1
                    j += 1
                can[j] += 1

        i -= 1

    print sum(can)


def candies2(ratings):
    """
    :type ratings: list
    >>> candies2([1,2,2])
    4
    >>> candies2([2,4,2,6,1,7,8,9,2,1])
    19
    """
    can = [1] * len(ratings)
    l = len(ratings)
    for i in xrange(l - 1):
        look_at = i + 1
        if ratings[look_at] > ratings[i]:
            can[look_at] = can[i] + 1
        elif can[i] > 1:
            can[look_at] = 1
        else:
            j = look_at
            while j > 0 and ratings[j - 1] > ratings[j] and can[j - 1] - can[j] <= 1:
                can[j - 1] += 1
                j -= 1
        # print can

    print sum(can)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
