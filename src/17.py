import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Assuming data is in a Pandas DataFrame named df
df = pd.DataFrame(data)

# Add a column to predict the target variable (using the last column)
df['predicted'] = df.iloc[:, -1]

# Create and train the linear regression model
model = LinearRegression()
model.fit(df.drop(columns=['predicted']), df.iloc[:, :-1])
