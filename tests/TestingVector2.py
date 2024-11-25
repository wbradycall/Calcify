from Vector import Vector


# Create two 3D vectors:
vector1 = Vector(0, 1, 2)
vector2 = Vector(7, 6, 3)


# Add both vectors and print:
v_sum = vector1.v_add(vector2)

print (f"{v_sum.x}, {v_sum.y}, {v_sum.z}")


# Subtracted vector2 from vector1 and print:
v_diff = vector1.v_subtract(vector2)

print (f"{v_diff.x}, {v_diff.y}, {v_diff.z}")


# Compute the dot product of both vectors and print:
dot = vector1.dot_product(vector2)

print(dot)


# Compute the magnitudes of both vectors and print:
mag1 = vector1.magnitude()
mag2 = vector2.magnitude()

print(mag1)
print(mag2)


# Compute the cross product of both vectors and print:
cross = vector1.cross_product(vector2)

print(f"{cross.x}, {cross.y}, {cross.z}")