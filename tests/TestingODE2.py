from ODE import solve_first_order
import numpy as np


# Define y  prime:
def yp(y, x):
    return 1 / ((x + 1) * y)


# Create x and y lists:
x_list = np.linspace(0, 10, 1000001)

y_list = solve_first_order(1, yp, [0, 10])


# Write to .csv file:
with open("TestingODE2.csv", "w") as file:
    file.write(f"x,y\n")
    for i in range(len(x_list)):
        file.write(f"{x_list[i]},{y_list[i]}\n")