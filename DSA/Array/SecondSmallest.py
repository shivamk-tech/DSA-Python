import sys
arr = [18, 19, 23, 1, 6 ,8, 5, 3]

def SecondSmallest(arr):
    smallest = arr[0]
    ssmallest = sys.maxsize
    print(ssmallest)
    for i in range(1, len(arr)):
        if(arr[i] < smallest):
            smallest = arr[i]
            smallest = smallest
        elif(arr[i] > smallest and arr[i] < ssmallest):
            ssmallest = arr[i]
    return ssmallest

print(SecondSmallest(arr))