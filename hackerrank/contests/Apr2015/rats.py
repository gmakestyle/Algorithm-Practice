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