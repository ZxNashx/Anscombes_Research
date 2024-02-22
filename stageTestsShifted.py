import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

ybar = 7.5
n = 11.0
variance = 33/8
slope = 1/2

##
##
# stage 1

xs = 9
ys = 7.5

x = np.arange(4-xs, 16-xs)  # x values from 4 to 15
M = np.column_stack((x**2, x, np.ones(len(x))))

a, b, c = sp.symbols('a b c')

M_sympy = sp.Matrix(M)
vector = sp.Matrix([a, b, c])

ones_vector = sp.ones(result.shape[0], 1)

result = (M_sympy * vector) - 7.5 * ones_vector

print("THE MATRIX TIMES THE VECTOR A,B,C")

print(result)

# stage 2.1
equation1 = sp.Eq(result.dot(ones_vector), 0)
solution1 = sp.solve(equation1, (a, b, c))
print("\n\nTHE RESULTING VECTOR 2.1")
print(solution1)

#stage 2.2

modified_dot_product = result.dot(result)

equation2 = sp.Eq(modified_dot_product, 10 * (33/8))

solution2 = sp.solve(equation2, (a, b, c))
print("\n\nTHE RESULTING VECTOR 2.2")
print(solution2)

# stage 2.3

x_vector = sp.Matrix([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
modified_x_vector = x_vector - 9 * ones_vector
modified_result_vector = result - 7.5 * ones_vector
equation3 = sp.Eq(modified_x_vector.dot(modified_result_vector), 10 * 11 * 1/2)

# Create a vector of ones
ones_vector = sp.ones(len(x_vector), 1)

modified_dot_product = modified_x_vector.dot(modified_result_vector)

equation3 = sp.Eq(modified_x_vector.dot(modified_result_vector), 10 * 11 * 1/2)
solution3 = sp.solve(equation3, (a, b, c))
print("\n\nTHE RESULTING VECTOR 2.3")
print(solution3)

solution_final = sp.solve((equation1, equation2, equation3), (a, b, c))

# Print the final solution
print("\n\nTHE FINAL SOLUTION")
print(solution_final)

def get_q(fx):
    return "%sx^2 + %sx + %s" % (s[0],s[1],s[2])

for s in solution_final:
    print(get_q(s))

def line_equation(x):
    return 1/2 * x + 3

def parabola_equation(x, a, b, c):
    return a * x**2 + b * x + c

def add_parabola_to_plot(a, b, c, x_values, label):
    y_values = parabola_equation(x_values, a, b, c)
    plt.plot(x_values, y_values, label=label)

x_line_values = np.linspace(0, 20, 400)  # x values for the line
x_parabola_values = np.linspace(4, 15, 400)  # x values for the parabola

plt.figure(figsize=(6, 4))

y_line_values = line_equation(x_line_values)
plt.plot(x_line_values, y_line_values, label='y = 1/2x + 3')

for s in solution_final:
    a, b, c = s
    add_parabola_to_plot(a, b, c, x_parabola_values, 'Parabola')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


