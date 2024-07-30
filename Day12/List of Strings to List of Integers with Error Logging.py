def convert_str_to_ints(str_list):
    int_list = []
    error_log = []
    
    for item in str_list:
        try:
            int_list.append(int(item))
        except ValueError:
            error_log.append(f"Error converting '{item}' to integer.")
    
    return int_list, error_log

strings = ["123", "abc", "456", "78.9", "100"]
integers, errors = convert_str_to_ints(strings)

print("Converted integers:", integers)
print("Error log:", errors)