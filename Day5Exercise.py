"""
Day 5: 30DaysPythonChallenge.
Exercises:_

. Declare an empty list

. Declare a list with more than 5 items

. Find the length of your list

. Get the first item, the middle item and the last item of the list

. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

. Print the list using print()

. Print the number of companies in the list

. Print the first, middle and last company

. Print the list after modifying one of the companies

. Add an IT company to it_companies

. Insert an IT company in the middle of the companies list

. Change one of the it_companies names to uppercase (IBM excluded!)

. Join the it_companies with a string '#;  '

. Check if a certain company exists in the it_companies list.

. Sort the list using sort() method

. Reverse the list in descending order using reverse() method

. Slice out the first 3 companies from the list

. Slice out the last 3 companies from the list

. Slice out the middle IT company or companies from the list

. Remove the first IT company from the list

. Remove the middle IT company or companies from the list

. Remove the last IT company from the list

. Remove all IT companies from the list

. Destroy the IT companies list

. Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
"""

empty_list = []


countries = ['Pakistan', 'India', 'Bangladesk', 'Sir Lanka', 'Saudi Arabia', 'Sudan', 'Morroco']

print(len(countries)) # Finds the length of this list.

print(countries[0]) # Gets the first item in the list.
print(countries[(len(countries) - 1) // 2]) # Gets the middle item from the list.
print(countries[len(countries) - 1]) # Gets the last item from the list.


mixed_data_types = ['Sarim', 24, 5.8, 'Single', 'Street 1, Block 2, Manhattan, New York']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print('Number of companies:', len(it_companies))

print('First company:', it_companies[0])
print('Middle company:', it_companies[(len(it_companies) -1) // 2])
print('Last company:', it_companies[len(it_companies) - 1])

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('OpenAI')

middle_index = it_companies[(len(it_companies) -1) // 2]
it_companies.insert(it_companies.index(middle_index), 'Huawei')

it_companies[len(it_companies) - 1] = it_companies[len(it_companies) - 1].upper()
print(it_companies)


it_companies = '# '.join(it_companies)
print(it_companies)


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
does_exist = 'IBM' in it_companies
print('Does IBM exist? ', does_exist)


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3]) # Slices out first three companies from the list.

print(it_companies[-3:])

print(it_companies[(len(it_companies) - 1) // 2])



it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print(it_companies)



it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop((len(it_companies) - 1) // 2)
print(it_companies)


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

del it_companies
# print(it_companies) it_companies destroyed.


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)


full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)



"""
Exercise Level 2:

The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

. Sort the list and find the min and max age
. Add the min age and the max age again to the list
. Find the median age (one middle item or two middle items divided by two)
. Find the average age (sum of all items divided by their number )
. Find the range of the ages (max minus min)
. Compare the value of (min - average) and (max - average), use abs() method
. Find the middle country(ies) in the countries list
. Divide the countries list into two equal lists if it is even if not one more country for the first half.
. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

"""

ages = [19, 22, 19, 24, 30, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[len(ages) - 1]
print("Min age:", min_age)
print('Max age:', max_age)

ages.append(min_age)
ages.append(max_age)
print(ages)

print('Median age 1: ', ages[(len(ages) - 1) // 2])
print('Median age 2: ', ages[(len(ages) + 1) // 2])

numbers = [19, 22, 19, 24, 30, 25, 26, 24, 25, 24]
average_age = sum(numbers) / len(numbers)
print('Average age: ', average_age)

ages = [19, 22, 19, 24, 30, 25, 26, 24, 25, 24]
min_age = min(ages)
max_age = max(ages)
range = min_age - max_age
print('Range : ', range)


ages = [19, 22, 19, 24, 30, 25, 26, 24, 25, 24]
minimum = min(ages)
maximum = max(ages)
average = sum(ages) / len(ages)

print(abs(minimum - average))
print(abs(maximum - average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

middle_country = countries[(len(countries) - 1) // 2]
print(middle_country)

mid = (len(countries) + 1) // 2  # first half gets the extra one if odd
first_half = countries[:mid]
second_half = countries[mid:]

print("First half:", first_half)
print("Second half:", second_half)


few_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country_one, country_two, country_three, *rest = few_countries
print(country_one)
print(country_two)
print(country_three)
print(rest)

