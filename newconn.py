import sqlite3

#Creating a connection
newcon = sqlite3.connect("employee.db")
#creating a cursor
c = newcon.cursor()
#Writing commands using that cursor
c.execute("""CREATE TABLE employees(
          first text,    
          last text,
          pay integer
)""")

# Commit changes in the database
newcon.commit()
newcon.close()