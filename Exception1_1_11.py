# # Error 
# # Exception

# try:
#     num = int(input())
#     print(9/num)
# # except ArithmeticError:
# #     print("Arithmetic Error")
# except ZeroDivisionError:
#     print("Divide by 0 is not Possible")
# except TypeError:
#     print("Type Mismatch")
# except ValueError:
#     print("Value Error")

# except Exception as err:
#     print("Error Occured",err)
# else:
#     print("if any error not occured then it will run")
# finally:
#     print(num, "This block is always Executed")

# print("Hello")




try:
    f1 = open("d.txt","r")
except FileNotFoundError:
    print("File Not Found")

import logging

logging.basicConfig(filename="Error.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

def Series(num):
    try:
        for i in range(1,num + 1):
            print('yielding',i)
            yield i
    except GeneratorExit:
        logging.warning("csdvcsvsdv")
        # logging.error("Generator Exit")
        # print("Generation Error")

    # except Exception as err:
        # logging.exception(err)

x = Series(10)
print(next(x))  # 1
print(next(x))  # 2