"""
30DaysPythonChallenge: List Comprehensions, and Lambda Functions.

1. Filter only negative and zero in the list using list comprehension
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

2. Flatten the following list of lists of lists to a one dimensional list :
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    output
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

3. Using list comprehension create the following list of tuples:
    [(0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    (3, 1, 3, 9, 27, 81, 243),
    (4, 1, 4, 16, 64, 256, 1024),
    (5, 1, 5, 25, 125, 625, 3125),
    (6, 1, 6, 36, 216, 1296, 7776),
    (7, 1, 7, 49, 343, 2401, 16807),
    (8, 1, 8, 64, 512, 4096, 32768),
    (9, 1, 9, 81, 729, 6561, 59049),
    (10, 1, 10, 100, 1000, 10000, 100000)]

4. Flatten the following list to a new list:
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    output:
    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [number for number in numbers if number <= 0]
print(negatives_and_zero)


list_of_lists = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
integers = [digit for i in list_of_lists for j in i for digit in j]
print(integers)


numbers = range(11)
result = [(n, 1, n, n**2, n**3, n**4, n**5) for n in numbers]

for item in result:
    print(item)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_countries = []
for country_info in countries:
    for country, city in country_info:
        country_upper = country.upper()
        city_upper = city.upper()
        country_code = country_upper[:3]
        list_of_countries.append([country_upper, country_code, country_upper])

print(list_of_countries)