

import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_FileName TEXT) ")
    conn.commit()
conn.close ()




conn = sqlite3.connect('assignment.db')

# tuple of files
files_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')




# Loops through each object to find the files that end in '.txt'
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # x representing the name of each object in the tuple, will denote a one element tuple for each name ending in '.txt'
            cur.execute("INSERT INTO tbl_Files (col_FileName) VALUES (?)", (x,))
            print(x)
conn.close()
