import random
def get_random_number(minimum=1, maximum=6):
    """
    Returns a random number between minimum and maximum (inclusive).
    """
    return random.randint(minimum, maximum)

def get_random_string(length=8):
    """
    Returns a random string of length 8.
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for i in range(length))
