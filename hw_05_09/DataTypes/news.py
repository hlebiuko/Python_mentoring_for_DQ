from hw_05_09.DataTypes.record import Record


class News(Record):

    def __init__(self, text, tech_text):
        self.title = Record.generate_header('News ')
        print("hello kurwa")
        super().__init__(self.title, text)
        self.tech_text = tech_text
