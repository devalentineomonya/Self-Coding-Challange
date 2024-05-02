# def common_character (string):
#     if len(string) == 0:
#         return None
#     char_dict = {}
#     largest_count = 0
#     for char in string:
#         if char in char_dict:
#             char_dict[char] += 1
#         else:
#             char_dict[char] = 1
#     for dict_char in char_dict:
#         if char_dict[dict_char] > largest_count:
#             largest_count = char_dict[dict_char]
#     return list(char_dict.keys())[list(char_dict.values()).index(largest_count)]

# print(common_character("worlldoo"))


#
# GPT Solution
#

def common_character(string):
    if len(string) == 0:
        return None

    char_dict = {}
    largest_count = 0

    for char in string.lower().replace(" ", ""):
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
            if char_dict[char] > largest_count:
                largest_count = char_dict[char]

    return  [char for char, count in char_dict.items() if count == largest_count]

print(common_character("worlllldoo"))