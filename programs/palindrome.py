string = input("Enter a string: ")

# convert to lowercase for uniform comparison
string = string.lower()

# reverse the string using slicing
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
