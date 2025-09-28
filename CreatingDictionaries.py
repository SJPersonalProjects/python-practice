"""
Day 8: 30DaysPythonChallenge

Working with dictionaires.
"""

# Creating a dictionary.
person = {
    'first_name':'Sarim',
    'last_name':'Jokhio',
    'age':250,
    'country':'Japan',
    'is_married':False,
    'skills':['Bash', 'Linux', 'Python'],
    'address':{
        'street':'space market',
        'zipcode': '02210'
    }
}


# Checking the length of a dictionary.
print(len(person))


# Accessing dictionary items.
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
# print(person['city']) KeyError: 'city'
print(person.get('city')) # This way, it doesn't throw error.


# Adding items to a dictionary.
person['job_title'] = 'Instructor'
person['skills'].append('Java')
print(person)


# Modifying items in a dictionary.
person['first_name'] = 'Mohammed'
person['age'] = 69

print(person['first_name'])
print(person['age'])


# Checking keys in a dictionary.
print('first_name' in person)
print('skills' in person)



# Removing keys and value pairs from a dictionary.
person.pop('country') # removes the country.
print(person)

person['height'] = 5.9
print(person)

person.popitem() # Removes the last item which is height.
print(person)

del person['last_name'] # Removes the last name from the dictionary.
print(person)


# Changing dictionary to a list items.
print('\n\n', person.items())


# Clearing a dictionary.
print(person.clear())


# Deleting a dictionary.
del person
# print(person) NameError: 'person' is not defined.


# copying a dictionary.
person = {
    'first_name':'Sarim',
    'last_name':'Jokhio',
    'age':250,
    'country':'Japan',
    'is_married':False,
    'skills':['Bash', 'Linux', 'Python'],
    'address':{
        'street':'space market',
        'zipcode': '02210'
    }
}

employee = person.copy()
print(employee)


# Getting dictionary keys as a list.
keys = person.keys()
print(keys)


# Getting dictionary values as a list.
values = person.values()
print(values)

