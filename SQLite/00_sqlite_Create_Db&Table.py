import sqlite3

# 连接到数据库
conn = sqlite3.connect('SQLite\\mydatabase.db')

# 创建一个游标对象
cursor = conn.cursor()

# 创建表格
# 创建一个名为students的表，包含id, name, photo, resume对象
cursor.execute('''CREATE TABLE students (
                id INTEGER PRIMAY KEY,
                name TEXT NOT NULL,
                photo BLOB NOT NULL,
                resume BLOB NOT NULL);''')
conn.commit()
conn.close()
