import numpy as np


def solve_first_order(y, yp, x_range, n=pow(10, 6), method="euler"):
    if isinstance(x_range, list) and len(x_range) == 2:
        if method == "euler":
            y_list = np.zeros(n + 1)
            dx = (x_range[1] - x_range[0]) / n

            # Euler's method:
            for i in (range(n+1)):
                a = x_range[0] + i * dx

                if i == 0:
                    y_list[i] = y
                else:
                    y_list[i] = yp(y_list[i - 1], a) * dx + y_list[i - 1]

            return y_list
    else:
        raise TypeError("The variable 'x_range' must be a list with a length of 2.")


def solve_second_order(y, yp, ypp, x_range, n=pow(10, 6)):
    if isinstance(x_range, list) and len(x_range) == 2:
        y_list = np.zeros(n + 1)
        yp_list = np.zeros(n + 1)
        dx = (x_range[1] - x_range[0]) / n

        # Euler-like method:
        for i in (range(n+1)):
            a = x_range[0] + i * dx

            if i == 0:
                yp_list[i] = yp
                y_list[i] = y
            else:
                yp_list[i] = ypp(yp_list[i - 1], y_list[i - 1], a) * dx + yp_list[i - 1]
                y_list[i] = yp_list[i - 1] * dx + y_list[i - 1]

        return y_list
    else:
        raise TypeError("The variable 'x_range' must be a list with a length of 2.")