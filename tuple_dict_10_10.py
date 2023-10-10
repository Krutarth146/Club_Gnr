# Anagram

# str1 = "act"
# str2 = 'cat'

str3 = 'listen'
str4 = 'silent' 


# Method - 1

list1 = []
list2 = []


for i in str3:
    list1.append(i) 

for j in str4:
    list2.append(j)

print(list1)   # ['l', 'i', 's', 't', 'e', 'n']
print(list2)   # ['s', 'i', 'l', 'e', 'n', 't']

if sorted(list1) == sorted(list2):
    print("Anagram")


# Method - 2
str3 = 'listeni'
str4 = 'silent' 

list1 = []
list2 = []


for i in set(str3):
    list1.append((i,str3.count(i)))

print(list1)   # [('l', 1), ('t', 1), ('i', 2), ('s', 1), ('n', 1), ('e', 1)]

for i in set(str4):
    list2.append((i,str4.count(i)))

print(list2)   # [('i', 1), ('l', 1), ('t', 1), ('s', 1), ('n', 1), ('e', 1)]


# Method - 3

# Dict ----> key, Values

dict1 = {}   # {'Name' : "Aman"}
dict2 = {}

str3 = 'listen'
str4 = 'silent' 



for i in str4:
    # dict1[i] = str4.count(i)
    dict1.update({i : str4.count(i)})   # {'n': 1, 'l': 1, 'e': 1, 's': 1, 'i': 1, 't': 1}

for i in set(str3):
    # dict1[i] = str4.count(i)
    dict2.update({i : str3.count(i)})

# {'s' : 1, 'i' : 2....}

print(dict1)   # {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
print(dict2)   # {'t': 1, 'l': 1, 's': 1, 'i': 2, 'n': 1, 'e': 1}


# dict1['s'] = 9

# print(dict1)   # {'s': 9, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}


# dict1['M'] = 10

# print(dict1)   # {'s': 9, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1, 'M': 10}


# dict1.update({'D' : 4, 'Y' : 9})
# print(dict1)   # {'s': 9, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1, 'M': 10, 'D': 4, 'Y': 9}


print(dict1)   # {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
print(dict2)   # {'t': 1, 'l': 1, 's': 1, 'i': 1, 'n': 1, 'e': 1}

if dict1 == dict2:
    print(True)     # True


dict1 = {}   # {'Name' : "Aman"}
dict2 = {}

str3 = 'listen'
str4 = 'silent' 

for i in str4:
    # dict1[i] = str4.count(i)
    dict1.update({i : str4.count(i)})   # {'n': 1, 'l': 1, 'e': 1, 's': 1, 'i': 1, 't': 1}

for i in set(str3):
    # dict1[i] = str4.count(i)
    dict2.update({i : str3.count(i)})


dict5 = {i : str4.count(i) for i in str4}   # {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
dict6 = {i : str3.count(i) for i in str3}   # {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}

print(dict5)
print(dict6)


list1 = (10,20,905,63,21)

# ans = {num : [k for k in range(1,num+1) if num % k == 0]  for num in list1}
  
# print(ans)  # {10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20], 905: [1, 5, 181, 905], 63: [1, 3, 7, 9, 21, 63], 21: [1, 3, 7, 21]}

main = []
new_dict = {}
temp = []

for ele in list1:
    # ele = 10
    # temp = []
    temp.clear()
    for k in range(1,ele+1):
        if ele % k == 0:
            temp.append(k)
            # print(k)

    # print(temp)
    main.append(temp)
    # new_dict[ele] = temp
    new_dict.update({ele : temp})

temp.clear()  

print(main)   # [[1, 2, 5, 10], [1, 2, 4, 5, 10, 20], [1, 5, 181, 905], [1, 3, 7, 9, 21, 63], [1, 3, 7, 21]]
print(new_dict)   # {10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20], 905: [1, 5, 181, 905], 63: [1, 3, 7, 9, 21, 63], 21: [1, 3, 7, 21]}


# Que - 1
tup2 = ((10,20), (9,333), (4,), (23,), (90,89), (111,89,44))
k = 2

# (10,20), (23,), (90,89)

tup1=((10,20),(9,333),(4,),(23,),(90,89),(111,89,94))
k=2
l1=[]

for i in range(len(tup1)):
    flag = 0
    for j in range(len(tup1[i])):
        if(len(str(tup1[i][j]))!=k):
            flag = 1
            break
    if flag == 0:
        l1.append(tup1[i])
print(l1)

# Que = 1
# list Comprehension

# Que - 2

# Sort by Second Element