import numpy as np
import sympy as sp
import re
import math
def print_matrix(matrix):
    print("(",end="")
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    max_widths = [max([len(str(matrix[i][j])) for i in range(matrix.shape[0])]) for j in range(matrix.shape[1])]
    end_str = ""
    for row in matrix:
        end_str += " ".join(f"{str(element).rjust(max_widths[i])}" for i, element in enumerate(row)) + "\n"
    print(end_str[0:-1] + ")")
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
def solve_quadratic(equation):
    # Regular expression to extract coefficients
    coeffs = re.findall(r'([+-]?\d*\.?\d*)x\^2|([+-]?\d*\.?\d*)x|([+-]?\d+)', equation)
    # Function to convert coefficient to float
    def to_float(coef):
        if coef in ["+", "-"]:  # Handle cases like '+' or '-'
            return float(coef + "1")
        return float(coef) if coef else 0
    # Extract and convert coefficients
    a, b, c = [to_float(coef) for group in coeffs for coef in group if coef]
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    # Compute solutions
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    else:
        # Return complex solutions if the discriminant is negative
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)




