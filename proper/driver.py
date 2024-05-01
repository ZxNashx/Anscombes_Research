import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from GenerateGraph import GraphBuilder as GB
from math import sin, cos
from scipy.stats import linregress

from functions.quadratic import f, g, h

# Initialize the GraphBuilder
builder = GB()

SHOW_VALUES = False
# Setup the range of x values for plotting
x_values_continuous = np.linspace(0, 100, 100)
x_values_dots = np.arange(builder.start_value, builder.start_value + builder.n)

# Use these functions to generate the matrix and solve for coefficients
matrix_result, active_vars = builder.generate_M_matrix(f, g, h)
print("Matrix Result:", matrix_result)
solution_sets = builder.solve(sum(x_values_dots) / len(x_values_dots))
print("Solution Sets:", solution_sets)

# Define the simple linear function to plot alongside
def linear_function(x):
    return builder.slope * x + builder.intercept

# Compute the values for the linear function
linear_values = [linear_function(x) for x in x_values_continuous]

# Create the plots
colors = ['b', 'r']  # Ensure you have enough colors for the number of solutions
fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # Two subplots side by side

if solution_sets:
    for idx, (ax, solution) in enumerate(zip(axs, solution_sets)):
        # Evaluate and convert to complex numbers properly
        a = complex(sp.N(solution[builder.a]))  # Evaluate and convert
        b = complex(sp.N(solution[builder.b]))
        c = complex(sp.N(solution[builder.c]))

        # Format numbers, handling real and imaginary parts
        label_a = f"{a.real:.2f} + {a.imag:.2f}i"
        label_b = f"{b.real:.2f} + {b.imag:.2f}i"
        label_c = f"{c.real:.2f} + {c.imag:.2f}i"
        print("-------------")
        combined_values_dots = [(f(x) * a.real + g(x) * b.real + h(x) * c.real) for x in x_values_dots]  # Use real parts for calculations
        for x, y in zip(x_values_dots, combined_values_dots):
            print(f"x: {x}, y: {y:.2f}")

        if SHOW_VALUES:
            ax.plot(x_values_dots, combined_values_dots, 'o', label=f'Set {idx+1}: a={label_a}, b={label_b}, c={label_c}', color=colors[idx], markersize=10)
            ax.plot(x_values_continuous, linear_values, label='Linear Function', linestyle='-', color='k')
        else:
            ax.plot(x_values_dots, combined_values_dots, 'o', label="Generated Data", color=colors[idx], markersize=10)
            ax.plot(x_values_continuous, linear_values, label="Best Fit Line", linestyle='-', color='k')

        # Set fixed axis limits
        ax.set_xlim(2, 18)
        ax.set_ylim(2, 14)

        ax.set_title(f'Set {idx+1}')
        ax.set_xlabel('x')
        ax.set_ylabel('Function values')
        ax.legend()
        ax.grid(True)

        # Calculate and display full regression analysis for each set
        slope, intercept, r_value, p_value, std_err = linregress(x_values_dots, combined_values_dots)
        print(f"Set {idx + 1} Regression Line: y = {slope:.2f}x + {intercept:.2f}")
        print(f"Set {idx + 1} Correlation Coefficient: {r_value:.2f}")
        print(f"Set {idx + 1} P-value: {p_value:.4f}")
        print(f"Set {idx + 1} Standard Error: {std_err:.2f}")

plt.show()