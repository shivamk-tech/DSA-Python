arr = [10,22,12,3,0,6]

# Brute Force
def leadersInArray(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] > nums[j]):
                if(j+1 == len(nums)):
                    result.append(nums[i])
            else:
                break
    result.append(nums[len(nums) - 1])
    return result


def OptimalSolForFindingLeadersInArray(nums):
    n = len(nums)
    max = float('-inf')
    result = []
    for i in range(len(nums)-1, -1, -1):
        if(nums[i] > max):
            result.append(nums[i])
            max = nums[i]
    return result

        
print(BetterSolForFindingLeadersInArray(arr))