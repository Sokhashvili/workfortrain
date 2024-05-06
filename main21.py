import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_main_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)

    def write_to_json(self):
        main_grade = self.calculate_main_grade()
        output_data = {self.name: main_grade}
        with open('output.json', 'w') as file:
            json.dump(output_data, file, indent=4)


students_data = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 75]},
    {"name": "Bob", "age": 21, "grades": [80, 88, 92]},
    {"name": "Charlie", "age": 22, "grades": [70, 75, 65]}
]


for student_data in students_data:
    name = student_data["name"]
    age = student_data["age"]
    grades = student_data["grades"]
    student = Student(name, age, grades)
    main_grade = student.calculate_main_grade()
    print(f"{name}: {main_grade}")