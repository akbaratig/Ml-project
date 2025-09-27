import sqlite3

def connect():
    connection = sqlite3.connect('Library.db')
    cur = connection.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS BOOKS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT, 
            Author TEXT,
            year INTEGER,
            isbn INTEGER
        );
    """
    cur.execute(sql)
    
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = sqlite3.connect('Library.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO BOOKS (Title, Author, year, isbn) VALUES (?, ?, ?, ?)",
                (title, author, year, isbn))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect('Library.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM BOOKS')
    rows = cur.fetchall()
    connection.close()
    return rows


def search(title="", author="", year="", isbn=""):
    connection = sqlite3.connect('Library.db')
    cur = connection.cursor()
    cur.execute('SELECT * FROM BOOKS WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cur.fetchall()
    connection.close()
    if len(rows) != 0:
        return rows
    else :
        return f"Wrong........"


def delete(id):
    connection = sqlite3.connect('Library.db')
    cur = connection.cursor()
    cur.execute('DELETE FROM BOOKS WHERE ID=?', (id,))
    connection.commit()
    connection.close()
   
    
def update(id,title, author, year, isbn ):
    connection = sqlite3.connect('Library.db')
    cur = connection.cursor()   
    cur.execute('UPDATE BOOKS SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
    connection.commit()
    connection.close()    
    
    
connect()
insert('Python books', 'akbar', 1998, 2525)
insert('java books', 'ali', 2001, 2525)
insert('c++ books', 'ehsan', 1965, 2525)
