# Task 2 Part 1
# Write a code, which will:
# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

import random
import string

list_of_dicts = []
number_of_dicts = random.randint(3, 10)


def dict_sort(my_dict: dict) -> dict:  # function that gets dict as argument and return sorted dict
    keys = list(my_dict.keys())  # getting list of keys for given dict
    keys.sort()  # sorting list of keys from the dict
    return {key: my_dict[key] for key in keys}  # returning dict with sorted keys


# 'while' loop was selected because of by using 'for' loop may cause loss duplicates of keys f.e. if generated value for
# amount of keys was 26, and we will have duplicates in keys value (2 times 'a' char) - we will have fewer keys in total
while True:  # Loop for filling in list by dicts
    temp_dict = {}  # initialization temp dict variable to collect generated values
    number_of_pairs_in_dict = random.randint(3, 26)  # initialization and generating value for number of pairs in dict
    while True:  # Loop for filling in the dict
        temp_dict[''.join(random.choices(string.ascii_lowercase))] = random.randint(0, 100)  # adding random char as
        # a key and random int in range 0-100 as a pair into the dict
        if len(temp_dict) == number_of_pairs_in_dict:  # Check if required amount of keys are already generated
            break  # Closing the loop filling the dict
    temp_dict = dict_sort(temp_dict)  # Sorting generated dict by function dict_sort
    list_of_dicts.append(temp_dict)  # Adding generated dict to the list of dicts

    if len(list_of_dicts) >= number_of_dicts:  # Check length of list with dicts is less than required
        break  # break for loop when list will be filled up appropriate count times

# Task 2 Part 2
# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
new_dict = {}  # Initialization new dict variable
dict_for_changed_elements = {}  # Initialization dict variable for changed elements (key = key, value = dict number)

for dict_num, current_dict in enumerate(list_of_dicts, start=1):        # Loop for detecting duplicates in keys
    for key in current_dict:            # loop for filling in new_dict with all values
        if key in new_dict:
            if current_dict[key] > new_dict[key]:
                new_dict[key] = current_dict[key]
                dict_for_changed_elements[key] = dict_num
        else:
            new_dict[key] = current_dict[key]
            dict_for_changed_elements[key] = dict_num

new_final_dict = {}  # dict variable for items with proper key names

for key in new_dict:        # loop for creating dict with proper keys
    new_final_dict[key + "_" + str(dict_for_changed_elements[key])] = new_dict[key]

new_final_dict = dict_sort(new_final_dict)  # sorting final dict
print(new_final_dict)  # print final result - can be deleted
