# 1. Print numbers from 1 to 10 using while loop

i = 1

while i <= 10:
    print(i)
    i = i + 1


# 2. Print numbers from 10 to 1

i = 10

while i >= 1:
    print(i)
    i = i - 1


# 3. Print all even numbers from 1 to 50

i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)
    i = i + 1


# 4. Print all odd numbers from 1 to 50

i = 1

while i <= 50:
    if i % 2 != 0:
        print(i)
    i = i + 1


# 5. Multiplication table of a given number

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1


# 6. Find the sum of numbers from 1 to N

n = int(input("Enter N: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)


# 7. Find the sum of even numbers from 1 to N

n = int(input("Enter N: "))

i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("Sum of even numbers =", sum)


# 8. Count the numbers from 1 to N

n = int(input("Enter N: "))

i = 1
count = 0

while i <= n:
    count = count + 1
    i = i + 1

print("Count =", count)


# 9. Question not visible in the image


# 10. Reverse a given number using while

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)


# 11. Find the sum of digits of a given number

n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)


# 12. Count the number of digits in a given number

n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits =", count)


# 13. Check whether a number is a palindrome

n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# 14. Check whether a number is an Armstrong number

n = int(input("Enter a number: "))

original = n
count = 0

while n > 0:
    count = count + 1
    n = n // 10

n = original
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** count
    n = n // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# 15. Find the largest digit in a given number

n = int(input("Enter a number: "))

largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest digit =", largest)


# 16. Find the smallest digit in a given number

n = int(input("Enter a number: "))

smallest = 9

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n = n // 10

print("Smallest digit =", smallest)


# 17. Fibonacci series up to N terms

n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)

    c = a + b
    a = b
    b = c

    i = i + 1


# 18. Check whether a number is prime using while

n = int(input("Enter a number: "))

i = 2
is_prime = True

if n <= 1:
    is_prime = False

while i < n:
    if n % i == 0:
        is_prime = False
        break

    i = i + 1

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")