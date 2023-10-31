class Expense():
    list1 = []   # Class Variable   ---> without Obj. using Class Name

    def __init__(self):   # constructor   __init__
        self.name = None
        self.email = None
        self.password = None
        self.movie_exp = 0
        self.groceery_exp = 0
        self.other_exp = 0


    def Signup(self):
        while True:
            temp_email = input("Enter Email: ")
            if temp_email.endswith(".") == False and temp_email.count('@') == 1 and temp_email.count('.') == 1 and temp_email.count('@.') == 0 and str(temp_email[0]) not in ["0123456789"]:
                if len(Expense.list1) > 0:
                    flg = 0
                    for g in Expense.list1:
                        if g.email == temp_email:
                            print("User Id already Taken")
                            print("Please Choose another ID")
                            flg = 1
                            break
                    
                    if flg == 0:
                        self.name = input("Enter your Name: ")
                        self.email = temp_email
                        self.password = input("Enter Password: ")
                        print("Registration Successfull!!")
                        return 1
                    
                elif len(Expense.list1) == 0:
                    self.name = input("Enter your Name: ")
                    self.email = temp_email
                    self.password = input("Enter Password: ")
                    print("Registration Successfull!!")
                    return 1

            else:
                return 0

    
    def Login(self, user_email, user_pass):
        return self.email == user_email and self.password == user_pass
        # return 1


    def M_Expense(self,amount):
        self.movie_exp += amount

    def G_Expense(self,amount):
        self.groceery_exp += amount
    
    def O_Expense(self,amount):
        self.other_exp += amount


import json


record = []
while True:
    print("1 - Signup")
    print("2 - Login")
    print("3 - DisplayCustomers")
    print("4 - Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        e = Expense()  # blank
        if e.Signup():  # fillup
            Expense.list1.append(e)  # list1 = [e1, e2]
            dict1 = {}
            dict1["Name"] = e.name
            dict1["Email"] = e.email
            dict1["Password"] = e.password
            record.append(dict1)
            r = json.dumps(record)
            fp = open("Exp_customers.txt","a")
            fp.write(r)
            fp.close()


    if choice == 2:
        e = input("Enter Email: ")
        p = input("Enter Password: ")
        flag = 0
        for x in Expense.list1:   # list1 = [obj1, obj2, obj3..]
            if x.Login(e,p):   # obj1.Login(e,p)
                flag = 1
                while True:

                    print(f"Welcome {x.name} To Exp. Manager")
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
                        print(f"Movie - {x.movie_exp}\nGrocerry - {x.groceery_exp}\nOther =  {x.other_exp}\nTotal Expense till Now = {x.movie_exp + x.groceery_exp + x.other_exp}")
                    
                    elif c == 5:
                    
                        break
                break
        if flag == 0:
            print('Cred. Invalid')
                

    if choice == 3:
        # for x in Expense.list1: 
        #     print(x.name)
        f1 = open("Exp_customers.txt","r")
        x = f1.read()
        record = json.loads(x)
        for subdict in record:
            print(subdict["Name"])
        f1.close()

    if choice == 4:
        exit()

    

 # Password Validation (reGex), Permanent Storage (file / Json)