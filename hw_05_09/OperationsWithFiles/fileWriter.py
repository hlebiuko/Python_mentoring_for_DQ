import os.path
from hw_05_09.config import FILE_TO_WRITE_PATH
from hw_05_09.CSVFiles.CSVOperations import CSVOperations
# from hw_05_09.OperationsWithFiles.fileReader import FileReader


class FileWriter:

    # function to detect does the provided file exist
    @staticmethod
    def write_string_to_the_file(string_to_write: str, file_path=FILE_TO_WRITE_PATH):
        try:
            # check if file exists - open to write
            if os.path.isfile(file_path):
                FileWriter.write_to_new_or_existed_file(file_path, 'a', string_to_write)
            # else - open with creation of the file
            else:
                FileWriter.write_to_new_or_existed_file(file_path, 'w', string_to_write)

            CSVOperations.create_csv_files()

        except BaseException as exception:
            print("Exception occurs during writing file (FileOperations.write_to_file method)", exception)

    # function to write string to the file with provided method
    @staticmethod
    def write_to_new_or_existed_file(file_path: str, method: str, string_to_write: str):
        with open(file_path, method, encoding="utf-8") as file_to_write:
            print(string_to_write, file=file_to_write)





