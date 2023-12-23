def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left != right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] > target:
            right = mid

    return -1


sample = [3, 7, 9, 11, 12, 15, 16, 18, 20]

index = binary_search(sample, 7)

print(index)
