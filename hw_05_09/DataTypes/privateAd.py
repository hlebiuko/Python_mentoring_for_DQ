from hw_05_09.DataTypes.record import Record
from datetime import datetime
from datetime import timedelta


class PrivateAd(Record):
    def __init__(self, text, tech_text):
        self.title = Record.generate_header('Private ad ')
        super().__init__(self.title, text)
        self.tech_text = tech_text
        # generating expiration date text
        self.tech_text = 'Actual until: ' + str(tech_text) + ', ' + str((tech_text - datetime.now().date()).days) \
                         + ' days left'

    # function to generate private ad record
    @staticmethod
    def create_private_ad_record():
        private_ad_text = input('Enter advertisement text: \n')
        # if nothing entered - fulfill with default value
        if len(private_ad_text) == 0:
            private_ad_text = 'Garaz for sale!'
        # infinite loop until enter of the correct date
        while True:
            private_ad_exp_date = input(
                'Enter the expiration date of the advertisement ( in yyyy-mm-dd format): \n')
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
