nums = [-1,0,1,2,-1,-4]



def bruteForce(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(i != j and j != k and i != k):
                    if(nums[i] + nums[j] + nums[k] == 0):
                        result.append(tuple(sorted([nums[i], nums[j], nums[k]])))
    return list(set(result))

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        low = i+1
        high = len(nums) - 1
        while(low < high):
                if(nums[low] + nums[high] == target):
                    result.append([nums[low], nums[high], -target])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low+=1
                    high-=1
                elif(nums[low] + nums[high] > target):
                    high-=1
                else:
                    low+=1
    return result


print(threeSum(nums))