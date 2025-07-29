# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1

# Number 1
print(len(it_companies))

# Number 2
it_companies.add("Twitter")
print(it_companies)

# Number 3
other_companies = ["Adobe", "NVDIA", "Logitech"]
it_companies.update(other_companies)
print(it_companies)

# Number 4
it_companies.remove("Adobe")
print(it_companies)

# Number 5
"""
The remove() method deletes an element from a set but raises an error if the element is not found,
whereas discard() removes the element without raising an error, even if it is not present. 
"""

# Level 2
# Number 1
C = A.union(B)
print(C)

# Number 2
print(A.intersection(B))

# Number 3
print(A.issubset(B))

# Number 4
print(A.isdisjoint(B))

# Number 6
print(A.symmetric_difference(B))

# Number 7
del it_companies, A, B

# Level 3

# Nuner 1
age_set = set(age)
print(f"Length of set : {len(age_set)}")
print(f"Length of list : {len(age)}")

# Number 2
"""
A string is a sequence of letters or characters
A list is an ordered collection that you can change
A tuple is like a list, but you can’t change it
A set is a collection of unique items, no duplicates, and it’s unordered
"""

# Number 3
sentence = "I am a teacher and I love to inspire and teach people"
sentence_splited = sentence.split()
sentence_set = set(sentence_splited)
print(f"In this sentence we have {len(sentence_set)} unique words")
