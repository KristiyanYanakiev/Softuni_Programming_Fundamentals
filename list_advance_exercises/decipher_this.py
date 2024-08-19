def change_character_code_to_letter_for_each_word(string):
    end_index_of_char_code = 0
    letter_code = ""
    for current_element in string:
        if current_element.isdigit():
            letter_code += current_element
            end_index_of_char_code += 1

    end_index_of_char_code -= 1
    letter_code_as_int = int(letter_code)
    final_word = string.replace(string[0:end_index_of_char_code + 1], chr(letter_code_as_int))

    return final_word

def swap_letters(string):
    new_word = change_character_code_to_letter_for_each_word(string)
    new_word_as_list = list(new_word)
    new_word_as_list[1], new_word_as_list[-1] = new_word_as_list[-1], new_word_as_list[1]
    final_new_word = "".join(new_word_as_list)

    return final_new_word


def decipher_the_message(some_message):
    some_message = [swap_letters(element) for element in some_message]
    result = " ".join(some_message)
    return result


message = input().split()
print(decipher_the_message(message))






