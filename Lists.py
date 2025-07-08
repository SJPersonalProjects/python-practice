# Lists practice program.

fruits = ["apple", "banana", "cherry", "malta"]

student_id = [101, 102, 103, 104, 105]


# Retrieving a complete list.
for fruit in fruits:
    print(fruit)


# Printing an item from a list.
print(student_id[0])

# with negative index.
print(student_id[-3])

# Extracting a part of list (slicing list).
print(fruits[1:3])

# Since lists are mutable, you can change items in it.
student_id[0] = "hundred_one"

for id in student_id:
    print(id)


# Printing length of a list.
print(len(fruits))


# Combining lists.

list_one = [1, 2, 3, 4, 5]
list_two = [6, 7, 8, 9, 10]

result = list_one + list_two

for item in result:
    print(item)


# Using extend keyword.
vegetables = ["Potato", "Tomato", "Cauli Flower"]

fruits.extend(vegetables)

for item in fruits:
    print(item)


# Copying a list.

updated_vegetables = vegetables.copy()

for item in updated_vegetables:
    print(item)


# Nested lists.

student_groups = [
    ["student_one", "student_two", "student_three"],
    ["student_four", "student_five", "student_six"],
    ["student_seven", "student_eight", "student_nine"]
]

# Retrieving on the nested list.
for students in student_groups:
    for each_one in students:
        print(each_one)