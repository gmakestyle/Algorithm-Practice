"""
This is a solution to the first problem of the April 2015 Hacker Rank contest.
The problem states that there are N rats that each begin a race at different
distances from a finish line. They each also begin with a constant speed. The
solution determines which rats finish first. The rats are identified by their 
respective positions in the input list (1-indexed). The output format is simply
a printout of the index of each winning rat on a separate line, sorted from 
least index to greatest.
"""
numRats = int(raw_input())
ratSpeeds = [int(s) for s in raw_input().split()]
ratDistances = [int(s) for s in raw_input().split()]
firstRats = [1]
lowestTime = float("inf")
for i in xrange(len(ratSpeeds)):
    timeToFinish = ratDistances[i] / float(ratSpeeds[i])
    if timeToFinish < lowestTime:
        firstRats = [i+1]
        lowestTime = timeToFinish
    elif timeToFinish == lowestTime:
        firstRats.append(i+1)
for rat in firstRats:
    print rat
