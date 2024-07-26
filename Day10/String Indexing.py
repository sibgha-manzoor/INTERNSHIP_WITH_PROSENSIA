def str_i(str, i):
    if i < 0 or i >= len(str):
        return "Error: Index is out of bounds"
    else:
        return str[i]
print(str_i("Hello, World!", 0)) 
print(str_i("Hello, World!", 7))  
print(str_i("Hello, World!", 15))  