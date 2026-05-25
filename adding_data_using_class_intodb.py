import sqlite3
from employee import Employee

connection = sqlite3.connect("employee.db")
curr = connection.cursor()

emp_1 = Employee("John","Doe", 400000)
emp_2 = Employee("Jane","Doe", 200000)
emp_3 = Employee("Jack", "Doe", 350000)

#Inserting values using the class into the database
#Method 1: Using .format as placeholders (SQL Injection Vulnerable)
curr.execute("INSERT INTO employees VALUES ('{}','{}','{}')".format(emp_1.first,emp_1.last,emp_1.pay))
#Method 2: Using ? as placeholders
curr.execute("INSERT INTO employees VALUES (?,?,?)",(emp_2.first,emp_2.last,emp_2.pay))
#Method 3: The dictionary method
curr.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp_3.first,'last':emp_3.last,'pay':emp_3.pay})

#Querying data using placeholders
curr.execute("SELECT * FROM employees WHERE last=?",('Doe',))
print(curr.fetchall())
curr.execute("SELECT * FROM employees WHERE last=:last",{'last':'Doe'})
print(curr.fetchall())


connection.commit()
connection.close()