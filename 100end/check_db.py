import sqlite3

conn = sqlite3.connect('contact.db')

c = conn.cursor()
c.execute('select * from messages;') 

data = c.fetchall()
print(data)

conn.commit()
conn.close()