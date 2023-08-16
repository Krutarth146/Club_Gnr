str1 = "The Haran is The king of The jungle"

ans = "a Haran is The king of a jungle"

# ans = str1.replace("The","a").replace("a king","The king").lower()

# print(ans)   # a Haran is The king of a jungle

list1 = str1.split()
print(list1)   # ['The', 'Haran', 'is', 'The', 'king', 'of', 'The', 'jungle']


for i in range(len(list1)):
    if list1[i] == 'The':
        list1[i] = 'a'
        break

print(list1)

for i in range(len(list1)-1, -1, -1):
    if list1[i] == 'The':
        list1[i] = 'a'
        break

print(list1)

str3 = ' '.join(list1)
print(str3)   # a Haran is The king of a jungle

print(str3.removeprefix('a H'))   # aran is The king of a jungle
print(str3.removesuffix('gle'))   # aran is The king of a jungle

print(str3.rsplit('a'))   # ['', ' H', 'r', 'n is The king of ', ' jungle']  return in List

str3 = "a Haran is The\nking of a jungle"
print(str3.splitlines())   # ['a Haran is The', 'king of a jungle']

# print(str3)

print(str3.startswith('a'))

str4 = '500'
print(str4.zfill(5))   # 00500



# ----------------------------------------

print(0b11)
print(0o11)   # 9


# ------------------------------------------------

# String Programs

str1 = "Dev Bhatt"

for i in range(len(str1)):
    # print(str1[i])
    # if str1[i] == 't':
    #     str1[i] = 'm'
    pass
# Dev Bhamm

str1 = str1.replace('t','m')

print(str1)


# -----------------------------------


str1 = "Yesha"

# ['Y', 'Ye', 'Yes', 'Yesh', 'Yesha']
# ['YY', 'Ye', 'Ys', 'Yh', 'Ya', 'eY', 'ee', 'es' ....]

list1 = []
for i in range(len(str1)):
    # print(str1[0:i+1])
    list1.append(str1[0:i+1])

print(list1)   # ['Y', 'Ye', 'Yes', 'Yesh', 'Yesha']


# -------------------------------


for i in str1:   # i = "Y"
    for h in str1:  # h = "a"
        print(i+h,end=' ')

# -----------------------------------------------


str5 = "MISSISSIPI"

# 'M' --> 1
# 'I' --> 4