"""
30DaysPythonChallenge: Lambda Functions.
"""

# Named function.
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))


# Lambda function.
add_three_nums = lambda a, b, c: a + b + c
print(add_three_nums(1, 2, 3))


square = lambda x : x ** 2
print(square(3))


cube = lambda x : x ** 3
print(cube(3))

# Multiple variables.
multiple_variables = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variables(5, 5, 3))


# Lambda functions inside another function.
def power(x):
    return lambda n:x ** n

cube = power(2)(3)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)