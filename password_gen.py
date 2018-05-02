from hashlib import sha256


def generate_password(master_password, service_name):
    secure_password = sha256((master_password + service_name).encode('utf-8')).hexdigest()
    print(secure_password)
    return secure_password
