import sqlite3

def connect():
    conn=sqlite3.connect("lib.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARY KEY,Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lib.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library ")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(title,author,year,isbn):
    conn=sqlite3.connect("lib.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL,?,?,?,?) ",(title,author, year, isbn))
    conn.commit()
    conn.close()
    view()

def delete(id):
    conn=sqlite3.connect("lib.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("lib.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
    entry=cur.fetchall()
    conn.close()
    return entry

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("lib.db")
    cur=conn.cursor()
    cur.execute("UPDATE library SET title=?,author=?,year=?, isbn=? WHERE id=?",(title,author,year, isbn, id))
    conn.commit()
    conn.close()

connect()
