def sort_tuples(d):
    list_of_tuples = list(d.items())
    print("Befor sorting:" ,list_of_tuples)
    
    list_of_tuples.sort(key=lambda x: x[1], reverse=True)
    return list_of_tuples

dict1 = {'a': 10, 'b': 1, 'c': 22}
print(sort_tuples(dict1))