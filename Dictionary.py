# Dictionary practice program.

# Creating a dictionary.
person = {
    "name": "Sarim",
    "age": 24,
    "is_student": True
}

# Creating a dictionary using the dict keyword.
student = dict(student_name="Aliya", student_age=16, student_class=12, is_good_student=True)

# Accessing dictionary values.
print(person["age"])
# Using get.
print(person.get("age"))

# Changing value.
student["student_age"] = 17
# Printing it.
print(student.get("student_age"))


# Adding new value-pair in the person.
person["city"] = "Hyderabad"

print(person)

# Removing an item from a dictionary.
person.pop("age")

print(person)

# Deleting an item from the dictionary using del keyword.
del student["is_good_student"]
print(student)

# Looping through a dictionary.
for key, values in person.items():
    print(f"{key}: {values}")

# Printing length of a dictionary.
print(len(person))

# Checking if key exists.
if "name" in person:
    print(person["name"])


# Nested dictionary.
persons = {"person_one": {"name": "Sarim", "age": 24},
           "person_two": {"name": "Wamik", "age": 22},
           "person_three": {"name": "Aliyan", "age":23}}

# Accessing a single item.
print(persons["person_one"]["name"])

# Retrieving all the items.
for key, info in persons.items():
    print(f"{key}: Name: {info["name"]} Age: {info["age"]}")
