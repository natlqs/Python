'''
本文将使用Python的SQLite3模块，来完成 在SQLite表 里 插入与保存 文件，这里使用的格式是BLOB。
使用 SQLite BLOB数据类型保存二进制数据于SQLite 表格中，用Python完成
从Sqlite表格 中 读取BLOB二进制数据，用Python完成

**前置知识**
在执行下面的SQLite BLOB操作前，需要知道插入数据的表名以及列名。
所以我们需要 新建 一个表可以存储数据。

教程里使用了名为 students 的表
你也可以用如下的query语句新建一个表，或则在SQLiteStudio软件里新建。

CREATE TABLE new_employee ( id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            photo BLOB NOT NULL,
                            resume BLOB NOT NULL);

这个表含有两个BLOB列。

一个 photo列用来保存员工的图片
一个 resume列用来保存员工的简历

**什么是BLOB**
BLOB(large binary object) 是一种SQLite的数据类型，用来存储大容量的对象，通常是较大的文件如图片，声音，适配，文档等。
   我们需要把文件与图片转化为二进制数据（byte array在Python里），然后再保存在SQLite数据库里。
'''
# region [插入图片和文件]
# 插入图片和文件
import sqlite3


def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBlob(empId, name, photo, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('SQLite\\mydatabase.db')
        cusor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO students
                            (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cusor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cusor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


insertBlob(1, "张三", "SQLite\\zs.jpg", "SQLite\\zs_resume.txt")
insertBlob(2, "ls", "SQLite\\ls.jpg", "SQLite\\ls_resume.txt")

# endregion
