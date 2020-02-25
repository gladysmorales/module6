# Gladys Morales
# February 18th, 2020
# This program calculates the factorial of a user input value.

import math

f = int(input("Enter a number to calculate the factorial: "))

n = 1

for i in range(1, f + 1):
    n = n * 1

print("My factorial: ", n)

print("Math factorial: ", math.factorial(f))