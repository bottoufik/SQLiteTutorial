import sqlite3
# This code is made to add data to the previously created employee.db in "newconn.py"

#Connect again to the db
newconn = sqlite3.connect("employee.db")
#Get a cursor
add_data = newconn.cursor()

add_data.execute("INSERT INTO employees VALUES ('Sajal','Gupta',350000)")
add_data.execute("INSERT INTO employees VALUES ('Kollu','Nikhil',250000)")
add_data.execute("INSERT INTO employees VALUES ('Sai','Vikas',150000)")
add_data.execute("INSERT INTO employees VALUES ('Vishnu','Vardhan',300000)")

newconn.commit()
newconn.close()