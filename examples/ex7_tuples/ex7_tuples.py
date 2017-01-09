# File: ex7_tuples.py
# Author: A. Laszlo Lazuer
# Date: 01/08/17
# Python Version: 2.7
# Description: A demonstration of dictionaries in Python

##Note
# In Python tuples are similar to lists, however,
# unlike lists they are immutable meaning they can not be changed.
# You would use tuples to preset things that shouldn't be changed,
# such as days of the week, or dates on a calendar.
##

# How to construct a tuple
#List: l = [1,2,3]

#tuple
t = (1,2,3)

print t

#tuple length
len(t)

#Redefine
t=('one',2)

print t

#Index a tuple
print t[1]

#Slicing a tuple
##grab the last item
print t[-1]

#Method for tuple

## Find the index of an item in the tuple
print t.index('one')

# Index
print t.index(2)

# Count items in tuple
print t.count('one')

## Redefine
print t.count(1)

##Immutability makes tuples unique

#Redefine l
#list
l = [1,2,3]
## Will support item assignment
#IE
l[0] = 's'


#tuple
t = (1,2,3)

#Item assingment not supported
#t[0]='s' #Will throw an error

##Lists has more support for methods.

##Why would you use a tuple?
# If you are dending on data that you do not want to change.
# I.E. Dates of a calendar, whenever you need immutable data.
# A tuple is ideal for these scenarios.
##
