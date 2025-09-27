"""
Day 6: 30DaysPythonChallenge

Creating and manipulating tuples.
"""

# Empty tuples.
empty_tuple = ()
# Tuple constructor.
empty_tuple = tuple()



# Tuple with values.
fruits = ('banana', 'orange', 'mango', 'lemon')


# Checking tuple length.
cities = ('New York', 'Manchester', 'London', 'Tehran', "DC")
print(len(cities))


# Tuple items.
vegetables = ('Tomato', 'Potato', 'Lady Finger', 'Cabbage', 'Lattuce')
first_vegetable = vegetables[0]
second_vegetable = vegetables[1]

print(first_vegetable)
print(second_vegetable)

last_index = len(vegetables) -1 
print(last_index)
last_vegetable = vegetables[last_index]
print(last_vegetable)


# Negative indexing.
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)



# Slicing out tuples (positive indexes)
students = ('Tobby', 'Mark', 'Ryan', 'Abdullah', 'Mohammed', 'Uthman')
print('All students: ', students[0:6])

print('All students: ', students[0:])

middle_students = students[2:4]
print('Middle 2 students: ', middle_students)


# Slicing out tuples (negative indexes)
fruits = ('banana', 'orange', 'mango', 'lemon')
print('All fruits: ', fruits[-4:])
print('Orange and mango: ', fruits[-3:-1])
print('Orange to the rest: ', fruits[-3:])


# Changing tuples to lists.
# Tuples are immutable so to modify them we should change them to lists.
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print('Tuple is now a list? ', type(fruits))
fruits[0] = 'Apple'
print(fruits)
fruits = tuple(fruits)
print('List is now a tuple? ', type(fruits))
print(fruits)



# Checking an item in a tuple.
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
# fruits[0] = 'apple' # Gives an TypeError: 'tuple' object doesn't support item assignment.



# Joining tuples.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)



# Deleting tuples.
# It's not possible to remove/delete an item from tuples because they are immutable.
# But it's possible to delete a tuple entirely.
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# print(fruits) # NameError: name 'fruits' is not defined.

