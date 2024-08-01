def matches_pattern(s, pattern):
    if len(s) != len(pattern):
        return False

    for char, pat in zip(s, pattern):
        if pat.isalpha():
            if not char.isalpha():
                return False
        elif pat.isdigit():
            if not char.isdigit():
                return False
        else:
            return False

    return True

s = "a1b2"
pattern = "a1b2"
result = matches_pattern(s, pattern)
print(f"Does the string match the pattern? {result}")

s = "a1bX"
pattern = "a1b2"
result = matches_pattern(s, pattern)
print(f"Does the string match the pattern? {result}")