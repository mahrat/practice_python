# searching algorithms

def linear_search(arr, target):
    # just check every single item, O(n), works on unsorted data
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    # array MUST be sorted for this to work, forgot that once and got confused why it failed
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    unsorted_data = [8, 2, 9, 1, 5, 3]
    sorted_data = sorted(unsorted_data)

    print("unsorted:", unsorted_data)
    print("sorted:  ", sorted_data)

    print("linear search for 5:", linear_search(unsorted_data, 5))
    print("linear search for 100 (not there):", linear_search(unsorted_data, 100))

    print("binary search for 5:", binary_search(sorted_data, 5))
    print("binary search recursive for 9:", binary_search_recursive(sorted_data, 9))
    print("binary search for missing value:", binary_search(sorted_data, 42))

    # compare against python's built-in index() just to sanity check
    assert sorted_data.index(5) == binary_search(sorted_data, 5)
    print("matches built-in .index() - good")
