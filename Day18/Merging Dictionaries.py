def merge_dictionaries(dict1, dict2):
   merged_dict = dict1.copy()  
   merged_dict.update(dict2)   
    
   return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

result = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", result)