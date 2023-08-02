
# List Characteristics: Mutable (Changeble), ordered (Indexed), Allow's Duplicates


list1 = [10,20,67,34,21,90,90]

# ans = [[10,0], [20,1]..]
ans = []

for ind in range(len(list1)):
    ans.append([ind,list1[ind]])

print(ans)

print([[ind,list1[ind]] for ind in range(len(list1))])


list1 = [10,20,67,34,21,90,90]

ans = [10,67,21,90]

list1 = [10,20,67,34,21,90,90]
x=[]
for i in range(len(list1)):  # 0 to 6
    
    if (i+1)%2==1:
        x.append(list1[i])
    
print(x)

d = [list1[i] for i in range(len(list1)) if (i+1)%2==1]
print(d)

# -------------------------
list1 = [10,20,67,34,21,90,90]
print([ele for ind,ele in enumerate(list1,100) if ind%2 == 0])  # [10, 67, 21, 90]


# -------------------------------------------------

list1 = [10,20,44,55,66]
list2 = [30,50,84,55,36]

# [(10,30), (20,50)...]

l1=[10,20,44,55,66]
l2=[30,50,84,55,36]
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if i==j:
            l3.append([l1[i],l2[j]])
            
print(l3)


# for i in range(len(l1)):
#         l3.append([l1[i],l2[i]])


for i,j in zip(list1,list2):
    print(i,j)

list5 = [[10,90], [34,784], [773,21], [34,], [9,90]]

k = 2

ans = [[10,90], [34,]]

# List Compre


# print(all([1,90,89,45,0]))

list5 = [[10,90],[34,784],[773,21],[34,],[9,90]]

res = []
for sublist in list5:
    lst1 = []
    for i in sublist:
        if len(str(i)) != 2:
            lst1.append(0)

    if all(lst1):
        res.append(sublist)

print(res)   # [[10, 90], [34]]

# List Comprehension ------ HW