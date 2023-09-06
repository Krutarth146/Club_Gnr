# Functions

# 1. Inbuilt Functions ----> print(), input(), len()

# 2. User Defined Functions

# include<stdio.h>
# void Dev();   # Func. Declaration
  
# void Dev()    # Func. Defination
# {
#     // statements
# }

# main()
# {
#     Dev();    // Func. Calling
# }

def Dev():   # Func. Defination
    try:
        printa("Hello Kaushal")
    except Exception as e:
        print("Spelling Error",e)


Dev()    # Func. Calling


print("Hello Agnivesh")
print("Hello Agnivesh")
print("Hello Agnivesh")
print("Hello Agnivesh")

# print(45/0)   # ZeroDivisionError

# f1 = open("Dev.txt", "r")   # FileNotFoundError


# Func. Types

# 1. without Return Type and Without Args.
# 2. without Return Type and With Args.
# 3. with Return Type and Without Args.
# 3. with Return Type and With Args.



# 1. without Return Type and Without Args.


def  Bhatt():
    print("Hello", 90+56)

Bhatt()   # Hello 146
print(Bhatt())   # Hello 146  None


# 2. without Return Type and With Args.

# def Agni(n1,n2,n3):
#     print(n1 + n2 * n3)

# Agni("Tripathi", ' Manoj', 3)   # Tripathi Manoj Manoj Manoj


def Agni(n1,n2 = "Manoj",n3 = 4):   # Default Function
    print(n1 + n2 * n3)

Agni("Tripathi", " Dev")   # Tripathi Dev Dev Dev Dev


x = 90   # Global
def Vishwa():
    global x
    # x = 80   # Local
    x += 10  # 130
    print(x)  # 130


x+=30  # Global   # 130

Vishwa()  # 130
print(x)  # 130



def Kaushal(n1,n2,n3, *sbpatel, n7 = 90):
    print(sbpatel)

    for i in sbpatel:
        print(i)
    print(len(sbpatel))
    print(type(sbpatel))

Kaushal(10,20,30,90,304,43232,"Agni")   # (10, 20, 30, 90, 304, 43232, 'Agni')
