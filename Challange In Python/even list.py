# def list_of_even_numbers(numbers: list)->list:
#     if len(numbers) == 0:
#         return []
#     new_list = []
#     for num in numbers:
#         if isinstance(num, int) and num % 2 == 0:
#             new_list.append(num)

#     new_list.sort()
#     return new_list


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_of_even_numbers(numbers))



def list_of_even_numbers(numbers: list) -> list:
    if len(numbers) == 0:
        return []

    even_numbers = [num for num in numbers if isinstance(num, int) and num % 2 == 0]
    sorted_even_numbers = sorted(even_numbers)

    return sorted_even_numbers


print(list_of_even_numbers(numbers))