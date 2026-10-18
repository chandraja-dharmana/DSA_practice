arr = ["flower", "flow", "flight"]

for i in range(len(arr[0])):
    for j in range(1, len(arr)):
        print("i: ",i)
        print("arr[j]: ",arr[j])
        print("len(arr[j]): ",len(arr[j]))
        print("arr[0][i]: ",arr[0][i])
        print("arr[j][i]: ",arr[j][i])
        if i >= len(arr[j]) or arr[0][i] != arr[j][i]:
            print(arr[0][:i])
            exit()

print(arr[0])