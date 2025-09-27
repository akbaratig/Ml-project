import sqlite3
from tkinter import messagebox
from tkinter import *


def connect():
    connection = sqlite3.connect('Phone_books.db')
    cur = connection.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS PHONE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME INTEGER,
            EMAIL TEXT,
            GENDER INTEGER,
            MOBILE INTEGER,
            TEL INTEGER,
            ADDRESS TEXT
            );
    """
    
    cur.execute(sql)
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect('Phone_books.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM PHONE')
    row = cur.fetchall()
    connection.close()
    return row


def delete(ID):
    connection = sqlite3.connect('Phone_books.db')
    cur = connection.cursor()
    cur.execute('DELETE FROM PHONE WHERE ID=?', (ID,))
    connection.commit()
    connection.close()


def insert(name, email, gender, mobile, tel, address):
    connection = sqlite3.connect('Phone_books.db')
    cur = connection.cursor()
    cur.execute('INSERT INTO PHONE(NAME, EMAIL, GENDER, MOBILE, TEL, ADDRESS) VALUES(?, ?, ?, ?, ?, ?)'
               , (name, email, gender, mobile, tel, address))
    connection.commit()
    connection.close()


def update(id,name, email, gender, mobile, tel, address):
    connection = sqlite3.connect('Phone_books.db')
    cur = connection.cursor()
    cur.execute('UPDATE PHONE SET NAME=?, EMAIL=?, GENDER=?, MOBILE=?, TEL=?, ADDRESS=? WHERE ID=?', 
                (name, email, gender, mobile, tel, address,id))
    connection.commit()
    connection.close()
    

def search(name='', email='', gender='', mobile='', tel='', address=''):
    connection = sqlite3.connect('Phone_books.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM PHONE WHERE NAME=? OR EMAIL=? OR GENDER=? OR MOBILE=? OR TEL=? OR ADDRESS=?',
                (name, email, gender, mobile, tel, address))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    if len(rows) != 0:
        return rows
    else :
        print(messagebox.showerror('Wrong...........'))




connect()
insert('akbar', 'akbaratig@gmail.com', 'male', 9101741622, 4143333720,
       'bostan')
print(view())