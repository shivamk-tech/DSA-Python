arr = [2, 0, 1, 2, 1, 0, 2, 2, 1, 0, 1, 2, 0, 1, 2]

def Sort(arr, low, high):
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid+=1
            low+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    return arr

low = 0
high = len(arr) - 1
print(Sort(arr, low, high))