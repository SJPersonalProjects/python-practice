"""
Day 7: 30DaysPythonChallenge

Working on Sets.
"""

# Creating set.
set_items = set() # It's an empty set.

# Set containing values.
set_items = {'value_1', 'value_2', 'value_3', 'value_4'}


# Getting length of a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))


# Checking an item in a set.
vegetables = {'Potato', 'Tomato', 'Cabbage', 'Lady Finger', 'Cucumber', 'Cauli Flower'}
print("Is Cauli Flower available? ", 'Cauli Flower' in vegetables)


# Adding items to a set.
countries = {'Pakistan', 'Finland', 'Japan', 'Canada', 'Malta', 'N. Korea', 'S. Korea'}
countries.add('China')
print(countries)

# Add multiple items.
countries.update(['Norway', 'Iceland', 'Russia', 'Lithuania', 'Latvia', 'Switzerland'])
print(countries)


# Removing items from a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop(), ' Removed')
print(fruits)


# Clearing items in a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)


# Deleting a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# print(fruits) # Gives a NameError.


# Converting a list to a set.
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(fruits)


# Joining sets.
brothers = {'Uthman', 'Ali', 'Abu Bakr', 'Omar'}
sisters = {'Ayesha', 'Khadija', 'Sarah', 'Habiba'}
siblings = brothers.union(sisters)
print(siblings)


# update() method inserts a set into a given set.
parents = {'Adam', "Hawwa"}
siblings.update(parents)
print(siblings)


# Finding a set of items which are in both sets intersection().
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

# Another example.
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon))



# Checking subset and super set.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.issuperset(dragon))



# Checking the difference between two sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))



# Finding symmetric difference between the two.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))



# Joining sets.
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))




