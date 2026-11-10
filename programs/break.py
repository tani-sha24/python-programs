print("Demonstration of break, continue, and pass statements\n")
print("*Using break:*")
for i in range(1, 5):
    if i == 4:
        break
    print(i)
print("\n*Using continue:*")
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
print("\n*Using pass:*")
for i in range(1, 5):
    if i == 3:
        pass
    print(i)
