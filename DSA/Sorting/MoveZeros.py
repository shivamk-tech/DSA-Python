arr = [0,1,3,12,4,6,0,7,7,4,4,7,0,0,7,9,7,9,90,7,66,0,0,7,5,7,0,]

def SortZero(arr, low, high):
    while low < high : 
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

print(SortZero(arr, low, high))