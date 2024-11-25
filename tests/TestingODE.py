from ODE import solve_second_order
import numpy as np


# Define y double prime:
def ypp(yp, y, x):
    return 2 * yp + y


# Create x and y lists:
x_list = np.linspace(0, 10, 1000001)

y_list = solve_second_order(0, 1, ypp, [0, 10])


# Write to .csv file:
with open("TestingODE.csv", "w") as file:
    file.write(f"x,y\n")
    for i in range(len(x_list)):
        file.write(f"{x_list[i]},{y_list[i]}\n")