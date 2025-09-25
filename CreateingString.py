"""
Day 4: 30DaysPythonChallenge

Creating string.
"""

letter = 'p'
print(letter)
print(len(letter)) # 1
greeting = 'Hello, World!'
print(greeting)
print(len(greeting)) #13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Multi-line strings.
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as wmpowering people.
That is why I created 30 days of Python.'''
print(multiline_string)

# Another way of doing this same thing.
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of Python."""
print(multiline_string)

# String concatenation.
first_name = 'Sarim'
last_name = 'Jokhio'
space = ' '
full_name = first_name + space + last_name
print(full_name)

# Checking the length of a string using len() built-in function.
print(len(first_name))
print(len(last_name))
print(len(full_name) > len(last_name))
print(len(full_name))

# Escape sequences with String.
print('I hope everyone is enjoying the Python Challenge.\nAre you?')
print('Days\tTopics\tExercises') #adding tab space or 4 spaces.
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')

# String formatting.
first_name = 'Sarim'
last_name = 'Jokhio'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a /b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


# String and numbers.
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}'.format(radius, area)
print(formated_string)

# String interpolation or f-string.
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Unpacking String.
language = 'Python'
a, b, c, d, e, f = language # This unpacks the string language.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Strings and index.
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# another way to see it.
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)