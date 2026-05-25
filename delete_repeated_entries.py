import sqlite3

newcon = sqlite3.connect("employee.db")
curr = newcon.cursor()

curr.execute("""
DELETE FROM employees
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM employees
    GROUP BY first, last, pay
);
""")

newcon.commit()
newcon.close()