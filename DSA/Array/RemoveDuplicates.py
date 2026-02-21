arr = [1,1,2,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

def RemoveDuplicates(arr, low):
    k = 1
    while(low < len(arr) - 1):
        if(arr[low+1] == arr[low]):
            low+=1
        elif(arr[low+1] != arr[low]):
            arr[k],arr[low+1] = arr[low+1], arr[k]
            k+=1
            low+=2
    return arr[:k]

low = 0
print(RemoveDuplicates(arr, low))