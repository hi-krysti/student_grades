import pandas as pd
import numpy as np
import statistics


grades_df = pd.read_csv('student-data.csv')
# print(grades_df)

print('\nQuestion 1.1: Calculate mean for each individual subject')
print(grades_df.mean(numeric_only=True))


print('\nQuestion 1.2: Find the median grade in Math for all students')
print(grades_df['Math'].median())



print('\nQuestion 1.3: Calculate the mode for History')
print(grades_df['History'].mode())


print('\nQuestion 2: Calculate correlation between the different subjects')
grades_df = grades_df.drop(0)
print(grades_df.corr(numeric_only=True))

# correlation_matrix = np.corrcoef(grades_df['Math'], grades_df['Science'])
# correlation = correlation_matrix[0, 1]

print("\nHistory and Math have the strongest inverse correlation. No other subjects have significant correlation.")


print('\nQuestion 3: Write a Python function named desc_stats() that takes a list of numbers and prints the following statistical calculations:')


def desc_stats(nums):
    print(f'Mean: {np.mean(nums)}')
    print(f'Median: {np.median(nums)}')
    print(f'Mode: {statistics.mode(nums)}')
    print(f'Minimum: {np.min(nums)}')
    print(f'Maximum: {np.max(nums)}')
    print(f'Range: {np.ptp(nums)}')
    print(f'Variance: {np.var(nums)}')
    print(f'Standard Deviation: {np.std(nums)}')


exam_grades = [24, 5, 15, 60, 54, 82, 99, 80, 70, 98, 93, 60, 33, 22, 65, 61, 51, 58, 83, 86, 42, 67, 60]
print(desc_stats(exam_grades))

