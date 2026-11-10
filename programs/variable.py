def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(5, 10))
print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers())
