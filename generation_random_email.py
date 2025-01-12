# Генерация рандомного почтового ящика

import random
import string

def generate_random_email(domain):
    username = "nikita_kopyev_17"

    digits = ''.join(random.choice(string.digits) for _ in range(3))

    email = f"{username}{digits}@{domain}"
    return email

domain = "yandex.ru"

random_email = generate_random_email(domain)