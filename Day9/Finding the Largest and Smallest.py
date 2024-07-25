sval = -1
lval = 0
for i in [5,4,7,8,34,56,78,23,58,37,15,17,27,35]:
    if sval is None:
        sval = i
    elif i < sval:
        sval = i
    if i > lval:
        lval = i 
print("Smallest value" , sval)    
print("Largest value" , lval) 