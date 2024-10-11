
# Anscombe's Quartet Research Project

This project aims to generate and analyze synthetic datasets that replicate the statistical properties of **Anscombe's Quartet**. Anscombe's Quartet is a set of four datasets with nearly identical summary statistics—mean, variance, and linear regression properties—yet vastly different visual patterns when plotted. This project demonstrates the importance of visual data analysis by recreating the quartet using **linear regression techniques**, **linear algebra**, and **numerical methods**.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Usage Example](#usage-example)
- [Function Declaration Example](#function-declaration-example)
- [Additional Resources](#additional-resources)

---

## Project Overview

The primary goal of this project is to reconstruct the datasets in Anscombe's Quartet, exploring how these datasets can exhibit identical summary statistics but drastically different visual representations. This reinforces the critical role of graphical data analysis in conjunction with statistical calculations.

### Key Concepts:
- **Synthetic Dataset Generation:** Replicate Anscombe’s Quartet.
- **Linear Regression:** Implement least squares regression to fit lines through datasets.
- **Data Visualization:** Demonstrate how identical statistical properties can yield different graph patterns.
- **Linear Algebra:** Use vectorized calculations to compute means, variances, and regression coefficients.

---

## Project Structure

- **`/proper`**: Contains all final source code for the project.
    - **`GenerateGraph.py`**: The primary object responsible for generating graphs and performing calculations.
    - **`driver.py`**: Sets up the calculations, calls the appropriate functions, and displays the results.
    - **`/functions`**: Contains the custom functions used for dataset generation and manipulation.

### Key Files:
- **`GenerateGraph.py`**: Handles all graph generation and mathematical computations.
- **`driver.py`**: The main driver script that orchestrates the program flow and visualization.

---

## Usage Example

Here’s an example of how to use the project in `driver.py`:

```python
# Imports
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from GenerateGraph import GraphBuilder as GB
from math import sin, cos
from scipy.stats import linregress

# Editable Code
builder = GB()
from functions.test import f, g, h # Replace test with the name of your file in '/functions/' do not include .py file extension
SHOW_VALUES = True # Show / Hide a, b, c values
LOWEST_VALUE = 0
HIGHEST_VALUE = 100

...
```

---

## Function Declaration Example

The project allows you to define custom functions for dataset generation. Below is an example:

```python
# Function Definitions
def f(x):
    return x ** 2

def g(x):
    return x

def h(x):
    return 1
```

These functions are used within the regression framework to generate data points that fit Anscombe’s linear regression model.

Mathematical representation:
$$f(x) = x^2$$
$$g(x) = x$$
$$h(x) = 1$$

The function:
$$a \cdot f(x) + b \cdot g(x) + c \cdot h(x)$$

Where the constants \(a\), \(b\), and \(c\) are solved to match the datasets in Anscombe's Quartet.

---

## Additional Resources

- **Anscombe's Quartet Research Paper**: [Graphs in Statistical Analysis](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)
- **Anscombe's Quartet Presentation**: [AMD Presentation](https://github.com/ZxNashx/Anscombes_Research/blob/main/AMD%20Math%20Presentation.pdf)



