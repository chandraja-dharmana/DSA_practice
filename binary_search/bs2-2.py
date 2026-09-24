# arr = [10, 20, 30, 40, 50]
# target = 40

def bs(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            print("element found :", arr[mid])
            print("target index", mid)
            break

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
    else:
        print("element not found")


test_cases = {
    "example1": {"arr": [3, 7, 12, 18, 25, 31, 39, 46, 52, 61, 68, 74, 81, 90, 97], "target": 7, "output": 1},

    "example2": {"arr": [5, 11, 17, 23, 29, 34, 41, 48, 56, 63, 71, 78, 85, 92, 99], "target": 92, "output": 13},

    "example3": {"arr": [10, 20, 30, 40, 50, 60, 70, 80, 90], "target": 55, "output": -1},

    "example4": {"arr": [4, 9, 15, 22, 28, 35, 41, 48, 53], "target": 28, "output": 4},

    "example5": {"arr": [-50, -42, -35, -27, -18, -10, -3, 5, 12, 21, 30], "target": -27, "output": 3},

    "example6": {"arr": [-80, -65, -51, -44, -32, -21, -9, 4, 16, 29, 45], "target": -50, "output": -1},

    "example7": {"arr": [-100, -75, -60, -42, -25, -11, 0, 8, 19, 34, 57, 81, 120], "target": 34, "output": 9},

    "example8": {"arr": [42], "target": 42, "output": 0},

    "example9": {"arr": [42], "target": 17, "output": -1},

    "example10": {"arr": [12, 24, 36, 48, 60, 72, 84, 96], "target": 100, "output": -1},

    "example11": {"arr": [2, 5, 9, 14, 21, 29, 38, 48, 59, 71, 84, 98, 113, 129, 146, 164, 183, 203], "target": 129, "output": 13},

    "example12": {"arr": [1, 4, 8, 13, 19, 26, 34, 43, 53, 64, 76, 89, 103, 118, 134, 151, 169, 188], "target": 100, "output": -1},

    "example13": {"arr": [2, 4, 4, 4, 7, 9, 12, 12, 15, 18, 21], "target": 12, "output": 6},

    "example14": {"arr": [1, 3, 3, 3, 6, 8, 8, 11, 14, 14, 20], "target": 10, "output": -1},

    "example15": {"arr": [-120, -95, -73, -51, -30, -12, 0, 17, 29, 44, 63, 81, 102, 127, 155, 190, 225], "target": 102, "output": 12}
}

for i in range(15):
    eg = "example"+str(i+1)
    print(eg)
    arr = test_cases[eg]["arr"]
    target = test_cases[eg]["target"]
    bs(arr, target)