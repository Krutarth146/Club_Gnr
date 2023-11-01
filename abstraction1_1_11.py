# Abstraction ----> To Hide unnecessary Details from the User

# Uber ---> Ride ---> request 5 Drivers

# User ------> Driver Car No, Phone No.

from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def I_Card():
        pass

    def Peon(self):   # Concrete Method
        print("There are Many Peons")


class Principal(Person):

    def I_Card(self):
        print("This is Principal Id")

class Student(Person):

    def I_Card(self):
        print("This is Student Id")



# p1 = Person()  # Error

p1 = Principal()
s1 = Student()
p1.I_Card()
s1.I_Card()


s1.Peon()   # There are Many Peons