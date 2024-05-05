
def prime_number(number):
    if number <= 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


print(prime_number(9))