str1 = "XXVVIIIIC"

list1 = [['X' , 10], ['V' , 5], ['I' , 1], ['C' , 100]]

sum = 0
for ele in str1:
    for k in range(len(list1)):
        if ele == list1[k][0]:
            sum += list1[k][1]
            break

print(sum)   # 134
ans = ''

while sum > 0:
    if sum >= 100:
        ans+='C'
        sum-=100
        continue

    if sum >= 10:
        ans+='X'
        sum-=10
        continue
    if sum >= 5:
        ans+='V'
        sum-=5
        continue
    if sum >= 1:
        ans+='I'
        sum-=1
        continue

print(ans)


#  -----------------------------------------------

# Map, Reduce, Filter

list1= [10,20,30,44,55]

square = lambda x : x**2

# for i in list1:
#     print(square(i))

# yesha = list(map(lambda x : x**2 , list1))
yesha = list(map(int , ['45', '23', '11', '90']))    # [45, 23, 11, 90]
yesha = list(map(lambda x : x**2 , list1))
print(yesha)   # [100, 400, 900, 1936, 3025]

# yesha = list(map(lambda x : x + 1000 , list1))    # [1010, 1020, 1030, 1044, 1055]
# x = [40]
# yesha = list(map(lambda x : x + 1000 , [int(k) for k in input().split()]))
# print(yesha)


list1 = [10,90,68,34,23, 64]


# dev = lambda x : x % 2
# print(dev(45))

agni = list(map(lambda x : x % 8, list1))

# agni = [0,0,0,0,1]

print(agni)  # [0, 0, 0, 0, 1]

agni = list(filter(lambda x : x % 8 == 0, list1))
print(agni)  # [64]
agni = list(map(lambda x : x % 8 == 0, list1))
print(agni)  # [False, False, False, False, False, True]

# agni = [0,0,0,0,1]


list1 = [10,90,34,2367, 91]

from functools import reduce

sum1 = reduce(lambda x, y : x + y , list1)

# x = 10, y = 90, x = 100, y = 34
print(sum1)   # 2592


from itertools import accumulate

x = list(accumulate(list1, lambda x, y : x + y))
print(x)   # [10, 100, 134, 2501, 2592]



list1 = [5,88,4,12]

# ans = [[1,5], [....], [1,2,4], [1,2,3,4,6,12]]


agni = list(map(lambda x : [k for k in range(1,x+1) if x % k == 0] , list1))
print(agni)   # [[1, 5], [1, 2, 4, 8, 11, 22, 44, 88], [1, 2, 4], [1, 2, 3, 4, 6, 12]]