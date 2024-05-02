def char_frequency(string):
    if len(string) == 0:
        return {}
    string = string.lower()
    dict_char = {}

    for letter in string:
        if letter in dict_char:
            dict_char[letter] += 1
        else:
            dict_char[letter] = 1
    return dict_char

print(char_frequency("wordword"))



