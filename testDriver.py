import numpy as np
import sympy as sp

def calculate_mean(vector):
    # Calculate the mean (average) of a vector
    # ybar (or xbar) is the mean of the vector y (or x)
    return np.dot(vector, np.ones(len(vector))) / len(vector)

def calculate_variance(vector):
    # Calculate the variance of a vector
    mean = calculate_mean(vector)  # Compute the mean of the vector
    deviations = vector - mean    # Calculate deviations from the mean (xi - xbar or yi - ybar)
    variance = np.dot(deviations, deviations) / (len(vector) - 1)  # Variance calculation using dot product
    return variance

def calculate_std_deviation(vector):
    # Calculate the standard deviation of a vector
    variance = calculate_variance(vector)  # First calculate variance
    std_deviation = np.sqrt(variance)      # Standard deviation is the square root of variance
    return std_deviation

# Define the x points
x_points = np.array(range(4, 15))  # This will create an array with integers from 4 to 14

print("Mean:", calculate_mean(x_points))
print("Variance:", calculate_variance(x_points))
print("Standard Deviation:", calculate_std_deviation(x_points))
print("Example Vector Used: ", x_points)


# Initialize y values as 'None' or 'np.nan'
y_values = np.full(x_points.shape, np.nan)  # This creates an array of the same shape as x_points, but filled with np.nan

print("X Points:", x_points)
print("Y Values:", y_values)
