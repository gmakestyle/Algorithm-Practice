# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

class ComplexNumber(object):
	
	def __init__(self, num):
		self.real = num[0]
		self.imaginary = num[1]
		
	def mod(self):
		return sqrt(self.real**2 + self.imaginary**2)
	
	def __add__(self, other):
		assert isinstance(other, ComplexNumber)
		real = self.real + other.real
		im = self.imaginary + other.imaginary
		return ComplexNumber((real, im))
	
	def __sub__(self, other):
		assert isinstance(other, ComplexNumber)
		real = self.real - other.real
		im = self.imaginary - other.imaginary
		return ComplexNumber((real, im))
	
	def __mul__(self, other):
		assert isinstance(other, ComplexNumber)
		real = self.real * other.real - self.imaginary * other.imaginary
		im = self.real * other.imaginary + self.imaginary * other.real
		return ComplexNumber((real, im))
		
	def __div__(self, other):
		assert isinstance(other, ComplexNumber)
		real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real**2 + other.imaginary**2)
		im  = (self.imaginary * other.real - self.real * other.imaginary) / (other.real**2 + other.imaginary**2)
		return ComplexNumber((real, im))
		
	def __str__(self):
		return repr(self)
	
	def __repr__(self):
		real, im = self.real, self.imaginary
		if real == 0 and im == 0: # print 0
			return '0.00'
		elif im == 0: # print only real part
			return "{0:.2f}".format(real)
		elif real == 0: # print only imaginary part
			sign = '' if im > 0 else '-'
			return sign + "{0:.2f}".format(abs(im)) + "i"
		else: # print both
			operator = ' + ' if im > 0 else ' - '
			return "{0:.2f}".format(real) + operator + "{0:.2f}".format(abs(im)) + "i"
        
C = ComplexNumber(map(float, raw_input().split()))
D = ComplexNumber(map(float, raw_input().split()))

print C + D
print C - D
print C * D
print C / D
print "{0:.2f}".format(C.mod())
print "{0:.2f}".format(D.mod())