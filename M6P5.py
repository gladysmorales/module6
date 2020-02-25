# Gladys Morales
# February 18, 2020
# This program converts radians to degrees.

import math

degree = 57.2958

degree_var = int(input("Enter radians to convert to degrees: "))

print("Your radians in degrees: ", degree_var * degree)

print("Using math module radians to degrees: ", math.degrees(degree_var))
