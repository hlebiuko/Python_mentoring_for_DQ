import json

from hw_05_09.config import DEFAULT_FILE_TO_JSON_FILE


class JSONManager:
    def __init__(self):
        self.file_path = DEFAULT_FILE_TO_JSON_FILE

    def get_json_file_data(self) -> dict:
        try:
            with open(self.file_path, "r", encoding="utf-8") as read_file:
                data = json.load(read_file)
            JSONManager.parse_json_file_data_to_objs_list(data)
            return data
        except FileNotFoundError as error:
            print("Error occurs during open json file (JSONManager): ", error)

    @staticmethod
    def parse_json_file_data_to_objs_list(data: dict) -> list:

        list_of_objects = []  # initialization of the empty list to hold list of objects
        news = data['News'] if type(data['News']) is list else [data['News']]
        private_ad = data['Private ad'] if type(data['Private ad']) is list else [data['Private ad']]
        jokes = data['Joke'] if type(data['Joke']) is list else [data['Joke']]

        list_of_records = []
        # for dict_item in data:

