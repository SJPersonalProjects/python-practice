"""
Day 9: 30DaysPythonChallenge

Working with conditionals.
"""

# if statement.
a = 3
if a > 0:
    print('A is positive number')


# if else statement.
a = 4
if a < 0:
    print('A is a negative number.')
else:
    print('A is a positive number')


# if elif else statements.
a = 0
if a > 0:
    print('A is a positive number.')
elif a < 0:
    print('A is a negative number.')
else:
    print('A is zero')


# Short hand.
a = 3
print('A is positive') if a > 0 else print('A is negative')



# Nested conditions.
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer.')
    else:
        print('A is a positive number.')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative integer.')



# if conditions with logical operators.
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer.')
elif a > 0 and a % 2 != 0:
    print('A is a positive and odd integer.')
elif a == 0:
    print('A is a zero.')
else:
    print('A is a negative integer.')



# if and Or logical operators.
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access deined :(')