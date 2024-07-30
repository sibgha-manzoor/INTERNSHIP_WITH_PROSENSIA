def split_and_join(string, delimiter1, delimiter2):
    if not isinstance(string, str):
        raise TypeError("The string must be of type str.")
    if not isinstance(delimiter1, str) or not isinstance(delimiter2, str):
        raise TypeError("Both delimiters must be of type str.")
    
    split_list = string.split(delimiter1)
    filtered_list = [element for element in split_list if len(element) > 3]
    joined_string = delimiter2.join(filtered_list)
    
    return joined_string

print(split_and_join("apple,banana,kiwi,grape", ",", ";"))