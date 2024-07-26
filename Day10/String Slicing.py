def string_slicing(s, start_i, end_i):
    if start_i < 0:
        start_i = 0

    if end_i > len(s):
        end_i = len(s)

    if start_i > end_i:
        start_i, end_i = end_i, start_i

    return s[start_i:end_i]

result = string_slicing("Hello, Ana", 6, 10)
print(result) 
