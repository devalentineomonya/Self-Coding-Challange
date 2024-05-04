def print_xmas_tree(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    trunk_spaces = ' ' * (height - 2)
    base_spaces = ' ' * (height-5)
    for letter in "XMAS":
        if letter[-1]:
            print(trunk_spaces + letter)
        else:
            print(trunk_spaces + letter + "\n")

    print(base_spaces + '=======')
print_xmas_tree(5)