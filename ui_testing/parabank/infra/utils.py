import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    # random_string = ''.join(random.choice(characters) for _ in range(length))
    random_string = ''
    for i in range(length):
        random_string += random.choice(characters)
    print(random_string)

    return random_string
