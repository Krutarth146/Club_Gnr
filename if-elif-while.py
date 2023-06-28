# num1 = int(input("Enter One Number: "))
# num2 = int(input("Enter One Number: "))
# num3 = int(input("Enter One Number: "))

num1 = 900
num2 = 7890
num3 = 56700

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)


# print(num1 if num1 > num2 else num2)

print((num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3))


num = 70
if num % 5 ==0:
    print("D by 5") 
elif num % 7 == 0:
    print("D By 7")
elif num % 10 == 0:
    print("D by 10")


# Loops ----> 1. ENtry Control  ----> while ,  for


ayush = 40   # start
counter_ayush = 0

while ayush <= 70:  # Condition

    print(ayush, end=' ')   # 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70

    counter_ayush += 1
    # ayush += 1
    ayush = ayush + 1   # Flow

print(counter_ayush)


k = 99

while k>=60:
    print(k,end=' ')   # 99 96 93 90 87 84 81 78 75 72 69 66 63 60
    k-=3
print()
print()
print()
k = 100

while k >= 60:
    if k % 3 == 0 and k == 99:
        print(k)
    k-=1

# Prime

# 29 ---> 1,29
# 24 ---> 1,2,3,4,6,8,12,24
# 31 ---> 1,31

num = 3
factors = 0

i = 1
while i<= num:
    if num % i == 0:
        print(i)
        factors += 1
    i+=1


print(factors)

if factors == 2:
    print("Prime Number")

# 1 to 10000 (Prime , Perfect Numbers, Palindrome, Armstrong, Twin)


# Fibonnaccii


n1,n2 = 0,1

print(n1,n2,sep=' ',end=' ')

i=1
while i<=3:
    n3 = n1 + n2
    print(n3,end=' ')
    n1 = n2
    n2 = n3

    i+=1
