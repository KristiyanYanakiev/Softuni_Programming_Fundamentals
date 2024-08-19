word = input()
reverse_word = ""

for current_index in range(len(word) - 1, -1, -1):
    reverse_word += word[current_index]

print(reverse_word)
