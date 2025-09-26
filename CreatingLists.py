"""
Day 5: 30DaysPythonChallenge

Creating and manipulating lists.
"""

# Creating lists.
empty_list = list() # It's an empty list.
print(len(empty_list))

another_empty_list = []
print(len(another_empty_list))


# Using len() method to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Now, printing the lists and its lengths
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web Techs:', web_techs)
print('Number of web techs:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))


# Lists can have items of different data-types.
new_list = ['Sarim', 24, True, {'country':'Pakistan', 'city':'Hyderabad'}]


# Unpacking lists.
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest) # It's a list.

# Unpacking another example.

first, second, third, fourth, *rest = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(first)
print(second)
print(third)
print(fourth)
print(rest)


# Slicing items from a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
# This also gets all fruits from the list.
full_bucket = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:4]
orange_and_lemon = fruits[::2]

# Negative indexing.
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
print(all_fruits)
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruit = fruits[::-1] # Negative stepping will reverse it.
print(reverse_fruit)


#Modifying lists.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) -1
fruits[last_index] = 'lime'
print(fruits)


# Checking items in a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)


# Adding items to a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)


# Inserting items into a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)


# Removing items from a list.
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)


# Removing items using pop()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop() # removes the last item.
print(fruits)

fruits.pop(0) # removes the item at a given index.
print(fruits)



# Removing items using del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0] # removes the item at a given index.
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3] # removes the items at a given range.
print(fruits)
del fruits # removes the whole list.
# print(fruits) Gives the NameError.



# Clearing list items.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear() # empties the list.
print(fruits)


# Copying a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy() # Copies the list from fruits to fruits_copy
print(fruits_copy)



# Joining lists.
# Using (+) operator.
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables # It joins the lists.
print(fruits_and_vegetables)

# Joining lists.
# Using extend() method.
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)



# Counting items in a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) # returns the numbers of times 'orange' appears in a list.
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) # 3.



# Finding index of an item.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange')) 
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) # the first occurrance.



# Reversing a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse() # Reverses the list.
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)



# Sorting list items.
# sort() method.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) # sorted in alphabetical order.
fruits.sort(reverse=True)
print(fruits) # It sorts and then reverse the list items.
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)


# sorted() method.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
# Reverse order.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)


