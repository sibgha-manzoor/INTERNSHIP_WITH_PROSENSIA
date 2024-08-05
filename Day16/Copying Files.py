sourcefile = 'data.txt'
destinationfile = 'data_copy.txt'

try:
    with open(sourcefile, 'r') as source_file:
        content = source_file.read()
    
    with open(destinationfile, 'w') as destination_file:
        destination_file.write(content)
    
    print(f"Contents of '{sourcefile}' have been copied to '{destinationfile}'.")
except FileNotFoundError:
    print(f"Error: The file '{sourcefile}' does not exist.")