import random

def get_random_number(n):
    return random.randint(0, n)

def get_random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

# Example Usage:
print(get_random_number(10))
print(get_random_string(5))