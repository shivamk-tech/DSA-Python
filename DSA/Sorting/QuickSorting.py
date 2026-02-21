arr = [4, 6, 2, 5, 7, 9, 1, 3]

def PivotIndex(arr, low, high):
    Pivot = arr[low]
    i = low
    j = high
    while(i < j):
        while(arr[i] <= Pivot and i <= high):
            i+=1
        while(arr[j] > Pivot and j >= low):
            j-=1
        if(i < j):
            arr[i] , arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

def QuickSort(arr, low, high):
    if(low < high):
        Pivot_index = PivotIndex(arr, low, high)
        QuickSort(arr, low, Pivot_index - 1)
        QuickSort(arr, Pivot_index + 1, high)

low = 0
high = len(arr) - 1

QuickSort(arr, low, high)
print(arr)




