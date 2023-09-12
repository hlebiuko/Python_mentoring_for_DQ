import os.path
import re
from hw_05_09.config import file_to_read_path, file_to_write_path, separator, pattern_text, pattern_city_timestamp, \
    pattern_ad_exp_date, default_file_to_read_news
from hw_05_09.DataTypes.news import News
from hw_05_09.DataTypes.privateAd import PrivateAd
from hw_05_09.DataTypes.joke import Joke
from hw_05_09.DataTypes.record import Record
from datetime import datetime



class FileReader:
    def __init__(self, input_file_path=default_file_to_read_news):
        self.input_file_path = input_file_path
        self.available_amount_records_to_read = len(self.get_unique_record_objs())

    # function to get unique recording objects by comparing existing records and records from the new file
    def get_unique_record_objs(self) -> list:
        list_of_existed_objs = FileReader.parse_list_of_records_to_objects(self.get_records_from_file())
        list_of_new_objs = FileReader.parse_list_of_records_to_objects(self.get_records_from_file(self.input_file_path))
        list_of_unique_objs = []
        for new_record in list_of_new_objs:
            flag = False
            for old_record in list_of_existed_objs:
                if Record.is_equal(old_record, new_record):
                    flag = True
                    break
            if not flag:
                list_of_unique_objs.append(new_record)
        return list_of_unique_objs  # return created list of unique recordings objs

    # function to read records from file
    @staticmethod
    def get_records_from_file(file_path=file_to_write_path) -> list:
        filtered_records_list = []
        if os.path.exists(file_path):   # if file exists
            with open(file_path, 'r', encoding='utf-8') as file_to_read:  # open file to read
                text = file_to_read.read()
            records_list = text.split(separator)
            for record in records_list:
                if record != '' and record != '\n':
                    record = FileReader.text_normalizing(record)
                    filtered_records_list.append(record.lstrip('\n'))
        return filtered_records_list                    # return created list with records from file

    # main function to write new records to the file, call other functions of the class inside
    def write_new_records_to_the_file(self):
        unique_objs = self.get_unique_record_objs()              # get list of record objs without duplicates
        amount_of_records_to_write = self.get_amount_of_records_to_write(self.available_amount_records_to_read)
        if len(unique_objs) != 0 and amount_of_records_to_write != 0:
            for x in range(amount_of_records_to_write):
                unique_objs[x].write_to_file()
            if amount_of_records_to_write == self.available_amount_records_to_read:  # if all records was written to the file
                self.delete_file(self.input_file_path)  # remove file without unique records
        else:
            print('No any unique recording available')

    # function to get amount of records to write to file from the console
    @staticmethod
    def get_amount_of_records_to_write(available_amount_of_records) -> int:
        while True:
            try:
                # get value from the console with providing max amount of records to write
                amount_of_records = input("Please define amount of records to write, available amount is " +
                                          str(available_amount_of_records) + " (press Enter for default value): ")
                if len(amount_of_records) == 0:
                    amount_of_records = available_amount_of_records  # put max value of records to variable
                if int(amount_of_records) > available_amount_of_records:  #
                    print("Entered amount is bigger than available, please try again: ")
                else:
                    break
            except ValueError:  # except handler
                print('Entered amount of records is not correct, please try again')
        return int(amount_of_records)  # return entered amount as int value

    # function to parse text to object in accordance with data types
    @staticmethod
    def parse_list_of_records_to_objects(list_of_records):
        list_of_object_records = []
        for record in list_of_records:
            lines = record.split('\n')
            if not len(lines) <= 2:
                if str(lines[0]).find('News') != -1:
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, lines[1]) and re.match(pattern_city_timestamp, lines[2]):
                        list_of_object_records.append(News(lines[1], lines[2]))
                elif str(lines[0]).find('Private ad') != -1:
                    # if text in record are validated by regular expressions
                    if re.match(pattern_text, lines[1]) and re.match(pattern_ad_exp_date, lines[2]):
                        expiration_date = datetime.strptime(lines[2][14:24], '%Y-%m-%d').date()
                        list_of_object_records.append(PrivateAd(lines[1], expiration_date))
                elif str(lines[0]).find('Joke') != -1:
                    if re.match(pattern_text, lines[1]) and re.match(pattern_text, lines[2]):
                        joke = Joke(lines[1], lines[2])
                        list_of_object_records.append(joke)
        return list_of_object_records

    # function to get file path from the console
    @staticmethod
    def get_file_path(extension: str):
        while True:  # infinite loop until correct path entered
            try:
                file_path = input("Please define path to the file (press Enter for default value): ")
                if len(file_path) == 0:  # if nothing was entered
                    file_path = default_file_to_read_news  # put default value to the variable
                if not file_path.endswith(extension) or len(file_path) < (
                        len(extension) + 1):  # validation of value entered
                    print('File should have file name and ' + extension + ' extension, please try again')
                else:
                    break  # break the loop
            except ValueError:  # exception handler
                print('Entered file path is not correct, please try again')
        return file_path  # return file path as string value

    # function to remove the file
    @staticmethod
    def delete_file(file_path: str):
        try:
            if os.path.isfile(file_path):       # if file by path exists
                os.remove(file_path)            # remove file
                print('File removed successfully due to no unique records available')
            else:
                print('File was not removed, incorrect file path')
        except FileExistsError:         # if not successfully - print exception
            print('Error occurs during file removing')

    # function to normalize string from previous home task
    @staticmethod
    def text_normalizing(string_to_normalize: str) -> str:
        string_to_normalize = string_to_normalize.lower().capitalize()
        flag_to_change_case = False
        for x in range(len(string_to_normalize) - 2):
            if flag_to_change_case and string_to_normalize[x].isalpha():
                # changing case of found char
                string_to_normalize = string_to_normalize[0:x] + string_to_normalize[x].swapcase() + \
                                      string_to_normalize[x + 1: len(string_to_normalize)]
                flag_to_change_case = False
            if string_to_normalize[x] in ['\n', '\t', '!', '?'] or \
                    (string_to_normalize[x] == '.' and not string_to_normalize[x + 1].isalpha()):
                flag_to_change_case = True
        return string_to_normalize
