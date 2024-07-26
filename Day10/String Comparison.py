def compare_strings_lexicographically(str1, str2):
    if str1 < str2:
        return f"'{str1}' comes before '{str2}' lexicographically."
    elif str1 > str2:
        return f"'{str1}' comes after '{str2}' lexicographically."
    else:
        return f"'{str1}' is equal to '{str2}' lexicographically."

result1 = compare_strings_lexicographically("apple", "banana")
result2 = compare_strings_lexicographically("orange", "apple")
result3 = compare_strings_lexicographically("grape", "grape")

print(result1)
print(result2)
print(result3)