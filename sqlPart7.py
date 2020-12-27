import sqlite3

# get personal dat from user
peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 423), ('Arthur', 'Belling', 30))

# execute insert statement for supplied person data
with sqlite3.connect("C:/Users/kevin/Documents/The Tech Academy/Python-Projects/test_database.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(firstName TEXT, lastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

# select all first and last names from people over age 30
    c.execute("SELECT firstName, lastName FROM People WHERE Age > 30")
    while True:
            row = c.fetchone()
            if row is None:
                    break
            print(row)
