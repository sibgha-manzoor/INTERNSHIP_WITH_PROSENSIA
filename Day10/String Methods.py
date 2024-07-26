def transform_string(s):
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title()
    }
result = transform_string("hello world")
print(result)
