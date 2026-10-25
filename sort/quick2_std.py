def quicksort(arr, low, high):
    if low >= high:
        return

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    p = i + 1

    quicksort(arr, low, p - 1)
    quicksort(arr, p + 1, high)

arr = [35, 50, 15, 25, 80, 20, 90, 45]
quicksort(arr, 0, len(arr) - 1)
print(arr)