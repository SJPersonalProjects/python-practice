"""
Day 9: 30DaysPythonChallenge
Exercises:_

Level 1:_
. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.


. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

    Enter your age: 30
    You are 5 years older than me.


. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
"""

user_age = int(input('Enter your age: '))
if user_age >= 18:
    print("You're old enough to drive.")
else:
    print("You need",(18 - user_age),'years to learn to drive.')



my_age = 24
your_age = int(input('Enter your age: '))

if my_age > your_age:
    if my_age == (your_age + 1):
        print("I'm",1,'year older than you.')
    else:
        print("I'm",my_age,'years old.',(my_age - your_age),'older than you')
elif my_age == your_age:
    print('We are the same age! :)')
else:
    if your_age == (my_age + 1):
        print("You're",1,'year older than me.')
    else:
        print("You're",your_age,'years old.',(your_age - my_age),'older than me')



value_one = int(input('Enter value A:'))
value_two = int(input('Enter value B:'))

if value_one > value_two:
    print('A is greater than B')
elif value_one < value_two:
    print('A is smaller than B')
else:
    print('A and B are equal.')


"""
Day 9: 30DaysPythonChallenge
Exercises:_

Level 2:

. Write a code which gives grade to students according to theirs scores:

    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F

. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

. The following list contains some fruits:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')


. The following list contains some fruits:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""

student_score = int(input('Enter your score:'))
if student_score >= 80 and student_score <= 100:
    print("Grade A")
elif student_score >= 70 and student_score <= 79:
    print('Grade B')
elif student_score >= 60 and student_score <= 69:
    print('Grade C')
elif student_score >= 50 and student_score <= 59:
    print('Grade D')
elif student_score >= 0 and student_score <= 49:
    print('Grade F (Failed)')
else:
    print('Incorrect Score')



current_season = input('Enter season: ')
current_season = current_season.lower()
if current_season == 'september' or current_season == 'october' or current_season == 'november':
    print('Autumn.')
elif current_season == 'december' or current_season == 'january' or current_season == 'february':
    print('Winter')
elif current_season == 'march' or current_season == 'april' or current_season == 'may':
    print('Spring')
elif current_season == 'june' or current_season == 'july' or current_season == 'august':
    print('Summer')
else:
    print('Incorrect season, please enter correct season.')


fruits = ['banana', 'orange', 'mango', 'lemon']
check_fruit = input('Enter fruit to check if it\'s availability: ')
check_fruit = check_fruit.lower()
if check_fruit in fruits:
    print(check_fruit,'is available in the list.')
else:
    fruits.append(check_fruit)
    print('Fruit has been added.')



"""
Day 9: 30DaysPythonChallenge
Exercises:_

Level 3:_

Here we have a person dictionary. Feel free to modify it!

    person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }

* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
* If the person is married and if he lives in Finland, print the information in the following format:
"""

person = {
    'first_name':'Sarim',
    'last_name':'Jokhio',
    'age':24,
    'country':'Pakistan',
    'is_married': False,
    'skills':['Python', 'Bash', 'Linux', 'Java'],
    'address':{
        'street':'Space market',
        'zipcode':'002210'
    }
}

if 'skills' in person:
    middle_skill = person['skills'][(len(person['skills'])) // 2]
    print(middle_skill)


if 'skills' in person and 'Python' in person['skills']:
    print("Yes, dude's got Python skills :)")
    


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


if 'skills' in person:
    if len(person['skills']) == 2:
        if 'JavaScript' in person['skills'] and 'React' in person['skills']:
            print("He's a front-end developer.")
    elif len(person['skills']) == 3:
        if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
            print("He's a backend developer.")
        elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
            print("He's a full-stack developer.")
    else:
        print("Unknown title.")


if 'is_married' in person:
    if person['is_married'] == True and 'country' in person:
        print(person['first_name'],person['last_name'],'lives in',person['country'],'and he\'s married')
    else:
        print(person['first_name'],person['last_name'],'lives in',person['country'],"and he's not married")