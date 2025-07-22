import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("INSERT INTO users (name,age)VALUES(?,?)",("Rumi",25))
cursor.execute("INSERT INTO users (name,age)VALUES(?,?)",("Mira",30))
conn.commit()
conn.close()
