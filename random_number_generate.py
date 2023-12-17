import random

def random_number_generate(count=5):
    unique_numbers = set()

    while len(unique_numbers) < count:
        unique_numbers.add(random.randint(1, 7))

    return list(unique_numbers)



