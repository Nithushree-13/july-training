import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
n=int(input("enter the value of n"))
for i in range(n):
    name=input("enter the name: ")
    age=input("enter the age:")
    cursor.execute("INSERT INTO users (name,age)VALUES(?,?)",(name,age))
    
conn.commit()
conn.close()