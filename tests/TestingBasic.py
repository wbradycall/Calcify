from Basic import derivative, integral


# Define function:
def f(x):
    return x ** 3


# Find derivative of function at x=2 and print:
der = derivative(f, 2)

print(der)


# Find integral of function from 0 to 2 and print:
integ = integral(f, 0, 2)

print(integ)