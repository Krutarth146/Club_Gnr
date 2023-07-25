
# 47. Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


list1 = [11, -6, -103, -200]

for num in list1:  # num = 11
    sum = 0
    # while num != 0:
    #     remainder = num % 10  # rem = 1
    #     sum = sum + remainder  # sum = 2
    #     num = num // 10  # num = 0
    copy = num

    

    num = copy

    print(sum)


# 47. Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


list1 = [10,20,]
# print(str(list1))

# for i in list1:
#     print(len(str(i)))



# 47. Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.
# Input:
# [11, -6, -103, -200]
# Output:
# [11, -103]
# Input:
# [1, 7, -4, 4, -9, 2]
# Output:
# [1, 7, 4, 2]
# Input:
# [10, -11, -71, -13, 14, -32]
# Output:
# [10, -13, 14]


list4 = [11, -6, -103, -200]
res = []

for num in list4:
    sum = 0
    copy = num

    if num > 0:
        res.append(num)
    
    elif num < 0:
        x = str(copy)
        for j in range(1, len(str(copy))):   # -6
            if j == 1:
                sum = sum - int(x[j])  # x[1]

            else:
                sum += int(x[j])



    num = copy

    if sum > 0:
        res.append(copy)

print(res)


# -------------------------------------------------
list3 = [10,11,12,13,14,15,16,17,18,19,20]

# 5 or 7 Divisible 



list5 = [10,20,30,90,22,11]

for i in range(len(list5)-1):   # 0 to 5  ---> i = 0
    for j in range(i+1,len(list5)):
        if list5[i] > list5[j]:
            list5[i], list5[j] = list5[j], list5[i]


print(list5)   # [10, 11, 20, 22, 30, 90]

list5 = [(10,20), (40,590,2), (23,12)]

ans = [(40,590,2), (23,12), (10,20)]

# list7 = [10,20,40,590,20,23,12]

# for subtuple in list5:
#     for ele in subtuple:
#         print(ele)


for i in range(len(list5)):   # 0 to 2    # i = 1
    for h in range(len(list5[i])):  # 0 to 1  # h = 1
        print(list5[i][h])  # list5[2][0]



list5 = [(10,20), (40,590,2), (23,12)]

for i in range(len(list5)-1):   #  i = 0
    for j in range(i+1, len(list5)): # j = 1
        if list5[i][-1] > list5[j][-1]:
            list5[i],list5[j] = list5[j],list5[i]

print(list5)   # [(40, 590, 2), (23, 12), (10, 20)]


l1 = [(10,20), (40,590,2), (23,12)]
for i in range(len(l1)-1):
        if l1[i][-1] > l1[i+1][-1]:
            l1[i] ,l1[i+1] = l1[i+1] ,l1[i]
            
print(l1)



# ----------------------------------

list6 = [(10,90), (333,43), (23,), (23,900), (20,90)]
k = 2


ans = [(10,90),  (23,), (20,90)]