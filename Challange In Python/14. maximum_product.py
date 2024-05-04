def max_product(numbers):
    if len(numbers) < 3:
        return 0
    sorted_numbers = sorted(numbers)

    largest = sorted_numbers[-1]
    second_largest = sorted_numbers[-2]
    third_largest = sorted_numbers[-3]
    return largest * second_largest * third_largest

print(max_product([-1, -2, -3, -4, -5, -6]))