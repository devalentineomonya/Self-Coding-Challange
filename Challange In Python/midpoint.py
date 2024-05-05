def mid(word):
    length = len(word)
    if length % 2 == 1:
        midpoint = length//2
        return word[midpoint]
    else:
        return ""

print(mid("Wel"))