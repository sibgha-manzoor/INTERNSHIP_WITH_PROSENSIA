fhand = open('log.txt', 'r')
lines = fhand.readlines()
for line in lines:
    if 'error' in line.lower():
        print(line.strip())
fhand.close()