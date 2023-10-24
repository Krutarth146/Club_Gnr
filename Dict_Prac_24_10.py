# 4. Write a Python script to check whether a given key already exists in a dictionary.

dict1 = {'Name' : "Krutarth", 'Roll' : 90}

user_need = 'Name'

if user_need in dict1:
    print('Exists')

# -------------------------------------------------------


str1 = "MISSISSIPI"
# ans = {'M' : 1, 'I' : 4...}

ans = {}

# for ele in set(str1):   # ele = 'M'
#     # ans[ele] = str1.count(ele)   # ans  = {'M' : 1, 'S' : 4, 'S' : 4}
#     ans.update({ele : str1.count(ele)})

# print(ans)   # {'M': 1, 'I': 4, 'S': 4, 'P': 1}

for k in str1:
    if k not in ans:
        ans[k] = 1
    else:
        ans[k] += 1

print(ans)   # {'M': 1, 'I': 4, 'S': 4, 'P': 1}

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# {1 : [1,1], 2 : [4,8]....}
sc = {x: [x**2, x**3] for x in range(1,16)}
print(sc)


# 19. Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
 

 
# 20. Write a Python program to print all distinct values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

list1 = []
for subdict in sample:  # {"V" : "S001"}
    list1.extend(tuple(val for val in subdict.values()))

print(set(list1))   # [dict_values(['S001']), dict_values(['S002']), dict_values(['S001']), dict_values(['S005']), dict_values(['S005']), dict_values(['S009']), dict_values(['S00..


# {'S009', 'S001', 'S002', 'S005', 'S007'}