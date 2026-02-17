arr = [1,0,1,0,1,1,0]

def Sort(arr, low, high):
    while low < high:
        if arr[low] == 1 and arr [high] == 0:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1
        elif arr[low] == 0:
            low+=1
        elif arr[high] == 1:
            high-=1
    return arr

low = 0
high = len(arr) - 1

print(Sort(arr, low, high))