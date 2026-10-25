arr=[4,6,2,5,7,9,1,3]

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)   # Left subarray
        quick_sort(arr, p + 1, high)  # Right subarray


def partition(arr, low, high):
    pivot = arr[high] #last element
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:  # Ascending order
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


#arr = [4, 9, 1, 6, 2, 5, 8, 3]
quick_sort(arr, 0, len(arr) - 1)

print(arr)