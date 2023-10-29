# class Student
# {
#     int rollno;  // 2
#     char name[30];  // 30
#     float marks;  // 4


        
#     void set_marks()
#     {

#     }

#     void display()
#     {

#     }
# };

# class Library
# {
#     int bookid;  // 2
#     char bname[30];  // 30
#     float price;  // 4
#     double balance;  // Private


#     void set_book()
#     {

#     }
# };


# Bank(name, age)
#     {
#         balance = 0
#         this->name = name
#         this->age = age
#     }



# void main()
# {
#              int     num;  // 2
#     struct Student st[50], kaushal; // 36
#            Student agni;

#     st[1].marks = 900;
# }


# class Student:


#     def display_student(self):
#         print("This is display Method")


# utsav = Student()   # utsav is an object

# utsav.display_student()


# Varibales: 
        # 1. Instance Variable     2. Class Variable

# Methods:
        # 1. Instance Method      2. Class Method      3. Static Method

# Constructor  ---> TO intialize Memeber Variable

# class Student:
    
#     def __init__(self) -> None:
#         self.id = 0
#         self.name = None
#         print("Constructor called")

#     def __init__(self,id=0, name=None) -> None:
#         self.id = id
#         self.name = name
#         print("Constructor called",self.id,self.name)


#     def display_data(sf):
#         print("Student's Record: ",sf.id,sf.name)

#     def update_name(tempppp):
#         tempppp.name = input("Enter Name: ")
#         print('Your Name is Updated',tempppp.name)

# kaushal = Student(10, "Aman")
# Dev = Student()

# kaushal.display_data()
# kaushal.update_name()


class Bank:
    ROI = 4   # Class Variable

    def __init__(self, age1 = 0, name1 = None):  # Parametrized Con.
        self.age = age1   # Instance Variable
        self.name = name1  # Instance Variable
        self.balance = 0   # Instance Variable


    def update_details(self):
        self.age = int(input())
        self.name = input()

    def display(self):
        print(self.age, self.name, self.balance)

    def deposit(self, amount):   # Instance Method
        self.balance += amount

    @classmethod   # Inbuilt Decorator
    def Change_ROI(cls, new_ROI):   # Class Method
        cls.ROI = new_ROI
        print("ROI changed",cls.ROI)

dev = Bank(20, "Dev Bhatt")
agni = Bank(19, "Agni Patel")

dev.display()
dev.deposit(5000)

agni.display() 
dev.display()


print(agni.balance)  # 0
print(dev.balance)   # 5000


# View Access
print(dev.ROI)
print(agni.ROI)
print(Bank.ROI)


dev.ROI = 10

print(dev.ROI)  # 10
print(agni.ROI)  # 4
print(Bank.ROI)  # 4

Bank.ROI = 6

print(dev.ROI)  # 10
print(agni.ROI)  # 6
print(Bank.ROI)  # 6


agni.Change_ROI(8)  # Class Method

print(dev.ROI)  # 10
print(agni.ROI)  # 8
print(Bank.ROI)  # 8