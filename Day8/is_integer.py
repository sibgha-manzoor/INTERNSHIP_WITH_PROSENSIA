def is_integer(str):
    try:
        int(str)
        return True
    except:
        return False

print("123",is_integer("123")) 
print("hello",is_integer("hello")) 