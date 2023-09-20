from datetime import datetime
from datetime import timedelta
# from OperationsWithFiles.fileWriter import FileWriter
from DataTypes.news import News
from DataTypes.privateAd import PrivateAd
from DataTypes.joke import Joke
from OperationsWithFiles.fileReader import FileReader


class Menu:

    # Method to get input from the console and return as a string
    @staticmethod
    def get_console_input() -> str:
        menu_input = input("> ")
        return menu_input.lower()

    # Main menu method with select other menus
    @staticmethod
    def main_menu():
        # infinite loop until exit
        while True:
            print("Main menu: \n"
                  "\t1. Generate records\n"
                  "\t2. Read records from file\n"
                  "\t0. Exit\n")
            choice = Menu.get_console_input()
            if choice.find('generate') != -1 or choice == "1":
                Menu.generate_records_menu()
            elif choice.find("read") != -1 or choice == "2":
                Menu.read_from_text_file_menu()
            elif choice.find("exit") != -1 or choice == "0":
                break
            else:
                print("Incorrect input. Try again")

    # function with menu for generating 3 types of records
    @staticmethod
    def generate_records_menu():
        # infinite loop until exit
        while True:
            print("Select data type to generate: \n"  # print menu text 
                  "\t1. News\n"  # to generate news
                  "\t2. Private ad\n"  # to generate ad 
                  "\t3. Joke of the day\n"  # to generate weather forecast
                  "\t0. Back")  # to exit from the loop

            choice = Menu.get_console_input()  # get input from the console

            if choice.find("news") != -1 or choice == "1":
                # Menu.news_record_generation()
                News.create_news_record()
            elif choice.find("ad") != -1 or choice.find("private") != -1 or choice == "2":
                PrivateAd.create_private_ad_record()
            elif choice.find("joke") != -1 or choice == "3":
                Joke.create_joke_record()
            elif choice.find("exit") != -1 or choice == "0":
                break
            else:
                print("Incorrect input, try again")

    # menu function to define input source for file to read
    @staticmethod
    def read_from_text_file_menu():
        while True:     # loop until exit
            print("Read from the default file or select another file?:\n"
                  "\t1. Default file\n"
                  "\t2. Personal file\n"
                  "\t0. Back")
            choice = Menu.get_console_input()
            if choice.find("default") != -1 or choice == "1":
                file_to_read_default = FileReader()
                file_to_read_default.write_new_records_to_the_file()
            elif choice.find("personal") != -1 or choice == "2":
                file_to_read_personal = FileReader(FileReader.get_file_path('.txt'))
                file_to_read_personal.write_new_records_to_the_file()
            elif choice.find("back") != -1 or choice == "0":
                break                                                      # go to previous menu
            else:                                                          # if input was not recognized - try again
                print("Incorrect input. Try again to type menu number (1/2/0) or type \'default\', "
                      "\'personal\' or \'back\'")


