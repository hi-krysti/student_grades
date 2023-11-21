import pandas as pd
import numpy as np
import statistics


grades_df = pd.read_csv('student-data.csv')
# print(grades_df)

print('\nQuestion 1.1: Calculate mean for each individual subject')
math_mean = np.mean(grades_df['Math'])
science_mean = np.mean(grades_df['Science'])
reading_mean = np.mean(grades_df['Reading'])
history_mean = np.mean(grades_df['History'])

print(f'Math mean: {math_mean}')
print(f'Science mean: {science_mean}')
print(f'Reading mean: {reading_mean}')
print(f'History mean: {history_mean}')


print('\nQuestion 1.2: Find the median grade in Math for all students')
math_median = np.median(grades_df['Math'])
print(f'Median math score: {math_median}')


print('\nQuestion 1.3: Calculate the mode for History')
history_mode = statistics.mode(grades_df['History'])
print(f'History mode: {history_mode}')


print('\nQuestion 2: Calculate correlation between the different subjects')
# corr = grades_df.corr()
# print(corr)

correlation_matrix = np.corrcoef(grades_df['Math'], grades_df['Science'])
correlation = correlation_matrix[0, 1]

print(f"Science and Match have the strongest correlation. \nCorrelation: {correlation}")


print('\nQuestion 3: Write a Python function named desc_stats() that takes a list of numbers and prints the following statistical calculations:')


def desc_stats(x):
    mean = np.mean(x)
    median = np.median(x)
    mode = statistics.mode(x)
    minimum = np.min(x)
    maximum = np.max(x)
    range_value = np.ptp(x)
    variance = np.var(x)
    std_dev = np.std(x)
    return f'Mean: {mean} \nMedian: {median} \nMode: {mode} \nMinimum: {minimum} \nMaximum: {maximum} \nRange: {range_value} \nVariance: {variance} \nStandard Deviation: {std_dev}'


exam_grades = [24, 5, 15, 60, 54, 82, 99, 80, 70, 98, 93, 60, 33, 22, 65, 61, 51, 58, 83, 86, 42, 67, 60]
print(desc_stats(exam_grades))
