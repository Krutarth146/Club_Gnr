# Files

# Text File (t)
# Binary File (b)

# File Operating Modes

# 'w' - Write Mode (Overwrite)  # If file is not created then it will create a New File
# 'r' - Read Mode  # If file does not Exist then it will create an Error
# 'a' - Append Mode (Overwrite)  # If file is not created then it will create a New File
# 'x' - if file exists then it will generate an Error, if not then it will create a file
# '+' - Read + Write


# fp = open("dev.txt", "wt")

# # fp.write("Hello DEV")

# # def FF():
# #     return 90

# # x = FF()
# # fp.write("Hello DEVaaaa\n")
# # fp.write(str(x))
# print(fp.tell())  # 1

# list1 = ["Aman is Good", " Arin is Bad", ' Royal is Best', " very Very Best"]

# fp.writelines(list1)

# print(fp.tell())   # 53
# fp.close()

fp = open("dev.txt", 'r')

print(fp.tell())   # 0
x = fp.read() 
# print(x)
# print(fp.tell())   # 53

# # fp.seek(0)
# fp.seek(39)
# # HW seek ni Second Arg.


# print(fp.read())
# # print(fp.read())
# # print(fp.read())
# # print(fp.read())
# fp.seek(0)
# print()
# print(fp.readline())  # Aman is Good
# print(fp.readline())  # Arin is Bad
# print(fp.readline())  # Royal is Best
# print(fp.readline())  # very Very Best
# print(fp.readline())  # 

# fp.seek(0)

# print(fp.readlines())  # ['Aman is Good\n', 'Arin is Bad\n', 'Royal is Best\n', 'very Very Best']


fp.seek(0)



print(x)
list1 = []

for j in fp.readlines():
    list1.append(j)


print(list1)
print(len(list1))

word1 = 0
ic = 0
for sen in list1:
    x = sen.split()
    for word in x:

        # print(word)
        word1+=1
        # if word.startswith("V"):
        #     print(word,'----')
    for char in sen:
        if char.lower() == 'i':
            ic+=1

print(word1)   # 12
print(ic)   # 4

fp.close() 


fp = open("dev.txt",'r+')

fp.seek(39)
fp.write("Excellent")

fp.seek(0)

print(fp.read())
fp.close()


fp = open('enquiry_Register.png','rb')

x = fp.read()
# print(x)
fp.close()

f1 = open('Copy_img.jpg','wb')
f1.write(x)
f1.close()


# pillow Module