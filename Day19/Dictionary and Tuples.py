def dict_to_list_of_tuples():
    
    dict1 = {'x': 1, 'y': 2, 'z': 3}
    list_of_tuples = list(dict1.items())
    return list_of_tuples

print(dict_to_list_of_tuples())