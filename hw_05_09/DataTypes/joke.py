from hw_05_09.DataTypes.record import Record


class Joke(Record):
    def __init__(self, text, tech_text):
        self.title = Record.generate_header('Joke of the day ')
        super().__init__(self.title, text)
        self.tech_text = tech_text

    # function to generate the joke record
    @staticmethod
    def create_joke_record():
        joke_text = input('Enter joke text: \n')
        # if nothing entered - fulfill with default value
        if len(joke_text) == 0:
            joke_text = 'Kolobok povesilsya'
        joke_author = input('Enter joke author: \n')
        # if nothing entered - fulfill with default value
        if len(joke_author) == 0:
            joke_author = 'Unknown'
        joke_obj = Joke(joke_text, joke_author)
        joke_obj.write_to_file()
