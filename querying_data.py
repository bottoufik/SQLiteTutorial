import sqlite3

conn = sqlite3.connect("employee.db")
curr = conn.cursor()

curr.execute("""SELECT * FROM employees""")
print(curr.fetchall())
curr.execute("""SELECT * FROM employees WHERE pay>200000""")
print(curr.fetchall())
curr.execute("""SELECT * FROM employees WHERE last = 'Vikas'""")
print(curr.fetchone())
curr.execute("""SELECT * FROM employees WHERE first LIKE 'S%';""")
print(curr.fetchall())


conn.commit()
conn.close()