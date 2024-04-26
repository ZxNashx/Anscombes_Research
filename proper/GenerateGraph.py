import numpy as np
import sympy as sp

class GraphBuilder():
    def __init__(self, ybar = 7.5, n = 11, variance = 33/8, slope = 1/2, intercept = 3, start_value = 4):
        self.ybar = ybar
        self.n = n
        self.variance = variance
        self.slope = slope
        self.intercept = intercept
        self.start_value = start_value

        self.a, self.b, self.c = sp.symbols('a b c')

    def generate_M_matrix(self, fx, gx, hx):
        # Generate the array x
        x = np.arange(self.start_value, self.n + self.start_value)

        # Initialize an empty matrix to store results
        M = np.zeros((len(x), 3))  # Create a matrix of zeros with appropriate dimensions

        # Apply the functions fx, gx, hx to each element of x individually
        for i, xi in enumerate(x):
            M[i, 0] = fx(xi)  # Apply fx to each element and assign to the first column
            M[i, 1] = gx(xi)  # Apply gx to each element and assign to the second column
            M[i, 2] = hx(xi)  # Apply hx to each element and assign to the third column

        vector = sp.Matrix([self.a, self.b, self.c])

        self.result = sp.Matrix(M) * vector
        return self.result

    def solve(self):
        ones_vector = sp.ones(self.result.shape[0], 1)
        equation1 = sp.Eq(self.result.dot(ones_vector), self.n * self.ybar)

        modified_vector = self.result - self.ybar * ones_vector
        modified_dot_product = modified_vector.dot(modified_vector)
        equation2 = sp.Eq(modified_dot_product, (self.n - 1) * self.variance)

        x_vector = sp.Matrix(np.arange(self.start_value, self.n + self.start_value))
        modified_x_vector = x_vector - 9 * ones_vector  # Note: '9' should be defined or explained
        modified_result_vector = self.result - self.ybar * ones_vector
        equation3 = sp.Eq(modified_x_vector.dot(modified_result_vector), (self.n - 1) * self.n * self.slope)

        self.solution = sp.solve((equation1, equation2, equation3), (self.a, self.b, self.c))
        return self.solution

