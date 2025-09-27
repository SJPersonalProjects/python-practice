"""
Day 6: 30DaysPythonChallenge

Exercises:_
Level 1:

. Create an empty tuple
. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
. Join brothers and sisters tuples and assign it to siblings
. How many siblings do you have?
. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

"""

# An empty tuple.
fruits = ()

# Tuple containing brothers names.
brothers = ('Abdullah', 'Uthman', 'Omar', 'Abu Bakr', 'Ali', 'Zubair', 'Khalid')
sisters = ('Ayesha', 'Radiya', 'Fatima', 'Zahra', 'Sidra', 'Sana')

siblings = brothers + sisters
print('Numbers of my siblings: ', len(siblings))

family_members = list(siblings)
family_members[0] = 'Ibrahim'
family_members[1] = 'Sarah'

family_members = tuple(family_members)
print(family_members)




"""
Day 6: 30DaysPythonChallenge

Exercises:_
Level 2:

. Unpack siblings and parents from family_members
. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
. Change the about food_stuff_tp tuple to a food_stuff_lt list
. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
. Slice out the first three items and the last three items from food_staff_lt list
. Delete the food_staff_tp tuple completely
. Check if an item exists in tuple:
. Check if 'Estonia' is a nordic country

. Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

"""

# Unpacking parents and siblings.
father, mother, *siblings = family_members
print('Parents: ', father + ' ' + mother)
print('Siblings: ', siblings)


fruits = ('banana', 'mango', 'orange', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Lettuce')
animal_products = ('milk', 'meat', 'bread', 'cheese')

food_stuff_tuple = fruits + vegetables + animal_products

# Changing tuple to a list.
food_stuff_list = list(food_stuff_tuple)

print(food_stuff_list)

print('Middle 2 items from list: ', food_stuff_list[4:6])
print('First three items: ', food_stuff_list[:3])
print('Last three items: ', food_stuff_list[-3:])

del food_stuff_tuple # deletes the tuple entirely.

fruit_bucket = ('banana', 'mango', 'orange', 'peach', 'pomogranate', 'strawberry')
print('Does strawberry exist in in fruit\'s bucket? ', 'strawberry' in fruit_bucket)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia is nordic country?: ', 'Estonia' in nordic_countries)
print('Iceland is nordic country?: ', 'Iceland' in nordic_countries)
