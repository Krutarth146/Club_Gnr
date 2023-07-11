list1 = []
print(type(list1))   # <class 'list'>

l4 = [10,10,20,90.89,"str1",'V',[(10,20,30)], {10,20,30,10}, {"name": "Agnivesh"}]

print(l4)  # [10, 10, 20, 90.89, 'str1', 'V', [(10, 20, 30)], {10, 20, 30}, {'name': 'Agnivesh'}]

# List Characteristics: 

# Ordered (Indexed), Allow's Duplicates, Muatble (Changeble)

# Indexing
print(l4[1])  # 10
print(l4[2])  # 20
print(l4[-2])  # {10, 20, 30}
print(type(l4[-2]))  # <class 'set'>
print(l4[4])  # "str1"


# Slicing

# print(l4[start : end(n-1) : step(n-1)])

l4 = [10,90,89,677,57,43,21,32,121,22,2,34]
print(l4[1:2])  # 90
print(type(l4[1:2]))  # <class 'list'>
print(l4[3:7])  # [677, 57, 43, 21]
print(l4[-5:-3])  # [32, 121]
print(l4[-3:-2:-1])  # No o/p
print(l4[-3:-2:1])  # 22
print(l4[::])  # [10, 90, 89, 677, 57, 43, 21, 32, 121, 22, 2, 34]
print(l4[:-1:])  # [10, 90, 89, 677, 57, 43, 21, 32, 121, 22, 2]
print(l4[5:])  # [43, 21, 32, 121, 22, 2, 34]
print(l4[-5::])  # [32, 121, 22, 2, 34]
print(l4[6:2:-1])  # [21, 43, 57, 677]
print(l4[-3:3:2])  # []
print(l4[:-5:-2])  # [34, 22]
print(l4[-1:-5:2])  # [34, 22]
print(l4[::-1])  # [34, 2, 22, 121, 32, 21, 43, 57, 677, 89, 90, 10]
print(l4[5:-5:])  # [43, 21]
print(l4[4:-7:-1])  # []


# for k in range(-3,3,2):
#     print(k)  # -3 -1 1

l4 = [10,90,89,677,57,43,21,32,121,22,2,34,-10]
# print(sum(l4))  # 1198
# print(min(l4))  # 2
# print(max(l4))  # 677
# print(sum(l4) / len(l4))  # 99.8333333
# print(id(l4))  # 1295323483392
print(l4.__sizeof__())  # 136
print(all(l4))  # True   like and
print(any(l4))  # like or