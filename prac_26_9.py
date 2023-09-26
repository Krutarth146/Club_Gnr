
# # 18. Write a Python program to generate all permutations of a list in Python.

# list1 = [10,20,30,40,50,60,70,80]   # len = 8

# # target1 = [(10), (10,20), (10,20,30), (10,20,30,40), .....]

# # for k in range(8):   # Start = 0, End = 7

# # for k in range(len(list1)):   # list1[0]  = 10  , k = 1
# #     for m in range(k+1, len(list1)+1):   # 2 to 8
# #         print(list1[k:m],end=' ')  # list1[1:6]


# # target2 = [[10,20], [10,30], [10,40] ....]


# # 19. Write a Python program to calculate the difference between the two lists.

# list1 = [10,290,45,32,21,89,67]
# list2 = [10,290,45,34,22,11,244,66]


# res = []
# for j in list1:
#     for k in list2:
#         if j == k:
#             res.append(j)

# print(res)


# ans = []
# for k in list1:
#     if k not in res:
#         ans.append(k)
# for k in list2:
#     if k not in res:
#         ans.append(k)

# print(ans)   # [32, 21, 89, 67, 34, 22, 11, 244, 66]


# list1 = [10,290,45,32,21,89,67]
# list2 = [10,290,45,34,22,11,244,66]


# s1 = set(list1)
# s2 = set(list2)

# print(list(s1.symmetric_difference(s2)))



list1 = [10,20,30,40,50,60,70,80]   # len = 8

# for k in range(8):   # list1[0]  = 10  , k = 0
for k in range(len(list1)):   # list1[0]  = 10  , k = 5
    for m in range(k+1, len(list1)+1):   # 6 to 9
        print(list1[k:m],end=' ')  # list1[5:8]


# # 0
#  0,1,
#  0 1 2
#  0 1 2 3 
#  0 1 2 3 4
#  0 1 2 3 4 5

list1 = [10,20,30,40,50,60,70,80] 
# target2 = [[10,20], [10,30], [10,40] ....]
print()

for i in list1:   # i = 30
    for j in list1:  # 10
        print((i,j),end=' ')

l1 = list(set(list1))
print(l1)  # [70, 40, 10, 80, 50, 20, 60, 30]

k = 50
# ------------------------------------------------

# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.

def makeBricks(small, big, goal):
    pass

makeBricks(3,2,9)


# odoo


