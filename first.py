# Python is Intrepreted, High Level Lang., Dynamic Language

# int x = 90;

x = 900000000000000000000000
y = 89.89
y = "Agnivesh"

# Single Line Comment

'''
Multi
Line
Comment
'''


print('Royal Technosoft',end=' Yesha ')  
print("Student")    # Royal Technosoft Yesha Student


print('''
    Sarghasan Br.
    Gnr - 788111
    90212121121
''')

print("Hello Raghav! Good Evening!", file = open('agni.txt','w'))

x = 90
y = 80
z = 0

print(x,y,z,sep=' Dev ',end= ' ##### ')   # 90 80 0
print("The Great EShrey Sir")   # 90 Dev 80 Dev 0 ##### The Great EShrey Sir

name = "Dev"
money = 400

print(name,"has",money,'rupees only.')  # Dev has 400 rupees only.
print(name+" has",money,'rupees only.')  # Dev has 400 rupees only.

print(f"{name} has -({money}) Rupees only.")   # fstring (Adv. Formatted String)

x = 89
print(x)  # 89
print(type(x))  # <class 'int'>


y = 89.78
print(type(y))   # <class 'float'>

print(round(90.89))  # 91
print(round(90.89,2))  # 90.89
print(round(90.89,1))  # 90.9
print(round(90.89,0))  # 90.0
print(round(90.89,-1))  # 90.0
print(round(96.89,-1))  # 100.0
print(round(96.89,-2))  # 100.0
print(round(30.89,-2))  # 0.0


print(21 + 89)  # 110
print(21 + 89.89)  # 110.89
print(21 + True)  # 22
print(21 + False)  # 21