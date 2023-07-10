# Loops 
# 1. Entry Control Loops -----> 1. While   2. For

# For Loop

# for(start ; Condition ; Flow)
# for(ayush = 1 ; ayush <=50 ; ayush++) in C

for ayush in range(10):  # (End (n-1)), start default = 0
    print(ayush,end=' ')    # 0 1 2 3 4 5 6 7 8 9

print()

for dev in range(5,13):  # start = 5, end 13(n-1) = 12
    print(dev,end=' ')  # 5 6 7 8 9 10 11 12
print()

for dev in range(-3,5):  
    print(dev,end=' ')  # -3 -2 -1 0 1 2 3 4
print()

for dev in range(5,-3):  
    print(dev,end=' ')  # No o/p
print()

for dev in range(3,31):  
    if dev % 2 == 1:
        print(dev,end=' ')  # 3 5 7 9 11 13 15 17 19 21 23 25 27 29

print()

for dev in range(3,31,2):    # (start, end(n-1),step(n-1))
    print(dev,end=' ')  # 3 5 7 9 11 13 15 17 19 21 23 25 27 29


print()

for j in range(35,40,3):
    print(j)   # 35 38

print()

for l in range(-5,-10,3):
    print(l)  # blank

print()

for jk in range(100,80,-1):
    print(jk,end=' ')   # 100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81

print()

for ui in range(-25,-31,-2):
    print(ui,end=' ')  # -25 -27 -29

print()

for k in range(-4,4,2):
    print(k)  # -4 -2 0 2

print()

for n in range(10,-10,2):
    print(n,end=' ')  # blank

print()





