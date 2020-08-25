MIN_LENGTH = 6

password = input("Enter a password no less than {} characters: ".format(MIN_LENGTH))
while len(password) < MIN_LENGTH:
    password = input("Enter a password no less than {} characters: ".format(MIN_LENGTH))
print("*" * len(password))