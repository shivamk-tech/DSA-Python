nums = [-4,-2,1,4,8]

def closestToZero(nums):
    closest = nums[0]
    for i in range(1,len(nums)):
        if(abs(nums[i]) < abs(closest)):
            closest = nums[i]
        elif(abs(closest) == abs(nums[i])):
            closest = nums[i] if nums[i] > closest else closest
    return closest

print(closestToZero(nums))