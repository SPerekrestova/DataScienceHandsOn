import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(filepath):
    # Data Loading and Exploration

    # Use Pandas to read the CSV file.
    try:
        df = pd.read_csv('../resources/data.csv')
    except FileNotFoundError as e:
        print("Error: File not found.")
        exit()

    # Display the first 10 rows of the dataset.
    print(df.head(10).to_markdown(tablefmt="grid"))
    # Check for any missing values.
    print(df.isnull().sum())

    # Data Manipulation
    df = df.assign(AverageScore=df.loc[:, ["MathScore", "ReadingScore", "WritingScore"]].mean(axis=1))
    df = df.sort_values(by='AverageScore', ascending=False)
    return df

def calculate_statistics(df):
    # Find mean, median and mode
    for score in ['MathScore', 'ReadingScore', 'WritingScore']:
        print(f"Mean for {score} is {df[score].mean()}")
        print(f"Median for {score} is {df[score].median()}")
        print(f"Mode for {score} is {df[score].mode().values}")

    print("Overall mean", np.mean(df['AverageScore']))
    print("Standard deviation", np.std(df['AverageScore']))
    pass


def perform_t_test(df):
    #  T-test
    df_1 = df[df.TestPrepCourse == 'Completed']
    df_2 = df[~df.isin(df_1)].dropna(how='all')

    print(stats.ttest_ind(df_1['AverageScore'].values, df_2['AverageScore'].values))
    pass

def visualize(df):
    # Data Visualization
    # Boxplot showing the distribution of MathScore for males and females.
    sns.boxplot(data=df, x="MathScore", y="Gender")
    sns.despine()
    plt.show()

    # Scatter plot of ReadingScore vs. WritingScore colored by TestPrepCourse
    sns.lmplot(x="ReadingScore", y="WritingScore", col="TestPrepCourse", data=df)
    sns.despine()
    plt.show()
    pass