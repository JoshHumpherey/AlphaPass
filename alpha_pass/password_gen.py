from hashlib import sha256
special_characters = ['!','@','#','$','%','^','&','*','(',')','?']
amount_of_special_characters = len(special_characters)
import re

def generate_password(master_password, service_name):
    long_password = sha256((master_password + service_name).encode('utf-8')).hexdigest()
    valid_password = trim_password(long_password,15)
    better_password = insert_special_character(valid_password)
    best_password = capitalize_first_letter_of_string(better_password)
    return best_password

def trim_password(long_password, length):
    return long_password[:length]

def insert_special_character(less_secure_password):
    number_array = re.findall('\d+', less_secure_password)
    amount_of_numbers = len(number_array)
    if amount_of_numbers > amount_of_special_characters:
        new_password = less_secure_password + special_characters[amount_of_special_characters-1]
    else:
        new_password = less_secure_password + special_characters[amount_of_numbers]

    return new_password

def capitalize_first_letter_of_string(lowercase_password):
    return lowercase_password.title()
