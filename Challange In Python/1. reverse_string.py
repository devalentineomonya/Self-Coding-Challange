def reversed_string(string):
    if len(string) < 2:
        return string
    
    reversed_string_result = ""
    for letter in string:
        reversed_string_result = letter + reversed_string_result
    return reversed_string_result

result = reversed_string("Valentine")

print(result)