# # Prime NUmbers in range

# # num = 24 #  ---> 1,23
# num = 1
# while num <= 10000:
#     counter = 0
#     i=1
#     while i<=num:
#         if num%i == 0:
#             counter += 1
#         i+=1

#     if counter == 2:
#         print(num,end=' ')

#     num += 1


# ------------------------

num = 4
step = 3

# 4
# 44
# 444

# 5
# 55
# 555
# 5555
# 55555

# sum = ??

# Armstrong  153 -----> 3*3*3 + 5*5*5 + 1*1*1
        #    8208 ----> 8*8*8*8 + 0*0*0*0 + 2*2*2*2 + 8*8*8*8

num = 1
while num <= 100000:
    xerox = num
    xerox1 = num
    # print(len(str(num)))    # 4

    digits = 0

    # while num > 0:
    while xerox != 0:
        xerox = xerox // 10
        digits+=1

    # print(digits)  # 4
    sum = 0

    while num > 0:   # 783
        remainder = num % 10   # 7
        # sum = sum + remainder ** digits

        k = 1    # Reset
        mul = 1  # Reset

        while k<=digits:
            mul = mul * remainder    # 343
            k+=1

        sum = sum + mul   # 27 + 512 + 343 = 882
        num = num // 10  # 0

    # print(sum)

    if xerox1 == sum:
        print(xerox1)
    num = xerox1

    num += 1


# Factorial

# k = 1
# mul = 1

# num = 5

# while k<=num:
#     mul = mul * k  # 120 = 24 * 5
#     k+=1

# print(mul)   # 120

# Power  2 power 3 ----> 2*2*2 = 8

# k = 1
# mul = 1

# num = 5

# while k<=3:
#     mul = mul * num   # 8 = 4 * 2
#     k+=1