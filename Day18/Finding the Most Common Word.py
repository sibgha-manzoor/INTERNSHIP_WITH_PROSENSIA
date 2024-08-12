def count_words_in_file(filename):
    word_count = {}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.lower().split()
                
                for word in words:
                    word = word.strip(".,!?\"'()[]{}:;")
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
                        
        most_frequent_word = max(word_count, key=word_count.get)
        print(f"The most frequent word is '{most_frequent_word}' with a count of {word_count[most_frequent_word]}.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'Error.txt'
count_words_in_file(filename)