""" Description
homEwork: tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. - DONE also, create one MORE senTENCE witH LAST WoRDS of each
existING SENtence and add it to the END OF this Paragraph. - DONE

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. - DONE

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I
got 87."""

import re


input_string = """ 
homEwork:
  tHis iz your homeWork, copy these Text to variable.


  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

input_string = input_string.capitalize()

# get list of words from the input string
sentences = re.split(r"(?<=\.|\?|\!)\s", input_string)

# normalizing string from letter case point of view
flag_to_change_case = False
for x in range(len(input_string) - 2):
    if flag_to_change_case and input_string[x].isalpha():
        input_string = input_string[0:x] + input_string[x].swapcase() + input_string[x + 1: len(input_string)]
        flag_to_change_case = False
    if input_string[x] in ['.', '\n', '\t']:
        flag_to_change_case = True

# creating string with last words of each sentence
string_with_last_words = ''
for sentence in sentences:
    # list_of_last_words.append(sentence)
    # print(sentence.split(" "))
    split_sentence = sentence.split(" ")
    # adding last words to the string without last dot symbol
    string_with_last_words += split_sentence[len(split_sentence) - 1][:len(split_sentence[len(split_sentence) - 1]) - 1] + ' '

string_with_last_words = string_with_last_words[:len(string_with_last_words) - 1] + '.'
input_string += ' ' + string_with_last_words

# fixing 'iz' to 'is'
input_string = re.sub(r'\b iz \b', ' is ', input_string)
print(input_string)

# counting of the whitespaces in the string
counter = len(re.findall(r'\s', input_string))
print("amount of whitespaces in the string is ", counter)


