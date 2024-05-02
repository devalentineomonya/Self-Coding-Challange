def add_dots(not_dotted):
    dotted_word = ""
    for letter in not_dotted[:len(not_dotted)]:
        letter += "."
        dotted_word = dotted_word + letter
    return dotted_word
print(add_dots("testtest"))


def remove_dots(dotted_word):
    not_dotted = ""
    for letter in dotted_word:
        if letter == ".":
            continue
        else:
            not_dotted += letter
    return not_dotted

print(remove_dots(add_dots("text")))