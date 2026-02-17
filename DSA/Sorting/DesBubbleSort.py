arr = [56,24,57,98,13,56,87]

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0 , n - i - 1):
            if(arr[j + 1] > arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

print(BubbleSort(arr))