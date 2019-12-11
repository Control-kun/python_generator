import mysql.connector
import random
from faker import Faker

fake = Faker()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test",
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

query = 'INSERT INTO employee(dep_id,name) VALUES (%s, %s)'

for x in range(0, 1000):
    print(x)
    my_data = tuple((random.randint(1, 2), fake.name()) for i in range(0, 1000))
    # print(my_data)
    cursor.executemany(query, my_data)
    mydb.commit()


query = 'INSERT INTO salary(ts,empl_id,amount) VALUES (%s, %s, %s)'

for x in range(0, 1000):
    # print(x)
    my_data = tuple((fake.date_time_this_year(), fake.random_int(1, 1000000), fake.random_int()) for i in range(0, 1000))
    print(my_data)
    cursor.executemany(query, my_data)
    mydb.commit()
cursor.close()
