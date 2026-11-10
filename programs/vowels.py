string = input("Enter a string: ")

vowels = 0
consonants = 0
string = string.lower()

for ch in string:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
