def largest_difference(numbers):
    if len(numbers) < 2:
        return 0
    numbers.sort()
    return numbers[-1] - numbers[0], numbers


numbers = [3, 6, 7, 9, 1, 2, 0, 5, 4]
print(largest_difference(numbers))
