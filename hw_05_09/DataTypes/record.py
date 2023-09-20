from hw_05_09.config import TITLE_LENGTH, SEPARATOR
from hw_05_09.OperationsWithFiles.fileWriter import FileWriter
# from hw_05_09.CSVFiles.CSVOperations import CSVOperations


class Record:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    @staticmethod
    def generate_header(header_name):
        return str(header_name + '-' * (TITLE_LENGTH - len(header_name)))

    def convert_to_string(self):
        record_in_string = ''
        for key, value in self.__dict__.items():
            record_in_string += value + '\n'
        record_in_string += SEPARATOR
        return record_in_string

    def write_to_file(self):
        FileWriter.write_string_to_the_file(self.convert_to_string())

    # function to compare 2 provided objects by class and attributes
    @staticmethod
    def is_equal(object_1, object_2):
        if object_1.__class__ != object_2.__class__:    # if objects doesn't have the same class
            return False    # they are not equal
        # if dict of attributes and it's values are equal for 2 objects
        if object_1.__dict__.items() == object_2.__dict__.items():
            return True     # return true
        else:           # if not
            return False    # return false
