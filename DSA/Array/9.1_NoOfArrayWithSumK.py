arr = [1,2,3,-3,1,1,1,4,2,-3]

def totalArray(nums, k):
    prefixSum = {0:1}
    currentSum = 0
    count = 0
    for i in range(len(nums)):
        currentSum+=nums[i]
        remaining = currentSum - k

        if remaining in prefixSum:
            count+=prefixSum[remaining]

        prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1

    return count

print(totalArray(arr, 3))
        