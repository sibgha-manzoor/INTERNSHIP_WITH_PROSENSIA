def Convert_Str_to_Int(str):
    try:
        int(str)
        return str
    except:
        return None  
print(Convert_Str_to_Int("123")) 
print(Convert_Str_to_Int("HI")) 