def format_binary_string(binary_str, fixed_length):
    integer_value = int(binary_str, 2)
    
    formatted_binary_str = format(integer_value, f'0{fixed_length}b')
    
    return integer_value,formatted_binary_str

result = format_binary_string("1101", 8)
print(result) 