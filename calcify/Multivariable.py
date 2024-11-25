import Basic
from Vector import Vector


def partial_derivative_x(f, x, y, h=pow(10, -9), z=None):
    if z == None:
        return (f(x + h, y) - f(x, y)) / h
    else:
        return (f(x + h, y, z) - f(x, y, z)) / h


def partial_derivative_y(f, x, y, h=pow(10, -9), z=None):
    if z == None:
        return (f(x, y + h) - f(x, y)) / h
    else:
        return (f(x, y + h, z) - f(x, y, z)) / h


def partial_derivative_z(f, x, y, z, h=pow(10, -9)):
    return (f(x, y, z + h) - f(x, y, z)) / h


def gradient(f, x, y, z=None):
    if z == None:
        return Vector(partial_derivative_x(f, x, y), partial_derivative_y(f, x, y))
    else:
        return Vector(partial_derivative_x(f, x, y, z), partial_derivative_y(f, x, y, z), partial_derivative_z(f, x, y, z))


def double_integral(f, a, b, c, d, n=pow(10, 3)):
    def integrated_f(y):
        dx = (b - a) / n

        sum = 0

        i = 0

        # First Simpson's rule term:
        x_i = a + i * dx
        sum += f(x_i, y)
        i += 1

        # Middle Simpson's rule terms:
        while i < n:
            x_i = a + i * dx
            sum += (3 + (-1) ** (i + 1)) * f(x_i, y)
            i += 1

        # Final Simpson's rule term:
        x_i = a + i * dx
        sum += f(x_i, y)

        return sum * dx / 3

    dy = (d - c) / n

    sum = 0

    i = 0

    # First Simpson's rule term:
    y_i = c + i * dy
    sum += integrated_f(y_i)
    i += 1

    # Middle Simpson's rule terms:
    while i < n:
        y_i = c + i * dy
        sum += (3 + (-1) ** (i + 1)) * integrated_f(y_i)
        i += 1

    # Final Simpson's rule term:
    y_i = c + i * dy
    sum += integrated_f(y_i)

    return sum * dy / 3


def triple_integral(f, a, b, c, d, g, h, n=pow(10, 2)):
    def integrated_f1(y, z):
        dx = (b - a) / n

        sum = 0

        i = 0

        # First Simpson's rule term:
        x_i = a + i * dx
        sum += f(x_i, y, z)
        i += 1

        # Middle Simpson's rule terms:
        while i < n:
            x_i = a + i * dx
            sum += (3 + (-1) ** (i + 1)) * f(x_i, y, z)
            i += 1

        # Final Simpson's rule term:
        x_i = a + i * dx
        sum += f(x_i, y, z)

        return sum * dx / 3

    def integrated_f2(z):
        dy = (d - c) / n

        sum = 0

        i = 0

        # First Simpson's rule term:
        y_i = c + i * dy
        sum += integrated_f1(y_i, z)
        i += 1

        # Middle Simpson's rule terms:
        while i < n:
            y_i = c + i * dy
            sum += (3 + (-1) ** (i + 1)) * integrated_f1(y_i, z)
            i += 1

        # Final Simpson's rule term:
        y_i = c + i * dy
        sum += integrated_f1(y_i, z)

        return sum * dy / 3

    dz = (h - g) / n

    sum = 0

    i = 0

    # First Simpson's rule term:
    z_i = g + i * dz
    sum += integrated_f2(z_i)
    i += 1

    # Middle Simpson's rule terms:
    while i < n:
        z_i = g + i * dz
        sum += (3 + (-1) ** (i + 1)) * integrated_f2(z_i)
        i += 1

    # Final Simpson's rule term:
    z_i = g + i * dz
    sum += integrated_f2(z_i)

    return sum * dz / 3


def directional_derivative(f, t, vector):
    if isinstance(f, list) and isinstance(vector, Vector):
        Df = []

        for i in range(len(f)):
            der = Basic.derivative(f[i], t)
            Df.append(der)

        sum = Df[0] * vector.x + Df[1] * vector.y

        if vector.z != None:
            sum += Df[2] * vector.z

        if vector.w != None:
            sum += Df[3] * vector.w

        return sum
    else:
        raise TypeError("The first input of the function 'cartesian_to_polar' must be a list of multiple functions of t, the second input must be an int or float, and the third input must be a vector.")


def divergence(vector_function, x, y, z):
    return partial_derivative_x(vector_function.x, x, y, z) + partial_derivative_y(vector_function.y, x, y, z) + partial_derivative_z(vector_function.z, x, y, z)


def curl2D(vector_function, x, y):
    return partial_derivative_x(vector_function.y, x, y) - partial_derivative_y(vector_function.x, x, y)


def curl3D(vector_function, x, y, z):
    new_x = partial_derivative_y(vector_function.z, x, y, z) - partial_derivative_z(vector_function.y, x, y, z)
    new_y = partial_derivative_z(vector_function.x, x, y, z) - partial_derivative_x(vector_function.z, x, y, z)
    new_z = partial_derivative_x(vector_function.y, x, y, z) - partial_derivative_y(vector_function.x, x, y, z)

    return Vector(new_x, new_y, new_z)