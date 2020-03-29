#!/usr/bin/python
# This python script serves as an example to reference
# while learning/re-learning python. There will be different
# Sections added and they will be labeled accordingly.

#---------------------------#
# Object and Data Structure #
#---------------------------#
my_string = 'String'
my_second_string = 'String 2'
my_third_string = "There's an single quote in here!"
my_fourth_string = '"Python is cool"'
my_math_variable = 5*10
my_list = [1,2,3,4,5]
my_second_list = [6,7,8]
my_dictionary = {'key1':'value1','key2':'value2'}
my_dictionary_fmt = {'apple':2.25,
                     'bread':5.99,
                     'milk':4.80}
my_flex_dictionary = {'key':'value',           # Key value pair
                      'keylist':[1,2,3],       # Key contains list as value. Can pull from list like: my_flex_dictionary['keylist'][2]
                      'kik':{'insidekey':100}, # Key inside of key (call using my_flex_dictionary['kik']['insidekey']
                      'ree':['one', 'two', 'three']}                                                 # ^ returns 100
my_tuple = (1,2,3)


# Strings, indexing, and slicing
#-------------------------------#
# Print string variable...
print(my_fourth_string)

# Print tri from the word string...
print('string'[1:4])

# Print ring from the word string...
print('string'[2::])


# Concatenation - merging
#-------------------------------#
# Concatenate lists...
print(my_list + my_second_list)


# Using methods
#-------------------------------#
# Print uppercase variable with method...
print(my_third_string.upper())

# Methods, append 9...
my_second_list.append(9)
print(my_second_list)

# Methods, remove 9...
my_second_list.pop()
print(my_second_list)

# Using the sort method to sort lists...
my_third_list = ['a','e','x','b','c']
print(my_third_list)
my_third_list.sort() # Actually sorts variable assigning new sorted var.
print(my_third_list)

my_num_list = [4,1,8,3]
print(my_num_list)
my_num_list.sort() # Actually sorts variable assigning new sorted var.
print(my_num_list)

# Reverse method...
my_third_list.reverse() # Actually reverses variable assigning new reversed var.


# Math and numbers
#-------------------------------#
# Print number variable (integer)...
print(my_math_variable)

# Do math with variable and set new variable (float)...
my_math_variable_2 = my_math_variable / 11
print(my_math_variable_2)

# Use float formatting... "{value:width:precision f}"
print("The formatted result is {r:4.2f}".format(r=my_math_variable_2))


# Print formatting
#-------------------------------#
# Print formatting examples...
print('Python formatting {}'.format('rules!'))
name = "Sam"
age = 3
print(f'{name} is {age} years old.')


# Dictionaries
#-------------------------------#
# Print entire dictionary...
print(my_dictionary)

# Print key1 value...
print(my_dictionary['key1'])
print(my_dictionary_fmt['milk'])

# Print specific from list and format with method...
print(my_flex_dictionary['ree'][2].upper())

# Add new key value pair to dictionary...
my_flex_dictionary['newkey'] = 300
print(my_flex_dictionary)

# List all keys in dictionary...
print(my_dictionary_fmt.keys())

# List all values...
print(my_dictionary_fmt.values())


# Tuples (Immutable)
#-------------------------------#
# Tuples are like lists, but immutable and have less methods...
t2 = ('one', 2, 'one')
print(t2)

# Count instances of 'one' in t2...
print(t2.count('one'))

# Show index of where 'one' appears in tuple the first time...
print(t2.index('one'))