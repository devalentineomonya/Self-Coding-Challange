def perfect_square(number):
    if number < 1:
        return False

    sqrt_candidate = 1
    while sqrt_candidate * sqrt_candidate <= number:
        if sqrt_candidate * sqrt_candidate == number:
            return True
        sqrt_candidate += 1

    return False
print(perfect_square(4))