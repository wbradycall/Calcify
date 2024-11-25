from Multivariable import *


# Define multivariable function:
def f(x, y):
    return x ** 3 + y ** 2 + 1


# Find partial derivative of function with respect to x at (x,y)=(1,1) and print:
par_x = partial_derivative_x(f, 1, 1)

print(par_x)


# Find partial derivative of function with respect to y at (x,y)=(1,1) and print:
par_y = partial_derivative_y(f, 1, 1)

print(par_y)


# Find double integral of function from 0 to 2 for both independent variables and print:
double_int = double_integral(f, 0, 2, 0, 2)

print(double_int)