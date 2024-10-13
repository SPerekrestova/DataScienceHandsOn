Requirements:

1. Data Loading and Exploration:
   - Use Pandas to read the CSV file.
   - Display the first 10 rows of the dataset.
   - Check for any missing values.
   - Provide basic statistics (mean, median, mode) for MathScore, ReadingScore, and WritingScore.
2. Data Manipulation:
   - Add a new column AverageScore that contains the average score of MathScore, ReadingScore, and WritingScore for each student.
   - Sort the dataset based on AverageScore in descending order.
3. Statistical Analysis:
   - Use NumPy to compute the overall mean and standard deviation of the AverageScore.
   - Use SciPy to perform a t-test to determine if there’s a significant difference in AverageScore between students who completed the test preparation course and those who did not.
4. Data Visualization:
   - Use Matplotlib or Seaborn to create a boxplot showing the distribution of MathScore for males and females.
   - Create a scatter plot of ReadingScore vs. WritingScore colored by TestPrepCourse completion status.
5. Advanced Analysis:
   - Use SciPy to perform a linear regression predicting MathScore based on ReadingScore and WritingScore.
   - Report the regression coefficients and the R-squared value.
   - Plot the regression plane (if possible) or provide insights based on the results.
6. Data Export:
   - Save the modified dataset with the new AverageScore column to a new CSV file.
