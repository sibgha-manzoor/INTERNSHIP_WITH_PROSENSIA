def clean_whitespace(i_str):
    stripped_string = i_str.strip()
    
    cleaned_string = ' '.join(stripped_string.split())
    return cleaned_string

result = clean_whitespace("   This is  an example   string with  irregular spacing.  ")
print(result)
