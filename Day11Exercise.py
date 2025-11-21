"""
Day 11: 30DaysPythonChallenge

1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
4. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
5. Write a function called calculate_slope which return the slope of a linear equation
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list1(["A", "B", "C"]))
    # ["C", "B", "A"]

10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
    numbers = [2, 3, 7, 9]
    print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    numbers = [2, 3, 7, 9]
    print(remove_item(numbers, 3))  # [2, 7, 9]

13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

    print(sum_of_numbers(5))  # 15
    print(sum_of_numbers(10)) # 55
    print(sum_of_numbers(100)) # 5050

14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
"""

def add_two_numbers(value_one, value_two):
    return value_one + value_two

# Running the above function.
print(add_two_numbers(3, 5))

def area_of_circle(radius):
    PI = 3.1415
    area_of_circle = PI * radius * radius
    return area_of_circle
# Running the above function.
print(area_of_circle(6))


def add_all_nums(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum
# Running the above function.
print("Sum of numbers: ", add_all_nums(1, 2, 3, 4, 5))


def check_season(month):
    if month == 'December' or month == 'January' or month == 'February':
        print('Winter')
    elif month == 'March' or month == 'April' or month == 'May':
        print('Spring')
    elif month == 'June' or month == 'July' or month == 'August':
        print("Summer")
    elif month == 'September' or month == 'October' or month == 'November':
        print("Autumn")
    else: print('Invalid statement')
# Running the above function.
check_season('January')


def print_list(items_list):
    for item in items_list:
        print(item)
# Running the above function.
list_items = ['apple', 'banana', 'cat', 'dog', 'elements', 'french-fries']
print_list(list_items)


def reverse_list(items_list):
    last_index = len(items_list)
    while (last_index - 1) >= 0:
        print(items_list[last_index - 1])
        last_index = last_index - 1
# Running the above function.
numbers = ["A", "B", "C", "D", "E"]
reverse_list(numbers)


def capitalize_list_items(items_list):
    for item in items_list:
        print(item.capitalize())

# Running the above function.
fruits = ['apple', 'banana', 'cactus', 'durain']
capitalize_list_items(fruits)


def add_item(items_list, item):
    items_list.append(item)
    return items_list

# Running the above function.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))


def remove_item(items_list, item):
    items_list.remove(item)
    return items_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))


def sum_of_numbers(number):
    sum = 0
    while number >= 0:
        if number % 2 == 0:
            sum = sum + number
        number = number - 1
    return sum
# Running the above function.
print('Sum: ', sum_of_numbers(10))


"""
Exercise: Level 2

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
"""

def evens_and_odds(number):
    even_count = 0
    odd_count = 0
    while number >= 0:
        if number % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        number -= 1
    
    print('Even count: ', even_count)
    print('Odd count: ', odd_count)
# Running the above function.
evens_and_odds(100)


def factorial(number):
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result
# Running the above function.
print(factorial(3))



def is_empty(item):
    print("Is empty?", not item)
# Running the above function.
is_empty("")