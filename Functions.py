"""
Exercise 11: 30DaysPythonChallenge.

Working with Functions.
"""

# Functions without parameters.
# Full name generator.
def generate_full_name():
    first_name = "Sarim"
    last_name = "Jokhio"
    full_name = first_name + " " + last_name
    print(full_name)

generate_full_name()

# Addition
def add_two_numbers():
    number_one = 10
    number_two = 20
    total = number_one + number_two
    print(total)

add_two_numbers()


# Functions returning values.
def generate_full_name():
    first_name = "Sarim"
    last_name = "Jokhio"
    full_name = first_name + " " + last_name
    return full_name

print(generate_full_name())

def add_two_numbers():
    value_one = 2
    value_two = 3
    total = value_one + value_two
    return total

print(add_two_numbers())


# Functions with Parameters.
def greetings(name):
    message = name + ", welcome to Python for everyone!"
    return message

print(greetings("Sarim"))

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(90))

def square_number(x):
    return x * x

print(square_number(8))

def area_of_circle(r):
    PI = 3.1415
    area = PI * r ** 2
    return area
print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)
    
sum_of_numbers(7)

def generate_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

print("Full name is: ", generate_full_name("Sarim", "Jokhio"))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print("Sum of two numbers: ", sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print("My age is: ", calculate_age(2025, 2001))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + "N" # the value has to be changed to a string first
    return weight
print("Weight of an object in Newtons: ", weight_of_object(100, 9.81))


# Passing arguments with key and value pairs.
def print_fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

print(print_fullname(last_name="Jokhio", first_name="Sarim"))


# Returning String.
def full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

print("Full name is: ", full_name(last_name="Jokhio", first_name="Sarim"))


# Returning numbers.
def add_values(value_one, value_two):
    total = value_one + value_two
    return total

print(add_values(value_two=13, value_one=7))


# Returning a boolean.
def is_even(n):
    if n % 2 == 0:
        print("Even")
        return True
    return False

print(is_even(10))
print(is_even(7))


# Returning a list.
def find_even_numbers(n):
    even = []
    for i in range(n + 1):
        if i % 2 == 0:
            even.append(i)
    return even

print(find_even_numbers(10))


# Default parameters.
def greetings(name="Peter"):
    message = name + ", welcome to Python for Everyone!"
    return message
print(greetings())
print(greetings("Sarim"))


# Arbitrary number of arguments.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total
print(sum_all_nums(2, 5, 13, 7))


