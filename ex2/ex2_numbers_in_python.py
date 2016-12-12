__author__ = "Laszlo Lazuer"
__credits__ = ["Laszlo Lazuer"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Laszlo Lazuer"

print 'Numbers in Python'

print 'Basic Arithmetic'

#Addition
print 2+1
print 2+2

#Subtraction
print 2-1
print 3-2

#Multiplication
print 2*2
print 3*2

#Division
print 'Division in Python 2 we use Classic division truncates the remainder.  Python 3 will show true division'
print 3/2

#Floating point issue workaround
#Deine one value as a float
print 3.0/2

print 2.0/3

#Cast a number as a float
print float(3)

#Import features from Python 3 must be at the top of the file.
#from __future__ import division
#print 3/2

#Powers
#Double Asterisk

print 2**3
print 4**5
print 4**0.5

#PEMDAS Order of operations

print 2 + 10 * 10 + 3

##This means you can use traditional arithmetic formatting, such as parenthesis to define order of execution.

print (2+10)*(10+3)

#Variables
a = 5
print a

a = 10
print a

#Re-using variable to assign to itself

a = a+a

print a

#Exmample of utilization of variables

my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
print my_taxes



