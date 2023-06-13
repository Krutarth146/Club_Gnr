# operators

# days = int(input("Enter days: "))  # 400

# print(type(days))  # <class 'int'>

# year = days // 365

# month = (days % 365) // 30

# rem_days = (days % 365) % 30

# print("Total Years =",year,"Total Month =",month, "Remaining Days are",rem_days)

# Total Years = 11 Total Month = 0 Remaining Days are 8

# Seconds ----------

# Operators 

# 1. Arithmetic O/p ---->   +  -  *  /  //  %  **

print(25 / 2)  # 12.5  # Float
print(25 // 2) # 12   # Floor Division
print(25 % 2)  # 1
print(25 ** 2) # 625

print(-22 // 4) # -6

print(3**2**3)   # 6561

# Assignment O/p

# += -= *= /= //= %= <<= >>= ^= |= &= =

c = 90 # Assignment (Lowest Priority)
# c == 90 # Relational

c += 10  # c = c+10  # 100
c += 200    # c = 300
c /= 2      # c = 150.0
c %= 2      # c = 0.0
c -= 200    # c = -200.0

print(c)   # -200.0



# Bitwise O/p  -->   &  |  ^  <<  >>  ~


print(0b01011)  # 11
print(0x783)  # 1923
print(0o732)  # 474

print(56 & 34)  # 32
print(bin(56))  # 111000
print(bin(34))  # 100010
# -------------------------
                # 100000                
print(0b100000)  # 32

# & Table (a*b)

# 1  0  0   0
# 0  0  1   0
# 0  1  0   0
# 1  1  1   1

print(46 | 31)   # 63

# OR Table (a+b)

# 0  0  0
# 0  1  1   
# 1  0  1   
# 1  1  1  

print(32 ^ 21)  # 53

# XOR Table same = 0, otherthan 1

# 0  0  0
# 0  1  1   
# 1  0  1   
# 1  1  0  

print(hex(10))  # a
print(oct(10))  # 12


print(21 << 2)    # 84
print(bin(21))   # 1010100
print(0b1010100)   # 84

print(560 >> 3)  # 70


print(~45)    # -46
print(~(-34)) # 33

# Comparison o/p < > <= >= == !=

if 45 <= 45:
    print(True)

if -56:
    print("True")