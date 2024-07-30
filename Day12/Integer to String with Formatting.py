def format_int(ival,format_spec):
    formatted_value = format(ival,format_spec)
    return formatted_value

print(format_int(1234, 'o'))
print(format_int(1234, 'e'))
print(format_int(1234, 'E'))
print(format_int(1234, 'x'))
print(format_int(1234, 'X'))