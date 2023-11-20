import mysql.connector


mydb = mysql.connector.connect(user = 'root', password = 'mysql', database = 'club', host = 'localhost')


if mydb.is_connected():
    print("Database Connected....")
else:
    print("Not Connected....")

cur = mydb.cursor()

print("Gym Management System".center(40))


cur.execute("CREATE TABLE IF NOT EXISTS CUST_DETAILS (ID INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(30) NOT NULL, GENDER CHAR NOT NULL, AGE INT NOT NULL, USERNAME VARCHAR(30) NOT NULL UNIQUE, PASSWORD VARCHAR(30) NOT NULL)")


cur.execute("CREATE TABLE IF NOT EXISTS PHY_DETAILS (PID INT PRIMARY KEY AUTO_INCREMENT, USERNAME VARCHAR(30), HEIGHT FLOAT, WEIGHT FLOAT, BMI FLOAT, ID INT, FOREIGN KEY(ID) REFERENCES CUST_DETAILS(ID))")

cur.execute("create table if not exists logs (lid int primary key auto_increment, username varchar(30), entry_time datetime, exit_time datetime, id int, foreign key (id) references cust_details(id))")

# cur.execute('alter table cust_details add column (joining_date date, ending_date date)')

class UniqueCred(Exception):  # User Defined Exception
    pass 

class wrongCred(Exception):
    pass



try:
    while 50:  # True
        print("1 ---- Signup")
        print("2 ---- Login")
        print("3 ---- Exit")
    
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input('Enter Name: ')
            gender = input('Enter Gender: ')
            age = int(input('Enter Age: '))
            username = input('Enter Email: ')
            cur.execute("select username from cust_details")
            list1 = cur.fetchall()   # [('A@gmail.com',), ('k@gmail.com',)]

            try:
                f = 0
                for subtup in list1:  # subtup = ('A@gmail.com',)
                    if subtup[0] == username:
                        f = 1
                        raise UniqueCred
                    
                if f == 0:
                    password = input('Enter Password: ')   # Regex
                    cur.execute("select date_format(sysdate(), '%Y-%m-%d') from dual")
                    joining_date = cur.fetchone()   # ('20-11-2023',)

                    cur.execute("select date_format(date_add(sysdate(), interval 1 year), '%Y-%m-%d') from dual")
                    ending_date = cur.fetchone()

                    print(joining_date, ending_date)   # ('20-11-2023',) ('20-11-2024',)
                    q = "insert into cust_details (NAME, GENDER, AGE, USERNAME, PASSWORD, joining_date, ending_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    t10 = (name, gender, age, username, password, joining_date[0], ending_date[0])
                    cur.execute(q, t10)
                    mydb.commit()

                    height = float(input('Enter height: '))
                    weight = float(input('Enter Weight: '))
                    BMI = 5   # formula


                    cur.execute("select id, username from cust_details")
                    list2 = cur.fetchall()
                    
                    for subtup in list2:
                        if subtup[1] == username:
                            id1 = subtup[0]
                            break
                    # print(id1)

                    s = "insert into phy_details (username, height, weight, bmi, id) values (%s, %s, %s, %s, %s)"
                    d3 = (username, height, weight, BMI, id1)
                    cur.execute(s, d3)
                    mydb.commit()
                    print('User Registred')

            except UniqueCred:
                    print("UserId Already Taken, Pls Choose Another")
            
    
        elif choice == 2:
            user_name = input('Enter Email: ')
            pass_word = input('Enter Password: ')

            cur.execute("select id, username, password from cust_details")
            list2 = cur.fetchall()

            p = 0   
            try:  
                for subtup in list2:
                    if subtup[1] == user_name and subtup[2] == pass_word:

                        cur.execute("select date_format(sysdate(), '%Y-%m-%d %h:%i:%s') from dual")
                        s_time = cur.fetchone()   # ('20-11-2023',)
                        print(s_time)
                        f1 = "insert into logs (username, entry_time, id) values (%s, %s, %s)"
                        d4 = (user_name,s_time[0], subtup[0])
                        print('Login Successfull....')

                        cur.execute(f1, d4)
                        mydb.commit()
                        p=1
                        break
                
                if p == 0:
                    raise wrongCred
            except wrongCred:
                print('Cred. Invalid, Pls Try Again')


        elif choice == 3:
            print('Thank you!!')
            break


except:
    print("Error Occured")

finally:
    if mydb.is_connected():
        cur.close()
        mydb.close()