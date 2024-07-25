nset = [5,4,7,8,34,56,78,23,58,37,15,17,27,35,34,67,67,15,58,35]
unique = []
for i in nset:
    if i not in unique:
        unique.append(i)
print(unique)