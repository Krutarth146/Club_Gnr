str1 = "Nayan"

# if str1.lower()[::-1] == str1.lower():
#     print("Palindrome")

# ---------------------------------------
flag = 0
str1 = str1.lower()
for k in range(len(str1) //2):
    if str1[k] == str1[len(str1) - 1 - k]:
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print("Palindrome")