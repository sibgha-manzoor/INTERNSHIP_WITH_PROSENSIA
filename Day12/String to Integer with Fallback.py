def str_to_int(str,def_val):
    try:
        return int(str)
    except:
        return def_val

print(str_to_int("123",0))
print(str_to_int("r",-1))