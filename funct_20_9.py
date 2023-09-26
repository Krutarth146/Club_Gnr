# dict1 = {}

# dict1 = {"name" : "Amion", 'address' : [10,20,30,40,50] , 78 : 90, "name" : "Dev", 90 : 90}

# print(dict1)  # {'name': 'Dev', 'address': [10, 20, 30, 40, 50], 78: 90, 90: 90}   # Mutable

# dict1['school'] = "HBK"
# dict1.update({'Ins' : 'Royal', 'Dev' : 90})
# print(dict1)   # {'name': 'Dev', 'address': [10, 20, 30, 40, 50], 78: 90, 90: 90, 'school': 'HBK', 'Ins': 'Royal', 'Dev': 90}

# del dict1['address'] 
# print(dict1)  # {'name': 'Dev', 78: 90, 90: 90, 'school': 'HBK', 'Ins': 'Royal', 'Dev': 90}


# # import csv
# # from bidict import bidict

# def Harit(list4, *jk):
#     print(id(list4))

#     list4[3] = 8090

# list1 = [[10,20,30,], 10,90,90.89,67]
# Harit(list1, 90)   # (10, 90, 90.89, [10, 20, 30])
# print(id(list1))
# print(list1)


def Yesha(n1,n2, *args, **agni):
    print(agni)

    for k in agni.values():
        print(k)

    for key, val in agni.items():
        print(key,'----->',val)
        if val == 89:
            print(key,'----')
    print(args)

Yesha(10,20,30,name = "Aman", roll = 89)   # {'name': 'Aman', 'roll': 89}


def Ayush(a1,a2,a3):

    print(a1 * a3)


tup1 = ('10', 90, 3)
Ayush(*tup1)


# Type - 4

def Dev(n1,n2):
    return n1 + n2 * n1

print(Dev(10,20))   # 210



def Apollo(ceat):
    def Jktyre():
        print('Jktyre')
        ceat()
        return 'Jk is Best'[::-1]
    return Jktyre()

@Apollo
def ceat1():
    print('Aman')

@Apollo
def tvs():
    print('tvs')

# x = Apollo(ceat1)
# print(x)

@classmethod


@staticmethod   # Inbuilt Decorators
def dev():
    '''Docstring'''
    pass

print(dev.__doc__)


