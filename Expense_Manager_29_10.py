class Expense():
    list1 = []

    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
        self.movie_exp = 0
        self.groceery_exp = 0
        self.other_exp = 0


    def Signup(self):
        name = input("Enter your Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if email.endswith(".") == False and email.count('@') == 1 and email.count('@.') == 0 and str(email[0]) not in ["0123456789"]:
            # if len(password) >= 5 and   apply after regex
            self.name = name
            self.email = email
            self.password = password
            Expense.list1.append(self)
            print("Registration Successfull!!")

    
    def Login(self, user_email, user_pass):
        self.flag = 0
        
            # print(user_email, user_pass, obj.email, obj.password)
        if self.email == user_email and self.password == user_pass:
                self.flag = 1
                print(f"Welcome {self.name}, Login Successfull!")
                return 1

        if self.flag == 0:
            print("Cred. Invalid")
            return 0


    def M_Expense(self,amount):
        self.movie_exp += amount


    def G_Expense(self,amount):
        self.groceery_exp += amount
    
    def O_Expense(self,amount):
        self.other_exp += amount


while True:
    print("1 - Signup")
    print("2 - Login")
    print("3 - DisplayCustomers")
    print("4 - Exit")


    choice = int(input("ENter Choice: "))

    if choice == 1:
        Expense().Signup()

    if choice == 2:
        e = input("Enter Email: ")
        p = input("Enter Password: ")
        for x in Expense.list1:
            if x.Login(e,p):
                while True:
                    print("Welcome TO Exp Manager")
                    print("1 --- M Exp")
                    print("2 --- G Exp")
                    print("3 --- O Exp")
                    print("4 --- Show Exp")
                    print("5 --- Back to Dashboard")

                    c = int(input())
                    if c == 1:
                        x.M_Expense(int(input("Enter Bill Amount: ")))

                    elif c == 2:
                        x.G_Expense(int(input("Enter Bill Amount: ")))

                    elif c == 3:
                        x.O_Expense(int(input("Enter Bill Amount: ")))

                    elif c == 4:
                        print(x.movie_exp, x.groceery_exp, x.other_exp)
                    
                    elif c == 5:
                        break
                break
            else:
                print('Not Matched')
                

    if choice == 3:
        for x in Expense.list1: 
            print(x.name)

    if choice == 4:
        exit()

 