import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("INSERT INTO users (name,age)VALUES(?,?)",("deepika",24))
cursor.execute("INSERT INTO users (name,age)VALUES(?,?)",("medha",31))
conn.commit()
conn.close()