arr = [56,24,57,98,13,56,87]

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            print(j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(BubbleSort(arr))