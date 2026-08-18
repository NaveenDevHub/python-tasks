# Write a Python program to swap (exchange) values of two variables. A and B.

a=int(input(enter the a value))
b=int(input(enter the B value))

temp=a
a=b
b=temp

print("After swapping: a =", a, "b =", b)