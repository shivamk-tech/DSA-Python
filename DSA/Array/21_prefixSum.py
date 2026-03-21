arr = [1,-1,3,2,-2,-8,1,7,10,23]

def prefixSum(nums):
    hashMap = {}
    maxLen = 0
    sum = 0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum == 0:
            maxLen = max(maxLen,i + 1)

        if sum in hashMap:
            length = i - hashMap[sum]
            maxLen = max(maxLen, length)
        elif sum not in hashMap:
            hashMap[sum] = i

    return maxLen

print(prefixSum(arr))
