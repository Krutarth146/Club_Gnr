# # num = 5673
# # while(num > 0)

# # for(   ; num > 0 ;  )

# # 25 to 60

# for dev in range(10):   # start - 0, End = 10 (n-1) ---> 9
#     print(dev,end=' ')   # 0 1 2 3 4 5 6 7 8 9

# print()

# for j in range(25, 41):  # start - 25, End = 41 (n-1) 40
#     print(j,end=' ')  # 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40

# print()

# for vishwa in range(-4,5):
#     print(vishwa,end=' ')   # -4 -3 -2 -1 0 1 2 3 4
# print()  

# for w in range(5,-4):
#     print(w)   # No o/p

# print()


# for s in range(3,12,3):   # start , end (n-1), step(n-1)
#     print(s,end=' ')  # 3 6 9

# print()

# for jk in range(5,-6,-1):
#     print(jk,end=' ')  # 5 4 3 2 1 0 -1 -2 -3 -4 -5
# print()

# for yesha in range(12,-12,3):
#     print(yesha)  # No o/p


# for r in range(-9,0,2):
#     print(r,end=' ')  # -9 -7 -5 -3 -1

# print()

# for n in range(-10,-4,-3):
#     print(n)   # No o/p


# Table 

# 23 * 1 = 23

num = 23 # Use Fstring

for i in range(10,0,-1):
    print(f"{num} * {i} = {num * i}")


counter = 0

for k in range(3):   # k = 0
    for j in range(2):  # j = 0
        for w in range(4): # w = 0
            pass
            counter += 1 


print(counter)  # 24



# ---------------------------
print()
print()
print()

for i in range(3):
    for j in range(i):
        if i==j:
            print(j,end=' ')
            break
    else:
        print("Internal Else Executed!")
    print(i,end=' ')
else:
    print("External Else is Executed!")


l1 = [10,90.90,34,"str1",True]

for k in l1:
    print(k)

for h in range(len(l1)):
    print(l1[h])  # l1[0]

# res = [(10,10), (10,90.90), (10,34) .....]

l1 = [10,90.90,34,"str1",True]

for k in l1:  # 5  # k = 10
    for l in l1: #  l = 34
        print((k,l),end=' ')  # (10,34)

# (10, 10) (10, 90.9) (10, 34) (10, 'str1') (10, True) (90.9, 10) (90.9, 90.9) (90.9, 34) (90.9, 'str1') (90.9, True) (34, 10) (34, 90.9) (34, 34) (34, 'str1') (34, True) ('str1', 10) ('str1', 90.9) ('str1', 34) ('str1', 'str1') ('str1', True) (True, 10) (True, 90.9) (True, 34) (True, 'str1') (True, True)