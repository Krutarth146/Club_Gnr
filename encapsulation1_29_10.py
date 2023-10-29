class Royal:
    Faculties = 20  # Class Variable
    __balance = 100000000000 # Class Variable # Private
    _accountant = 3    # Protected Variable


    @staticmethod
    def show_faculty():   # Static Method (For Faster Conversasion)
        print("This is static Method For fater Use",Royal.Faculties)


sauban = Royal()
sauban.show_faculty()

print(sauban.Faculties)  # 20  # Public

# print(sauban.accountant)  # Error
print(sauban._accountant)   # 3 # Protected


# print(sauban.balance)
# print(sauban._balance)
# print(sauban.__balance)  # Private

print(sauban._Royal__balance)   # 100000000000


# x = "Dev"
# assert x == 'dev', "Did u mean Dev"