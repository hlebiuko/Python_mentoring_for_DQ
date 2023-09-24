import sqlite3
import re
from hw_05_09.config import DEFAULT_DB_FILE
from datetime import datetime


class SQLManager:
    params_list_news = ['news_text TEXT', 'news_city TEXT', 'news_timestamp TEXT']
    params_list_private_ad = ['ad_text TEXT', 'actual_until TEXT']
    params_list_joke = ['joke_text TEXT', 'joke_author TEXT']

    def __init__(self):
        self.connection = sqlite3.connect(DEFAULT_DB_FILE)
        self.cursor = self.connection.cursor()
        self.params_list = []

    def create_table_if_not_exist(self, table_name: str, params_list: list):
        params = '(id integer not null primary key autoincrement, ' + ', '.join(params_list) + ')'
        create_table_text = "create table if not exists " + table_name + params
        self.cursor.execute(create_table_text)
        self.connection.commit()

    def write_obj_to_db(self, record_obj):
        dict_of_params = list(record_obj.__dict__.items())
        table_name = str(dict_of_params[0][1]).strip('-')
        record_text = str(dict_of_params[1][1])
        secondary_text = str(dict_of_params[2][1])
        list_of_values = [record_text]

        if table_name == 'News ':
            self.create_table_if_not_exist(table_name, self.params_list_news)
            list_of_values.extend(SQLManager.parse_news_second_text(secondary_text))
            self.params_list = SQLManager.params_list_news
        elif table_name == 'Private ad ':
            table_name = 'Private_ad '
            self.create_table_if_not_exist(table_name, self.params_list_private_ad)
            list_of_values.extend(SQLManager.parse_private_ad_second_text(secondary_text))
            self.params_list = self.params_list_private_ad
        elif table_name == 'Joke of the day ':
            table_name = 'Joke '
            self.create_table_if_not_exist(table_name, self.params_list_joke)
            list_of_values.extend([secondary_text])
            self.params_list = self.params_list_joke
        else:
            print('Incorrect table name occurs while writing to the DB')

        if self.is_record_unique(record_obj):
            self.insert_for_table(table_name, self.params_list, list_of_values)

    def insert_for_table(self, table_name: str, params_list: list, values_list: list):
        params = '(' + ', '.join([item.split(' ')[0] for item in params_list]) + ')'
        values = '(\"' + '\", \"'.join(values_list) + '\")'
        insert_string = "insert into main." + table_name + params + ' values ' + values
        self.cursor.execute(insert_string)
        self.connection.commit()

    def select_all_record_from_db(self, table_name) -> list:
        list_of_object_from_db = []
        self.cursor.execute('select * from main.' + table_name + ';')
        records = self.cursor.fetchall()
        for record in records:
            if table_name == 'News ':
                from hw_05_09.DataTypes.news import News
                list_of_object_from_db.append(News(record[1], record[2] + ", " + record[3]))
            elif table_name == 'Private_ad ':
                from hw_05_09.DataTypes.privateAd import PrivateAd
                exp_date = datetime.strptime(str(record[2]), '%Y-%m-%d').date()
                list_of_object_from_db.append(PrivateAd(record[1], exp_date))
            elif table_name == 'Joke ':
                from hw_05_09.DataTypes.joke import Joke
                list_of_object_from_db.append(Joke(record[1], record[2]))
        return list_of_object_from_db

    def is_record_unique(self, obj_to_check) -> bool:
        list_of_existed_in_db_objs = []
        if 'News' in obj_to_check.title:
            list_of_existed_in_db_objs = self.select_all_record_from_db('News ')
        elif 'Private ad' in obj_to_check.title:
            list_of_existed_in_db_objs = self.select_all_record_from_db('Private_ad ')
        elif 'Joke' in obj_to_check.title:
            list_of_existed_in_db_objs = self.select_all_record_from_db('Joke ')

        for item in list_of_existed_in_db_objs:
            from hw_05_09.DataTypes.record import Record
            if Record.is_equal(item, obj_to_check):
                return False
        return True

    @staticmethod
    def parse_news_second_text(record_text: str):
        try:
            timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"
            match = re.search(timestamp_pattern, record_text)
            if match:
                return [record_text[:match.start() - 2].strip(), match.group(0)]
        except ValueError as error:
            print(error, " occurs during parsing news second text to city and timestamp")

    @staticmethod
    def parse_private_ad_second_text(record_text: str):
        match = re.search(r'\d{4}-\d{2}-\d{2}', record_text)
        return [match.group(0)]
