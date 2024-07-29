def Convert_Str_to_Int(str_list):
    integers = []
    for i in string_list:
        try:
            num = int(i)
            integers += [num]   
        except:
            continue
    return integers
    
string_list = ["hi","24","13"]
print(Convert_Str_to_Int(string_list)) 




