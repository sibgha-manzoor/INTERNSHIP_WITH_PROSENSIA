def format_string(template, values):
    result = template
    for key, value in values.items():
        placeholder = f'{{{key}}}'
        result = result.replace(placeholder, str(value))
    return result

template = "Hello, {name}! You are {age} years old."
values = {"name": "Sara", "age": 20}

formatted_string = format_string(template, values)
print(formatted_string)