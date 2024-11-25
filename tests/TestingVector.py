from Vector import Vector


# Create two 2D vectors:
vector1 = Vector(0, 1)
vector2 = Vector(7, 6)


# Add both vectors and print:
v_sum = vector1.v_add(vector2)

print (f"{v_sum.x}, {v_sum.y}")


# Subtracted vector2 from vector1 and print:
v_diff = vector1.v_subtract(vector2)

print (f"{v_diff.x}, {v_diff.y}")


# Compute the dot product of both vectors and print:
dot = vector1.dot_product(vector2)

print(dot)


# Compute the magnitudes of both vectors and print:
mag1 = vector1.magnitude()
mag2 = vector2.magnitude()

print(mag1)
print(mag2)


# Print the 2D angles of both vectors and print:
angle1 = vector1.angle2D()
angle2 = vector2.angle2D()

print(angle1)
print(angle2)