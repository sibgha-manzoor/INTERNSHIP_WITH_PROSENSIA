def transform_string(text):
    digit_to_word = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    replaced_digits = ''.join(digit_to_word.get(char, char) for char in text)
    
    words = replaced_digits.split()
    
    transformed_words = [word[::-1] if len(word) > 5 else word for word in words]
    
    title_case_text = ' '.join(transformed_words).title()
    
    return title_case_text

text = "The quick brown fox jumps over the lazy dog 1 2 3 4 5."
print(transform_string(text))