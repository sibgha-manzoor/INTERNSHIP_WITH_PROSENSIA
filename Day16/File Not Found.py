filename = 'dat.txt'

try:
    with open(filename, 'r') as fhand:
        content = fhand.read()
        print("Content of the file:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")