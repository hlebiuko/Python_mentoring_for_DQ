""" Description
homEwork: tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. - DONE also, create one MORE senTENCE witH LAST WoRDS of each
existING SENtence and add it to the END OF this Paragraph. - DONE

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. - DONE

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I
got 87."""

import re


# Function to normalize given string
def string_normalizing(current_string: str) -> str:
    current_string = current_string.capitalize()
    flag_to_change_case = False
    for x in range(len(current_string) - 2):
        if flag_to_change_case and current_string[x].isalpha():
            current_string = current_string[0:x] + current_string[x].swapcase() + current_string[
                                                                                  x + 1: len(current_string)]
            flag_to_change_case = False
        if current_string[x] in ['.', '\n', '\t', '?', '!']:
            flag_to_change_case = True
    return current_string  # returning changed string


# Function to create sentence from the last words in the text
def create_sentence_of_the_last_words(current_string: str) -> str:
    sentences = re.split(r"(?<=\.|\?|\!)\s", current_string)
    string_with_last_words = ''
    for sentence in sentences:
        split_sentence = sentence.split(" ")
        string_with_last_words += split_sentence[len(split_sentence) - 1][
                                  :len(split_sentence[len(split_sentence) - 1]) - 1] + ' '
    return string_with_last_words[:len(string_with_last_words) - 1] + '.'


# Function to fix string
def fix_substring_in_string(current_string: str, initial_substring='iz', correct_substring='is') -> str:
    # return the string with replacements of provided substrings
    return current_string.replace(initial_substring, correct_substring)


# function to calculate the whitespaces in provided string
def calculating_whitespaces(current_string: str) -> int:
    return len(re.findall(r'\s', current_string))


input_string = """  
homEwork:
    tHis iz your homeWork, copy these Text to variable.

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

"""


# function to reformat provided text
def reformat_the_text(initial_string: str) -> str:
    reformatted_string = string_normalizing(initial_string)
    reformatted_string += ' ' + create_sentence_of_the_last_words(reformatted_string)
    reformatted_string = fix_substring_in_string(reformatted_string, ' iz ', ' is ')  # calling function to fix iz to is

    return reformatted_string  # return reformatted text


print(reformat_the_text(input_string))
# print to the console counter of the whitespaces for modified string
print("Number of whitespace characters in modified text = ", calculating_whitespaces(reformat_the_text(input_string)))
