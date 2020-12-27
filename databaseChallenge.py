import sqlite3

conn = sqlite3.connect(':memory:')


Name = input("Full Name: ")
Species = input("Species: ")
IQ = int(input("Enter IQ: "))
rosterData = (Name, Species, IQ)


with sqlite3.connect("db_Roster.db") as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS Roster;
                    CREATE TABLE Roster(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
                    Name TEXT,
                    Species TEXT,
                    IQ INT);
                    """)
    
    c.execute("INSERT INTO Roster (Name, Species, IQ)VALUES(?, ?, ?)", rosterData)
    conn.commit()
conn.close()
    


