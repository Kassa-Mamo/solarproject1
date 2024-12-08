import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_data.csv')  # Replace with the correct path to your data file

# Calculate summary statistics
print(df.describe())
