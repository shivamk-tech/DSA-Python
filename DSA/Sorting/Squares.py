arr = [-4, -3, 2, 4,-4 ,5 ,6 ,6, -4, 7 ,-2, -8]

def SortBubble(arr):
    for i in range (len(arr) - 1):
        for j in range (len(arr) - 1 - i):
            if(arr[j+1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def SquareOfSortedArr(arr):
    result = list(map(lambda x:x**2, arr))
    SortBubble(result)
    return result

print(SquareOfSortedArr(arr))




