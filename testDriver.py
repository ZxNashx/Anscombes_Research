import numpy as np

def calculate_mean(vector):
    return np.dot(vector, np.ones(len(vector))) / len(vector)

def calculate_variance(vector):
    mean = calculate_mean(vector)
    deviations = vector - mean
    variance = np.dot(deviations, deviations) / (len(vector) - 1)
    return variance

def calculate_std_deviation(vector):
    variance = calculate_variance(vector)
    std_deviation = np.sqrt(variance)
    return std_deviation

