def reverse_string(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

str = "QWERTY"
print("Reversed string:", reverse_string(str))