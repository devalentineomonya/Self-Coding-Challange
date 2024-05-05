def palindromes(*list_words):
    if len(list_words) == 0:
        return []
    palindrome_words = []

    for word in list_words:
        reverse_word = ""
        for letter in word:
            reverse_word = letter + reverse_word

        if reverse_word == word:
            palindrome_words.append(word)

    return palindrome_words

print(palindromes("radar","level","Welcome","non"))