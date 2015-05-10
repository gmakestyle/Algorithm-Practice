# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

numTests = int(raw_input())
for i in xrange(numTests):
    candidateNumber = raw_input()
    if len(candidateNumber) != 10:
        print 'NO'
    elif not candidateNumber[0] in {'7', '8', '9'}:
        print 'NO'
    else:
        candidateNumber = re.sub(r"\D", "", candidateNumber)
        print 'YES' if len(candidateNumber) == 10 else 'NO'