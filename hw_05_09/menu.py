from datetime import datetime
from datetime import timedelta
from OperationsWithFiles.fileWriter import FileWriter
from DataTypes.news import News
from DataTypes.privateAd import PrivateAd
from DataTypes.joke import Joke


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
                  # "\tTBD\n"
                  "\t0. Exit\n")
            choice = Menu.get_console_input()
            if choice.find('generate') != -1 or choice == "1":
                # call menu for generating records
                Menu.generate_records_menu()
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
                Menu.news_record_generation()
            elif choice.find("ad") != -1 or choice.find("private") != -1 or choice == "2":
                Menu.private_ad_record_generation()
            elif choice.find("joke") != -1 or choice == "3":
                Menu.joke_generation()
            elif choice.find("exit") != -1 or choice == "0":
                break
            else:
                print("Incorrect input, try again")

    # function to generate news record
    @staticmethod
    def news_record_generation():
        news_body = input("What's happen? \n")
        # if nothing entered - fulfill with default value
        if len(news_body) == 0:
            # print default text for news feed
            news_body = "Something happen"
        news_city_timestamp = input("Where something happen? \n")
        # if nothing entered - fulfill with default value
        if len(news_city_timestamp) == 0:
            news_city_timestamp = "Somewhere"  # put default value as a city
        # adding timestamp string city timestamp
        news_city_timestamp += datetime.now().strftime(", %Y-%m-%d %H:%M")
        # initialization of the News object with provided text, city and timestamp
        news = News(news_body, news_city_timestamp)
        # calling the method of the Record class to write object to the file
        news.write_to_file()

    # function to generate private ad record
    @staticmethod
    def private_ad_record_generation():
        private_ad_text = input('Enter advertisement text: \n')
        # if nothing entered - fulfill with default value
        if len(private_ad_text) == 0:
            private_ad_text = 'Garaz for sale!'
        # infinite loop until enter of the correct date
        while True:
            private_ad_exp_date = input('Enter the expiration date of the advertisement ( in yyyy-mm-dd format): \n')
            # if nothing entered - fulfill with default value
            if len(private_ad_exp_date) == 0:
                private_ad_exp_date = datetime.now().date() + timedelta(days=7)
                break
            else:
                try:
                    private_ad_exp_date = datetime.strptime(str(private_ad_exp_date), '%Y-%m-%d').date()
                    if private_ad_exp_date < datetime.now().date():
                        print("Entered expiration date is less than current one. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Entered expiration date has wrong format. Please, try again.")
        private_ad_obj = PrivateAd(private_ad_text, private_ad_exp_date)
        # calling the method of the Record class to write object to the file
        private_ad_obj.write_to_file()

    # function to generate the joke record
    @staticmethod
    def joke_generation():
        joke_text = input('Enter joke text: \n')
        # if nothing entered - fulfill with default value
        if len(joke_text) == 0:
            joke_text = 'Kolobok povesilsya'
        joke_author = input('Enter joke author: \n')
        # if nothing entered - fulfill with default value
        if len(joke_author) == 0:
            joke_author = 'Unknown'
        joke_obj = Joke(joke_text, joke_author)
        # calling the method of the Record class to write object to the file
        joke_obj.write_to_file()
