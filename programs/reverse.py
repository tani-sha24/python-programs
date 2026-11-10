num = int(input("Enter an integer: "))
reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)
