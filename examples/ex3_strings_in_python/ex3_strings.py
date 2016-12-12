# file: ex3_strings.py
# Author: A. Laszlo Lazuer
# date: 12/12/16
# Python Version: 2.7
# description: Examples demoing how to use strings in Python

#You can use double quotes "" or single quotes ''

print 'Hello'

print 'This is also a string'

print "This is a string"

print "The use case for using sinle over double, lies in allowing for the use of the other type within a string."

print ' Example: "This is a quote" '

#Printing a new line in Python
print 'Here is a new line \nand here is the second line'

#Tabbing in Python
print 'Here is a new line \n\tand here is the second line tabbed'

#String Length
print len('Hello World')

#Using a variable with strings
s = 'Hello World'
print s

#Indexing in Python
## As in Java & JavaScript Indexing begins at 0 in Python
print s[0]
print s[1]

#Slicing a string
##No change to the original string

##Grab everything from
print s[1:] #Python will look at the s object, then grab from the 1 index, : (onwards)

##Grab everything up to
print s[:3] #This will grab everything from 0 -> 3

#Grabbing everything
print s[:]

#Indexing in reverse
print s[-1]  #Loops backwards and grabs the last letter

##Grabbing everything but the last letter
print s[:-1]

#Step size default is 1 in Python

##Changing the step size

print s[::1] #Grabbs everything "::" with step size of "1"
print s[::2] #Grabbs everything "::" with step size of "2"

#Printing a string backwards
print s[::-1] #This will tell Python to traverse the string backwards

#Immutability
##Strings have a property immutability, once the string is created.
##The elements within it can not be changed or destroyed.

#Assumption
#s[0] = 'x' #Not allowed!

# Traceback (most recent call last):
#   File "ex3_strings.py", line 70, in <module>
#     s[0] = 'x'
# TypeError: 'str' object does not support item assignment

#While you can not change a string you can concatenate strings

print s + ' concatenate me!'

#You can redefine your string variables
s = s + ' concatenate me!'
print s

#Using Arithmetic symbols with strings

letter = 'z'

#The multiplication * will repeate the string x ammount of times
print letter*10

#Actions or commands on objects

s = 'Hello'

#Syntax for methods on objects label_name.method

#Capitalize string
print s.upper()

#Lower case string
print s.lower()

#Split a string
print s.split() #Returns a list

#You can split by an elements
print s.split('e') #This will split the string at char e
