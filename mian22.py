from faker import Faker
import json

fake = Faker()

student_records = []
for i in range(100):
    name = fake.name()
    age = fake.random_int(min=18, max=25)
    grade = fake.random_int(min=60, max=100)
    active = fake.random_element(elements=[True, False])
    student = {
        "name": name,
        "age": age,
        "grade": grade,
        "active": active
    }
    student_records.append(student)

active_students = [student for student in student_records if student['active']]
inactive_students = [student for student in student_records if not student['active']]

print("Active Students:")
for student in active_students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

print("\nInactive Students:")
for student in inactive_students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

student_records_json = {
    "active_students": active_students,
    "inactive_students": inactive_students
}

with open('student_records.json', 'w') as f:
    json.dump(student_records_json, f, indent=4)
