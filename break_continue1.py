royal = 1

while royal <= 10:
    print(royal,end=' ')  # 1 2 3 4 5
    if royal == 5:
        break
    royal+=1


k = 20

while k<=25:
    if k == 23:
        k+=1
        continue
    print(k)  # 20 21 22 24 25
    k+=1


# -------------------------------------

k = 25
m = 25
while k<=30:
    while m<=30:
        if k == m:
            break
        m+=1
        print(m,end=' ')
    print(k,end=' ')
    k+=1

# 25 26 26 27 27 28 28 29 29 30 30

print()
k = 25
while k<=30:
    m = 25
    while m<=30:
        if k == m:
            m+=1
            continue
        m+=1
        print(m,end=' ')
    print(k,end=' ')
    k+=1


# 27 28 29 30 31 25 26 28 29 30 31 26 26 27 29 30 31 27 26 27 28 30 31 28 26 27 28 29 31 29 26 27 28 29 30 30