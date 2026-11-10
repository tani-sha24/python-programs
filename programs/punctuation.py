text = input("Enter a string: ")

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""

for ch in text:
    if ch not in punctuations:
        result += ch

print("String without punctuation:", result)
