arr = [2,3,-2,4]

def maxProdcut(nums):
    Pro = float('-inf')
    for i in range(len(nums)):
        maxPro = 1
        for j in range(i, len(nums)):
            maxPro*=nums[j]
            Pro = max(Pro, maxPro)
    return Pro





def optimalSolution(nums):
    pre = 1
    suff = 1
    ans = float('-inf')
    for i in range(len(nums)):
        if(pre == 0): pre = 1
        if(suff == 0): suff = 1
        pre*=nums[i]
        suff*=nums[len(nums) - i - 1]
        ans = max(ans,max(pre, suff))
    return ans


print(optimalSolution(arr))