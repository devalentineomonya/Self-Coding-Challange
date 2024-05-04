def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(numbers, 5))