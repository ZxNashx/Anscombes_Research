import numpy as np

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

# Example usage
vector_example = np.array([1, 2, 3, 4, 5])
print("Mean:", calculate_mean(vector_example))
print("Variance:", calculate_variance(vector_example))
print("Standard Deviation:", calculate_std_deviation(vector_example))
