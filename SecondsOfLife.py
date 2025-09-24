"""
Day 3: 30DayPythonChallenge.

. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

. Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

number_of_years = input('Enter the number of years you have lived: ')
seconds_in_year = 3600 * 24 * 365
print('You have lived for ', seconds_in_year * 100, ' seconds.')


# Table.
print('\n1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')