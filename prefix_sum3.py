arr = [1, 2, 3, 1, 1, 1, 1]
k = 3
prefix_sum = 0
max_len = 0

mp = {}

for i in range(len(arr)):
    prefix_sum += arr[i]

    # Case 1: subarray starts from index 0
    if prefix_sum == k:
        max_len = i + 1

    # Case 2: previous prefix sum exists
    if prefix_sum - k in mp:
        length = i - mp[prefix_sum - k]
        print("mp[prefix_sum - k]: ",mp[prefix_sum - k])
        print("i:",i)
        max_len = max(max_len, length)

    # Store ONLY the first occurrence
    if prefix_sum not in mp:
        mp[prefix_sum] = i

print(mp)
print(max_len)