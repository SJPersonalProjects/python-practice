"""
Day 4: 30DaysPythonChallenge

String methods.
"""

# capitalize()
challenge = 'thirty days of python'
print(challenge.capitalize())

# count()
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# endswith()
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# expandtabs()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))


# find()
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# format()
first_name = 'Sarim'
last_name = 'Jokhio'
age = 24
job = 'programmer'
country = 'Pakistan'
sentence = 'I am {} {}. I\'m a {}. I\'m {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence)

# index()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
# print(challenge.index(sub_string, 9)) # Causing value-error.

# rindex()
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
# print(challenge.rindex(sub_string, 9)) # Causing value-error.
print(challenge.rindex('on', 8))


# isalnum()
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirty days of python 2025'
print(challenge.isalnum())


#isalpha()
challenge = 'thirty days of python'
print(challenge.isalpha())
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
num = '123'
print(num.isalpha())


# isdecimal()
challenge = 'thirty days of python'
print(challenge.isdecimal())
challenge = '123'
print(challenge.isdecimal())
challenge = '\u00B2'
print(challenge.isdecimal())
challenge = '12 3'
print(challenge.isdecimal())



#isdigit()
challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())


# isnumeric()
num = 10
print(str(num).isnumeric())
num = '\u00BD'
print(num.isnumeric())
num = '10.5'
print(num.isnumeric())

# isidentifier()
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
challenge = 'thirty days of python'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python_30'
print(challenge.isidentifier())


#islower()
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

# isupper()
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())


#join()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)



# strip()
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))


# replace()
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))


#split()
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(' '))



#title()
challenge = 'thirty days of python'
print(challenge.title())


# swapcase()
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())


# startswith()
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))

challenge = '30 days of python'
print(challenge.startswith('thirty'))