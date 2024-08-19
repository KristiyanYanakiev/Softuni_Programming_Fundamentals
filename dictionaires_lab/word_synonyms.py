count_of_words = int(input())
synonyms = {}

for _ in range(count_of_words):
    term = input()
    synonym = input()
    if term not in synonyms.keys():
        synonyms[term] = [synonym]
    else:
        if synonym not in synonyms.values():
            synonyms[term].append(synonym)


for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")



