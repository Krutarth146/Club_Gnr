# Type - 2  with return Type and without Args


def Akshat():
    # print(67 + 90)
    pass
    # return 90

print(Akshat())   # m - 1

# x = Akshat()  # m - 2
# print(x)


def Royal():
    return 90, 80.78, 'str1'
    # print()  # Unreachable

print(Royal())   # (90, 80.78, 'str1')

x = Royal()
print(x[-1])  # str1


def Techno():
    num = 45
    # 45 to 66

    list1 = []

    for i in range(45,67):
        list1.append(i)

    return list1

print(Techno())   # [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]




def Kaushal(num):

    for n in range(10,num+1):   # Start = 10, End = 16 (n-1)  # 10,11,12,13,14,15
        yield n    # Generator
    
# print(Kaushal(15))   # <generator object Kaushal at 0x000001E1BA1B9A10>

# print(Kaushal(15).__next__())
# print(Kaushal(15).__next__())

x = Kaushal(15)

# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

for i in Kaushal(15):
    print(i)


#
# Factorial()

# 5!-------> 5*4*3*2*1,,,,,,,1*2*3*4*5


def Factorial(num):
    multiply = 1


    for j in range(1,num + 1):  # 1,2,3,4,5
        multiply = multiply * j   # 120 = 2 * 3

    return multiply

print(Factorial(10))

# ----------------------------------------------
def Fact_Rec(num):
    if num == 1 or num == 0:
        return 1
    return num * Fact_Rec(num-1)   # 5


print(Fact_Rec(5))


# With Args and Without Return Type


def rrr(n1,n2,n3):
    print(n1 , n2 * n3)


rrr(10, 'Kaushal ', 3)   # 10 Kaushal Kaushal Kaushal

def Ak1(x1 = 11, x2 = 80, x3 = 34):   # Default Function
    return x1 + x2

print(Ak1(10,20))



def Kaushal1(n1,n2,*kkkk, n3 = None):
    print(kkkk)   # ('Amana', [10, 10, 10])
    for d in kkkk:
        print(d)



Kaushal1(10,90.89,'Amana', [10,10,10])



def Kru(*args, **kwargs):
    print(kwargs)  # {'name': 'Krutarth', 'School': 'HBK'}

    keys = [i for i in kwargs.keys()]
    values = [f for f in kwargs.values()]
    items = [key for key,val in kwargs.items() if val == "Krutarth"]

    print(keys)   # ['name', 'School']
    print(values)   # ['Krutarth', 'HBK']
    print(items)   # [('name', 'Krutarth'), ('School', 'HBK')]

Kru(10,20,30,40,name = 'Krutarth', School = 'HBK')


dict1 = {'Name' : 'Ak', 'Roll' : [10,20]}


for k,v in dict1.items():
    print(k,'----->',v)