import sqlite3
import os
import time

# Subroutine to print table from SELECT statement
def print_table(sql):
    db.execute(sql)
    all_rows = db.fetchall()
    for row in all_rows:
        for i in row:
            print(i, end='|')
        print()
    print()

# Removing any prexisting database
if os.path.isfile('database.db'):
    os.remove('database.db')

# Initialising the database connection
conn = sqlite3.connect('database.db')
db = conn.cursor()

# Creating Books table
db.execute('CREATE TABLE Books (bookID INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, publisher TEXT)')

# Inserting into Books table
db.execute('INSERT INTO Books VALUES (1, "JK Rowling", "Harry Potter and the Order of the Phoenix", 2003, "Bloomsbury")')
db.execute('INSERT INTO Books (bookID, author, title, year, publisher) VALUES (2, "Michael Morpurgo", "War Horse", 1982, "HarperCollins")')
db.execute('INSERT INTO Books VALUES (NULL, "Michael Morpurgo", "Private Peaceful", 2003, "HarperCollins")')

# Inserting using variables
author = 'Roald Dahl'
title = 'The BFG'
publisher = 'Penguin'
db.execute('INSERT INTO Books (bookID, author, title, publisher) VALUES (NULL,?,?,?)',(author,title,publisher))

# Updating year of Roald Dahl books
db.execute('UPDATE Books SET year=1982 WHERE author = "Roald Dahl"')

# Deleting JK Rowling books
db.execute('DELETE FROM Books WHERE author="JK Rowling"')

# Selecting all data in Books table
sql = 'SELECT * FROM Books'
print_table(sql)

# Saving database
conn.commit()
conn.close()

num = 1
while True:
    print('Si' + num * 'u')
    num+=1
    time.sleep(0.1)
