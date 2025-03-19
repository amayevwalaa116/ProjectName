import random

def get_random_code():
    numbers = "23456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*()_+-=[]{}|;':\"<>,./?`~"
    code = ""
    for i in range(8):
        code += random.choice(numbers)
        code += random.choice(letters)
        code += random.choice(special_characters)
    return code