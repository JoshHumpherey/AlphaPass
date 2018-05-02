from hashlib import sha256

def GeneratePassword(masterPassword, serviceName):
    securePassword = sha256((masterPassword+serviceName).encode('utf-8')).hexdigest()
    print(securePassword)
    return securePassword
