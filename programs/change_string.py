def change_string(s):
    s = s.replace(s[0], 'X')
    return s

str_value = "hello world"
new_str = change_string(str_value)

print(new_str)    
print(str_value)