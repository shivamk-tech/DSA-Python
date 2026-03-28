arr = [1,2,4,5,67,78,4,3,3,5,7,]

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] == target):
            return mid
        elif(target > nums[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch(arr, 67))