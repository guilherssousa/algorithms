import random


def generate_random_array(length):
    arr = []

    for _ in range(length):
        arr.append(random.randint(0, length))

    return arr
