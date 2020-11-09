from RegisteredUser import RegisteredUser
import Helpers

#dataDict =  {"email": email, "password": password}

class NoUserWithThisName(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()


def is_email_and_passw_in_data():
    if email in dataDict.values() and password in dataDict.values():
        print("OK")
    else:
        raise NoUserWithThisName()


try:
   is_email_and_passw_in_data()
except Exception:
   print("There is no such email and password in database")
