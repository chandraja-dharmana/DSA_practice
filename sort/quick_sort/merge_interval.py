
intervals = [[8,10],[1,3],[15,18],[2,6]]


# Step 1: Sort by starting value
intervals.sort(key=lambda x: x[0]) #[[1, 3], [2, 6], [8, 10], [15, 18]]

# Step 2: Initialize the result
merged = [intervals[0]] 

# Step 3: Compare and merge intervals
for i in range(1, len(intervals)):
    current = intervals[i]
    previous = merged[-1]

    if current[0] <= previous[1]:
        # Overlapping: update the ending value
        previous[1] = max(previous[1], current[1])
    else:
        # Not overlapping: add a new interval
        merged.append(current)

print(merged)

