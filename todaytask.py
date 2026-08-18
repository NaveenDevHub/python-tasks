a = int(input("Enter the sales value: "))

if a <= 500:
    print("Your Commission is", a * 5 / 100)

elif a>500 and a <= 2000:
    print("Your Commission is", 35 + (a - 500) * 10 / 100)

elif a>2000 and a <= 5000:
    print("Your Commission is", 185 + (a - 2000) * 12 / 100)

else:
    print("Your Commission is", 545 + (a - 5000) * 12.5 / 100)