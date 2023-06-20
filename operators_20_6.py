# # Logical Operators

# # and or not 

# num = 56

# if num % 5 == 0 or num % 2 == 0:
#     print("Divisible by 5 or 2")  # Divisible by 5 or 2

# if -67:
#     print(True)
# else:
#     print(False)





# _ = 10  # start Point

# while _ <= 100:  # End Point (Condition)
    
#     if _ % 5 == 0 or _ % 7 == 0 and _ % 10 == 0:
#         print(_,end=' ')
    
#     _ += 1  # Flow

#     # _ = _ + 1

# if not 0:
#     print(True)  # True
# else:
#     pass


# # Membership O/p  --->  in  ,  not in


# list1 = [10, 90, 89, 78, 56, 32]
# print(type(list1))   # <class 'list'>

# print(len(list1)) # 6   # Length starts from 1, Index starts from 0


# # Linear Search
# user_need = int(input("Enter any Number: "))

# for j in list1:
#     # print(j)
#     if j == user_need:
#         print("Element is found")
#         break
# else:
#     print("Not Found")   # If loop is Naturally Executed then it will Run otherwise Not.



# # ----------------------------------------------


# if user_need in list1:
#     print("Element is found")
# else:
#     print("Not Found")

# fruit = ["lichi", 'apple', 'banana', 'papaya']

# # ------------------------------------------

# # Identity Operator   is   is not 

# x = 90
# y = 90

# # print(id(x))  # 2784142363664
# # print(id(y))  # 2784142363664

# # x+=90
# # print(id(x))  # 2769270019920
# # print(id(y))  # 2769270017040

# if x == y:
#     print("x == y")

# if x is y:
#     print("x is y")

l1 = [10,20,30]
l2 = [10,20,30]

print(id(l1))   # 2757450255616
print(id(l2))   # 2757445957376

if l1 == l2:
    print("l1 == l2")   # l1 == l2

if l1 is l2:
    print("l1 is l2")

l1 = l2    # Deep Copy
  
if l1 is l2:
    print("l1 is l2")

l3 = l1.copy()   # shallow Copy
print(id(l1))   # 2757450255616
print(id(l3))   # 27574459573

print(l3)

# maths + sci + eng ---> Total, avg, Required 40 marks in all sub 


num1 = 56
num2 = 45

if num2 < num1:
    print(num1)
else:
    print(num2)

print(num1 if num2 < num1 else num2)

# 3 numbers one Linear
# 
# https://pynative.com/python-operators-and-expression-quiz/ 