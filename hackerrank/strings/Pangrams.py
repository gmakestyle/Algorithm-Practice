__author__ = 'Maajid'


def is_pangram(s):
    # Determines if the input string contains every letter in the alphabet.
    return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

if is_pangram(raw_input()):
    print(u'pangram')
else:
    print(u'not pangram')