sequence_of_words = input().split()

words_dict = {}


for word in sequence_of_words:
    word_lower = word.lower()
    if word.lower() not in words_dict.keys():
        words_dict[word.lower()] = 0
    words_dict[word.lower()] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key.lower(), end=" ")
