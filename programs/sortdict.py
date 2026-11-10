my_dict = {"banana": 3, "apple": 10, "mango": 5, "orange": 2}

print("Original Dictionary:", my_dict)

sorted_by_key = dict(sorted(my_dict.items()))
print("\nDictionary Sorted by Keys:", sorted_by_key)

sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary Sorted by Values:", sorted_by_value)
