a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Maximum number is:", a)
    else:
        print("Maximum number is:", c)
else:
    if b >= c:
        print("Maximum number is:", b)
    else:
        print("Maximum number is:", c)
