
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    print("left: ",left)

    right = merge_sort(arr[mid:])
    print("right: ",right)

    return merge(left, right)


def merge(left, right):

    print("left: ",left)
    print("right: ",right)
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    print("result:",result)
    return result


arr = [4, 9, 1, 6, 2, 5, 8, 3, 8]

arr = merge_sort(arr)
print(arr)
