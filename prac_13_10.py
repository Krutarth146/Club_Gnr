tup1 = ((5,6), (5,7), (5,90), (6,5), (6,9))
# ans = ((5,6,7,90), (6,5,9))

list1 = [list(i) for i in tup1]

print(list1)   # [[5, 6], [5, 7], [5, 8], [6, 5], [6, 9]]

start = {subtup[0] for subtup in tup1}
start = list(start)
print(start)



dev = [list(set([v for subtup in list1 if subtup[0] == k for v in subtup])) for k in start]
print(dev)   # [[90, 5, 6, 7], [9, 5, 6]]


# ------------------------------------


tup1 = ((1,9,4), (8,3,2), (9,1,2))
k = 4

ans = ((5,13,8), (12,7,6), (13,5,6))


# --------------------------------------


# Encryption - Decryption

# Jalp Panchal ----> lXIM XXXXXX

# capital ---> +2 (Small)   C --> e
# small   ---> -3 (Capital)  # c ---> Z

print(ord('A'))   # 65

print(chr(ord('A') + 2))   # C