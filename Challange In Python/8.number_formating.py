# def format_number(number):
#     if number < 0:
#         return None
#     number = str(number)
#     if len(number) < 3:
#         return number
#     separated =[ number[i-3:i]  for i in range(1, len(number)+1)]
#     # print(separated)
#     return separated


# print(format_number(1000000))
def format_number(number):
    if number < 0:
        return None
    number = str(number)
    if len(number) < 4:
        return number
    
    separated = []
    reversed_number = number[::-1]
    for i in range(0, len(reversed_number), 3):
        chunk = reversed_number[i:i+3]
        separated.append(chunk)

    return ','.join(separated)[::-1]

print(format_number(1000000))
