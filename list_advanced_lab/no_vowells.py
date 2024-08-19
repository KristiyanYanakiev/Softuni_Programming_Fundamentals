def no_vowels_filtered_text(some_text: str) -> str:
    filtered_text = [letter for letter in some_text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
    return "".join(filtered_text)

text = input()
print(no_vowels_filtered_text(text))
