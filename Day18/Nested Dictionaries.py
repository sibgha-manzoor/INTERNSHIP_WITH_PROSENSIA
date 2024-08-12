students = {
    'student1': {
        'name': 'Jihan',
        'age': 20,
        'grades': {
            'Math': 85,
            'English': 92,
            'Science': 78
        }
    },
    'student2': {
        'name': 'Faris',
        'age': 22,
        'grades': {
            'Math': 88,
            'English': 79,
            'Science': 91
        }
    },
    'student3': {
        'name': 'Salar',
        'age': 21,
        'grades': {
            'Math': 95,
            'English': 85,
            'Science': 89
        }
    }
}

for student, info in students.items():
    print(f"{student}:")
    for key, value in info.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for subject, grade in value.items():
                print(f"    {subject}: {grade}")
        else:
            print(f"  {key}: {value}")