import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")
curr = conn.cursor()

def insert_emp(emp):
    # Using context manager "with" so that no need to commit again
    with conn:
        curr.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
    curr.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname})
    return curr.fetchall()

def update_pay(emp, pay):
    with conn:
        curr.execute("""UPDATE employees SET pay=:pay
                     WHERE first=:first AND last=:last""",
                     {'first':emp.first, 'last': emp.last, 'pay':pay})

def remove_emp(emp):
    with conn:
        curr.execute("DELETE from employees WHERE first=:first AND last=:last",
                     {'first':emp.first, 'last': emp.last})