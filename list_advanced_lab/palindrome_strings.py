def check_palindrome(some_word):
    return some_word == some_word[::-1]


list_of_words = input().split()
palindrome = input()

list_of_palindromes = [element for element in list_of_words if check_palindrome(element)]
print(list_of_palindromes)
number_of_palindrome_occurrences = list_of_palindromes.count(palindrome)

print(f"Found palindrome {number_of_palindrome_occurrences} times")

