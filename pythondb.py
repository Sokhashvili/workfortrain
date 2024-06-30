import sqlite3


conn = sqlite3.connect('company.db')
cursor = conn.cursor()


cursor.execute("SELECT * FROM department")
departments = cursor.fetchall()
print("Departments:")
for dept in departments:
    print(dept)


cursor.execute("SELECT * FROM employee")
employees = cursor.fetchall()
print("\nEmployees:")
for emp in employees:
    print(emp)

conn.close()