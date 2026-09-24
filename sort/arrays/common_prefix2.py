#https://chatgpt.com/share/6aa18a2a-5880-83e8-82df-abb06930204d

arr = ["flower", "flow", "flight"]

for i in range(len(arr[0])):
    prefix = arr[0][:i + 1]
    print("prefix",prefix)

    for word in arr:
        if not word.startswith(prefix):
            print(arr[0][:i])
            exit()

print(arr[0])