arr = [102, 4, 100, 1, 101, 3, 2, 1, 1 ]


def longConscutive(nums):
    longest = 1
    for i in range(len(nums)):
        n = nums[i]
        count = 1
        while (n + 1) in nums:
            n =  n + 1
            count = count + 1
        longest = max(longest, count)
    return longest


def BetterSolForConscutive(nums):
    longest = 1
    count = 0
    lastSmaller = float('-inf')
    nums.sort()
    for i in range(len(nums)):
        if(nums[i] - 1 == lastSmaller):
            count = count + 1
            lastSmaller = nums[i]
        elif(nums[i] != lastSmaller):
            count = 1
            lastSmaller = nums[i]
        longest = max(longest, count)
    return longest
    

print(BetterSolForConscutive(arr))
