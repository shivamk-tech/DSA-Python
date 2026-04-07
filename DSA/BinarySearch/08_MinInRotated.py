arr = [4,5,6,7,0,1,2]

def minInRotated(nums):
    low = 0
    high = len(nums) - 1
    ans = float('inf')
    while(low <= high):
        mid = (low + high) // 2
        if(nums[low] <= nums[mid]):
            ans = min(nums[low], ans)
            low = mid + 1
        else:
            ans = min(nums[mid], ans)
            high = mid - 1
    return ans

print(minInRotated(arr))
