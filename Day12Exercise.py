"""
Day12Exercise: 30DaysPythonChallenge Modules.


Level 1:
1. Writ a function which generates a six digit/character random_user_id.
        print(random_user_id());
        '1ee33d'

2.Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
        print(user_id_gen_by_user()) # user input: 5 5
        #output:
        #kcsy2
        #SMFYb
        #bWmeq
        #ZXOYh
        #2Rgxf
        
        print(user_id_gen_by_user()) # 16 5
        #1GCSgPLMaBAVQZ26
        #YD7eFwNQKNs7qXaT
        #ycArC5yrRupyG00S
        #UbGxOFI7UXSWAyKN
        #dIV0SSUTgAdKwStr

3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
        print(rgb_color_gen())
        # rgb(125,244,255) - the output should be in this form
"""

import random, string

# def random_user_id():
#     characters = string.ascii_letters + string.digits
#     print(characters)
#     user_id = ''

#     for _ in range(6):
#         random_char = random.choice(characters)
#         user_id = user_id + random_char

#     return user_id


# print(random_user_id())


# def user_id_gen_by_user():
#     num_chars = int(input("Enter the number of characters for each ID: "))
#     num_ids = int(input("Enter the number of IDs to generate: "))

#     characters = string.ascii_letters + string.digits

#     for _ in range(num_ids):
#         user_id = ''
#         for _ in range(num_chars):
#             user_id = user_id + random.choice(characters)
#         print(user_id)


# user_id_gen_by_user()


# def rgb_color_gen():

#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     return f"rgb({r},{g},{b})"

# print(rgb_color_gen())



"""
30DaysPythonChallenge: Level 2

1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

3. Write a function generate_colors which can generate any number of hexa or rgb colors.

    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
    generate_colors('hexa', 1) # ['#b334ef']
    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""

# def list_of_hexa_colors():
#     num_colors = int(input("Enter the number of hex colors to generate: "))

#     hex_chars = '0123456789abcdef'

#     colors_list = []

#     for _ in range(num_colors):
#         hex_color = '#'

#         for _ in range(6):
#             hex_color += random.choice(hex_chars)

#         colors_list.append(hex_color)

#     return colors_list

# print(list_of_hexa_colors())

# def list_of_rgb_colors():
#     num_of_colors = int(input("Enter number of rgb colors: "))

#     rgb_colors = []
#     for _ in range(num_of_colors):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         rgb_colors.append(f"rgb({r},{g},{b})")

#     return rgb_colors

# print(list_of_rgb_colors())


# def generate_colors(color_type, color_quantity):

#     list_of_colors = []
#     if color_type == 'hexa':
#         # Generates hexa colors.
#         characters = '123456789abcdef'

        
#         for _ in range(color_quantity):
            
#             color = ''
#             for _ in range(6):
#                 color += random.choice(characters)
#             list_of_colors.append("#"+color)
#     elif color_type == 'rgb':
        
#         for _ in range(color_quantity):
#             r = random.randint(0, 255)
#             g = random.randint(0, 255)
#             b = random.randint(0, 255)
            
#             list_of_colors.append(f"rgb({r},{g},{b})")            
    
#     print(list_of_colors)

# generate_colors('hexa', 3)
# generate_colors('rgb', 2)

"""
30DaysPythonChallenge: Level 3

1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
"""

def shuffle_list(list_items):
    random.shuffle(list_items)
    return list_items

print(shuffle_list([1, 2, 3, 4, 5]))



def seven_unique_integers():
    unique_integers = []
    for _ in range(7):
        digit = random.randint(0, 9)

        if not digit in unique_integers:
            unique_integers.append(digit)
    return unique_integers

print(seven_unique_integers())