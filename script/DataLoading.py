import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

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

print("Overall mean", np.mean(df['AverageScore']))
print("Standard deviation", np.std(df['AverageScore']))

#  T-test
df_1 = df[df.TestPrepCourse == 'Completed']
df_2 = df[~df.isin(df_1)].dropna(how = 'all')

print(stats.ttest_ind(df_1['AverageScore'].values, df_2['AverageScore'].values))

# Data Visualization
# Boxplot showing the distribution of MathScore for males and females.
sns.boxplot(data=df, x="MathScore", y="Gender")
sns.despine()
plt.show()

# Scatter plot of ReadingScore vs. WritingScore colored by TestPrepCourse
sns.lmplot(x="ReadingScore", y="WritingScore", col="TestPrepCourse", data=df)
sns.despine()
plt.show()

# Advanced Analysis

# Data Export

df.to_csv('../resources/data_new.csv', index=False)