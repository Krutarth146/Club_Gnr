str1 = "Girnar_Yatra 123."


place = "Girnar"
code = 123
print(f"{place} Yatra {code}")  # fstring  # Girnar Yatra 123

# [] - list
# () - Tuple
tup1 = (10,)
print(type(tup1))


dict1 = {}
print(type(dict1))   # <class 'dict'>

set1 = {10}
print(type(set1))   # <class 'set'>


dict2 = {'Name' : "Vishwa", 'roll' : 9002, 'pincode' : [10,20,30,40,50]}


print("{Name} 's pincode is {pincode}".format_map(dict2))  # Vishwa 's pincode is [10, 20, 30, 40, 50]



str1 = "Girnar_Yatra_123"
print(str1.isidentifier())   # True
print(str1.isspace())   # False
print(str1.istitle())   # True

var1 = "1_"
print(var1.isidentifier())   # False


str1 = "Girnar_Yatra_123"

print('_'.join(str1))   # G_i_r_n_a_r___Y_a_t_r_a___1_2_3

str1 = "Harit is a Goodi Boy."

list1 = str1.split()
print(list1)   # ['Harit', 'is', 'a', 'Good', 'Boy.']

list1[0] = 'Daiv'

print(list1)   # ['Daiv', 'is', 'a', 'Good', 'Boy.']

str1 = ' '.join(list1)
print(str1)   # Daiv is a Good Boy.

print(str1.split('i'))       # ['Da', 'v ', 's a Good', ' Boy.']
print(str1.partition('i'))   # ('Da', 'i', 'v is a Goodi Boy.')
print(str1.rpartition('i'))   # ('Daiv is a Good', 'i', ' Boy.')

str3 = "aman is Good Boy."

print(str3.split('a'))       # ['', 'm', 'n is Good Boy.']
print(str3.partition('a'))   # ('', 'a', 'man is Good Boy.')
print(str3.rpartition('a'))   # ('am', 'a', 'n is Good Boy.')


str3 = "*****a*an is Good Boy.     "
print(str3.lstrip('*'))   # aman is Good Boy.
print(str3.rstrip())   # *****a*an is Good Boy.

print(len(str3))   # 27
print(str3.ljust(30,'%'))   # *****a*an is Good Boy.
print(str3.rjust(35,'&'))   # &&&&&&&&*****a*an is Good Boy.


str4 = "Hello Sam123"

table1 = str4.maketrans('Sa', 'Rw', '13')
print(table1)   # {83: 82, 49: None, 51: None}


print(str4.translate(table1))   # Hello Rwm2


str5 = "Yesha KeYa"

print(str5.translate({89:66}))    # Besha KeBa
print(str5.replace("Y", 'Diya'))   # Diyaesha KeDiyaa


# HW

str4 = "The Haran is The king of The jungle"

ans = "a Haran is The king of a jungle"