import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute ('''
CREATE TABLE IF NOT EXISTS customer(
    O_id INTEGER PRIMARY KEY AUTOINCREMENT,
    C_id INTEGER,
    Amount FLOAT,
    date DATE        
)
''')
conn.commit()
conn.close()