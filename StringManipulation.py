"""
Day 4: 30DaysPythonChallenge

String manipulation.
"""

# Slicing strings.
language = 'Python'
first_three = language[0:3]
print(first_three)

last_three = language[3:]
print(last_three)

# Another way.
last_three = language[-3:]
print(last_three)



# Reverse a string.
greeting = 'Hello, World!'
reversed_string = greeting[::-1]
print(reversed_string)


# Skipping characters while slicing.
language = 'Python'
pto = language[0:6:2]
print(pto)