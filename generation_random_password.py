# Генерация рандомного пароля

import random
import string

def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password(6)