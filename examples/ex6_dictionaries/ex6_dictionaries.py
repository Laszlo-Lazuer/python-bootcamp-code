# File: ex6_dictionaries.py
# Author: A. Laszlo Lazuer
# Date: 12/13/16
# Python Version: 2.7
# Description: A demonstration of dictionaries in Python

#Example list
l = [1,2,3]
print l

#Index a list
print l[0]

#Dictionary consists of a key and an associated value

##Example Dictionary
my_dict = {'key1':'value','key2':'value2'}
print my_dict

##Square brackets can be used to access keys
#my_dict[0] #Will not work because it is not a sequence it is a mapping

print my_dict['key1']

##New Dictionary
my_dict = {'k1':123,'k2':3.4,'k3':'string'}
print my_dict['k3']

##Based on output we can call different methods
print my_dict['k3'].upper() #We can manipulate the object

print my_dict['k1'] - 120 #Subtract

##Value not stored
print my_dict['k1'] - 120 #Subtract

##Storing new Value
my_dict['k1'] = my_dict['k1'] - 120 #Subtract
print my_dict

##Self Subtraction/Addition/...
my_dict['k1'] = my_dict['k1'] + 100
print my_dict['k1']

# my_dict = {'k1':123,'k2':3.4,'k3':'string'}
my_dict['k1'] += 100 #These two are the same
print my_dict['k1']

#Creating Keys by assignment
## Empty Dictionary
d = {}
print d

d['animal'] = 'Dog'
d['answer'] = 42
print d

#Nesting dictionaries
d = {'k1':{'nestkey': {'subnestkey':'value'}}}
print d

##Accessing the inner value
print d['k1']['nestkey']['subnestkey']

##Applying a method
print d['k1']['nestkey']['subnestkey'].upper()

#Dictionary methods built into Python 2.7
d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
print d

#Method for Keys
print d.keys()

##Dictionaries are never going to hold a specific order, IE NO indexing
##Lists and Strings can be indexed as they are Sequences

#Method for values
print d.values()

#Return a mix of both keys and values
print d.items() #Tuples

##Summary Notes:
##Dictionaries are Mappings in Python, they reffer to their contents by keys.
##Key value pair system.  They are flexible in regards to the data types they
##can hold.  Shorthand Addition/Subtraction is also known as quick notation.
