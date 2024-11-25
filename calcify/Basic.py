def derivative(f, x, h=pow(10, -9)):
    return (f(x + h) - f(x)) / h


def integral(f, a, b, n=pow(10, 6)):
    dx = (b - a) / n

    sum = 0

    i = 0

    # First Simpson's rule term:
    x_i = a + i * dx
    sum += f(x_i)
    i += 1

    # Middle Simpson's rule terms:
    while i < n:
        x_i = a + i * dx
        sum += (3 + (-1) ** (i + 1)) * f(x_i)
        i += 1

    # Final Simpson's rule term:
    x_i = a + i * dx
    sum += f(x_i)

    return sum * dx / 3