count = dict()
line = input("Enter a line:")
words = line.split()

print("Words:",words)

for word in words:
    count[word] = count.get(word,0) + 1
    
print("Count:", count)