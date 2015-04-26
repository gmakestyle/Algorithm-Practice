__author__ = 'Maajid'

import operator as op


def lonelyinteger(duplicateList):
    """ Determine the sole 'lonely' integer in duplicateList.

    The input is a list of integers that all appear twice except for one.
    The function returns the exceptional integer.
    :param duplicateList: list
    :return: int
    """
    answer = reduce(op.xor, duplicateList)
    return answer

if __name__ == '__main__':
    a = input() # length of the array, not necessary for us (in hackerrank spec)
    duplicateList = map(int, raw_input().strip().split(" "))
    print lonelyinteger(duplicateList)