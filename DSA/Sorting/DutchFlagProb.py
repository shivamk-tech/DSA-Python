arr = [2, 0, 1, 2, 1, 0, 2, 2, 1, 0, 1, 2, 0, 1, 2]

def Sort(nums):
    high = len(nums) - 1
    low = 0
    mid = 0
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid+=1
            low+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1
    return nums

low = 0
high = len(arr) - 1
print(Sort(arr))