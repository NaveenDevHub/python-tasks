# Write a python program to find the area & circumference of circle of radius r. area = π * r * r circumference = 2 * π * r;


import math
r = float(input("Enter the radius of the circle: "))

area = math.pi * r * r
circumference = 2 * math.pi * r

print("Area of the circle is:", area)
print("Circumference of the circle is:", circumference)