list1 = [10,20,30,40,44,22]

for patel in list1:
    print(patel,end=' ')   # 10 20 30 40 44 22 

for x in reversed(list1):
    print(x,end=' ')   # 22 44 40 30 20 10 

for g in list1[::-1]:
    print(g,end=' ')   # 22 44 40 30 20 10

# for k in range(len(list1))
for k in range(0,6):  # 0 1 2 3 4 5
    print(k,end=' ')  #  0 1 2 3 4 5 


for k in range(0,6):  # 0 1 2 3 4 5
    print(list1[k],end=' ')  #  10 20 30 40 44 22 



# Truthy Values  ==> 1 23 -56 True [10,20], "Dev"
# Falsy Values ===> [] False 0 ""

if "Dev":
    print(True)



list1 = [10,20,30,40,44,22]


# for i in list1:
#     print(i)


# ans = [i for i in list1]
ans = tuple(i for i in list1)
print(ans)   # (10, 20, 30, 40, 44, 22)


list1 = [10,20,30,40,44,22]

# res = []

for k in list1:
    if k % 5 >= 1 and k % 5 < 5:    # Not Div By 5
        print(k)


ans = [k for k in list1 if k % 5 >= 1 and k % 5 < 5]
print(ans)   # [44, 22]


lst5 = [10,90,67,32,45,10]

# [[10,90], [10,67], [10,32], [10,45], [10,10], [90,10], [90,67]...]

new = []

for m in lst5:       # m = 10
    for x in lst5:   # x = 10
        new.append((m,x))

print(new)


ayush = [(m,x) for m in lst5 for x in lst5]

print(ayush)


# -------------------------------

lst5 = [10,90,67,32,45,10]


for i in range(len(lst5)):  # Index  i = 0
    for j in range(len(lst5)): # INdex j = 0
        if i!=0:
            print([[lst5[i], lst5[j]]])


# ---------------------------------------------

lst5 = [10,20,30,22,20,30,10,44,20]

unique = []

for i in lst5:
    # if i not in unique:
    #     unique.append(i)

    if lst5.count(i) == 1:
        print(i,end=' ')   # 22 44

# print(unique)



dev = ['m', 'i', 's', 's', 'i','s','s','i','p','p','i']

# # m --> 1 , i --> 4, s --> 4, p --> 2
s1 = set(dev)

for i in s1:
    print(i,'--->',dev.count(i))