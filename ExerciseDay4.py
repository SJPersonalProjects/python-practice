"""
Day 4: 30DaysPythonChallenge

Exerxise - Day 4

. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
. Declare a variable named company and assign it to an initial value "Coding For All".
. Print the variable company using print().
. Print the length of the company string using len() method and print().
. Change all the characters to uppercase letters using upper() method.
. Change all the characters to lowercase letters using lower() method.
. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
. Cut(slice) out the first word of Coding For All string.
. Check if Coding For All string contains a word Coding using the method index, find or other methods.
. Replace the word coding in the string 'Coding For All' to Python.
. Change Python for Everyone to Python for All using the replace method or other methods.
. Split the string 'Coding For All' using space as the separator (split()) .
. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
. What is the character at index 0 in the string Coding For All.
. What is the last index of the string Coding For All.
. What character is at index 10 in "Coding For All" string.
. Create an acronym or an abbreviation for the name 'Python For Everyone'.
. Create an acronym or an abbreviation for the name 'Coding For All'.
. Use index to determine the position of the first occurrence of C in Coding For All.
. Use index to determine the position of the first occurrence of F in Coding For All.
. Use rfind to determine the position of the last occurrence of l in Coding For All People.
. Use index or find to find the position of the first occurrence of the word 'because' in the . ..following sentence: 'You cannot end a sentence with because because because is a conjunction'
. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
. Does ''Coding For All' start with a substring Coding?
. Does 'Coding For All' end with a substring coding?
. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
"""

word_one = 'Thirty'
word_two = 'Days'
word_three = 'Of'
word_four = 'Python'
sentence = word_one + ' ' + word_two + ' ' + word_three + ' ' + word_four
print(sentence)

word_one, word_two, word_three = 'Coding', 'For', 'All'
print(word_one + ' ' + word_two + ' ' + word_three)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding'))

company = 'Coding For All'
print(company.replace('Coding', 'Python'))

sentence = 'Python to Everyone'
print(sentence.replace('Python to Everyone', 'Python For All'))


sentence = 'Coding For All'
print(sentence.split(' '))

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(","))


sentence = "Coding For All"
print(sentence[0]) # It's C

print(sentence[-1]) # It's l

print(sentence[10]) # space

sentence = 'Python For All'
print(sentence[0] + sentence[7] + sentence[11])

sentence = "Coding For All"
print(sentence[sentence.index('C')] + sentence[sentence.index('F')] + sentence[sentence.index('A')])

print(sentence.index('C'))

print(sentence.index('F'))

sentence = "Coding For All People"
print(sentence.rfind('l'))

sentence = "You cannot end a sentence with because because because is a conjunction."
print(sentence.find('because'))


print(sentence.rindex('because'))

sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find('becuase')
end = start + len('because because because')
print(sentence[start:end])


sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.split()
print(position.index('because'))


sentence = 'You cannot end a sentence with because because because is a conjunction'
start = sentence.find('because')
end = start + len('because because because')
print(sentence[start:end])


sentence = "Coding For All"
print(sentence.startswith('Coding'))
print(sentence.endswith('Coding'))

sentence = '   Coding For All   '
print(sentence.strip())


sentence = '30DaysOfPython'
print(sentence.isidentifier())
sentence = 'thirty_days_of_python'
print(sentence.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))
