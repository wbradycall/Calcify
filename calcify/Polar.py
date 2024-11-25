import math
import Basic


def polar_to_cartesian(r, theta):
    x = r(theta) * math.cos(theta)
    y = r(theta) * math.sin(theta)

    return [x, y]


def cartesian_to_polar(f, t):
    if isinstance(f, list):
        return f[0] / math.cos(t)
    else:
        raise TypeError("The input of the function 'cartesian_to_polar' must be a list of two functions of t.")


def polar_integral(r, alpha, beta):
    return Basic.integral(0.5 * r ** 2, alpha, beta)