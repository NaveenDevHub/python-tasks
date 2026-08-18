# Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#. Largest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

#4. Largest of Three Numbers


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is", a)
elif b > c:
    print("Largest number is", b)
else:
    print("Largest number is", c)


#Eligible to Vote


age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#6. Leap Year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")