arr = [1, 2, 4, 6, 8]

print("hello")
def floorBinary(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1
    while(low <= high):
        mid = (low + high) // 2
        if (nums[mid] <= target):
            ans = nums[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans

def ceilBinary(nums, target):
    low = 0
    high = len(nums) - 1
    ans = -1
    while(low <= high):
        mid = (low + high) // 2
        if (nums[mid] >= target):
            ans = nums[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans 

print(ceilBinary(arr, 5))