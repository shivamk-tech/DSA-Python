arr = [3,1,2,4,2,4,5,3,5,6,7,98,0]

def Sort(arr, low, high):
     while low < high:
        if arr[low] % 2 != 0 and arr[high] % 2 == 0:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1
        elif arr[low] % 2 == 0:
            low+=1
        elif arr[high] % 2 != 0:
            high-=1
     return arr

low = 0
high = len(arr) - 1

print(Sort(arr, low, high))