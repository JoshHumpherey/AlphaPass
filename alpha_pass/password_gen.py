from hashlib import sha256


def generate_password(master_password, service_name):
    long_password = sha256((master_password + service_name).encode('utf-8')).hexdigest()
    valid_password = trim_password(long_password,16)
    return valid_password

def trim_password(long_password, length):
    return long_password[:length]
