arr = [1,2,3,4,5,4,7,8,9]

def CheckArraySorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

print(CheckArraySorted(arr))