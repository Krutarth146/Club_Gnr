list1 = [10,20,30,40,5,50,[22,89],1,356,78]


# Indexing

print(list1[4])  # 5
print(type(list1[4]))  # int

print(list1[-4])  # [22, 89]
print(type(list1[-4]))  # <class 'list'>


# Slicing
list1 = [10,20,30,40,5,50,[22,89],1,356,78]

# print(list1[start : end (n-1): step (n-1)])

print(list1[::])  # start default = 0, End default Last, Step default = 1
# 10,20,30,40,5,50,[22,89],1,356,78]

print(list1[1:4])   # [20, 30, 40]
print(list1[1:2])   # [20]  # List
print(list1[1])   # 20  # Int
print(list1[-3:-1])  # [1,356]
print(list1[-1:-3])  # []
print(list1[5:])  # [50,[22,89],1,356,78]
print(list1[5:-1])  # [50, [22, 89], 1, 356]
print(list1[-4:])  # [[22,89],1,356,78]
print(list1[:-4])  # [10, 20, 30, 40, 5, 50]

list1 = [10,20,30,40,5,50,[22,89],1,356,78]

print(list1[:5:1])  # [10, 20, 30, 40, 5]
print(list1[-5:-1:2])  # [50,1]
print(list1[-5:-1:-2])  # []
print(list1[-3:5:3])  # []

for k in range(-3,5,3):
    print(k)  # -3 0 3

for k in range(-3,5,-3):
    print(k)  #

for k in range(-2,-5,2):
    print(k)  # blank

for k in range(-2,-5,-2):
    print(k)  # -2 -4



list1 = [10,66,43,32,(30),21,90]

print(list1[4:-2:-1])  # []
print(type(list1[4:-2:-1]))  # list
print(type(list1[4]))  # int

for i in range(4,-2,-1):
    print(i,end=' ')  # 4 3 2 1 0 -1


l3 = [10,20,"Aman"]

# list1.extend(l3)
# list1+=l3
# print(list1)

l3.append([10,20,30])
l3.append(500)
l3.append(True)

print(l3)   # 4 3 2 1 0 -1 [10, 20, 'Aman', [10, 20, 30], 500, True]

# del l3
# print(l3)   # name 'l3' is not defined

del l3[5:]

print(l3)  # [10, 20, 'Aman', [10, 20, 30], 500]

lst4 = [20,201,20,10]

l3.append(lst4)
print(l3)   # [10, 20, 'Aman', [10, 20, 30], 500, [20, 201, 20, 10]]
 
# l3.extend(lst4)
# print(l3)   # [10, 20, 'Aman', [10, 20, 30], 500, 20, 201, 20, 10]


# l3.append(l3)

l7 = [10,20]
l8 = [30,20]

l3.extend([l7,l8])
l3.append(l7,l8)
print(l3)  # [10, 20, 'Aman', [10, 20, 30], 500, [20, 201, 20, 10], [10, 20], [30, 20]]