def second_smallest(*list_integers):
    if len(list_integers) < 2:
        return 0
    unique_list = list(set(list_integers))
    if len(unique_list) < 2:
        return 0

    first_smallest_num = unique_list[0]
    second_smallest_num = unique_list[1]
    for integer in unique_list[2:]:
        if integer < first_smallest_num:
            second_smallest_num = first_smallest_num
            first_smallest_num = integer
        elif integer < second_smallest_num:
            second_smallest_num = integer

    return second_smallest_num


print(second_smallest(1, 5, 3, 4, 2, 6, 7))

