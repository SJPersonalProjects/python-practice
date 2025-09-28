"""
Day 8: 30DaysPythonChallenge

Exercises:_

. Create an empty dictionary called dog
. Add name, color, breed, legs, age to the dog dictionary
. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
. Get the length of the student dictionary
. Get the value of skills and check the data type, it should be a list
. Modify the skills values by adding one or two skills
. Get the dictionary keys as a list
. Get the dictionary values as a list
. Change the dictionary to a list of tuples using items() method
. Delete one of the items in the dictionary
. Delete one of the dictionaries
"""

# Empty dictionary.
dog = dict()

# Another empty dictionary.
another_dog = {}

dog['name'] = 'Spike'
dog['color'] = 'Grey'
dog['breed'] = 'Pakistani'
dog['legs'] = 4
dog['age'] = 3

print(dog)


# student dictionary.
resident = {
    'first_name':'Khalid',
    'last_name':'Marwan',
    'gender':'male',
    'age':99,
    'marital_status':'Married',
    'skills':['shepard', 'milk-seller', 'cook'],
    'country':'Syria',
    'city':'Holmes',
    'address': {
        'town':'Al-Noor',
        'street':'Tareeq-al-wahid'
    }
}

print(len(resident)) # length of the resident.

print(resident['skills']) # values of the skills.
print(type(resident['skills'])) # type of the values of skills.

# Adding 2 more skills to resident.
resident['skills'].append('hunting')
resident['skills'].append('archery')

print(resident['skills'])


# Get the dictionary keys as a list.
print(resident.keys())


# Get the dictionary values as a list.
print(resident.values())

# Changing the dictionary to a list of tuples.
print(resident.items())


# Deleting one of the items from a dictionary.
del resident['marital_status']
print(resident)


# Deleting a dictionary.
del resident
# print(resident) NameError: 'resident' is not defined.
