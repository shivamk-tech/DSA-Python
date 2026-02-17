arr = [56,24,57,98,13,56,87]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            if (arr[j-1] > arr[j]):
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
    return arr


print(InsertionSort(arr))