import sqlite3

conn = sqlite3.connect('contact.db')
c = conn.cursor()

c.execute("""
    create table if not exists messages(
        id integer primary key autoincrement,
        name text not null,
        email text not null,
        message text not null,
        create_at timestamp defualt current_timestamp
          )
    """)

conn.commit()
conn.close()