arr = [1,2,3]
result = []

def permutations(nums, idx, result):

    if idx == len(nums):
        result.append(nums)   # copy list
        return

    for i in range(idx, len(nums)):
        nums[i], nums[idx] = nums[idx], nums[i]

        permutations(nums, idx+1, result)

        nums[i], nums[idx] = nums[idx], nums[i]   # backtrack

print(result)
    

