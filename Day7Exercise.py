"""
Day 7: 30DaysPythonChallenge
Exercises:_

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

Level 1:
. Find the length of the set it_companies
. Add 'Twitter' to it_companies
. Insert multiple IT companies at once to the set it_companies
. Remove one of the companies from the set it_companies
. What is the difference between remove and discard


Level 2:
. Join A and B
. Find A intersection B
. Is A subset of B
. Are A and B disjoint sets
. Join A with B and B with A
. What is the symmetric difference between A and B
. Delete the sets completely


Level 3:
. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
. Explain the difference between the following data types: string, list, tuple and set
. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies)) # Finding the length.

it_companies.add('Twitter') # Added 'Twitter' to the set.
print(it_companies)

it_companies.update(['OpenAI', 'Devin AI', 'Panasonic'])
print(it_companies)

it_companies.pop()
print(it_companies)


# it_companies.remove('Grok AI') # remove() gives error if the element doesn't exist.
# print(it_companies)

it_companies.discard('Grok AI') # Doesn't give error if the item is not available.
print(it_companies)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B)) # Joined A and B

print(A.intersection(B)) # Intersection of A and B

print(A.issubset(B)) # A is a subset of A.

print(A.isdisjoint(B)) # A isn't disjoint of B.

print(A.union(B))
print(B.union(A))


print(A.symmetric_difference(B))

del A, B
# print(A) # NameError: varaible not defined.
# print(B) # NameError: variable not defined.


age = [22, 19, 24, 25, 26, 24, 25, 24]
length_of_list = len(age)
print('List length: ', length_of_list)
age = set(age)
length_of_set = len(age)
print('Set length: ', length_of_set)
print('Is list bigger than set: ', length_of_list > length_of_set)



"""
Explain the difference between the following data types:
. String
. List
. Tuple
. Set

String: It's a sequence of characters. Enclosed with single and double quotes.

List: It's a collection of different data types. Lists are ordered, mutable. Allow duplicate elements. Enclosed in square
brackets with the items separated by commas.

Tuple: It's a collection of different data types. Tuples are ordered. Cannot be modified once created. Allow duplicate elements. Enclosed with round parenthesis, and items separated wth commas.

Set: It's a collection of unique data types. Sets are unordered. Can be modified once created. Don't allow duplicate elements. Enclosed with curly braces. and items separated by commas.

"""

sentence = 'I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?'
words = set(sentence.split())
print(words)




