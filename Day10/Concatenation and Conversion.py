def concatenate_and_convert(s1, s2):
    concatenated = s1 + s2
    try:
        return int(concatenated)
    except :
        return concatenated

print(concatenate_and_convert("Hi ","Sara"))  
print(concatenate_and_convert('1', '5'))  
print(concatenate_and_convert('1', 'f'))  