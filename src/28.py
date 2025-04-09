import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Parameters:
    - length (int): The length of the generated string.
    
    Returns:
    - str: A randomly generated string.
    """
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

random_string = generate_random_string(10)
print(random_string)
