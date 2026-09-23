import sqlite3


# Connect to SQLite and create company.db if it does not already exist.
connection = sqlite3.connect("company.db")

# Create a cursor for executing SQL statements.
cursor = connection.cursor()

# Create the department and employee tables.
cursor.execute("DROP TABLE IF EXISTS department")
cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute(
	"""
	CREATE TABLE department (
		id INTEGER PRIMARY KEY,
		name TEXT,
		location TEXT
	)
	"""
)
cursor.execute(
	"""
	CREATE TABLE employee (
		id INTEGER PRIMARY KEY,
		name TEXT,
		deptid INTEGER
	)
	"""
)

# Insert exactly five department records and five employee records.
departments = [
	(1, "Sales", "Mumbai"),
	(2, "Human Resources", "Delhi"),
	(3, "Information Technology", "Bengaluru"),
	(4, "Finance", "Chennai"),
	(5, "Research", "Hyderabad"),
]

employees = [
	(1, "Aarav Sharma", 1),
	(2, "Diya Patel", 3),
	(3, "Rohan Kumar", 3),
	(4, "Meera Singh", 2),
	(5, "Kabir Joshi", 99),
]

cursor.executemany(
	"INSERT INTO department (id, name, location) VALUES (?, ?, ?)",
	departments,
)
cursor.executemany(
	"INSERT INTO employee (id, name, deptid) VALUES (?, ?, ?)",
	employees,
)

# Save the inserted records to the database.
connection.commit()

# Fetch and display all employee records.
print("Employees:")
print("ID | Name           | DeptID")
print("---|----------------|-------")
cursor.execute("SELECT id, name, deptid FROM employee")
for employee in cursor.fetchall():
	print(f"{employee[0]}  | {employee[1]:14} | {employee[2]}")

print()

# Fetch and display all department records.
print("Departments:")
print("ID | Name                | Location")
print("---|---------------------|---------")
cursor.execute("SELECT id, name, location FROM department")
for department in cursor.fetchall():
	print(f"{department[0]}  | {department[1]:19} | {department[2]}")

# Find and display employees who work in the HR department.
print()
print("Employees in Human Resources:")
cursor.execute(
	"""
	SELECT employee.name
	FROM employee
	JOIN department ON employee.deptid = department.id
	WHERE department.name = 'Human Resources'
	"""
)
for employee in cursor.fetchall():
	print(employee[0])

# Close the cursor and the database connection.
cursor.close()
connection.close()
  