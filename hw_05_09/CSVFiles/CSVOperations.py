import csv
import re
from hw_05_09.config import DEFAULT_FILE_TO_CSV_WORDS_FILE, DEFAULT_FILE_TO_CSV_LETTERS_FILE, FILE_TO_WRITE_PATH

"""Calculate number of words and letters from previous Homeworks 5/6 output test file.

Create two csv:

1.word-count (all words are preprocessed in lowercase)

2.letter, count_all, count_uppercase, percentage (add header, space characters are not included)

CSVs should be recreated each time new record added.

"""


class CSVOperations:

    # function to create csv file with words and count of it's appearance
    @staticmethod
    def create_csv_with_words(dict_of_words: dict):
        file_path = DEFAULT_FILE_TO_CSV_WORDS_FILE  # get path to file that will be created
        try:  # error handler
            # open file to write
            with open(file_path, 'w', newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)  # initialization of the file writer
                for key, value in dict_of_words.items():  # loop threw dict with words
                    writer.writerow([key, value])  # write dict item to the file
        except BaseException as exception:  # exception handler
            print(exception)  # print appeared exception

    # function to create csv file with letters
    @staticmethod
    def create_csv_with_letters(list_of_dicts_with_letters: list):
        file_path = DEFAULT_FILE_TO_CSV_LETTERS_FILE  # get path to file that will be created
        fieldnames = ["letter", "count_all", "count_uppercase", "percentage"]  # list of headers
        try:  # error handler
            with open(file_path, 'w', newline="", encoding="utf-8") as csv_file:  # open file to write
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  # initialization of the file writer
                writer.writeheader()  # write headers
                for sublist in list_of_dicts_with_letters:  # for each provided list item
                    # write line with provided date
                    writer.writerow({'letter': sublist[0], 'count_all': sublist[1],
                                     'count_uppercase': sublist[2], 'percentage': sublist[3]})
        except BaseException as exception:  # exception handler
            print(exception)  # print found exception

    @staticmethod
    def create_csv_files(file_path=FILE_TO_WRITE_PATH):
        from hw_05_09.OperationsWithFiles.fileReader import FileReader
        records_list = FileReader.get_records_from_file(file_path)
        CSVOperations.create_csv_with_words(CSVOperations.get_dict_with_all_words_and_its_count_from_file(records_list))
        CSVOperations.create_csv_with_letters(
            CSVOperations.get_dict_of_all_letters_with_its_count_from_file(records_list))

    @staticmethod
    def get_dict_with_all_words_and_its_count_from_file(records_list: list) -> dict:
        dict_of_words = {}
        separated_list_of_words = []
        for record in records_list:
            separated_list_of_words.append(re.findall(r"[\w'-]+", record.lower()))  # separating records by words
        for list_of_words in separated_list_of_words:
            for word in list_of_words:
                if word.isalpha() and word not in '\'':
                    if word in dict_of_words:
                        dict_of_words[word] += 1
                    else:
                        dict_of_words[word] = 1
        return dict_of_words

    @staticmethod
    def get_dict_of_all_letters_with_its_count_from_file(records_list):
        dict_of_letters = {}
        dict_of_capital_letters = {}
        separated_list_of_words = []
        counter_of_all_letters = 0
        for record in records_list:
            separated_list_of_words.append(re.split(r'\W+', record))  # separating records to the words
        for list_of_words in separated_list_of_words:
            for word in list_of_words:
                if word.isalpha():
                    for char in word:
                        counter_of_all_letters += 1
                        if char.isupper():
                            dict_of_capital_letters[char.lower()] = dict_of_capital_letters.get(char.lower(), 0) + 1
                        dict_of_letters[char.lower()] = dict_of_letters.get(char.lower(), 0) + 1

        list_of_lists_of_records = []

        for key in dict_of_letters:
            sub_list = [key]
            if key in dict_of_capital_letters:
                sub_list.append(dict_of_letters[key])
                sub_list.append(dict_of_capital_letters[key])
            else:
                sub_list.append(dict_of_letters[key])
                sub_list.append(0)
            sub_list.append(sub_list[1] * 100 / counter_of_all_letters)
            list_of_lists_of_records.append(sub_list)

        return list_of_lists_of_records
