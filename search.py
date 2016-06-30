# -*- coding: utf-8 -*-
__author__ = 'smg'

import sys
from pprint import pprint


def read_cases():
    inp = sys.stdin
    cases = int(inp.readline())
    for i in range(cases):
        inp.readline()  # raw_input()
        array = inp.readline()
        yield array


def sherlock_and_array(args):
    """
    https://www.hackerrank.com/challenges/sherlock-and-array

    >>> sherlock_and_array('1 2 3')
    NO
    >>> sherlock_and_array('1 2 3 3')
    YES
    """
    array = map(int, args.split())
    sum_r = sum(array)
    sum_l = 0

    for i in range(len(array)):
        e = array[i]
        sum_r -= e
        if sum_l == sum_r:
            print "YES"
            return
        sum_l += e

    print "NO"


def max_index_product(args):
    """
    https://www.hackerrank.com/challenges/find-maximum-index-product
    not solved yet
    >>> max_index_product('5 4 3 4 5')
    8
    >>> max_index_product('7 1 3 2 4')
    15
    >>> max_index_product('0 1 0 1')
    8
    >>> max_index_product('0 1')
    0
    >>> max_index_product('0')
    0
    """
    array = map(int, args.split())
    if len(array) <= 2:
        print 0
        return

    ind = [dict(l=None, r=None) for _ in xrange(len(array))]

    def calc_ind(i, left):
        j = i
        while 0 < j < len(array) - 1 and array[j] <= array[i]:
            prev_ans = ind[j]['l' if left else 'r']
            if prev_ans is not None and array[i] <= array[j]:  # use solved cases
                return prev_ans
            j += -1 if left else 1
        return j + 1 if array[j] > array[i] else 0

    for i in xrange(0, len(array)):
        ind[i]['l'] = calc_ind(i, True)
    for i in xrange(len(array) - 1, -1, -1):
        ind[i]['r'] = calc_ind(i, False)

    return max(map(lambda x: x['r'] * x['l'], ind))


def pairs(args, diff):
    """
    https://www.hackerrank.com/challenges/pairs
    >>> pairs('1 5 3 4 2', 2)
    3
    >>> pairs('1 3 4 8 9 13 14', 5)
    4
    """
    array = map(int, args.split())
    if len(array) <= 1:
        print 0
        return

    # группируем, [1,3,4],[8,9],[13,14]
    array.sort()
    o = []
    for x in array:
        if o and o[-1] and x - o[-1][0] < diff:
            o[-1].append(x)
        else:
            o.append([x])

    ans = 0
    for i in xrange(len(o) - 1):
        for x in o[i + 1]:
            for y in o[i]:
                if x - y == diff:
                    ans += 1

    return ans


def count_luck(rows, cols, lines, guessed):
    """
    https://www.hackerrank.com/challenges/count-luck
    >>> count_luck(2, 3, ['*.M',
    ...                   '.X.'],1)
    'Impressed'
    >>> count_luck(4,11, ['.X.X......X',
    ...                   '.X*.X.XXX.X',
    ...                   '.XX.X.XM...',
    ...                   '......XXXX.'], 4)
    'Oops!'
    >>> count_luck(4,11,['XXXX......X',
    ...                  '....X.XXX.X',
    ...                  'X*X.X.XM...',
    ...                  'XX....XXXX.'], 4)
    'Impressed'
    """
    maze = [list(line) for line in lines]

    start = 'M'
    end = '*'
    tree = 'X'
    free = '.'
    wands = []

    def print_m():
        pprint([''.join(line) for line in maze])
        print(wands[0])
        print

    def surround():
        for row in maze:
            row.insert(0, tree)
            row.append(tree)
        maze.insert(0, list(tree * (cols + 2)))
        maze.append(list(tree * (cols + 2)))

    def is_cross(x, y, min_free_nei=2):
        from collections import Counter

        nei = [maze[y + d][x] for d in [-1, 1]]
        nei.extend([maze[y][x + d] for d in [-1, 1]])
        c = Counter(nei)
        return c[free] + c[end] >= min_free_nei

    def solve(x, y):
        # Base case
        if y > len(maze) or x > len(maze[y]):
            return False

        if maze[y][x] == end:
            return True

        if maze[y][x] != free:
            return False

        # marking
        maze[y][x] = "o"

        cross = is_cross(x, y)

        # развилка
        if cross:
            wands[0] += 1

        # print_m()

        # recursive case
        if solve(x + 1, y):  # right
            return True
        if solve(x, y + 1):  # down
            return True
        if solve(x - 1, y):  # left
            return True
        if solve(x, y - 1):  # up
            return True

        # Backtracking
        if cross:
            wands[0] -= 1
        maze[y][x] = free
        return False

    surround()
    for y in xrange(rows + 2):
        try:
            mx = maze[y].index(start)
            my = y
            break
        except ValueError:
            pass

    wands = [0]
    maze[my][mx] = free
    solve(mx, my)

    return 'Impressed' if guessed == wands[0] else 'Oops!'


