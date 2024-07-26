def str_len(str_list):
    return [len(s) for s in str_list]

str = ["apple", "banana", "orange"]
lengths = str_len(str)
print(lengths)