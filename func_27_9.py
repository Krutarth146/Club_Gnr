def series(num):
    # list1 = []
    for j in range(1,num+1):
        yield j
        # print(j,end=' ')
        # return j, [10,20], 90.89, 90+34
        # list1.append(j)
    # return list1

# x = series(10)
# print(x)   # <generator object series at 0x0000012995229A10>

# x = series(10)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

for k in series(10):
    print(k,end=' ')


for k in '363322':
    print(k)


# ----------------------------

def Agni(x2):
    def Vishwa():
        print('Vishwa FUnction')
    Vishwa()
    return x2()


@Agni
def Dev():
    print('Dev Fun')

@Agni
def Ayush():
    print('Ayush Fun')

# Agni(Dev)


# --------------------------------------------------

# lambda (One Liner) (Annomous Function)

def square(num):
    return num ** 2

print(square(5))  # 25


dev = lambda num : num ** 2
print(dev(5))


# x1 = lambda num1, num2 : num1 if num1 > num2 else num2
x1 = lambda num1, num2 = 33332, num3 = 4444: (num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)
# print(x1(10,90,88))
print(x1(10,90))


# a*x**2 + b*x + c = 0

def quadratic_Fun(a,b,c):
    return lambda x : a*x**2 + b*x + c


# ayush = quadratic_Fun(10,20,30)

# print(ayush(5))  # 380

print(quadratic_Fun(10,20,30)(5))   # 380


# Nested lambda

# tanush = lambda x : 50
tanush = lambda x : lambda a1, b1, c1 : a1 + b1 + c1 * x


# m - 1
harit = tanush(10)

print(harit(1,9,4))   # 50


# m - 2
print(tanush(10)(1,9,4))
