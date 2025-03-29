def calculate_square_root(number):
    if number >= 0:
        square_root = number ** 0.5
    else:
        square_root = None
    return square_root

calculate_square_root(-4)  # Output: -2.0
