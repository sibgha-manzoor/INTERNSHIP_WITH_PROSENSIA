def compare_tuples(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")
    
    comparison_results = []
    for i in range(len(t1)):
        comparison_results.append(t1[i] == t2[i])
    return comparison_results

tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)

result = compare_tuples(tuple1, tuple2)
print(result)