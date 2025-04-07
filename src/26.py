import numpy as np

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numerical values.
        
    Returns:
        float: The average of the given numbers.
    """
    if not numbers:
        return 0.0
    else:
        total = np.sum(numbers)
        average = total / len(numbers)
        return average

# Example usage
numbers = [1, 2, 3, 4, 5]
print(calculate_average(numbers))
