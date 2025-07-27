#names
import re
from operator import truediv


def name_checker(name)
    if re.match(r"^[a-zA-Z]{3,30}$" , name)
        return True
    else:
        print("Error: name is not valid")
        return False

def last_name_checker(last_name):
    if re.match(r"^[a-zA-Z]{3,30}$" , last_name)
        return True
    else:
        print("Error: last name is not valid")
        return False


def address_checker(address):
    if re.match(r"^[a-zA-Z0-9]$" , address)
        return True
    if len(address) < 3:
        print("it's too short")
        return False
    if len(address) > 250:
        print("it's too long")
        return False
    else:
        return False


def email_checker(email):
    if re.match(r"^[a-zA-Z0-9][@gmail.com]{5,65}$" , email)
        return True
    else:
        print("Error: email is not valid")
        return False


def national_code_checker(national_code):
    if re.match(r"^[0-9]{10}$" , national_code)
        return True
    else:
        print("Error: national code is not valid")
        return False


def phone_number_checker(phone_number):
    if re.match(r"^[0-9]{11}$" , phone_number)
        return True
    else:
        print("Error: phone number is not valid")
        return False


