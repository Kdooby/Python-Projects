import sqlite3

# get personal dat from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

# execute insert statement for supplied person data
with sqlite3.connect("C:/Users/kevin/Documents/The Tech Academy/Python-Projects/test_database.db") as connection:
    c = connection.cursor()
    c.execute("UPDATE People SET Age=? WHERE firstName = ? AND lastName = ?", (45, 'Luigi', 'Vercotti'))
