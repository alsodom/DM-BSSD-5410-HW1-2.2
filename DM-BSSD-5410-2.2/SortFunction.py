#https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/
#sort function
#some implementation of files were adapted from GeeksforGeeks "Iterative Quick Sort"
#https://www.geeksforgeeks.org/python/python-program-for-iterative-quick-sort/
# and some general binary search from https://en.wikipedia.org/wiki/Binary_search_algorithm
#modifications came from me


def partition(arr, low, high, compare):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if compare(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_iterative(arr, compare):
    size = len(arr)
    stack = []

    # Push initial low and high indices
    stack.append((0, size - 1))

    # Pop and push while stack is not empty
    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high, compare)
            # Push left side
            stack.append((low, p - 1))
            # Push right side
            stack.append((p + 1, high))
