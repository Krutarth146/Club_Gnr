list1 = [10,20,30,40,50,9,43,21,43,21,24,678]

# List is Mutable (Changeble)

print(len(list1))  # 12   # len starts from 1 , Index starts from 0

list1.append("Yesha")
list1.append(9002)
list1.append(True)

print(list1)  # [10, 20, 30, 40, 50, 9, 43, 21, 43, 21, 24, 678, 'Yesha', 9002, True]


tup1 = (10 , 90, 78)
list1.append(tup1)
print(list1)   # [10, 20, 30, 40, 50, 9, 43, 21, 43, 21, 24, 678, 'Yesha', 9002, True, (10, 90, 78)]


list1.extend("Agni")
print(list1)   # [10, 20, 30, 40, 50, 9, 43, 21, 43, 21, 24, 678, 'Yesha', 9002, True, (10, 90, 78), 'A', 'g', 'n', 'i']

# list1.extend(500)  # int object is not Iterable
list1.extend([500, 900])  # [10, 20, 30, 40, 50, 9, 43, 21, 43, 21, 24, 678, 'Yesha', 9002, True, (10, 90, 78), 'A', 'g', 'n', 'i', 500, 900]
list1.extend('500')  # [10, 20, 30, 40, 50, 9, 43, 21, 43, 21, 24, 678, 'Yesha', 9002, True, (10, 90, 78), 'A', 'g', 'n', 'i', 500, 900, '5', '0', '0']
print(list1)   


del list1[6:]
print(list1)   # [10, 20, 30, 40, 50, 9]


l2 = [89,90,56]

list1.append(l2)
print(list1)    # [10, 20, 30, 40, 50, 9, [89, 90, 56]]  # len - 7

# list1.extend(l2)
# print(list1)   # [10, 20, 30, 40, 50, 9, 89, 90, 56]  # len - 9


#  [10, 20, 30, 40, 50, 9, [89, 90, 56]] 
list1.insert(2, 678)
print(list1)  # [10, 20, 678, 30, 40, 50, 9, [89, 90, 56]]   # len = 8

list1 = [10,20,30,40,50]
list1.insert(-1,456)
print(list1)   # [10, 20, 30, 40, 456, 50]

list1[-1] = 55

print(list1)  # [10, 20, 30, 40, 456, 55]

# list1[10] = 900

l1 = [90,32,11]

print(id(list1))   # 1305985957760

list1 += l1
print(list1)   # [10, 20, 30, 40, 456, 55, 90, 32, 11]
print(id(list1))   # 1305985957760


# list1.clear()
# print(list1)  # []

# del list1  # Deleted
# del list1[3:4]

print(list1)   # [10, 20, 30, 40, 456, 55, 90, 32, 11]

removed_ele = list1.pop()
print(removed_ele)  # 11
print(list1)   # [10, 20, 30, 40, 456, 55, 90, 32]

list1.pop(3)
print(list1)   # [10, 20, 30, 456, 55, 90, 32]

list1.remove(10)
print(list1)   # [20, 30, 456, 55, 90, 32]

list1 = [10,20,10,20,30,10]

for agni in list1:
    print(agni,end=' ')  # 10 20 10 20 30 10


for k in range(len(list1)):
    print(list1[k])

list1 = [10,20,10,20,30,10]
new = []


for k in range(len(list1)):
    if list1[k] != 10:
        new.append(list1[k])

print(new)   # [20, 20, 30]


l1 = [10,10,10,20,30,40,50,30,40]

# l1 = set(l1)
# l1 = list(l1)
# print(list(l1))
# print(type(l1))   # <class 'list'>


list1 =[10,20,20,30]
# l1 = []
# for i in range(len(list1)):   # 0 to 3
#     for k in range(i+1,len(list1)):      # 0 to 3
#         if list1[i] == list1[k]:
#             l1.append(list1[i])

# print(l1)

l1=[10,10,10,20,30,40,50,30,40]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

# l2=[]
# for i in l1:
#     if l1.count(i) == 1:
#         l2.append(i)
# print(l2)   # [20,50]


print(l1.count(10))  # 3
print(l1.index(10))  # 0

l1.reverse()
print(l1)

l1.sort()
print(l1)  # [10, 10, 10, 20, 30, 30, 40, 40, 50]


l1.sort(reverse=True)
print(l1)   # [50, 40, 40, 30, 30, 20, 10, 10, 10]