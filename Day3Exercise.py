"""
Day 3: 30DayPythonChallenge

. Declare your age as integer variable
. Declare your height as a float variable
. Declare a variable that store a complex number
. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
. Use and operator to check if 'on' is found in both 'python' and 'dragon'
. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
. There is no 'on' in both dragon and python
. Find the length of the text python and convert the value to float and convert it to string
. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
. Check if type of '10' is equal to type of 10
. Check if int('9.8') is equal to 10
"""

age = 24
height = 5.5
complex_number = 1 + 2j

print('Area of Triangle:_')
base = input('Enter base value: ')
height = input('Enter height value: ')
area_of_triangle = 0.5 * int(base) * int(height)
print('Triangle area: ', area_of_triangle)


print('__________________________________________________________')

print('Calculate the perimeter of Triangle:_')
value_one = input('Enter side "a" of triangle: ')
value_two = input('Enter side "b" of triangle: ')
value_three = input('Enter side "c" of triangle: ')
print('The perimeter of triangle: ', (int(value_one) + int(value_two) + int(value_three)))


print('__________________________________________________________')
print('Area and Perimeter of Rectangle')
length = input('Enter the length of rectangle: ')
width = input('Enter the width of rectangle: ')

area_of_rectangle = int(length) * int(width)
perimeter_of_rectangle = 2 * int(length + width)

print('Area of rectangle: ', area_of_rectangle)
print('Perimeter of rectangle: ', perimeter_of_rectangle)


print('__________________________________________________________')
print('Area and Circumference of Circle')
radius_of_circle = input('Enter the radius of circle: ')
area_of_circle = 3.14 * float(radius_of_circle ** 2)
circumference_of_circle = 2 * 3.14 * float(radius_of_circle)


print('Area of circle: ', area_of_circle)
print('Circumference of circle: ', circumference_of_circle)


print('__________________________________________________________')
print('Python' == 'Dragon') # Falsy statement.

print('__________________________________________________________')
print(not 'on' in 'Python' and 'on' in 'Dragon') # Falsy statement.


print('__________________________________________________________')
print('in' in 'I hope this course is not full of jargon.') # Truthy statement.


print('__________________________________________________________')
length_of = 'Python'
float_length = float(length_of)
string_length = str(float_length)
print(string_length)


print('__________________________________________________________')
number = 25
print(number % 2 == 0) # Shows even if remainder is 0 otherwise odd.


print('__________________________________________________________')
print(7 // 3 == 2.7) # False.

print('__________________________________________________________')
print(type(10) == type(10)) # True.

print('__________________________________________________________')
print(int(9.8) == 10) # False.



