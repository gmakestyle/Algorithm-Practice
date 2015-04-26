__author__ = 'Maajid'
# -*- coding: utf-8 -*-
"""
Taken from https://www.hackerrank.com/challenges/the-love-letter-mystery
Problem Statement

James found a love letter his friend Harry has written for his girlfriend.
James is a prankster, so he decides to meddle with the letter. He changes all
the words in the letter into palindromes.

To do this, he follows two rules:

He can reduce the value of a letter, e.g. he can change d to c,but he cannot
change c to d. In order to form a palindrome, if he has to repeatedly reduce the
value of a letter, he can do it until the letter becomes "a". Once a letter
has been changed to a, it can no longer be changed. Each reduction in the
value of any letter is counted as a single operation. Find the minimum number of
operations required to convert a given string into a palindrome.

Input Format

The first line contains an integer T, i.e., the number of test cases.
The next T lines will contain a string each. The strings do not contain any spaces.

Constraints
1≤T≤10
1≤ length of string ≤104
All characters are lower case English letters.

Output Format

A single line containing the number of minimum operations corresponding to each test case.
"""
# Read input from STDIN. Print output to STDOUT
from collections import deque


def count_reductions(characters):
    """ Returns the number of character reductions necessary to change the
    input deque of characters into a palindrome.

    :param characters: deque
    :return: int
    """
    reductions = 0
    while characters:
        if len(characters) > 1:
            left, right = characters.popleft(), characters.pop()
            reductions += abs(ord(left) - ord(right))
        else:
            return reductions
    return reductions

testCases = int(raw_input())
for i in xrange(testCases):
    print count_reductions(deque(raw_input()))