"""
Day 2: 30DaysPythonChallenge

. Declare a first name variable and assign a value to it
. Declare a last name variable and assign a value to it
. Declare a full name variable and assign a value to it
. Declare a country variable and assign a value to it
. Declare a city variable and assign a value to it
. Declare an age variable and assign a value to it
. Declare a year variable and assign a value to it
. Declare a variable is_married and assign a value to it
. Declare a variable is_true and assign a value to it
. Declare a variable is_light_on and assign a value to it
. Declare multiple variable on one line

. Check the data type of all your variables using type() built-in function
. Using the len() built-in function, find the length of your first name
. Compare the length of your first name and your last name
. Declare 5 as num_one and 4 as num_two
. Add num_one and num_two and assign the value to a variable total
. Subtract num_two from num_one and assign the value to a variable diff
. Multiply num_two and num_one and assign the value to a variable product
. Divide num_one by num_two and assign the value to a variable division
. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
. Calculate num_one to the power of num_two and assign the value to a variable exp
. Find floor division of num_one by num_two and assign the value to a variable floor_division

"""

first_name = 'Sarim'
last_name = 'Jokhio'
country_name = 'Pakistan'
city_name = 'Hyderabad'
age = 24
year = 2025
is_married = False
is_true = False
is_light_on = True
is_laptop_on, is_phone_on, is_code_working = True, False, False

# Checking data-type of all the above variables.
print(type(first_name))
print(type(last_name))
print(type(country_name))
print(type(city_name))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(is_laptop_on), type(is_phone_on), type(is_code_working))

# Finding the length of first_name variable.
print(len(first_name))
print(len(first_name) == len(last_name))

# Variables.
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_two ** num_one
floor_division = num_one // num_two


radius = input('Enter the radius: ')

area_of_circle = 3.1415 * (int(radius) ** 2)
circum_of_circle = 2 * 3.1415 * int(radius)
print('Area of a circle: ', area_of_circle)
print('Circumference of a circle: ', circum_of_circle)


# Updating the variables.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country_name = input('Enter your country: ')
age = input('Enter your age: ')

print(help('keywords'))


