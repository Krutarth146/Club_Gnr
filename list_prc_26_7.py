list1 = [[10,20,30],
         [40,66,22],
         [90,78,67]]


for sublist in list1:
    # print(sublist)  # [10,20,30]    [40,66,22]   [90,78,67]
    for ele in sublist:
        print(ele, end=' ')
    print()

# 10 20 30 
# 40 66 22
# 90 78 67


for row in range(len(list1)):  # 3   ---> 0,1,2           # row = 1
    for col in range(len(list1[row])): # 3 ----> 0,1,2    # col = 0
        # print(list1[row][col],end=' ')  # list1[0][1]   # 10 20 30
        print(list1[col][row],end=' ')  # list1[0][1]   # 10 20 30
    print()


list1 = [[10,20,30],
         [40,66,22],
         [90,78,67]]

sum = 0
for i in range(len(list1)):  # 3   ---> 0,1,2           # row = 1
    sum += list1[i][(len(list1) - i -1)]

print(sum)  # 186

list1 = [[10,20,30],
         [40,66,22],
         [90,78,67]]
 
for row in range(len(list1)):

    if row % 2 == 0:
        for col in range(len(list1[row])):
            print(list1[row][col],end=' ')
    
    else:
        for col in range(len(list1[row])-1, -1, -1):
            print(list1[row][col], end=' ')

    print()