def find_first(arr, key):
    left = 0
    right = len(arr) - 1
    fo = -1  # To store the index of the first occurrence

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            fo = mid  # Update first occurrence
            right = mid - 1  # Move left to find the first occurrence
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return fo

def find_last(arr, key):
    left = 0
    right = len(arr) - 1
    lo = -1  # To store the index of the last occurrence

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            lo = mid  # Update last occurrence
            left = mid + 1  # Move right to find the last occurrence
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return lo

def fin_occ(arr, key):
    fo = find_first(arr, key)
    if fo == -1:
        return 0
    lo = find_last(arr, key)

    return lo - fo + 1

# Test with the provided list
L = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
print(fin_occ(L, 3))  # Output should be 4
