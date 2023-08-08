str1 = 'K'
str2 = "H"
str3 = '''A'''

print(type(str3))


# String ---> Immutable (Not Changeble)

list1 = [10,20,30]
list1[1] = 900
print(list1)   # [10, 900, 30]


str1 = "Agnivesh"
# str1[2] = 'm'  # string is Immutable

print(str1)

str1 = "Harit" 
str2 = "Good"

# print(str1+str2)  # HaritGood
print(id(str1))  # 1705393882800
str1 += str2

print(str1)   # HaritGood
print(id(str1))   # 1705397837616
# print(str1,str2,sep=' ')  # Harit Good


# str1 = "Dev"

# print(str1 * 3)  # DevDevDev

str1 = "agniv Zensh"

print(str1.replace('n', 'm'))   # Agmivemsh
print(str1.replace('n', 'm', 1))   # Agmivensh
print(str1.replace('n', 'm', -1))   # Agmivemsh

print(min(str1))   # 
print(max(str1))   # v
print(len(str1))   # 11   # starts from 1

str2 = ''   # Falsy Values
if str2:
    print(True)
else:
    print(False)


print(ord('X'))   # 88
print(ord(' '))   # 32
print(chr(44))   # ,

# Indexing

str1 = 'Royal_is Best Institute Ever123.'

print(str1[-3])   # 2
print(str1[3])   # a
print(type(str1[3]))   # <class 'str'>


# Slicing

print(str1[3:7:2])   # start : end(n-1) : step (n-1)
print(str1[-3::1])   # 23.
print(str1[-3:5:-2])   # 2rv tttn sBs

str1 = 'Royal_is B123.'
print(len(str1))  # 14
print(str1[4:-6])   # l_is

for i in range(4,-6):
    print(i)  # blank

# while 0:
#     print("Yesha")

# ----------------------------------------

# MEthods

str1 = 'Royal_is B123.'

print(str1.capitalize())  # Royal_is b123.
print(str1.title())   # Royal_Is B123.
print(str1.upper())   # ROYAL_IS B123.
print(str1.lower())   # royal_is b123.
print(str1.casefold())   # royal_is b123.
print(str1.swapcase())   # rOYAL_IS b123.
print(str1.islower())   # False
print(str1.istitle())   # False
print(str1.isalpha())   # False
print(str1.isnumeric())   # False
print(str1.isdigit())   # False
print(str1.isdecimal())   # False
print(str1.isalnum())   # False
print(str1.isspace())   # False