# set

dict1 = {}

set1 = {}

print(type(dict1))     # <class 'dict'>

set1 = {10}
print(type(set1))   # Set

set2 = set()   # Using Constructor

print(type(set2))   # <class 'set'>


# Set ----> Don't Allow Duplicates, Unordered, Unchangeble (But We can add or Remove Elements)

set1 = {10,90.89,True,(10,20,10),(10)}
print(set1)   # {True, 10, 90.89, (10, 20, 10)}

print(id(set1))   # 2077242921632


# ---------------------------------
set1 = {10,20,30,10,20}
set1.update({10,20,30,40,50})
print(set1)   # {40, 10, 50, 20, 30}

set1.add(("Str1", 'Aman'))
# set1.add({False, "False"})   # Error
print(set1)   # {('Str1', 'Aman'), 40, 10, 50, 20, 30}


deleted_item = set1.pop()
print(set1)
print(deleted_item)
deleted_item = set1.pop()
print(set1)
print(deleted_item)

set1.remove(20)
print(set1)   # {50, ('Str1', 'Aman'), 30}

set1.discard(20)
set1.discard(20)
set1.discard(20)
set1.discard(20)
print(set1)   # {50, ('Str1', 'Aman'), 30}


set1 = {10,20,30}
set2 = {30,40,50}
print(set1.difference(set2))
print(set2.difference(set1))


# set1.difference_update(set2)
# print(set1)   # {10, 20}

print(set1.union(set2))   # {50, 20, 40, 10, 30}

# set2 = set1.copy()   # Shallow Copy   Xerox

# set3 = set1  # Digilocker  Deep Copy

# set4 = set(set1)  # Shallow Copy


# set3.add(444)

# print(set1,set2,set3,set4)   # {10, 444, 20, 30} {10, 20, 30} {10, 444, 20, 30} {10, 20, 30}

# print(set1.intersection(set2))   # 30

# print(set1-set2)   # {10,20}
# print(set2-set1)   # {40,50}

# intersection_update

set1 = {10,20,30,40,50}
set2 = {40,50}
print(set1.symmetric_difference(set2))   # {40, 10, 50, 20}

print(set1.isdisjoint(set2))  
print(set2.issubset(set1))   
print(set1.issuperset(set2)) 

set5 = frozenset(set1)
print(set5)   # frozenset({50, 20, 40, 10, 30})


print(type(set5))   # <class 'frozenset'>

list1 = [10,20,30,405,0]

dict1 = {'Aman' : 90}
print(frozenset(list1))
print(frozenset(dict1))   # frozenset({'Aman'})


# Exercises::::::

# 1 . anagram   ARC == CAR


set1 = "AARC"
set2 = "CAR"


dict4 = {}
dict5 = {}
for k in set1:
    dict4[k] = set1.count(k)
for k in set1:
    dict5[k] = set2.count(k)

print(dict4 == dict5)

# 2. Panagram A to Z and space

str2 = "The quick brown fox jumps over the lazy dog"

if len(set(str2.lower())) == 27:
    print('Pangram')


# 3. Heterogram No repetation

# str4 = "the big dwarf only jumps"


# Check whether all Vowels are Present or not in string
# Set Comprehension
vowels = "aeiou"

