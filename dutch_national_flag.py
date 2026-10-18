
arr = [2, 0, 1, 2, 0, 0, 1, 1, 1, 2, 0, 1, 2, 2, 1, 1, 0, 0]
print("unsorted:\n", arr)

# l -> low pointer
# m -> mid pointer
# h -> high pointer
l, m = 0, 0  # not arr[0]
h = len(arr) - 1 # not arr[len(arr) - 1]

while m <= h:
    if arr[m] == 0:
        arr[l], arr[m] = arr[m], arr[l]
        l += 1
        m += 1
    elif arr[m] == 1:
        m += 1
    elif arr[m] == 2:
        arr[m], arr[h] = arr[h], arr[m]
        h -= 1
    else:
        print("Invalid entry: array should contain only 0,1,2")
        break

print("sorted:\n", arr)
