# Recursion

def factorial(num):
    mul = 1
    for k in range(1,num + 1):
        mul = mul * k

    return mul

print(factorial(5))


def factorial_rec(num):
    # 5*4*3*2*1
    if num == 1:    # Base Condition
        return 1

    return num * factorial_rec(num - 1)


print(factorial_rec(5))   # 120


# Fibonnacci

def fibo(step):
    n1,n2 = 0, 1

    print(n1,n2,end=' ')

    for i in range(step-2):
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3

fibo(5)   # 0 1 1 2 3 5 8


# Iterator
print()

import time


def fibo_iterator(step):
    list1 = [1,1]

    for j in range(step):
        list1.append(list1[-1] + list1[-2])


    return list1[:-2]    # [0, 1, 1, 2, 3]
    # return list1[-3]   # [0, 1, 1, 2, 3, 5, 8]
    # return list1   # [0, 1, 1, 2, 3, 5, 8]

before_f_iter = time.time() 
print(fibo_iterator(100))   # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(time.time() - before_f_iter)



# Recursion
from functools import lru_cache
before_f_rec = time.time()
@lru_cache(maxsize=1000)
def fibo_recursion(step):
    if step == 0 or step == 1:
        return step
    return fibo_recursion(step-1) + fibo_recursion(step-2)    



print(fibo_recursion(100))   # 55
print(time.time() - before_f_rec)


# Recursion


# def series(num):
#     if num == 100:
#         return num
#     print(num)
#     return series(num + 1)

# print(series(1))

def series(s, num):

    if s == num:
        return s
    print(s)
    return series(s+1, num)

print(series(1,100))