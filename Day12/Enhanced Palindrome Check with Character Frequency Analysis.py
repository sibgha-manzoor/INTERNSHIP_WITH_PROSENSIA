def process_string(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    is_palindrome = cleaned_string == cleaned_string[::-1]
    
    char_frequencies = {}
    for char in cleaned_string:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1
    
    return is_palindrome, char_frequencies

result = process_string("A man, a plan, a canal: Panama")
print(result)