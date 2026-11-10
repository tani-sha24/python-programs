from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

mapped = list(map(lambda x: x * 2, nums))
print(mapped)

filtered = list(filter(lambda x: x % 2 == 0, nums))
print(filtered)

reduced = reduce(lambda a, b: a + b, nums)
print(reduced)
