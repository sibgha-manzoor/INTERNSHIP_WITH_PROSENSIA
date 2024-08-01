import re
from collections import Counter

def are_anagrams(str1, str2):
    def clean_string(s):
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    
    freq1 = Counter(cleaned_str1)
    freq2 = Counter(cleaned_str2)

    are_anagrams = freq1 == freq2

    return are_anagrams, {'freq1': dict(freq1), 'freq2': dict(freq2)}

str1 = "Listen!"
str2 = "Silent!"
result, frequencies = are_anagrams(str1, str2)
print(f"Are anagrams: {result}")
print(f"Frequencies: {frequencies}")