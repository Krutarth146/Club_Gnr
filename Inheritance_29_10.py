# Inheritance ----> to Inherit  (Use ---> Code Reusability)

# class Alto:
#     def __init__(self, seats):
#         self.wheels = 6
#         seat = seats
#         print("Alto Con.",seat)

#     def mA(self):
#         print("mA Method Under Alto Class",self.wheels)

# # class Innovaa : protected Alto   in Cpp
# class Innova(Alto):
#     def __init__(self, airbag_c,total_seats):
#         super().__init__(total_seats)
#         airbag = airbag_c
#         print("Innova Con.",airbag)

#     def mB(self):
#         print("mB Method Under Innova class")


# diya = Innova(4,5)

# diya.mA()


# Multilevel Inheritance H.w


# Multiple Inheritance: ----


class Father:
    def __init__(self):
        print("Father Con.")


    def car(self):
        print("Fortuner Car")

class Mother:
    def __init__(self):
        self.con = 1000000000000000000000
        print("Mother Con.")

    def Love(self):
        print("Getting Love",self.con)

class Pupil(Father, Mother):  # MRO  (Method Resolution Order)
    def __init__(self):
        Mother().Love()
        super().__init__()
        print('Pupil Constructor Called')

    def Reel(self):
        print("Reelster")

Agni = Pupil()
Agni.car()
# Agni.Love()


class GrandPa():
    @classmethod
    def Car(cls):
        print("RRR")

    def Home(self):
        print("Home")


class F(GrandPa):
    def Car(self):
        print("Alto Car")

class Me(F):

    # pass
    def Car(self):
        # super().Car()
        print("i20")


yesha = Me()
yesha.Car()

list1 = [F(), Me(), GrandPa]

for i in list1: 
    # print(i)  # <__main__.F object at 0x00000207DE797FD0>

    i.Car()


# ------------------------------------------------------

class A:
    def mA(self):
        print('mA Method under A class')

class B(A):
    def mB(self):
        print('mB Method under B class')

class C(A):
    def mC(self):
        print('mC Method under C class')

class D(B, C):
    def mD(self):
        print('mD Method under D class')


d1 = D()
d1.mA()