s = "anagram"
t = "nagram"

new1 = []


for i in set(s):
    new1.append([i,s.count(i)])   # [['m', 1], ['r', 1], ['n', 1], ['g', 1], ['a', 3]]


new2 = []
for j in set(t):
    new2.append([j,t.count(j)])   # [['m', 1], ['r', 1], ['n', 1], ['g', 1], ['a', 3]]


print(new1)
print(new2)

if sorted(new1) == sorted(new2):
    print("Anagram")