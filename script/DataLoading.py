import pandas as pd
import numpy as np

# Data Loading and Exploration

# Use Pandas to read the CSV file.
df = pd.read_csv('../resources/data.csv')
# Display the first 10 rows of the dataset.
print(df.head(10).to_markdown(tablefmt="grid"))
# Check for any missing values.
print(df.isnull())

# Find mean
print("Mean for MathScore is ", df['MathScore'].mean())
print("Mean for ReadingScore is ", df['ReadingScore'].mean())
print("Mean for WritingScore is ", df['WritingScore'].mean())

# Find median
print("Median for MathScore is ", df['MathScore'].median())
print("Median for ReadingScore is ", df['ReadingScore'].median())
print("Median for WritingScore is ", df['WritingScore'].median())

# Find mode
print("Mode for MathScore is ", df['MathScore'].mode())
print("Mode for ReadingScore is ", df['ReadingScore'].mode())
print("Mode for WritingScore is ", df['WritingScore'].mode())

# Data Manipulation
df = df.assign(AverageScore=df.loc[:, ["MathScore", "ReadingScore", "WritingScore"]].mean(axis=1))
df = df.sort_values(by='AverageScore', ascending=False)

# Statistical Analysis

print("Overall mean")
