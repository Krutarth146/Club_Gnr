# Functions -----> Code reusability

# Predefined ----> print(), input(), len()

print(len('78'))

# User Defined  UDF

# 1. Without Return Type and Without Args

def Agni():
    print("Hello Agni Bhai")

# 1. Func. Defination   2. Func. Calling


def dev():
    print(90+23)
    # return 90


print(dev())   # None


x = 90   # Global
def Ayush():
    x = 80   # local Variable
    x+=10
    print(x)  

Ayush()   # 90
x+=10  # Global  # 100  # x = x + 10
print(x+2)  # 102  
print(x)   # 100


y = 91
def Kru():
    global y
    y+=10
    printA(y)
    # while y < 90:
    #     y+=1
    #     if True:
    #         pass
    #     print('Manoj')

# Kru()   # 101
y+=10   
print(y)  # 101

# ---------------------------------------------

# Type - 2  with return Type and Without Args

def Yesha(): return 90

x = Yesha()
print(x)   # 90


def Diya():
    return "taj mahal".title()

print(Diya())   # Taj Mahal


def Agni():
    return 90,89.78,[10,20,30],{'Name' : 'Manoj'}

print(Agni())   # (90, 89.78, [10, 20, 30], {'Name': 'Manoj'})

x = Agni()
print(x[-2])   # [10, 20, 30]


# Type - 3  with Args and Without Return Type

def Yesha(num1 = 45, n2=9, *diya, n90=89):
    print(num1 * n2)
    print(diya)
    print(type(diya))

    print(diya[2])


Yesha('45',3, 10,20,30,4,[10,20,30])   # 454545


# public class Agni
# {
#     public static void main(String []dev)
# }


#  main()

int(90.90)
def Agni(n1,n2):
    pass


Agni(10,20)


def Harit():
    print('Hello')

def Agni(aman):
    print('Agni Fun')
    return aman()

Agni(Harit)