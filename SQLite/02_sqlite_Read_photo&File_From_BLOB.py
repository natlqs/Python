'''
**从BLOB格式的数据，保存为图片和文件**
假如你现在想要读取保存在SQLite 表格里的 文件或图片，将它们以文件的格式重写写入到磁盘中，方便使用。
   下面将完成这个功能。步骤如下：

SQLite\\mydatabase.db 自己数据库的位置要放对。要做到与代码相符合。
SQLite和Python建立连接
建立一个cursor对象使用 connection对象
写好SELECT SQL语句完成自己需要的功能
用cursor.execute()执行SQL语句
使用 cursor.fetchall() 去取回所有符合要求的行，并遍历取回的数据。
然后，写一个函数完成将BLOB数据转化并保存为合适的格式。
关闭cursor和connection连接
'''
import sqlite3
import numpy


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect("SQLite\\mydatabase.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from students where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id= ", row[0], "Name= ", row[1])
            name = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            photoPath = "SQLite\\sqlite_Create" + name + ".jpg"
            resumePath = "SQLite\\sqlite_Create" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


readBlobData(1)
readBlobData(2)
