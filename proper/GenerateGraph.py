import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

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
        x = np.arange(self.start_value, self.n + self.start_value)

