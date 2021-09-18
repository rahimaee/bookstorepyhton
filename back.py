import sqlite3


def connect():
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT  * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def Search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT  * FROM book WHERE  title=? OR  author=? OR year=? OR isbn=?", (title, author, year, isbn))
    res = cur.fetchall()
    conn.close()
    return res


def Delete(id):
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()


def Update(id, title, author, year, isbn):
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?" , (title, author, year, isbn,id))
    conn.commit()
    conn.close()


connect()
# insert("python book","ahmad",2020,2030)
# print(Search(isbn=2030))
# Update(4,"Csharp","mohammadreza",2021,1020)

# Delete(2)
