while True: 
    line = input(">>")
    if line[0] == "#":
        continue
    if line  == "done":
        break
    print("Output" , line)