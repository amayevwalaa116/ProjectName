import random

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_list = []
    for i in range(length):
        result_list.append(random.choice(letters))
    return ''.join(result_list)