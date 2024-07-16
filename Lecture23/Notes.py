"""Advanced Statistical Measures and Distributions

Descriptive Statistics - Mean

Definition:
The mean represents the average value of a dataset, calculated by summing all values and dividing by the count of values.

Use Case:
In social sciences, the mean is employed to summarize the average value of a dataset, such as the average test score or average household income."""


import pandas as pd

# Sample data
data = {
    'Test_Score': [80, 75, 90, 85, 95, 70, 85, 80, 92, 88],
    'Income': [50000, 120000, 70000, 60000, 80000, 55000, 85000, 90000, 150000, 62000]
}
df = pd.DataFrame(data)

# Mean calculation
mean_score = df['Test_Score'].mean()
mean_income = df['Income'].mean()

print("Mean Test Score:", mean_score)
print("Mean Income:", mean_income)

"""Descriptive Statistics - Median
Definition:
The median is the middle value in a dataset, separating the higher and lower halves of the data.

Use Case:
In healthcare, the median is used to understand the central tendency of patient recovery times, especially when there are extreme values."""

# Median calculation
median_score = df['Test_Score'].median()
median_income = df['Income'].median()

print("Median Test Score:", median_score)
print("Median Income:", median_income)
"""Descriptive Statistics - Mode
Definition:
The mode is the most frequently occurring value in a dataset.

Use Case:
In retail, the mode identifies the most popular product sold or the most common transaction amount."""

# Mode calculation
mode_score = df['Test_Score'].mode()[0]
mode_income = df['Income'].mode()[0]

print("Mode Test Score:", mode_score)
print("Mode Income:", mode_income)

"""Descriptive Statistics - Standard Deviation
Definition:
The standard deviation measures the dispersion of values from the mean, indicating data variability.

Use Case:
In engineering, standard deviation assesses the consistency of manufacturing processes or product dimensions."""

# Standard deviation calculation
std_score = df['Test_Score'].std()
std_income = df['Income'].std()

print("Standard Deviation Test Score:", std_score)
print("Standard Deviation Income:", std_income)

"""Descriptive Statistics - Variance
Definition:
Variance measures the spread of values around the mean, indicating data distribution.

Use Case:
In environmental studies, variance helps assess annual rainfall variability or temperature fluctuations."""

# Variance calculation
var_score = df['Test_Score'].var()
var_income = df['Income'].var()

print("Variance Test Score:", var_score)
print("Variance Income:", var_income)

"""Probability Distributions - Normal Distribution
Definition:
The normal distribution is a continuous probability distribution with a symmetric bell-shaped curve around the mean.

Use Case:
In economics, the normal distribution models stock market returns or GDP growth rates."""

import numpy as np
import matplotlib.pyplot as plt

# Normal distribution example
mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

# Plotting the histogram
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.title('Normal Distribution')
plt.show()

"""Probability Distributions - Binomial Distribution
Definition:
The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of trials.

Use Case:
In manufacturing, the binomial distribution predicts defective items in production batches."""

# Binomial distribution example
n, p = 10, 0.5
binomial = np.random.binomial(n, p, 1000)

# Plotting the histogram
plt.hist(binomial, bins=10, density=True, alpha=0.6, color='b')
plt.title('Binomial Distribution')
plt.show()

"""Quartiles
Definition:
Quartiles divide a dataset into four equal parts, useful for analyzing data spread and identifying outliers.

Use Case:
In education, quartiles help analyze student performance across different subjects."""

import numpy as np

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate quartiles
Q1 = np.percentile(data, 25)
Q2 = np.median(data)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

print(f"Q1: {Q1}")
print(f"Q2 (Median): {Q2}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")

"""Z-Scores
Definition:
A Z-score measures how many standard deviations an element is from the mean, used to identify outliers and compare different datasets.

Use Case:
In sports analytics, Z-scores compare player performance across different seasons to assess consistency."""

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Calculate Z-scores
z_scores = [(x - mean) / std_dev for x in data]

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print("Z-scores:", z_scores)