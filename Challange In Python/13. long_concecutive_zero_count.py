def consecutive_zeros(binary_number):
    count = 0
    zeros_list = binary_number.split("1")
    for combination in zeros_list:
        length = len(combination)
        if length > count:
            count = length
    return count

print(consecutive_zeros("1010000011"))