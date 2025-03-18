import random
def generate_random_code():
    num = 0
    while(num < 16):
        char = chr(random.randint(97, 122))
        print(char)
        num += 1