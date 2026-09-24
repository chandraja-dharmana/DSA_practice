arr = [10, 20, 30, 40, 50]
target = 40

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2
    print("mid",mid)
    print("arr[mid]",arr[mid])

    if arr[mid] == target:
        print("target index", mid)
        break

    elif arr[mid] < target:
        low = mid + 1
        print("low",low)

    else:
        high = mid - 1
        print("low",low)
