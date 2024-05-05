def middle_letter(input_string):
    """
    Returns the middle letter(s) of the input string.
    """
    length = len(input_string)
    middle_index = length // 2

    if length % 2 == 0:
        return input_string[middle_index - 1:middle_index + 1]
    else:
        return input_string[middle_index]

input_str1 = "banana"
input_str2 = "apple"
result1 = middle_letter(input_str1)
result2 = middle_letter(input_str2)
print(f"Middle letter(s) of '{input_str1}': {result1}")
print(f"Middle letter(s) of '{input_str2}': {result2}")
