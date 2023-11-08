import mysql.connector

mydb = mysql.connector.connect(user = "root", password = "mysql", host = "localhost", database = "club")

if mydb.is_connected():
    print("Database Connected...")
else:
    print("Error ocuured")


cur = mydb.cursor()

cur.execute("create table if not Exists Demo (id int primary key auto_increment, name varchar(30) Not null) ")
cur.execute("create table if not Exists royal (id int, name varchar(30) Not null) ")


# cur.execute("Alter table royal add primary key(id)")

# cur.execute("insert into royal values (10, 'Aman')")
# cur.execute("insert into demo (name, gender) values ('Aman', 'M')")
# cur.execute("insert into demo (id, name, gender) values (56, 'Aman', 'M')")

name = "jk"
gender = 'F'
id = 88

# query = "INSERT INTO DEMO (NAME, GENDER) VALUES (%s, %s)"
# tuple1 = (name, gender)

# cur.execute(query, tuple1)

# cur.execute("INSERT INTO DEMO (id, NAME, GENDER) VALUES (%s, %s, %s)".format(id, name, gender))


cur.execute("Select name, id from demo where gender = 'M'")

# x = cur.fetchone()   # ('Aman', 1)
x = cur.fetchall()
print(x)  # [('Aman', 1), ('Aman', 2), ('Aman', 56), ('Aman', 57), ('Kaushal', 58)]


for subtup in x:
    if subtup[0] == 'Kaushal':
        print(True)

from datetime import datetime

joining = datetime.today()

print(joining)
cur.execute("select date_add(sysdate(), interval 1 year) sdcvsdcsc from dual")

# mydb.commit()