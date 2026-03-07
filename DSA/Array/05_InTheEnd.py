arr = [1,0,2,6,0,3,0,8,0,4,8,0,0,9,0]

def zeroToEnd(arr, low, high):
    while low < high:
        if arr[low] == 0 and arr[high] != 0:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1
        elif arr[low] != 0:
             low+=1
        else:
            high-=1
    return arr

low = 0
high = len(arr) - 1

print(zeroToEnd(arr, low, high))   