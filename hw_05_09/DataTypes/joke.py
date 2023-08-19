from hw_05_09.DataTypes.record import Record


class Joke(Record):
    def __init__(self, text, tech_text):
        self.title = Record.generate_header('Joke of the day ')
        super().__init__(self.title, text)
        self.tech_text = tech_text
