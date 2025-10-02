
#http://geeksforgeeks.org/dsa/binary-search/
# Python program for implementation of Selection
# Sort
#update, the code was changed


def binary_search_sub(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Check if current element is >= threshold
        if arr[mid] >= x:
            high = mid - 1  # Look in the left half
        else:
            low = mid + 1  # Look in the right half

    # Return the index of the first element >= x
    return low


# Optional test when run directly
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binary_search_sub(arr, x)
    if result < len(arr) and arr[result] >= x:
        print("First element >= x is at index", result, "->", arr[result])
    else:
        print("No element >= x was found.")
