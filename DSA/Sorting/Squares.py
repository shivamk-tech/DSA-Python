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

def sortedSquares(nums):
    result = list(map(lambda x:x**2, nums))
    result.sort()
    return result

print(sortedSquares(arr))



























def ByTwoPointer(arr, low, high):
    result = list(map(lambda x:x**2, arr))
    for i in range(len(arr)):
        if(arr[low] > arr[high]):
            arr[low], arr[high] = arr[high], arr[low]
            