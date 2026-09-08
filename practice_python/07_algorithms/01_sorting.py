# sorting algorithms - classic interview prep stuff
# obviously python's built-in sorted()/list.sort() (timsort) is better than all of these
# doing this just to actually understand how sorting works under the hood

def bubble_sort(arr):
    arr = arr.copy()   # don't mutate the original, learned to do this after messing up earlier
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break   # already sorted, no need to keep looping, small optimization
    return arr


def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]   # picking middle element as pivot, simplest for practice
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_data = [5, 2, 9, 1, 5, 6, 3, 8, 7]

    print("original:      ", test_data)
    print("bubble sort:   ", bubble_sort(test_data))
    print("selection sort:", selection_sort(test_data))
    print("insertion sort:", insertion_sort(test_data))
    print("merge sort:    ", merge_sort(test_data))
    print("quick sort:    ", quick_sort(test_data))
    print("builtin sorted:", sorted(test_data))

    # quick sanity check they all agree with each other
    assert bubble_sort(test_data) == sorted(test_data)
    assert selection_sort(test_data) == sorted(test_data)
    assert insertion_sort(test_data) == sorted(test_data)
    assert merge_sort(test_data) == sorted(test_data)
    assert quick_sort(test_data) == sorted(test_data)
    print("all sorts match builtin sorted() - good")
