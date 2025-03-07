def get_random_string(length):
    """Generate a random string of letters and digits.
    
    Parameters:
        length (int): The desired length of the string
    
    Returns:
        str: A random string with the specified length
    """
    import random
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))
