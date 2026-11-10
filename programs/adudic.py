# Creating an empty dictionary
my_dict = {}

print("Initial Dictionary:", my_dict)

# -----------------------------
# 1. ADDING ELEMENTS
# -----------------------------

# Adding key-value pairs
my_dict["name"] = "Tanisha"
my_dict["age"] = 20
my_dict["course"] = "CSE"

print("\nAfter Adding Elements:", my_dict)

# -----------------------------
# 2. UPDATING ELEMENTS
# -----------------------------

# Updating existing value
my_dict["age"] = 21        # Update age
my_dict["course"] = "Cyber Security"

print("\nAfter Updating Elements:", my_dict)

# -----------------------------
# 3. DELETING ELEMENTS
# -----------------------------

# Deleting a key-value pair
del my_dict["age"]

print("\nAfter Deleting 'age':", my_dict)

# Using pop() to delete and return the value
removed_value = my_dict.pop("course")
print("\nRemoved value using pop():", removed_value)

print("\nFinal Dictionary:", my_dict)
