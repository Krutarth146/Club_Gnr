# Power
# print(2 ** 3)   # 2*2*2

# digit = 4

# k = 1
# num = 2
# mul = 1
# while(k<=digit)
# {
#     mul = mul * remainder   # 8 = 4*2
#     k++;
# }


# ------------------------------------------------


# Functions

# 1. Inbuilt Functions ----> print(), input()

# 2. User Defined Functions   ---> Code Reusability

# void Kaushal():
#     dictc
#     scsc
#     slicecss
#     casecsc
#     s


# void main()
# {

# }


# 1. Func. Defination
# 2. Func. Calling


def Kaushal():
    printa()
    pass

# Kaushal()





# Func. 
# 1. Without Return Type and Without Arguments
# 2. Without Return Type and With Arguments
# 3. With Return Type and Without Arguments
# 4. With Return Type and With Arguments


# 1. Without Return Type and Without Arguments

def Kaushal():
    print(90+57)
    # return 40


Kaushal()
Kaushal()

print(Kaushal())   # None



# Global Scope - local Scope

x = 80   # Global Scope

def Amin():
    x = 20   # Local Scope
    x+=10

    print(x)  # 30

# Amin()  # x = 30
x+=20  # 100
print(x)  # 100


x = 80   # Global Scope

def Amin():
    global x
    x+=10

    print(x)  # 90

Amin()  # x = 90
x+=20 
print(x)  # 110


def Kru():
    def Aman():
        print('This is Aman Fun.')
    print('This is Kru() FUn.')
    Aman()

# Aman()  Local


Kru()



# ---------------------------------------------


# def Dev():
#     print('Dev Function')

# def Manan(Raman):
#     print('This is Manan FUnction')
#     Raman()

# Manan(Dev)


list1 = [10,20,30,88,21]
print(id(list1))

def odd(Manoj):
    print(id(Manoj))
    for j in Manoj:
        if j % 2:
            print(j)

    Manoj.append(2002)

odd(list1)

print(list1)


x = 90

print(id(x))
def Kaushal(w):
    w+=100
    print(id(w))
    print(w)

Kaushal(x)
x+=10
print(x)