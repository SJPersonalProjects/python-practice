"""
Day 10: 30DaysPythonChallenge

Working with loops.
"""

# While loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
print('Loop is done!')


# # While with else.
# # Guess the secret number.
secret_number = 7
attempts = 0

while attempts < 3:
    guess_number = int(input('Guess the number (1-10):'))
    if guess_number == secret_number:
        print('You guessed it right!')
        break
    attempts = attempts + 1
else:
    print('Sorry, you used all your attemps!')



# For loop with a list.
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)


# For loop with string.
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


# For loop with tuple.
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# For loop with a dictionary.
person = {
    'first_name':'Sarim',
    'last_name':'Jokhio',
    'age':24,
    'country':'Pakistan',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street':'Space street',
        'zipcode':'02210'
    }
}


for key in person:
    print(key)

for key, value in person.items():
    print(key, value)


# Loops in set.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


# the range function.
list_ = list(range(11))
print(list_)

st = set(range(1, 11))
print(st)

list_ = list(range(0, 11, 2))
print(list_)

st = set(range(1, 11, 2))
print(st)


for number in range(11):
    print(number)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)


# Print message when the loop ends.
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)