# file: ex4_print_formatting.py
# Author: A. Laszlo Lazuer
# date: 12/12/16
# Python Version: 2.7
# description: A demonstration of print formatting in Python

#Basic string print
print 'This is a string'

#Formatted string print
x = 13.13

print 'Place my variable here: %s' %(x)

#Printing floating point Numbers

#The precision is defined after the decimal, for fractions.
print 'Floating point number: %1.2f' %(13.145)

#Conversion format methods

##Convert to string
print 'Convert to string %s' %(123) #You can also use %r instead of %s

#Using more than one variable in your strings

print 'First: %s, Second: %s, Third %s' %('hi!','two', 3)

#*Note: ^ The order in which the variables are called define the order displayed.

print 'First: %s, Second: %s' %(2,2)

#Format method
##This allows you to change the order
print 'First: {x} Second: {x}'.format(x='inserted')

#You know longer need to worry about formatting the print order this way.
print 'First: {x} Second: {y} Third: {x}'.format(x='inserted', y='two!')
