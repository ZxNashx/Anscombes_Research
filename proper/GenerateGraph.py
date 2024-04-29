import numpy as np
import sympy as sp
import random

def is_fun_zero(fx, x_values):
    # Improved check to see if the function is zero over a specific range
    return all(fx(x) == 0 for x in x_values)
class GraphBuilder():
    def __init__(self, ybar=7.5, n=11, variance=33/8, slope=1/2, intercept=3, start_value=4):
        self.ybar = ybar
        self.n = n
        self.variance = variance
        self.slope = slope
        self.intercept = intercept
        self.start_value = start_value

        self.a, self.b, self.c = sp.symbols('a b c')

    def generate_M_matrix(self, fx, gx, hx):
        x = np.arange(self.start_value, self.start_value + self.n)
        M = []
        functions = [fx, gx, hx]
        active_vars = []
        # Populate the matrix and track active variables
        for func, var in zip(functions, [self.a, self.b, self.c]):
            if not is_fun_zero(func, x):  # Check if function is zero over the range
                M.append([func(xi) for xi in x])
                active_vars.append(var)

        if not M:  # If all functions are zero
            raise ValueError("All input functions are zero; no valid matrix can be generated.")

        M = sp.Matrix(M).T  # Transpose to correct the orientation
        vector = sp.Matrix(active_vars)
        self.result = M * vector
        return self.result, active_vars

    def solve(self):
        ones_vector = sp.ones(self.result.shape[0], 1)
        equation1 = sp.Eq(self.result.dot(ones_vector), self.n * self.ybar)
        modified_vector = self.result - self.ybar * ones_vector
        modified_dot_product = modified_vector.dot(modified_vector)
        equation2 = sp.Eq(modified_dot_product, (self.n - 1) * self.variance)
        x_vector = sp.Matrix(np.arange(self.start_value, self.n + self.start_value))
        modified_x_vector = x_vector - self.n * ones_vector
        modified_result_vector = self.result - self.ybar * ones_vector
        equation3 = sp.Eq(modified_x_vector.dot(modified_result_vector), (self.n - 1) * self.n * self.slope)

        equations = [equation1, equation2, equation3]
        equations = [eq for eq in equations if eq.lhs != 0]  # Exclude trivially zero equations

        variables = self.result.free_symbols
        if not variables:
            return None  # No variables to solve for

        # Attempt to solve using assumptions about the system being potentially under-determined
        solution_set = sp.solve(equations, variables, dict=True, manual=True, simplify=False, rational=False)

        if isinstance(solution_set, list) and solution_set:
            return [{var: sol.get(var, 0) for var in [self.a, self.b, self.c]} for sol in solution_set]

        else:
            return None  # If no solutions or an error in solving

