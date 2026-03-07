nums = [-1,0,1,2,-1,-4]

num = 10
st = 10

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        low = i + 1
        high = len(nums) - 1
        target = nums[i]
        while low < high:
            if nums[low] + nums[high] == -target:
                result.append([nums[low], nums[high], target])
                low+=1
                high-=1
            elif nums[low] + nums[high] < -target:
                low+=1
            else:
                high-=1
    final = [list(x) for x in set(tuple(sorted(i)) for i in result)]
    return final

print(threeSum(nums))