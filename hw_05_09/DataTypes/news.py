from hw_05_09.DataTypes.record import Record
from datetime import datetime


class News(Record):

    def __init__(self, text, tech_text):
        self.title = Record.generate_header('News ')
        super().__init__(self.title, text)
        self.tech_text = tech_text

    # function to generate news record

    @staticmethod
    def create_news_record():
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
