arr = [[8,10], [1,3], [2,6], [3,10], [5,9], [12,10]]
  
def mergeIntervals(arr):
    if not arr:
        return []
    arr.sort()
    merged = []
    current = arr[0]
    for i in range(1, len(arr)):
        if arr[i][0] <= current[1]:
            current[1] = max(arr[i][1], current[1])
        else:
            merged.append(current)
            current = arr[i]
    merged.append(current)
    return merged

print(mergeIntervals(arr))