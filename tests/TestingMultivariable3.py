import math
from Multivariable import *


# Define 2D parametric function:
def x(t):
    return t ** 3

def y(t):
    return math.sin(t)

f = [x, y]


# Random vector:
vector = Vector(5, 3)


# Find the direction derivative of the function with respect to the vector at t=2 and print:
dir_der = directional_derivative(f, 2, vector)

print(dir_der)