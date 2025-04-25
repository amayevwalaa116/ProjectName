import pandas as pd

# Example data: students with their scores in different subjects
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [90, 85, 75],
    'Science': [80, 85, 75]
}

df = pd.DataFrame(data)
print(df)
