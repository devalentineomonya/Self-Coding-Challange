num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def binary_search(arr, target, start=0):
    if len(arr) == 0:
        return -1

    midpoint = len(arr) // 2

    if arr[midpoint] == target:
        return start + midpoint
    elif arr[midpoint] < target:
        return binary_search(arr[midpoint + 1:], target, start + midpoint + 1)
    else:
        return binary_search(arr[:midpoint], target, start)


print(binary_search(num_array, 5))