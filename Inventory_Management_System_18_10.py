# record = {
#     '1001' : {'pname' : 'Kellogs', 'qn' : 230, 'price' : 50},
#     '1002' : {'pname' : 'parleg', 'qn' : 130, 'price' : 10},
#     '1003' : {'pname' : 'Omega', 'qn' : 55, 'price' : 20},
#     '1004' : {'pname' : 'cadbury', 'qn' : 200, 'price' : 15}
# }

import json

f1 = open('inventory.txt','r')
x = f1.read()
record = json.loads(x)
f1.close()

print(record)
print(record.get('1003'))
print(record['1003'])
print(record['1003']['qn'])   # 55
print(record['1003']['pname'][-2])   # t
print(record['1003']['pname'][1:])   # ats

print('Menu'.center(40,'-'))

print("                Product Name    Quantity      Price")
print('                -------------------------------------')

for key, subdict in record.items():
    print(key,end=' -------> ')
    for value in subdict.values():
        print(value,end='            ')
    print()

p_choice = input('Enter PId: ')

try: 
    if p_choice not in record:
        raise ValueError(p_choice)
    
except ValueError as v:
    print("Value Error Occured and Handled",v)
    exit()

except Exception as e:
    print('Please Enter Valid Choice',e)
    exit()

user_need = int(input("Enter Quantity: "))

total_bill = 0
if record[p_choice]['qn'] > 0:
    if user_need <= record[p_choice]['qn']:
        total_bill = user_need * record[p_choice]['price']
        record[p_choice]['qn'] -= user_need
        print(f"Your total Bill Amount is {total_bill}.")
        print('Inventory Updated! Thank You...')
    else :
        print(f"We have only {record[p_choice]['qn']} Quantity.")
        choice = input("If u need then type Y or y: ")
        if choice.lower() == 'y':
            total_bill = record[p_choice]['qn'] * record[p_choice]['price']
            record[p_choice]['qn'] = 0
            print(f"Your total Bill Amount is {total_bill}.")
            print('Inventory Updated! Thank You...')
        else:
            print("Thank You...")
else:
    print("Thank You...")
    exit()

# print(record)   # Dict


# JSON ----> Javascript Object Notation

record_data = json.dumps(record)   # String
# print(record_data)
# print(type(record_data))   # str

fp = open('inventory.txt','w')   # Overwrite

fp.write(record_data)
fp.close()


# Task ----> Add Inventory, Bill.txt (Person Name, Date, Total Bill AMount) (Append Mode)
# CSV Module



