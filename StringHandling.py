# Practice all about strings.
programming_language = "Python"

programmer_story = """He'd always want to learn to code, whenever he gets time"""

# Method to print the text on terminal.
print(programming_language)
print(programmer_story)

# Converting from integer to string.
PI = 3.1415
value = str(PI)
print(value)

# String concatenation.
greeting = "Hello"
to_everyone = "World"

first_greeting = greeting + " " + to_everyone
print(first_greeting)

# String handling.
# upper case.
product_description = "Best qualtity product, almost brand new. Just bought it a few days before. Don't need it anymore."
product_description = product_description.upper()
print(product_description)

# lower case.
product_description = product_description.lower()
print(product_description)

# String slicing.
user_id = 12345678
user_id = str(user_id)
print(user_id)

print(user_id[:]) # Prints the whole thing.
print(user_id[0:]) # Prints the whole thing.
print(user_id[1:4])
print(user_id[1:-4])

# String formatting.
user_name = "Abdullah"
user_age = 23

print(f"My name is {user_name} and I'm {user_age} years old.")

