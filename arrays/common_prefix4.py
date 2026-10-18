arr = ["flower", "flow", "flight"]

prefix = arr[0]

for word in arr[1:]:
    print("word", word)
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        print("prefix", prefix)

print(prefix)