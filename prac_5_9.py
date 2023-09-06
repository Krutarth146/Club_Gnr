def birthday(s, d, m):
    count = 0
    
    if len(s) == 1:
        for i in s:
            if i == d:
                count+=1
        return count
 
    for i in range(len(s)-m+1):   # i = 4
        sum = 0
        for k in range(i,i + m):   # k = 4,11
            sum = sum + s[k]
        if sum == d:
            count +=1
        print()
    return count    

s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
d = 18
m = 7

print(birthday(s, d, m))