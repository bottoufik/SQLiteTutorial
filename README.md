## About
This is a tutorial on sqlite using python. SQLite is a popular, free, and open-source relational database engine. It is "serverless" and stores the entire database—tables, indexes, and data—as a single, ordinary disk file. Because there is no separate server process, it requires zero configuration.
This tutorial is inspired from this [Youtube Video](https://www.youtube.com/watch?v=pd-0G0MigUA).

## Contents
The code files should be viewed in a certain order:

1. `newconn.py`: This file is only for showing that a new connection can be created using `sqlite.connect` command and a database and a table `employees` is created.
2. `adding_data_todb.py`: This file mainly shows how to add data to the table created using SQL commands along with Python.
3. `delete_repeated_entries.py`: This file is used deleting multiple entries as the table as no primary key, many duplicate entries are there.
4. `querying_data.py`: This file is used to query data from the table using SQL queries with Python.
5. `employee.py`: This file is used to create an `Employee` class so that it can be used further for data entry in the table.
6. `adding_data_using_class_intodb.py`: This file used to enter data into the table `employees` using objects created from the `Employee` class in "employee.py". It further shows different insertion methods.
7. `crud_op_intodb.py`: 