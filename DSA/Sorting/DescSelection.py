arr = [23,5,56,56,67,657,5,43,4,346,657,4,3254]

def DesSelection(arr):
    for i in range(len(arr) - 1):
        min_index = 0
        for j in range(0,len(arr) - i):
            if arr[j] < arr[min_index]:
                min_index = j
        print(len(arr) - i - 1)
        arr[len(arr) - i - 1], arr[min_index] = arr[min_index], arr[len(arr) - i - 1]
    return arr

print(DesSelection(arr))


