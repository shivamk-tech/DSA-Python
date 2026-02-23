nums = [1,2,3,4,5,7,8]

# Brute Force
def findMissingNum(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] != 1:
            return nums[i] + 1
        
# Better Approach
def findMissingByHashing(nums):
    count = [0]*(len(nums)+1)
    for i in range(len(nums)):
        count[nums[i]-1] = 1

    for i in range(len(count)):
        if count[i] == 0:
            return i + 1
    return count

# Optimal Solution
def findMissingBySum(nums):
    oriSum = ((len(nums) + 1)*(len(nums) +1+1)) / 2
    listSum = 0
    for i in range(len(nums)):
        listSum+=nums[i]
   
    return oriSum - listSum

# Optimal Solution Using XOR
def findMissingByXOR(nums):
    XOR1 = 0
    XOR2 = 0
    for i in range(1, len(nums) + 2):
        XOR1 = XOR1^i
    for i in range(len(nums)):
        XOR2 = XOR2^nums[i]
    return XOR1^XOR2
    

print(findMissingByXOR(nums))