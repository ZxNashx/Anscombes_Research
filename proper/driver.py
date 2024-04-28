import numpy as np
import matplotlib.pyplot as plt
from GenerateGraph import GraphBuilder as gb
from math import sin, cos

# Initialize the GraphBuilder
builder = gb()

# Define the function behaviors
def f(x):

    if x > 8:
        return x ** 4
    else:
        return x
def g(x):
    return x # + C


def h(x):
    return 0


# Use these functions to generate the matrix and solve for coefficients
print(builder.generate_M_matrix(f, g, h))
solution_sets = builder.solve()
print(solution_sets)

# Setup the range of x values for the linear function
x_values_continuous = np.linspace(builder.start_value,  builder.start_value + builder.n, 100)  # For the linear function, use a continuous range
# Adjusted range for solution set plotting
x_values_dots = np.arange(builder.start_value, builder.start_value + builder.n)

# Define the simple linear function to plot alongside
def linear_function(x):
    return builder.slope * x + builder.intercept

# Compute the values for the linear function
linear_values = [linear_function(x) for x in x_values_continuous]

# Create the plots
plt.figure(figsize=(5, 4))  # Smaller, more concise figure size
colors = ['b', 'r']  # Colors for the two solution sets

for idx, (a, b, c) in enumerate(solution_sets):
    # Compute the combined function values for each coefficient set only at whole values
    combined_values_dots = [(f(x) * a + g(x) * b + h(x) * c) for x in x_values_dots]

    # Plot the combined function for each solution set as dots at whole numbers
    plt.plot(x_values_dots, combined_values_dots, 'o', label=f'Set {idx+1}: a={a:.2f}, b={b:.2f}, c={c:.2f}', color=colors[idx], markersize=5)

# Plot the simple linear function as a continuous line
plt.plot(x_values_continuous, linear_values, label='Linear Function', linestyle='-', color='k')

plt.title('Graphs (%s)' % (len(solution_sets)))
plt.xlabel('x')
plt.ylabel('Function values')
plt.legend()
plt.grid(True)
plt.show()
