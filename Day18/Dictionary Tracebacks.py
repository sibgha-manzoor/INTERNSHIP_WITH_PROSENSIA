student_grades = {
    'Ayeshs': 85,
    'Babar': 92,
    'Sara': 78
}

try:
    name = 'Dani'
    grade = student_grades[name]
except KeyError:
    print(f"Error: The key {name} does not exist in the dictionary.")
else:
    print(f"{name}'s grade is {grade}.")