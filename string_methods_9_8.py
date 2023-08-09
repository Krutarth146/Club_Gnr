str1 = 'Royall_is B123.'

print(len(str1))   # 14
print(str1.center(20,'*'))  # ***Royal_is B123.***

print(str1.count('l',5))   # 1

print(str1.find('z'))   # -1
# print(str1.index('z'))  # Generates An Error


str2 = "Ståle"   # 
print(str2.encode())   # b'St\xc3\xa5le'
print(str2.encode(encoding='ASCII', errors="replace"))   # b'St?le'
print(str2.encode(encoding='ASCII', errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding='ASCII', errors="ignore"))   # b'Stle'
print(str2.encode(encoding='ASCII', errors="backslashreplace"))   # b'St\\xe5le'
print(str2.encode(encoding='ASCII', errors="xmlcharrefreplace"))   # b'St&#229;le'

str1 = 'Royall_is\tB123.'
print(str1.endswith('23.'))   # True
print(str1.endswith('23.',3,5))   # True
print(str1.expandtabs())   # Royall_is       B123.
print(str1.expandtabs(32))   # Royall_is                       B123.


str1 = "{} is {} Boy.".format("Dev", "Good")
str1 = "{1} is {0} Boy.".format("Dev", "Good")
str1 = "{name} is {mode} Boy.".format(name = "Kaushal", mode = "Good")
print(str1)


name = "Utsav"
mode = 'GOod'
print(f"{name} is {mode} Boy.")   # Utsav is GOod Boy.