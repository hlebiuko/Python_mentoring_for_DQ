from hw_05_09.config import title_length, separator
from hw_05_09.OperationsWithFiles.fileWriter import FileWriter


class Record:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    @staticmethod
    def generate_header(header_name):
        return str(header_name + '-' * (title_length - len(header_name)))

    def convert_to_string(self):
        record_in_string = ''
        for key, value in self.__dict__.items():
            record_in_string += value + '\n'
        record_in_string += separator
        return record_in_string

    def write_to_file(self):
        FileWriter.write_string_to_the_file(self.convert_to_string())

