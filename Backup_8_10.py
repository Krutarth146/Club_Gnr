
def sum_of_unlimited(n1 = 40,n2 = 20, *args, mn = 90):
    sum = 0
    # sum += n1
    # sum += n2
    print(args)   # (30, 40, 50, 60, 70)
    print(type(args))   # <class 'tuple'>

    for i in args:
        sum += i
    return sum

print(sum_of_unlimited(10,20,30,40,50,60,70))  # 250


# ----------------------------------------------------------------------

dict1 = {"name" : "Kaushal", 90 : 89, 78 : True, 'address' : {'City' : ['Ahm', 'Gnr'], 'Area' : ('Sargasan', 'Reliance Chokdi')}}
# Ordered, No Index

# print(dict1['name'])
print(dict1['address'])   # {'City': ['Ahm', 'Gnr'], 'Area': ('Sargasan', 'Reliance Chokdi')}
print(dict1['address']['Area'])   # ('Sargasan', 'Reliance Chokdi')
print(dict1['address']['Area'][-1])   # Reliance Chokdi
print(dict1['address']['Area'][-1][-6:])   # Chokdi
print(dict1['address']['Area'][-1][-6:].upper())   # CHOKDI

def show_detail(*aman, **op):
    # print(op)   # {'name': 'Manoj', 'address': 'Gnr', 'roll': 90}
    # print(type(op))   # <class 'dict'>
    # print(op['roll'])   # 90
    # print(op['roll']//10)   # 9

    # print(aman)   # (10, 20, 30)


    for k in op:
        print(k)


    for k in op.keys():
        print(k)

    for k in op.values():
        print(k)

    for k in op.items():
        print(k)  # ('name', 'Manoj')

        
    for key,val in op.items():
        # print(k)  # ('name', 'Manoj')
        if val == 'Gnr':
            print(key)   # address



show_detail(10,20,30,name = "Manoj", address = "Gnr", roll = 90)