arr = [23423,543,5,65,45,34,5,36,54,34,43654]

def Merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while (left <= mid and right <= high ):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left <= mid):
        temp.append(arr[left])
        left+=1

    while(right <= high):
        temp.append(arr[right])
        right+=1
   
    for i in range(len(temp)):
        arr[low+i] = temp[i]

def MergeSort(arr, low , high):
    if(high <= low):
        return 
    mid = (low + high)//2
    MergeSort(arr , low , mid)
    MergeSort(arr, mid + 1, high)
    Merge(arr, low, mid, high)
    return arr

low = 0
high = len(arr) - 1
print(MergeSort(arr, low, high))
