# Tuple ------> Ordered (Indexed), Allow's Duplicates, Immutable (Unchangeble)

tup1 = ()
print(type(tup1))   # <class 'tuple'>

tup1 = (10)
print(type(tup1))   # <class 'int'>
# print(tup1[0])   # Error
 
tup1 = (10,)
print(type(tup1))   # <class 'tuple'>

t1 = ('Agni')
print(t1[-2])  # n   # Slicing


dict1 = {}
print(type(dict1))   # <class 'dict'>

d2 = {10}
print(type(d2))   # <class 'set'>

d3 = {'Name' : 'Harit'}
print(type(d3))   # dict

# d4 = {30, {10 : 90}}  # Error
# print(type(d4))   # TypeError: unhashable type: 'dict'

s2 = set()   # set constructor

print(type(s2))   # set

t1 = (10,20,30,{10 : 90}, {101,101,20}, "str1", None, True)

print(t1)
print(id(t1))
t1+=(10,20)
print(id(t1))
print(t1)   # (10, 20, 30, {10: 90}, {20, 101}, 'str1', None, True, 10, 20)

print(t1[3][10])   # 90
print(t1[4])   # {20,101}

print(t1.count(10))  # 2
print(t1.index(20,3))  # 9

tup1 = (56,90,23,12,9,'')
# print(sorted(tup1))  # [9, 12, 23, 56, 90]
# print(tuple(reversed(tup1)))  # (9, 12, 23, 90, 56)


print(all(tup1))   # False
print(any(tup1))   # True

t1 = (10,20,30,90)
t2 = (90,)
t3 = (91,34,31)

for i,j in zip(t1,t2):
    print(i,j)

for i in zip(t1,t2,t3):
    print(i)  # (10,90,91)


for k in enumerate(t1,100):
    print(k)

# Ex - 1

list1 = (10,20,905,63,21)

# ans = [(1,2,5,10), (1,2,4,5,10,20), ...]

ans = (tuple(k for k in range(1,num+1) if num % k == 0)  for num in list1)

# print(ans)
print(ans.__next__())
print(ans.__next__())
print(ans.__next__())

ans = {num : [k for k in range(1,num+1) if num % k == 0]  for num in list1}
print(ans)  # {10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20], 905: [1, 5, 181, 905], 63: [1, 3, 7, 9, 21, 63], 21: [1, 3, 7, 21]}
# Ex - 2

# tup1 = [(10,20), (333,90), (45,), (10,900), (24,90)]
# k = 2
# ans = [(10,20), (45,), (24,90)]

