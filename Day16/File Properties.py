import os

filename = 'log.txt'

try:
    file_size = os.path.getsize(filename)
    print(f"The size of '{filename}' is {file_size} bytes.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")