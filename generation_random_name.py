# Генерация рандомного имени пользователя

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

length = random.randint(1, 10)

random_value = ''.join(random.choice(characters) for _ in range(length))