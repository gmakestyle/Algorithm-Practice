# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import itemgetter

def print_list(l):
    s = ''
    for item in l:
        s += str(item) + ' '
    print s.strip()

N, M = tuple(map(int, raw_input().split()))
attributeList = []
for i in xrange(N):
    attributeList.append(map(int, raw_input().split()))
    
K = int(raw_input())
attributeList = sorted(attributeList, key=itemgetter(K))
for item in attributeList:
    print_list(item)
    
