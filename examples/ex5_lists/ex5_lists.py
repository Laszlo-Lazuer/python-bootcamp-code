# file: ex5_lists.py
# Author: A. Laszlo Lazuer
# date: 12/12/16
# Python Version: 2.7
# description: A demonstration of lists in Python

print 'Lists'

#Assign a list to a variable
##Lists are constructed with square brackets and are comma delimited

my_list =  [1,2,3]

print my_list

#Lists can contain different object types
my_list = ['string',23,1.2,'o']
print my_list #You can mix and match different object types

#List Length
print len(my_list)

#Indexing & Slicing

my_list = ['one','two','three',4,5]
print my_list[0] #This will grab the element at index 0 = one

##Grabbing index 1 and everything past it
print my_list[1:]

##Grabbing everything up to index 3
print my_list[:3]

#Concatenation of string
print 'hello' + 'world'

#Concatenation of a List
print my_list + ['new item'] #Appends to the end of the list

#To save a modified list
my_list = my_list + ['permanent add']
print my_list

#Multiplication of a list
print my_list *2 #Prints the list twice over, not permanent

#Lists in python tend to be more flexible than arrays in
#other languages.  1. No fixed size constraint, 2. They have no type constraint.

#Methods for Lists
l = [1,2,3]
print l

##Append
l.append('append me')
print l

#Pop
print l.pop() #Will return the last item in the list and remove it from the list.
print l

##Specifying an index to pop
x = l.pop(0)
print x
print l #Will return the remaining items in the list

#Sort & Reverse
new_list = ['a','e','x','b','c']
print new_list

#Reverse
new_list.reverse()
print new_list

#Sort
new_list.sort()
print new_list

#Data structures in Python support nesting

#Nesting
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

##List inside of a list
matrix = [l_1,l_2,l_3]
print matrix

#Indexing Two levels
print matrix[0][0]
print matrix[1][1]
print matrix[2][0]

#List comprehensions
first_col = [row[0] for row in matrix]
print first_col
