# Class for handling date and time management:


from datetime import datetime

class RegistrationDateTime:

    @staticmethod
    def get_registration_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
