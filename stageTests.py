import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# working file

ybar = 7.5
n = 11.0
variance = 33/8
slope = 1/2
intercept = 3

##
##
# stage 1

x = np.arange(4, n+4)  # x values from 4 to 15
M = np.column_stack((x**2, x, np.ones(len(x))))

a, b, c = sp.symbols('a b c')

M_sympy = sp.Matrix(M)
vector = sp.Matrix([a, b, c])

result = M_sympy * vector

print("THE MATRIX TIMES THE VECTOR A,B,C")

print(result)

# stage 2.1
ones_vector = sp.ones(result.shape[0], 1)
equation1 = sp.Eq(result.dot(ones_vector), n * ybar)
solution1 = sp.solve(equation1, (a, b, c))
print("\n\nTHE RESULTING VECTOR 2.1")
print(equation1)

#stage 2.2
modified_vector = result - ybar * ones_vector
modified_dot_product = modified_vector.dot(modified_vector)
equation2 = sp.Eq(modified_dot_product, (n-1) * variance)
solution2 = sp.solve(equation2, (a, b, c))
print("\n\nTHE RESULTING VECTOR 2.2")
print(equation2)

# stage 2.3

x_vector = sp.Matrix(np.arange(4, n+4) )
modified_x_vector = x_vector - 9 * ones_vector
modified_result_vector = result - ybar * ones_vector
equation3 = sp.Eq(modified_x_vector.dot(modified_result_vector), (n-1) * n * slope)
ones_vector = sp.ones(len(x_vector), 1)
solution3 = sp.solve(equation3, (a, b, c))
print("\n\nTHE RESULTING VECTOR 2.3")
print(equation3)

solution_final = sp.solve((equation1, equation2, equation3), (a, b, c))

# Print the final solution
print("\n\nTHE FINAL SOLUTION")
print(solution_final)

def get_q(fx):
    return "%sx^2 + %sx + %s" % (s[0],s[1],s[2])

for s in solution_final:
    print(get_q(s))

def line_equation(x):
    return slope * x + intercept

def parabola_equation(x, a, b, c):
    return a * x**2 + b * x + c

def add_parabola_to_plot(a, b, c, x_values, label):
    y_values = parabola_equation(x_values, a, b, c)
    plt.plot(x_values, y_values, label=label)

x_line_values = np.linspace(0, 20, 400)  # x values for the line
x_parabola_values = np.linspace(4, n+4, 400)  # x values for the parabola

plt.figure(figsize=(6, 4))

y_line_values = line_equation(x_line_values)
plt.plot(x_line_values, y_line_values, label='y = b1x + b0')
i = 0

titles = [
    "Anscombe's Parabola",
    "Second Parabola"
]

for s in solution_final:
    a, b, c = s
    add_parabola_to_plot(a, b, c, x_parabola_values, titles[i])
    i = i + 1

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("Two Parabolas Sharing Common Values", fontsize=20)
plt.show()


