# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

def print_complex(real, im):
    if real == 0 and im == 0: # print 0
        print '0.00'
    elif im == 0: # print only real part
        print "{0:.2f}".format(real)
    elif real == 0: # print only imaginary part
        sign = '' if im > 0 else '-'
        print sign + "{0:.2f}".format(abs(im)) + "i"
    else: # print both
        operator = ' + ' if im > 0 else ' - '
        print "{0:.2f}".format(real) + operator + "{0:.2f}".format(abs(im)) + "i"

def print_sum(C, D):
    real = C[0] + D[0]
    im = C[1] + D[1]
    print_complex(real, im)

def print_diff(C, D):
    real = C[0] - D[0]
    im = C[1] - D[1]
    print_complex(real, im)

def print_prod(C, D):
    real = C[0] * D[0] - C[1] * D[1]
    im = C[0] * D[1] + C[1] * D[0]
    print_complex(real, im)
    
def print_quot(C, D):
    real = (C[0] * D[0] + C[1] * D[1]) / (D[0]*D[0] + D[1]*D[1])
    im  = (C[1] * D[0] - C[0] * D[1]) / (D[0]*D[0] + D[1]*D[1])
    print_complex(real, im)
    
def print_mod(C):
    mod = sqrt(C[0]**2 + C[1]**2)
    print "{0:.2f}".format(mod)
        
C = tuple(map(float, raw_input().split()))
D = tuple(map(float, raw_input().split()))

print_sum(C, D)
print_diff(C, D)
print_prod(C, D)
print_quot(C, D)
print_mod(C)
print_mod(D)