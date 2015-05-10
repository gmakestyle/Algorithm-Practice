# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
width = len(bin(N)[2:])
for i in xrange(1, N+1):
    dec = str(i)
    row = (width - len(dec)) * ' ' + dec + ' '
    octal = oct(i)[1:]
    row += (width - len(octal)) * ' ' + octal + ' '
    hexa = hex(i)[2:].upper()
    row += (width - len(hexa)) * ' ' + hexa + ' '
    bina = bin(i)[2:]
    row += (width - len(bina)) * ' ' + bina
    print row