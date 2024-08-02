import re
from datetime import datetime

def validate_entries(entries):
    def is_valid_length(entry, min_length=5, max_length=20):
        return min_length <= len(entry) <= max_length

    def is_alphabetic(entry):
        return entry.isalpha()

    def is_numeric(entry):
        return entry.isdigit()

    def is_alphanumeric(entry):
        return entry.isalnum()

    def is_valid_email(entry):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, entry) is not None

    def is_valid_date(entry):
        try:
            datetime.strptime(entry, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    report = {}

    for entry in entries:
        report[entry] = {
            'length_valid': is_valid_length(entry),
            'alphabetic': is_alphabetic(entry),
            'numeric': is_numeric(entry),
            'alphanumeric': is_alphanumeric(entry),
            'email': is_valid_email(entry),
            'date': is_valid_date(entry)
        }
    
    return report

entries = [
    "test@example.com", "2024-08-01", "12345", "hello", "world123", 
    "short", "thisisaverylongstring", "invalid@date", "anotherinvalidemail@"
]

validation_report = validate_entries(entries)
for entry, results in validation_report.items():
    print(f"Entry: {entry}")
    for criterion, passed in results.items():
        status = "Passed" if passed else "Failed"
        print(f"  {criterion.replace('_', ' ').capitalize()}: {status}")
    print()