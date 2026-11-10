numbers = [10, 20, 30, 20, 10, 40, 50, 30]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)
