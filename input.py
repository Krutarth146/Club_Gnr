# %c - char
# %d - int
# %f - float
# %F - float
# %o - Octal
# %x - Hexadecimal
# %s - string
# %e - Exponenet
# %E - Exponenet


print(ord('A'))  # 65
print(ord('z'))  # 122
print(ord("'"))  # 39
print(ord("0"))  # 48

print(chr(32))  # space
print(chr(91))  # [

print('[%c]' % 65)  # [A]
print('%c' % 91)  # [
print('%d' % 91)  # 91
print('%f' % 3.14566)  # 3.145660
print('%.2f' % 3.14566)  # 3.15
print('%2.3f' % 3.14566)  # 3.146
print('%x' % 15)  # f
print('%X' % 15)  # F
print('%o' % 15)  # 17


print("Ayush is a %s Student" % 'Good')  # Ayush is a Good Student

x = "Manoj Sir"

print("%s is best Guru." % x +" Dev is also good Student.")  # Manoj Sir is best Guru.
 # Manoj Sir is best Guru. Dev is also good Student.

print("{} is {} girl.".format("Diya", 'Good'))  # Diya is Good girl.
print("{1} is {0} girl.".format("Priya", 'Good'))  # Good is Priya girl.
print("{name} is {mode} girl.".format(mode = "Good" , name = "Vishwa"))  # Vishwa is Good girl.

name = "Ayush"
mode = "Good"

print(f"{name} is {mode} Student. {1000}")


# Input Statements:

num3 = 900

# print(type(num3))  # <class 'int'>
# # scanf("%d",&num1);

# num1 = input("Enter First Number: ")  # 100 ---> str
# num2 = input("Enter second Number: ") # 10 ---> str

# print(num1 + num2)   # 10010  # str + str


# Typecasting ---> One datatype to Another Datatype

# (int) x

# Datatypes

x = 900000000
print(x) # 90
print(type(x))  # <class 'int'>
print(id(x))    # 1771187145744
print(x.__sizeof__())  # 28

y = -90.89
print(type(y))  # <class 'float'>

print(x + y)  # Int + float  # 899999909.11

print(True + 45)  # 46   # Implicit Typecasting
print(False + 45)  # 45


_ = True
print(type(_))  # <class 'bool'>

v = 90 + 8j
print(type(v))  # <class 'complex'>  # 90 is Real Part, 8j is Imaginary Part

v1 = 80

print(v + v1)  # 170 + 8j

f = None
print(type(f))  # <class 'NoneType'>

g = 'e'
print(type(g))  # <class 'str'>

# Collections

l1 = []
print(type(l1))   # <class 'list'>

l2 = [10,20,30,10,10,20,90,True, 89+8j,[(10,20,30)], {10,20,30,40}, {"Name" : "Utsav", 'roll' : [90,10,10,]}, "Pramukh Tengent"]

print(type(l2))  # <class 'list'>

tup1 = (10)
print(type(tup1))   # <class 'int'>

tup1 = (10,90.90, ((10,20), (30,40)), {10,102,10})
print(type(tup1))   # <class 'tuple'>

set1 = {}
print(type(set1))  # <class 'dict'>

set2 = {10,(10,20,)}

print(type(set2))  # <class 'set'>

dict2 = {'Name' : "Ayush", "roll" : 9000 }
print(type(dict2))   # <class 'dict'>  # Key - value---> Dict

# Typecasting

x = 90
print(float(x))  # 90.0

x = '4590'
print(int(x))   # 4590
 
x = '45.90'
print(int(float(x)))   # 45   # Explicit Typecasting

x = 'A'
print(ord(x))   # 65
# print(int(x))  # Error


num1 = int(input("Enter First Number: "))  # 100 ---> str
num2 = int(input("Enter second Number: ")) # 10 ---> str


print(num1 + num2)

# Calc, 5 Area, Days, Seconds
