# Tuple practice program.

colors = ("red", "green", "purple")

numbers = (1, 2, 3, 4)

# Accessing tuple element using its index value.
print(colors[0])

# Slicing tuple.
print(numbers[1:3])

# Length of tuple.
print(len(colors))

# Nested tuple.
stationary = ("pen", "pencil", ("rubber", "sharpener", "scale"))

# Using loop to access tuple elements.
for items in stationary:
    print(items)