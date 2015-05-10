# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

numTests = int(input())
for i in range(numTests):
    t1 = datetime.datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print(abs(int(datetime.timedelta.total_seconds(t1 - t2))))