def reverse_and_sort_dict(d):
    return sorted([(v, k) for k, v in d.items()])

c = {'a': 10, 'b': 1, 'c': 22}
print(reverse_and_sort_dict(c))