student = {
    "name": "Pawan",
    "age": 30,
    "city": "Doha"
}

print(student["name"])  # Access name

student["course"] = "Python"  # Add new key
student["age"] = 31           # Update age
del student["city"]           # Remove city

print(student)
