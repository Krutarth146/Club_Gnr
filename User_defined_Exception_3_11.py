class ThreeDivisibleError(Exception):
    def __init__(self, msg):
        print("Three Div. Class Called",msg)


def CalcInterest():
    num = 43
    divisor = 3
    try:
        if divisor == 3:
            raise ThreeDivisibleError("User Define Error Occured")
        else:
            print(num // divisor)
    except ThreeDivisibleError as err:
        print("Division By 3 is Not Possible Here",err)

CalcInterest()

# Withdraw -----> Balance (50000)    1. 60000  --> Insufficient class     2. 45000  --->  MinBalanceRuleBroke class