arr = [-1,0,3,5,5,9,12]
def lowerBound(nums,target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] >= target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upperBound(nums,target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while(low <= high):
        mid = (low + high) // 2
        if(nums[mid] > target):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def lastAndFirstOcc(nums, target):
    first = lowerBound(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = upperBound(nums, target) - 1
    return [first, last]

def freq(nums, target):
    first = lowerBound(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = upperBound(nums, target) - 1
    frequncy = (upperBound(nums, target) - 1) - lowerBound(nums, target)
    return frequncy + 1

print(lastAndFirstOcc(arr, 5))
print(freq(arr, 5))