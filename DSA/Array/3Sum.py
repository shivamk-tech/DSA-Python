nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        low = 0 + 1
        high = len(nums) - 1
        target = nums[i]
        while low < high:
            if low == i:
                low+=1
            if high == i:
                high-=1

            if nums[low] + nums[high] == -target:
                result.append([nums[low], nums[high], target])
                low+=1
                high-=1
            elif nums[low] + nums[high] < -target:
                low+=1
            else:
                high-=1
    return result

print(threeSum(nums))