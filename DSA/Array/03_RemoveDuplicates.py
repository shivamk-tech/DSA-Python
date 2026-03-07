arr =  [1,1,2,3,3,3,4]

def RemoveDuplicates(arr):
    pos = 0
    for i in range(1, len(arr)):
        if(arr[i] != arr[pos]):
            arr[pos+1] = arr[i]
            pos+=1
    return arr

print(RemoveDuplicates(arr))