import random

def generate_code():
    characters = ['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'E']
    generated_code = ''.join(random.choice(characters) for _ in range(10))
    return generated_code