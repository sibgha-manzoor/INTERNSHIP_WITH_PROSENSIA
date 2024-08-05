filename = 'output.txt'
text_to_append = 'End of file'

try:
    with open(filename, 'a') as file:
        file.write(text_to_append + '\n')
    
    print(f"'{text_to_append}' has been appended to '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")