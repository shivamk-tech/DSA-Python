arr = [56,24,57,98,13,56,87]

def BubbleSort(arr):
    Array_sorted = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                Array_sorted = True
        if Array_sorted == False:
            print("Array is already sorted")
            break
        print(arr)

BubbleSort(arr)