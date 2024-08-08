def get_top_n_words(file_path, N):
    counts = {}
    
    with open(file_path, 'r') as fhand:
        for line in fhand:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
    
    lst = [(val, key) for key, val in counts.items()]
    
    lst.sort(reverse=True)

    return lst[:N]

file_path = 'Song Lyrics.txt'
N = 3
top_words = get_top_n_words(file_path, N)

for count, word in top_words:
    print(word, count)