import numpy as np
from helper import *

# Define the x points
x_points = np.array(range(4, 15))  # This will create an array with integers from 4 to 14

print("STATS TEST")
print("Mean:", calculate_mean(x_points))
print("Variance:", calculate_variance(x_points))
print("Standard Deviation:", calculate_std_deviation(x_points))
print("Example Vector Used: ", x_points)

# Coefficients matrix (A)
A = np.array([[3, 2], [7, -5]])
# Constants vector (B)
B = np.array([16, 14])
solution = np.linalg.solve(A, B)
print("Matrix Solve")
print_matrix(A)
print("= " + str(B) + "\nSolutions:")
print(solution)

print("Equation Solve")
equation = "1x^2 -3x + 2"
solutions = solve_quadratic(equation)
print(equation)
print("Solutions:", solutions)

# DOT product demo
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Dot Product Calculation")
print_matrix(A)
print_matrix(B)
dot_product = np.dot(A, B)
print("Dot Product of A and B:")
print(dot_product)
