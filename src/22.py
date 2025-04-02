def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    Args:
    n: An integer representing the position in the sequence of Fibonacci numbers.
    
    Returns:
    The nth Fibonacci number.
    """
    if n <= 0:
        return "The input should be a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# Example usage:
n = int(input("Enter the position: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
