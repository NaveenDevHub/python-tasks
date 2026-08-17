
numbers = [10,20,30,40,50,50]

result=sum(numbers) / len(numbers)

print(result)


# single line command

#  Write a Python program to convert temperature in F to C. C = 5/9(F - 32)

a= int(input("Enter the F Value :"))

C = 5/9 * (a - 32)

print("Celcius value is", C , "C")

'''
Write a Python program to find area of trianlge
area = sqrt(s *(s-a)*(s-b)*(s-c))
where s = a+b+c /2

'''

# method 1

a,b,c = int(input("Enter A value")),int(input("Enter B value")),int(input("Enter C value"))

s = (a+b+c)/2

area = (s *(s-a)*(s-b)*(s-c)) ** 0.5

print("The area of Triangle : ",area)

#method 2

import math

a,b,c = int(input("Enter A value")),int(input("Enter B value")),int(input("Enter C value"))

s = (a+b+c)/2

area =  math.sqrt(s *(s-a)*(s-b)*(s-c))

print("The area of Triangle : ",area)


# Write a python program to display the ASCII value of a given character.



for i in range(65,90):
    print(chr(i))


a='N'
print(ord(a))

# ord means print a --> 65