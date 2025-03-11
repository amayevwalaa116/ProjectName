
import random

def generate_random_python_code(n):
    """
    Generate a random Python code with n lines.
    """
    code = []
    for i in range(n):
        code.append(f'print("Hello, World!")')
    return '\n'.join(code)