students = []

def add_student(name, age):
    students.append({"name": name, "age": age, "courses": []})
students_to_add = [
    ("Alice", 22),
    ("Bob", 24),
    ("Charlie", 20),
    ("Pawan",30)
]
for name, age in students_to_add:
    add_student(name, age)

print("Students added:")
for student in students:
    print(student)
print("-" * 40)
def update_age(name, new_age):
    for student in students:
        if student["name"] == name:
            student["age"] = new_age
            break

def add_course(name, course):
    for student in students:
        if student["name"] == name:
            if course not in student["courses"]:
                student["courses"].append(course)
            break

def print_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")

# Test it out
add_course("Pawan", "Python")
add_course("Alice", "GCP")
add_course("Bob","Azure")
add_course("Charlie","AWS")
update_age("Pawan", 35)
print_students()
