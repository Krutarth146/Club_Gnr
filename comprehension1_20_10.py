# 5 Types  list, Tuple, Dict, set, Generator Comprehension
list1 = [10,20,44,22,33,90]

for ele in list1:
    if ele & 1 != 0:
        print(ele)

sauban = [ele for ele in list1 if ele & 1 != 0]
even = [ele for ele in list1 if ele & 1 == 0]

print(sauban,even)   # [33]
# print(bin(10))  # 0b1010


square = [k**2 for k in list1]
print(square,[k**3 for k in list1])



list1 = [10,90,23,45,66,21]

# target = [(10,100,1000), (4,16,64)....]


ans = [(num,num**2,num**3) for num in list1]
print(ans)   # [(10, 100, 1000), (90, 8100, 729000), (23, 529, 12167), (45, 2025, 91125), (66, 4356, 287496), (21, 441, 9261)]


ans = tuple((num,num**2,num**3) for num in list1)
print(ans)  # ((10, 100, 1000), (90, 8100, 729000), (23, 529, 12167), (45, 2025, 91125), (66, 4356, 287496), (21, 441, 9261))


x = 10
print(type(x))  # int


x = (10)
print(type(x))  # int

x = (10,)
print(type(x))  # <class 'tuple'>


list1 = [10,90,34,23,78]

# ans = [(1,2,5,10), (1,...), (1,23)]

# list1 = []
# for k in range(1,11):
#     # print(k)

#     list1.append(k)

# print(list1)

list2 = [k for k in range(1,11)]
print(list2)


list1 = [10,20,30,40,50,60]

# ans = [(10,10), (10,20), (10,30)....]

# for i in list1:   #  i = 20
#     for j in list1:   #  j = 10
#         print(i,j)   # 20,10

nested = [(i,j) for i in list1 for j in list1]
print(nested)   # [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50), (10, 60), (20, 10), (20, 20), (20, 30), (20, 40), (20, 50), (20, 60), (30, 10), (30, 20), (30, 30), (30, 40), (30, 50), (30, 60), (40, 10), (40, 20), (40, 30), (40, 40), (40, 50), (40, 60), (50, 10), (50, 20), (50, 30), (50, 40), (50, 50), (50, 60), (60, 10), (60, 20), (60, 30), (60, 40), (60, 50), (60, 60)]


# Simple Method

list3 = [10,33,24,22,12]
main =[]

for i in list3:   #  i = 10
    temp = []
    for k in range(1,i+1):
        if i % k == 0:
            temp.append(k)
    # print(temp)
    main.append(temp)
    # main.extend(temp)

print(main)   # [[1, 2, 5, 10], [1, 3, 11, 33], [1, 2, 3, 4, 6, 8, 12, 24], [1, 2, 11, 22], [1, 2, 3, 4, 6, 12]]

# List Comprehension

sauban = [tuple(k for k in range(1,i+1) if i % k == 0) for i in list3]
print(sauban)   # [(1, 2, 5, 10), (1, 3, 11, 33), (1, 2, 3, 4, 6, 8, 12, 24), (1, 2, 11, 22), (1, 2, 3, 4, 6, 12)]

# {10 : (1, 2, 5, 10), 33 : (1, 3, 11, 33)....}

dict1 = {i : tuple(k for k in range(1,i+1) if i % k == 0) for i in list3}
print(dict1)  # {10: (1, 2, 5, 10), 33: (1, 3, 11, 33), 24: (1, 2, 3, 4, 6, 8, 12, 24), 22: (1, 2, 11, 22), 12: (1, 2, 3, 4, 6, 12)}


list1 = [(45,89), (23,45), (12,88), (44,12)]

list1.sort()

print(list1)
sorted_list = [(44,12), (23,45), (12,88), (45,89)]


# --------------------------------------------------------------

# Generators

def series(num):
    # list1 = []
    # for k in range(1,num+1):
    #     list1.append(k)
    # return list1

    for k in range(1,num+1):   # k = 1
        # return k,'Aman',[10,20,30,]
        # return k
        yield k

# print(series(10))   # 1

# print(series(10))   # <generator object series at 0x0000020BC13A9A10>

# print(series(10).__next__())   # 1
# print(series(10).__next__())   # 1

# x = series(10)
# print(x.__next__())   # 1
# print(x.__next__())   # 2
# print(x.__next__())   # 3
# print(x.__next__())   # 4

for j in series(10):
    print(j,end=' ')   # 1 2 3 4 5 6 7 8 9 10