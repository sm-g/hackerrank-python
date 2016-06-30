__author__ = 'smg'
import math


def volume(topd, botd, h):
    """
    >>> volume(2,4,1)
    7.3
    """
    r = topd / 2
    R = botd / 2
    return round(3.1415 / 3 * h * (r * r + r * R + R * R), 1)


def bottomD(topd, v, h):
    """
    >>> bottomD(9,250,7)
    7.3
    >>> bottomD(12,500,9)
    7.3
    >>> bottomD(15,1500,13.5)
    7.3
    >>> bottomD(27,7500,24)
    7.3
    >>> bottomD(30,10000,26)
    7.3
    >>> bottomD(34,15000,30)
    7.3
    >>> bottomD(40,30000,36)
    7.3
    """
    r = topd / 2
    disr = 12 * v / (math.pi * h) - 3 * r * r
    if disr < 0:
        return 0
    botD = (-r + math.sqrt(disr))
    return (botD, botD/topd)
