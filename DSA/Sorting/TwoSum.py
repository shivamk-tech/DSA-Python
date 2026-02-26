nums = [2,7,11,15]

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def TwoSum(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1
    while(low < high):
        if(nums[low] + nums[high] == target):
            result = [nums[low], nums[high]]
            return result
        elif(nums[low] + nums[high] > target):
            high-=1
        else:
            low+=1

def TwoSumByHashing(nums,target):
    hashMap = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in hashMap:
            return [hashMap[needed], i]
        hashMap[num] = i
    return "not found"
    
print(TwoSumByHashing(nums,18))




