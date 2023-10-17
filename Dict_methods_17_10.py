#  Dict: Ordered (Not Indexed), Keys Unique (Don't Allow Duplicates), Mutable


dict1 = {'name' : "Krutarth", 'list1' : [10,20,30], 'name' : "Dev", 'val' : 'Dev', 'Address' : [{'city' : ['Ahm', 'Gnr']}]}

dict2 = {'list1' : [10,20,30], 'name' : "Krutarth"}

if dict1 == dict2:
    print('Dict is Same')   # Dict is Same

print(dict1)
print(dict1['Address'])   # [{'city': ['Ahm', 'Gnr']}]
print(dict1['Address'][0])   # {'city': ['Ahm', 'Gnr']}
print(dict1['Address'][0]['city'])   #  ['Ahm', 'Gnr']
print(dict1['Address'][0]['city'][-2])   #  Ahm
print(dict1['Address'][0]['city'][-2][1])   #  h

dict1 = {}   # dict
 
set1 = {10}
print(type(set1))  # <class 'set'>

set2 = set()

print(type(set2))   # <class 'set'>

dict2 = {'Name' : 'Royal', 'roll' : 900, 'isActive' : True}

print(dict2['Name'])   # Royal
# print(dict2['Royal'])   # Error

for i in dict2:
    print(i)   # Name

#     Name
# roll
# isActive

for i in dict2.keys():
    print(i)   # Name

#     Name
# roll
# isActive

for i in dict2.values():
    print(i)   # Name

#     Name
# roll
# isActive

for i in dict2.items():
    print(i)   # Name

# ('Name', 'Royal')
# ('roll', 900)
# ('isActive', True)

for key, val in dict2.items():
    # print(key)   # Name
    if val == 900:
        print(key)   # roll

# ('Name', 'Royal')
# ('roll', 900)
# ('isActive', True)


b = 20   # Global
def Dev(m1 ,m2):
    global b
    a = 80   # local
    # print(a+b)
    c = 30
    b = a+c
    return b
    # print(m1 , m2)
    # return a+b # 100

print(Dev(m2 = 10, m1 = 20))


from bidict import bidict

dict3 = bidict(dict2)
print(dict3)   # bidict({'Name': 'Royal', 'roll': 900, 'isActive': True})

dict3 = dict3.inverse
print(dict3)   # bidict({'Royal': 'Name', 900: 'roll', True: 'isActive'})

print(dict3['Royal'])   # Name
# print(dict3['Name'])   # Error


# Add Methods


dict2 = {'Name' : 'Royal', 'roll' : 900, 'isActive' : True}
dict2['Name'] = 'Yesha'

print(dict2)   # {'Name': 'Yesha', 'roll': 900, 'isActive': True}

dict2['Money'] = 9
print(dict2)   # {'Name': 'Yesha', 'roll': 900, 'isActive': True, 'Money': 9}

dict2.update({'Land' : 'Gnr', 'Car' : 15})
print(dict2)

dict3 = {'d' : 90}

# dict2 += dict3
# print(dict2)   # Error

# Delete Methods

# dict2.clear()
# del dict2
del dict2['Money']

print(dict2)   # {'Name': 'Yesha', 'roll': 900, 'isActive': True, 'Land': 'Gnr', 'Car': 15}


deleted_item = dict2.pop('Car')
print(deleted_item, dict2)   # 15 {'Name': 'Yesha', 'roll': 900, 'isActive': True, 'Land': 'Gnr'}


print(dict2.popitem())   # ('Land', 'Gnr')

print(dict2)   # {'Name': 'Yesha', 'roll': 900, 'isActive': True}

print(len(dict2))   # 3
print(dict2.__sizeof__())   # 344
print(id(dict2))
print(max(dict2))   # roll

dict2.setdefault('Model', 'Alpha')
dict2.setdefault('Name', 'Harit')
print(dict2)    # {'Name': 'Yesha', 'roll': 900, 'isActive': True, 'Model': 'Alpha'}


list1 = ['Model1', 'Model2', 'Model3']
val = None
dict6 = dict.fromkeys(list1,val)

print(dict6)    # {'Model1': None, 'Model2': None, 'Model3': None}


print(dict6.get('Model4'))   # None

try:
    print(dict6['Model4'])   # Error 
except Exception as e:
    print("Error",e)

print(90)