def connected_cell_in_a_grid(rows, cols, lines):
    """
    >>> connected_cell_in_a_grid(5,5,['1 1 0 1 0',
    ...                               '0 1 1 0 0',
    ...                               '0 0 1 0 1',
    ...                               '1 0 0 0 1',
    ...                               '0 1 0 1 1'])
    6
    >>> connected_cell_in_a_grid(5,4,['0 0 1 1',
    ...                               '0 0 1 0',
    ...                               '0 1 1 0',
    ...                               '0 1 0 0',
    ...                               '1 1 0 0'])
    8
    >>> connected_cell_in_a_grid(2,1,['0',
    ...                               '1'])
    1
    >>> connected_cell_in_a_grid(1,3,['0 0 1'])
    1
    >>> connected_cell_in_a_grid(1,1,['1'])
    1
    """
    maze = [list(map(int, line.split())) for line in lines]

    def ind(x, y):
        return str(x) + str(y)

    def surround():
        for row in maze:
            row.insert(0, 0)
            row.append(0)
        maze.insert(0, list([0] * (cols + 2)))
        maze.append(list([0] * (cols + 2)))

    surround()
    graph = {}
    for y in range(1, rows + 1):
        for x in range(1, cols + 1):
            if maze[y][x] == 1:
                graph[ind(x, y)] = {ind(x + dx, y + dy)
                                    for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1)]
                                    if maze[y + dy][x + dx] == 1}

    # pprint(maze, width=30)
    # pprint(graph)

    for node, edges in graph.items():
        for edge in edges:
            if graph.has_key(edge):
                graph[edge].add(node)
            else:
                graph[edge] = {node}

    def connected_components(nodes):
        """
        https://breakingcode.wordpress.com/2013/04/08/finding-connected-components-in-a-graph/

        """
        # List of connected components found. The order is random.
        result = []

        # Make a copy of the set, so we can modify it.
        nodes = set(nodes)

        # Iterate while we still have nodes to process.
        while nodes:

            # Get a random node and remove it from the global set.
            n = nodes.pop()

            # This set will contain the next group of nodes connected to each other.
            group = {n}

            # Build a queue with this node in it.
            queue = [n]

            # Iterate the queue.
            # When it's empty, we finished visiting a group of connected nodes.
            while queue:
                # Consume the next item from the queue.
                n = queue.pop(0)

                # Fetch the neighbors.
                neighbors = graph[n]

                # Remove the neighbors we already visited.
                neighbors.difference_update(group)

                # Remove the remaining nodes from the global set.
                nodes.difference_update(neighbors)

                # Add them to the group of connected nodes.
                group.update(neighbors)

                # Add them to the queue, so we visit them in the next iterations.
                queue.extend(neighbors)

            # Add the group to the list of groups.
            result.append(group)

        # Return the list of groups.
        return result

    ccomp = connected_components(graph.keys())
    # pprint(graph)
    # pprint(ccomp)

    if len(ccomp) == 0:
        max_comp = int(maze[rows][cols])
    else:
        max_comp = max(map(len, ccomp))
    return max_comp


def circle_city(r2, k):
    """
    >>> circle_city(25, 11)
    'impossible'
    >>> circle_city(25, 12)
    'possible'
    """
    import math

    dots = 0
    r = int(math.sqrt(r2))
    for x in xrange(1, r + 1):
        if math.sqrt(r2 - x * x) % 1 == 0:
            dots += 4

    return 'impossible' if dots > k else 'possible'


def encryption(line):
    """
    https://www.hackerrank.com/challenges/encryption
    >>> encryption('qwerty')
    'qr wt ey'
    >>> encryption('feedthedog')
    'fto ehg ee dd'
    """
    import math

    l = len(line)
    cols = int(math.ceil(math.sqrt(l)))
    s = [line[i:i + cols] for i in range(0, l, cols)]

    return ' '.join([''.join([line[i] if i < len(line) else ''
                              for line in s])
                     for i in range(0, cols)])


def maximize_sum(a, m):
    """
    >>> maximize_sum([3,3,9,9,5],7)
    6
    >>> maximize_sum([0,3],7)
    3
    >>> maximize_sum([1975960379,317097468,1892066602,1376710098,927612903,1330573318,603570493,1687926653,660260757,959997302,485560281,402724287,593209442,1194953866,894429690,364228445,1947346620,221558441,270744730,1063958032,1633108118,2114738098,2007905772,1469834482,822890676,1610120710,791698928,631704568,498777857,1255179498,524872354,327254587,1572276966,269455307,1703964684,352406220,1600028625,160051529,2040332872,112805733,1120048830,378409504,515530020,1713258271,1573363369,1409959709,2077486716,1373226341,1631518150,200747797], 2040651435)
    2040332872
    """
    # TODO editorial
    result = 0
    for i in xrange(0, len(a)):
        a[i] = a[i] % m
        if a[i] > result:
            result = a[i]

        for j in xrange(0, i):
            a[j] = (a[i] + a[j]) % m
            if a[j] > result:
                result = a[j]

    return result


if __name__ == '__main__':
    # inp = open('P:/test.txt')
    # cases = int(inp.readline())
    # for i in range(cases):
    #     args = map(int,inp.readline().split())
    #     print circle_city(args[0],args[1])

    import doctest

    doctest.testmod()
    with open('out.txt', 'w') as out:
        with open('input01.txt') as f:
            t = int(f.readline())
            for i in range(t):
                m = list(map(int, f.readline().split()))[1]
                a = list(map(int, f.readline().split()))
                out.write(str(maximize_sum(a, m)) + '\n')
