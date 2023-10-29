# Poly - Many
# Morph - Forms

# right ---> left - right, right - wrong

# print(len([10,20,30,40]))
# print(len("Harit"))
# print(len('89'))  # 1




def utsav():
    print('Without args')

def utsav(n1, n2):
    print('With args',n1,n2)

def utsav(n5):
    print(n5)

def utsav(n1=None,n2=None,n3=None,n4=None):
    print(n1,n2,n3,n4)

utsav(10)
utsav(40,90)
utsav()

class Aasam():
    def tea_leaves(self):
        self.labour = 10   # Labour
        print(self.labour)

class Tea(Aasam):   
    def tea_leaves(self):    # Different Class, Inheritance, Method Name Same, Args Same ---> Method Overriding
        super().tea_leaves()
        self.labour_sell = 30   # Marketing
        print(self.labour_sell)
    
    def waghbakri(self):
        print("Vaghbakri Tea Up")

    def waghbakri(self, no=None):   # Same Class, Method Name Same, Args Differ - Method Overloading (Not Supported)
        print("Vaghbakri Tea Down",no)


aman = Tea()
ashok = Tea()

aman.waghbakri()
aman.waghbakri(10)
aman.tea_leaves()  # 10

list1 = [Aasam(), Tea()]

for i in list1:
    i.tea_leaves()



# Operator Overloading   + - * / <= >= <   1. (3+2)  2. (as a Method Name)



# .Operator 


print(89 + 90)
# print(aman + ashok)


 
class K(Aasam):   
    def __init__(self, a1):
        self.a = a1

    def k1(self, Param):
        return self.a + Param.a 

    def __add__(self,Param):   # Dunder Method or Magic Methods
        return self.a + Param.a
    
    def __ge__(self,Param):   # Dunder Method or Magic Methods
        return self.a >= Param.a
    
    def __lt__(self,Param):   # Dunder Method or Magic Methods
        return self.a >= Param.a

aman1 = K(30)
ashok1 = K(40)

# print(aman1.k1(ashok1))   # ashok1 is Object
# print(aman1.+(ashok1))
print(aman1 + ashok1)   # 60
print(aman1 >= ashok1)   # False
print(aman1 < ashok1)   # False
