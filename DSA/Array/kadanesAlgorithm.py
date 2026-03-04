nums = [5, -2, 3, 4]

def maxSumSubArray(nums):
    mainSum = float('-inf')
    CurrentSum = 0
    fstart = -1
    fend = -1
    tstart = -1
    for i in range(len(nums)):
        if CurrentSum == 0: 
            tstart = i
        CurrentSum +=nums[i] 
        if CurrentSum > mainSum:
            mainSum = CurrentSum
            fstart = tstart
            fend = i
        if CurrentSum < 0:
            CurrentSum = 0
    return fstart, fend

print(maxSumSubArray(nums))
