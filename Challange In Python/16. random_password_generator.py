import random
import string


def generate_password(passlen):
    characters = list(string.ascii_letters + string.digits + "!@#$%&*?:;")
    int(passlen)
    random.shuffle(characters)
    password = []
    for x in range(passlen):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    return password


print(generate_password(19))
