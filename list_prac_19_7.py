list1 = [10,20,30,41,51,61,70,80]


for diya in list1:   # diya = 10
    if diya % 2 != 0:
        print(diya)


for agni in range(len(list1)):  # 8  ---> 0 to 7
    if list1[agni] % 2 != 0:   # list1[0] ---> 41
        # print(list1[agni])
        print(agni)


list1 = [10,41,20,30,41,51,61,70,80]
for harit in range(len(list1)):  # 8 -----> 0 to 7
    if list1[harit] % 2 != 0:  # list1[1]   41 % 2 != 0
        print(list1.index(list1[harit], harit),end=' ')  # list1[4], 4

print()
for num, element in enumerate(list1,0):
    if element % 2 != 0:
        # print(num,end=' ')   # (0, 10) (1, 41) (2, 20) (3, 30) (4, 41) (5, 51) (6, 61) (7, 70) (8, 80)
        print(num,end=' ')   # 1,4,5,6

# yesha = (19)
# print(type(yesha))  # int


# (0, 10)

l4 = [10,20,30,40,50,99,88,77]

# [(10,10), (10,20), (10,30) ....]
new = []
for j in l4:   # j = 10
    for h in l4:  # h = 50
        new.append((j,h))  # (10,10), (10,20)


print(new)

p4 = [10,20,30,40,50,99,88,77]


c= 0 
for i in range(len(p4)-1):   # i = 0   # 7  --_> 0 to 6
    for j in range(i+1,len(p4)):  # 7 + 6 + 5 + 4 + 3 + 2 + 1
        print(j)
        c+=1

print(c)