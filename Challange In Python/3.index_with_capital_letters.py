
# def capital_indexes(word:str):
#     if len(word) == 0:
#         return None
#     indexes_with_capital = [word.index(x) for x in word if x.isupper()]
#     return indexes_with_capital
#
#
#
# word = "Hello"
def capital_indexes(word:str):

    if len(word) == 0:
        return None
    
    indexes_with_capital = []
    
    for i in word:
        if i.isupper():
            indexes_with_capital.append(word.index(i))
    return indexes_with_capital

print(capital_indexes("HellO"))