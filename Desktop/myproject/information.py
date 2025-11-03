def calculate_student_gpa(student):
    grades = student["grades"]
    return sum(grades) / len(grades)

students_list = [
    {
        "student_id": 1,
        "name": "Ali",
        "grades": [18, 19, 20]
    },
    {
        "student_id": 2,
        "name": "Reza",
        "grades": [15, 14, 16.5]
    }
]

for student in students_list:
    gpa = calculate_student_gpa(student)
    print("--------------")
    print(f"ID: {student['student_id']}")
    print(f"Name: {student['name']}")
    print(f"GPA: {gpa:.2f}")

