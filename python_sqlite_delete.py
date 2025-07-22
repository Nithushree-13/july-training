import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("delete from users where age=31")
conn.commit()
conn.close()