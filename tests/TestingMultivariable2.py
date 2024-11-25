from Multivariable import *


# Define multivariable function:
def f(x, y, z):
    return x ** 3 + y ** 2 + z ** 4 + 1


# Find partial derivative of function with respect to x at (x,y,z)=(1,1,1) and print:
par_x = partial_derivative_x(f, 1, 1, z=1)

print(par_x)


# Find partial derivative of function with respect to y at (x,y,z)=(1,1,1) and print:
par_y = partial_derivative_y(f, 1, 1, z=1)

print(par_y)


# Find partial derivative of function with respect to z at (x,y,z)=(1,1,1) and print:
par_z = partial_derivative_z(f, 1, 1, 1)

print(par_z)


# Find triple integral of function from 0 to 2 for all 3 independent variables and print:
triple_int = triple_integral(f, 0, 2, 0, 2, 0, 2)

print(triple_int)