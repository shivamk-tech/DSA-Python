arr = [1,2,3,4,5]

def reverse(arr ,left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def RotateArrayByLeft(arr,k):
    reverse(arr,0,k-1)
    reverse(arr,k+1, len(arr)-1)
    reverse(arr,0, len(arr)-1)
    return arr

print(RotateArrayByLeft(arr, 4))