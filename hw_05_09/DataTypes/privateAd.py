from hw_05_09.DataTypes.record import Record
from datetime import datetime


class PrivateAd(Record):
    def __init__(self, text, tech_text):
        self.title = Record.generate_header('Private ad ')
        super().__init__(self.title, text)
        self.tech_text = tech_text
        # generating expiration date text
        self.tech_text = 'Actual until: ' + str(tech_text) + ', ' + str((tech_text - datetime.now().date()).days) \
                         + ' days left'
