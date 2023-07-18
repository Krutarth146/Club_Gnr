list1 = [10,20,30,40,55,66,77]

for dev in list1:
    print(dev,end=' ')   # 10 20 30 40 55 66 77 

print()
for dev in list1[::-1]:
    print(dev,end=' ')   # 77 66 55 40 30 20 10 

print()
for dev in reversed(list1):
    print(dev,end=' ')   # 77 66 55 40 30 20 10


# print()
# for agni in sorted(list1):
#     print(agni) 

# list1.sort()

# print(list1)

list1 = [10,201,303,40,5,66,77]

c = 0
print()
for i in range(len(list1)-1):
    for j in range(i+1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
        c+=1

print(list1)  #  [5, 10, 40, 66, 77, 201, 303]
print(c)

list2 = [[10,20], [20,90], [34,56], [22,21], [11,67]]

for i in range(len(list2)-1):
    for j in range(i+1,len(list2)):
        if list2[i][-1] > list2[j][-1]:
            list2[i], list2[j] = list2[j], list2[i]

print(list2)   # [[10, 20], [22, 21], [34, 56], [11, 67], [20, 90]]


# switch(num > 0)
# {
#     case 1:
#             positive

#     case 0:
#         swicth(num < 0)
#         {
#             case 1: Negative

#             case 0: Zero
#         }
# }

list2 = [[10,20], [20,90], [34,56], [22,21], [11,67]]

def Vishwa(list1):
    return list1[-1]


list2.sort(key=Vishwa)
print(list2)


p1 = [2,2,2,3,4,45,67,1,2,3,45,6,7,8]

# 2 ----> [0,1,2...]
# 3 ----> [3...]
# 4 ----> [4]

# while ---> List Excess 

p1 = [2,2,2,3,4,45,67,1,2,3,45,6,7,8]

unique = []

for i in p1:
    if i not in unique:
        unique.append(i)

print(unique)   # [2, 3, 4, 45, 67, 1, 6, 7, 8]

# print(list(set(p1)))   # [1, 2, 67, 3, 4, 6, 7, 8, 45]


for ele in unique:   # j = 2
    
    temp = []
    for ind in range(len(p1)):
        if ele == p1[ind]:
            temp.append(ind)
    print(ele, '--->', temp)

# index method

# list1.index(ele,2)

# List Puzzles 20