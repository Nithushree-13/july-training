import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("update users set name='Mira' where age=25")
conn.commit()
conn.close()